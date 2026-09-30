#!/usr/bin/env python3
"""Capture UI screenshots across viewports and color schemes, and flag common problems.

For each URL x viewport x color scheme it:
  - saves a screenshot (full page by default)
  - detects horizontal overflow (content wider than the viewport) and lists the widest offenders
  - collects console errors and uncaught page errors
  - on touch viewports, lists interactive elements smaller than the minimum touch target (default 44px)

Writes <out>/report.json and prints a summary. Exit code 1 if any issue was found.

Requires: pip install playwright  (and `python -m playwright install chromium` if no Chromium is present)
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Playwright is not installed. Run: pip install playwright && python -m playwright install chromium")

VIEWPORTS = {
    "mobile": {"width": 390, "height": 844, "is_mobile": True, "has_touch": True, "device_scale_factor": 2},
    "tablet": {"width": 820, "height": 1180, "is_mobile": True, "has_touch": True, "device_scale_factor": 2},
    "desktop": {"width": 1440, "height": 900, "is_mobile": False, "has_touch": False, "device_scale_factor": 1},
    "wide": {"width": 1920, "height": 1080, "is_mobile": False, "has_touch": False, "device_scale_factor": 1},
}

OVERFLOW_JS = """
() => {
  const vw = document.documentElement.clientWidth;
  const docWidth = Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0);
  const offenders = [];
  if (docWidth > vw + 1) {
    const bad = [];
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (getComputedStyle(el).visibility === 'hidden') continue;
      if (r.right > vw + 1 || r.left < -1) bad.push(el);
    }
    // keep only the innermost offenders; their ancestors overflow because of them
    const leaves = bad.filter(el => !bad.some(o => o !== el && el.contains(o)));
    for (const el of leaves) {
      const r = el.getBoundingClientRect();
      {
        let sel = el.tagName.toLowerCase();
        if (el.id) sel += '#' + el.id;
        else if (el.classList.length) sel += '.' + [...el.classList].slice(0, 3).join('.');
        offenders.push({ selector: sel, left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width) });
      }
    }
  }
  offenders.sort((a, b) => b.right - a.right);
  return { viewportWidth: vw, documentWidth: docWidth, overflow: docWidth > vw + 1, offenders: offenders.slice(0, 8) };
}
"""


TARGETS_JS = """
(minSize) => {
  const sel = 'a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=tab], [role=checkbox], [role=switch], [tabindex]:not([tabindex="-1"])';
  const small = [];
  for (const el of document.querySelectorAll(sel)) {
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || el.closest('[aria-hidden="true"], [inert]')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    // WCAG exempts links inside a sentence or paragraph of text
    if (el.tagName === 'A' && el.closest('p, li') && cs.display.startsWith('inline')) continue;
    if (r.width < minSize || r.height < minSize) {
      let s = el.tagName.toLowerCase();
      if (el.id) s += '#' + el.id;
      else if (el.classList.length) s += '.' + [...el.classList].slice(0, 2).join('.');
      const label = (el.getAttribute('aria-label') || el.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 40);
      small.push({ selector: s, label, width: Math.round(r.width), height: Math.round(r.height) });
    }
  }
  return small;
}
"""


def slug(url: str) -> str:
    p = urlparse(url)
    path = (p.path or "/").strip("/") or "home"
    if p.query:
        path += "_" + p.query
    if p.scheme == "file":
        path = Path(p.path).stem
    return re.sub(r"[^A-Za-z0-9._-]+", "-", path)[:80]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+", help="Pages to capture (http(s):// or file://)")
    ap.add_argument("--out", default="screenshots", help="Output directory (default: screenshots)")
    ap.add_argument("--viewports", default="mobile,tablet,desktop", help=f"Comma list from: {','.join(VIEWPORTS)}")
    ap.add_argument("--schemes", default="light,dark", help="Comma list of color schemes: light,dark")
    ap.add_argument("--rtl", action="store_true", help='Force dir="rtl" on <html> before capturing')
    ap.add_argument("--reduced-motion", action="store_true", help="Emulate prefers-reduced-motion: reduce")
    ap.add_argument("--wait", type=int, default=500, help="Extra milliseconds to wait after load (default 500)")
    ap.add_argument("--no-full-page", action="store_true", help="Capture only the visible viewport")
    ap.add_argument("--timeout", type=int, default=30000, help="Navigation timeout in ms (default 30000)")
    ap.add_argument("--min-target", type=int, default=44,
                    help="Minimum touch target size in px, checked on touch viewports (default 44; 0 disables)")
    args = ap.parse_args()

    viewports = [v.strip() for v in args.viewports.split(",") if v.strip()]
    unknown = [v for v in viewports if v not in VIEWPORTS]
    if unknown:
        sys.exit(f"Unknown viewport(s): {', '.join(unknown)}. Choose from {', '.join(VIEWPORTS)}")
    schemes = [s.strip() for s in args.schemes.split(",") if s.strip()]

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    results = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for url in args.urls:
            for vp_name in viewports:
                vp = VIEWPORTS[vp_name]
                for scheme in schemes:
                    ctx = browser.new_context(
                        viewport={"width": vp["width"], "height": vp["height"]},
                        device_scale_factor=vp["device_scale_factor"],
                        is_mobile=vp["is_mobile"],
                        has_touch=vp["has_touch"],
                        color_scheme=scheme,
                        reduced_motion="reduce" if args.reduced_motion else "no-preference",
                    )
                    page = ctx.new_page()
                    console_errors = []
                    page.on("console", lambda m, errs=console_errors: errs.append(m.text) if m.type == "error" else None)
                    page.on("pageerror", lambda e, errs=console_errors: errs.append(f"Uncaught: {e}"))

                    entry = {"url": url, "viewport": vp_name, "scheme": scheme}
                    try:
                        page.goto(url, wait_until="networkidle", timeout=args.timeout)
                    except Exception as e:  # networkidle can time out on apps with polling; fall back to load
                        try:
                            page.goto(url, wait_until="load", timeout=args.timeout)
                        except Exception as e2:
                            entry["error"] = f"Navigation failed: {e2}"
                            results.append(entry)
                            ctx.close()
                            continue
                    if args.rtl:
                        page.evaluate("() => document.documentElement.setAttribute('dir', 'rtl')")
                    page.wait_for_timeout(args.wait)

                    name = f"{slug(url)}_{vp_name}_{scheme}{'_rtl' if args.rtl else ''}.png"
                    page.screenshot(path=str(out / name), full_page=not args.no_full_page)
                    entry["screenshot"] = name
                    entry["overflow"] = page.evaluate(OVERFLOW_JS)
                    entry["console_errors"] = console_errors
                    entry["small_targets"] = (
                        page.evaluate(TARGETS_JS, args.min_target) if vp["has_touch"] and args.min_target > 0 else []
                    )
                    results.append(entry)
                    ctx.close()
        browser.close()

    (out / "report.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

    issues = 0
    print(f"Captured {sum(1 for r in results if 'screenshot' in r)} screenshots into {out}/")
    for r in results:
        tag = f"{r['url']} [{r['viewport']}/{r['scheme']}]"
        if "error" in r:
            issues += 1
            print(f"  ERROR     {tag}: {r['error']}")
            continue
        ov = r["overflow"]
        if ov["overflow"]:
            issues += 1
            worst = ", ".join(o["selector"] for o in ov["offenders"][:3]) or "unknown element"
            print(f"  OVERFLOW  {tag}: page is {ov['documentWidth']}px wide in a {ov['viewportWidth']}px viewport ({worst})")
        if r["console_errors"]:
            issues += 1
            print(f"  CONSOLE   {tag}: {len(r['console_errors'])} error(s), first: {r['console_errors'][0][:160]}")
        if r["small_targets"]:
            issues += 1
            ex = ", ".join(f"{t['selector']} {t['width']}x{t['height']}" for t in r["small_targets"][:3])
            print(f"  TARGETS   {tag}: {len(r['small_targets'])} touch target(s) under {args.min_target}px ({ex})")
    print("No issues found." if issues == 0 else f"{issues} issue(s) found. Details in {out}/report.json")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

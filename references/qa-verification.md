# QA & Verification

Verify each milestone before reporting it done. "It compiles" is not verification for UI work. You need to look at it.

## 1. Screenshots with `scripts/capture_screens.py`

A Playwright script that opens each URL at several viewports, in light and dark color schemes, saves full-page screenshots, and reports three common problems automatically: **horizontal overflow** (something wider than the viewport), **console errors**, and **small touch targets** (interactive elements under 44×44px on the mobile and tablet viewports; links inside running text are exempt, as in WCAG).

### Setup (once)
```bash
pip install playwright
python -m playwright install chromium   # skip if a Chromium is already installed
```

### Usage
```bash
# Start the app first (npm run dev, etc.), then:
python scripts/capture_screens.py http://localhost:3000 http://localhost:3000/settings \
  --out docs/screenshots/milestone-2

# Options
#   --viewports mobile,tablet,desktop   (default; also: wide)
#   --schemes light,dark                (default both; emulates prefers-color-scheme)
#   --rtl                               force dir="rtl" on <html> for a quick RTL check
#   --reduced-motion                    emulate prefers-reduced-motion
#   --wait 800                          extra ms to wait after load (for animations/data)
#   --no-full-page                      capture only the viewport
#   --min-target 44                     touch target minimum in px (24 = WCAG 2.2 AA floor; 0 disables)
```

It writes PNGs named `<page>_<viewport>_<scheme>.png` and a `report.json` with overflow, console-error and touch-target findings per capture, and prints a summary. Exit code 1 if any issues were found.

### Then look at them
Open the screenshots (and view them if your environment lets you view images). Check:
- Spacing rhythm and alignment; nothing cramped or floating in empty space
- Hierarchy: is the primary action obvious in each screen?
- Mobile: nothing cut off, touch targets big enough, no text overflow
- Dark mode: no leftover light surfaces, readable secondary text, images fit
- RTL: mirrored layout, correct icons, no physical-margin leftovers

For states that need specific data (empty, error), capture them through the app's own means: a query parameter, a mock mode, Storybook stories, or temporarily seeded data. Don't leave hacks in the code.

## 2. States checklist

Go through `states-checklist.md` for the screens and components in this milestone. Each state in the plan's tables should exist in the implementation. Report any that were deferred.

## 3. Accessibility

- Automated: `npx @axe-core/cli <url>` or `@axe-core/playwright` if available; Lighthouse accessibility audit
- Keyboard pass of the milestone's flows (Tab, Shift+Tab, Enter, Space, Esc)
- Contrast of any new color pairs
- Reduced motion on (`--reduced-motion`): nothing essential disappears

## 4. Performance (when relevant)

- Lighthouse performance on the main pages for heavy styles
- No layout shift when content loads (skeletons reserve space)

## 5. Report at the checkpoint

Keep it short:
- What was implemented (link to the plan's milestone)
- What was verified and how (e.g. "12 screenshots, 3 viewports × 2 themes × 2 pages; no overflow; 1 console warning fixed")
- Deviations from the plan and why
- Anything deferred or needing the developer's decision

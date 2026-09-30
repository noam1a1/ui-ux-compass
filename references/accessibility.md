# Accessibility

Baseline: **WCAG 2.2 level AA**, unless the developer sets a different target. Accessibility is part of good UX for everyone (keyboard power users, people in bright sunlight, people with a broken arm), and in many countries it is a legal requirement. In Israel, for example, Israeli Standard 5568 (based on WCAG) applies to many websites.

## Requirements to plan for

### Perception
- **Text contrast**: 4.5:1 for normal text, 3:1 for large text (≥ 24px, or ≥ 18.66px bold)
- **Non-text contrast**: 3:1 for UI component boundaries, icons that carry meaning, focus indicators, chart elements
- **Don't use color alone**: errors get an icon and text; links in body text get an underline; chart series get labels or patterns
- **Text alternatives**: meaningful `alt` for informative images, `alt=""` for decorative ones; labels for icon-only buttons
- **Resizable**: layouts work at 200% zoom and 320px width without horizontal scrolling (except data tables and maps)
- **Captions** for video with speech; transcripts for audio

### Operation
- **Keyboard**: everything works with a keyboard; logical tab order; no keyboard traps; modals trap focus while open and return focus on close
- **Visible focus**: a clear `:focus-visible` style on every interactive element (2px+ outline, 3:1 contrast, not hidden by sticky headers)
- **Target size**: at least 24×24px (WCAG 2.2). Recommended 44×44px on touch
- **Skip link** to main content on pages with repeated navigation
- **Motion**: honor `prefers-reduced-motion`; no auto-playing motion longer than 5 seconds without pause; nothing flashes more than 3 times per second
- **Time limits**: warn and allow extension (session timeouts)
- **Dragging**: every drag action has a single-pointer alternative (WCAG 2.2)

### Understanding
- **Language**: `lang` on `<html>` (and on inline passages in another language); `dir` for RTL
- **Labels and instructions** on all form fields; errors say how to fix them
- **Consistent navigation** and naming across pages
- **Help** available in a consistent place (WCAG 2.2)
- **Don't make users re-enter** information already given in the same process (WCAG 2.2)
- **Accessible authentication**: no cognitive tests without alternatives; allow paste and password managers

### Robustness
- **Semantic HTML first**: `<button>` for actions, `<a>` for navigation, real headings in order, landmarks (`header`, `nav`, `main`, `footer`), lists as lists, tables for tabular data
- **ARIA only when HTML can't do it**, and correctly (use established primitives such as Radix, React Aria, Headless UI or Angular CDK for complex widgets like comboboxes, menus and tabs)
- **Status messages** announced with `aria-live` (toasts, "3 results found", form submission results)

## Style-specific risks and mitigations

| Style | Risk | Mitigation |
|---|---|---|
| Glassmorphism / Liquid Glass / Acrylic | Contrast varies with background | Test against the worst background; raise surface opacity; opaque fallback under `prefers-reduced-transparency` |
| Neumorphism | Controls barely visible | Add borders or an accent fill to controls; strong focus rings |
| Minimal / Ultra Minimal / Line UI | Hidden affordances, thin strokes | Visible labels, filled primary buttons, 3:1 boundaries |
| Dark UI / Dark Luxe / Neon | Muted text too dim; glow on text | Check secondary text contrast; no glow on body text |
| Luxury (thin serifs, light gray) | Fails contrast at small sizes | Heavier weights for small text; darker grays |
| Motion-first / Scrollytelling / Parallax / Kinetic | Vestibular issues; content hidden until animated | Reduced-motion versions; content present in the DOM without JS animation |
| Glitch / Cyberpunk / FUI | Flashing; decorative noise | Flash rules; decoration marked `aria-hidden` |
| Immersive 3D / WebGL | Canvas is invisible to assistive tech | An HTML layer with the real content and controls |
| Data-Dense | Small targets and text | Density setting; minimum 24px targets |
| Pastel styles (Kawaii, Claymorphism) | Light text on light surfaces | Dark text on pastel surfaces |

## How to verify

- Automated: axe-core (browser extension, `@axe-core/playwright`, or Lighthouse). Automated tools catch only about 30–40% of issues
- Keyboard pass: Tab through each key flow; check focus visibility, order and traps
- Zoom to 200%, and set the viewport to 320px
- Screen reader smoke test on a key flow (VoiceOver on macOS/iOS, NVDA on Windows, TalkBack on Android)
- Contrast checks for the token pairs (can be scripted from the token file)
- `prefers-reduced-motion` and dark mode toggled on

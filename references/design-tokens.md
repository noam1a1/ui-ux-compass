# Design Tokens

Tokens are the named design decisions (colors, sizes, durations) that every component uses. Defining them before any screen is what keeps a product consistent, makes dark mode and theming cheap, and lets style changes happen in one place.

## Three layers

1. **Primitive tokens**: the raw palette and scales. `blue-500: #3B82F6`, `space-4: 16px`. Never used directly in components.
2. **Semantic tokens**: meaning. `color-bg-surface`, `color-text-muted`, `color-action-primary`, `color-border-danger`. These switch between light and dark themes.
3. **Component tokens** (optional, for larger systems): `button-primary-bg`, `card-radius`.

Components use semantic (or component) tokens only. That's what makes a theme swap work.

## What to define

### Color
- **Neutrals**: a 10–12 step gray scale, tinted slightly toward the brand hue for warmth or coolness
- **Brand / accent**: a primary scale (50–950), and a secondary if needed
- **Semantic**: success, warning, danger, info. Each needs a background, border, text and solid variant
- **Surfaces**: background, surface, surface-raised, overlay/scrim
- **Text**: primary, secondary/muted, disabled, on-accent (text on a colored button), link
- **Borders**: default, strong, focus ring
- **Both themes**: every semantic token gets a light and a dark value. Dark mode is designed, not inverted: lighter surfaces for elevation, desaturated accents, off-white text

Check contrast for every text/background pair you define (4.5:1 body, 3:1 large text and UI boundaries). Put the ratios in the plan for the main pairs.

### Typography
- **Families**: display/heading, body, mono. Include a fallback stack and a font for each script the product supports (see `rtl-i18n.md`)
- **Scale**: a modular scale (ratio 1.2 for dense apps, 1.25 for general use, 1.333 or more for expressive marketing), or a hand-tuned list. Typical steps: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, display
- **Fluid sizes** for headings on marketing pages: `clamp(min, preferred-vw, max)`
- **Line heights**: tighter for headings (1.1–1.25), comfortable for body (1.5–1.7; Hebrew and Arabic often need a little more)
- **Weights** used (limit to 3–4), and letter-spacing for caps and labels (never letter-space Hebrew or Arabic)

### Spacing
- A 4px base scale: 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128
- Semantic spacing if useful: `space-inset-card`, `space-stack-section`
- Dense products use the smaller steps more; marketing uses the larger ones

### Shape
- **Radii**: none, sm, md, lg, xl, full. The style decides the scale (Neo-Brutalism: 0–4px; Claymorphism: 24px+; Tech Minimalism: 6–12px)
- **Border widths**: hairline (1px), default, strong

### Elevation
- A shadow scale (sm, md, lg, xl) that matches the style: soft layered shadows, hard offset shadows (Neo-Brutalism), none (flat), or lighter surfaces instead of shadows (dark mode)

### Motion
- **Durations**: instant 100ms, fast 150ms, normal 250ms, slow 400ms, deliberate 600ms+
- **Easings**: standard `cubic-bezier(0.2, 0, 0, 1)`, enter/decelerate, exit/accelerate, spring (if the library supports it)
- **Reduced-motion rule**: what each token becomes under `prefers-reduced-motion` (usually 0ms or opacity-only)

### Layout
- **Breakpoints**: e.g. sm 640, md 768, lg 1024, xl 1280, 2xl 1536 (adapt to the stack's defaults)
- **Max content widths**: prose (~65ch), app content, full-bleed
- **Z-index scale**: base, dropdown, sticky, overlay, modal, toast, tooltip

## Implementation formats

Choose based on the stack. Plan in one format and implement in it:

- **CSS custom properties** (works everywhere):
  ```css
  :root { --color-bg: #ffffff; --color-text: #0f172a; --radius-md: 8px; }
  [data-theme="dark"] { --color-bg: #0b0b0f; --color-text: #e5e7eb; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { /* dark values */ } }
  ```
- **Tailwind v4**: `@theme { --color-surface: ...; }` in CSS. **Tailwind v3**: `theme.extend` in the config, pointing to CSS variables for themeable values
- **JSON (W3C Design Tokens format)**: when tokens are shared across platforms or with design tools (Style Dictionary can generate CSS/iOS/Android from it)
- **Native**: a Flutter `ThemeData`, a SwiftUI asset catalog and extensions, or a React Native theme object

## In the plan

Section 6 of the plan should list real values, not just categories: the palette with hex values, the type scale with sizes, and the main contrast ratios. That lets the developer judge the look before any component exists.

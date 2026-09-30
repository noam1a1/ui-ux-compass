# Existing Project Audit

Run this in Phase 0 for existing projects. The goal is to answer as many discovery questions as possible from the code, and to produce the "Current State" section of the plan. Scale it to the request: a scoped change only needs the parts that touch that area.

## 1. Detect the stack

Look at (whatever exists):
- `package.json` / lockfiles: framework (React, Next, Vue, Nuxt, Svelte/SvelteKit, Angular, Astro, Solid, Remix), styling (Tailwind, CSS Modules, styled-components, Emotion, Sass, vanilla-extract, UnoCSS), component libraries (shadcn/ui, Radix, MUI, Chakra, Mantine, Ant Design, Headless UI, Vuetify, PrimeVue), icons (Lucide, Heroicons, Phosphor, Font Awesome), animation (Motion/Framer Motion, GSAP, React Spring, Lottie, AutoAnimate), charts, i18n libs (i18next, next-intl, vue-i18n, FormatJS)
- `tailwind.config.*` or CSS `@theme` blocks, `globals.css`, `theme.ts`, token JSON files
- Native: `pubspec.yaml` (Flutter), React Native / Expo config, SwiftUI or Jetpack Compose files
- Plain HTML/CSS projects: the main stylesheet(s)

## 2. Visual system inventory

- **Colors**: collect every color used. Count distinct hex values; many near-duplicates mean no real palette. Are there semantic tokens (primary, danger) or only raw values?
- **Typography**: font families, sizes in use (a real scale, or 17 random sizes?), weights, line heights
- **Spacing**: consistent scale, or arbitrary pixel values?
- **Radii, shadows, borders**: consistent or ad hoc?
- **Dark mode**: exists? Token-driven or scattered overrides?
- **Components**: list the reusable ones. Where are one-off duplicates (three different button implementations)?

## 3. Experience inventory

- **Routes / screens**: list them (router config, `pages/` or `app/` directories)
- **States coverage**: for key screens, search for how loading, empty and error are handled. Common smells: a bare `Loading...` text, `null` returned while loading, no empty state, errors only in `console.error`
- **Forms**: labels, validation approach, error display
- **Navigation**: structure, active states, mobile behavior
- **Feedback**: toasts/notifications system present?

## 4. Quality checks

- **Accessibility**: semantic elements (buttons vs clickable divs), alt text, form labels, focus styles (search for `outline: none` without a replacement), color contrast of main text/background pairs, `lang` and `dir` on `<html>`
- **Responsive**: breakpoints used, fixed widths that break on mobile, horizontal overflow
- **RTL / i18n**: hardcoded strings vs translation keys; physical properties (`margin-left`, `left:`, `text-align: left`, Tailwind `ml-`/`pl-`) vs logical ones
- **Performance**: large images without optimization, many font files, heavy libraries for small effects, layout shift from late-loading content
- **Consistency**: same thing done different ways in different places

## 5. See it running (if possible)

If the app can be started locally, capture screenshots of the main screens with `scripts/capture_screens.py` (see `qa-verification.md`). Screenshots reveal problems the code hides: cramped spacing, weak hierarchy, awkward empty space.

## 6. Output: prioritized findings

Classify each finding:
- **Critical**: breaks usability or accessibility (unreadable contrast, broken mobile layout, missing error handling on a key flow)
- **Quick win**: small effort, visible improvement (consistent spacing, better empty states, focus styles, button loading states)
- **Structural**: needs foundation work (introduce tokens, consolidate components, RTL migration, navigation redesign)

Put the list in the plan's "Current State" section, and use it to order the milestones. Quick wins early give the developer visible progress, and structural foundations must come before screens that depend on them.

# Stack Guide

The skill works with any stack. For **existing projects**, the stack you find is a constraint: design within it, and list any new dependency in the plan with its reason. For **new projects**, recommend a stack that fits the direction, the developer's experience and the product, and offer an alternative.

## Ask or detect first

- What does the developer already know and like? Their preference beats a theoretically better choice. They'll maintain it.
- Platform: web only, mobile web, native mobile, desktop?
- Content-heavy/SEO (marketing, blog, e-commerce) or app-like (dashboard, tool)?

## Web foundations

| Need | Good defaults | Alternatives |
|---|---|---|
| App framework | Next.js (React) | Vite + React, Nuxt (Vue), SvelteKit, Angular, Remix/React Router, Solid |
| Content / marketing site | Astro (ship little JS, add islands) | Next.js, Nuxt, plain HTML + CSS |
| Styling | Tailwind CSS (fast, token-friendly) | CSS Modules + CSS variables, vanilla-extract, Sass, UnoCSS |
| Accessible primitives | Radix UI / shadcn/ui (React), React Aria | Headless UI, Ark UI (multi-framework), Reka UI / shadcn-vue (Vue), Bits UI / shadcn-svelte (Svelte), Angular CDK |
| Full component library (fast, less distinctive) | Mantine, MUI (Material), Fluent UI (Fluent), Ant Design (dense enterprise) | Chakra, PrimeReact/PrimeVue, Vuetify |
| Icons | Lucide | Phosphor (many weights, good for expressive styles), Heroicons, Tabler, Material Symbols |
| Forms | React Hook Form + Zod | TanStack Form, VeeValidate (Vue), Superforms (Svelte) |
| Charts | Recharts, Tremor (dashboards) | Visx, ECharts, Chart.js, Nivo, Observable Plot |

Headless primitives plus your own styling give full design control with accessibility handled. Full libraries are faster but look like themselves unless heavily themed. Pick based on how distinctive the direction must be.

## By style needs

| Direction needs | Recommend |
|---|---|
| Micro-interactions, layout animations, shared transitions | Motion (formerly Framer Motion) for React; Vue: `@vueuse/motion` or Motion One; Svelte built-in transitions; the native View Transitions API |
| Scrollytelling, pinned sections, complex timelines | GSAP + ScrollTrigger (free for all uses since 2025), Lenis for smooth scroll (use carefully) |
| Simple scroll reveals | CSS scroll-driven animations (`animation-timeline: view()`) with a fallback, or Intersection Observer |
| Immersive 3D / WebGL | three.js; React Three Fiber + drei for React; TresJS for Vue; Threlte for Svelte |
| 3D objects without code | Spline (embed or export), then optimize |
| Illustrations / animated icons | Lottie (lottie-web or dotLottie), Rive (interactive, state machines) |
| Liquid Glass refraction | SVG `feDisplacementMap` filters for simple cases; WebGL shaders for realistic ones |
| Grain / noise | Tiled PNG noise (cheapest) or SVG `feTurbulence` |
| Kinetic / split text | GSAP SplitText (free now), Splitting.js, Motion's text utilities |
| Hand-drawn look | Rough.js, Rough Notation |
| Dense data tables | TanStack Table (+ TanStack Virtual), AG Grid for heavy enterprise needs |
| Theming / dark mode | CSS variables + `data-theme`; next-themes for Next.js |
| i18n / RTL | next-intl, i18next/react-i18next, vue-i18n, Paraglide; Tailwind logical utilities |

## Native and cross-platform

| Platform | Notes |
|---|---|
| React Native / Expo | NativeWind (Tailwind for RN), Tamagui, Reanimated for motion, Expo Router. `I18nManager` for RTL (needs a restart to flip) |
| Flutter | ThemeData + custom extensions for tokens; `flutter_animate`; Material 3 by default; Cupertino widgets for iOS feel; built-in RTL via `Directionality` |
| SwiftUI | Follow HIG; asset catalogs for colors (light/dark); SF Symbols; built-in leading/trailing |
| Jetpack Compose | Material 3 with dynamic color; custom `CompositionLocal` for extra tokens |

## Fonts: loading and fallbacks

- **Next.js:** `next/font/google` downloads fonts at build time. If the build environment blocks Google Fonts (sandboxes, CI behind a firewall, offline builds), switch to **Fontsource** (`npm i @fontsource-variable/<font>` or `@fontsource/<font>`), import it in the root layout, and reference the family in the tokens. The result is also self-hosted, with no runtime dependency on Google. `next/font/local` with files in the repo is another option.
- **Other frameworks:** Fontsource works in any bundler (Vite, Astro, Nuxt, SvelteKit). Plain HTML can self-host WOFF2 files with `@font-face`.
- **Subsets:** import only the scripts you need (e.g. `latin` + `hebrew`) to keep the payload small.
- Record the choice in the plan's Stack section, and if you switch during execution, log it in the changelog as a deviation.

## Principles

- **Don't add a library for one effect.** A 60KB animation library for one fade is not worth it; CSS can do it.
- **Check maintenance and license** before recommending (recent releases, license fits the project).
- **Match the team.** In a collaborative project, prefer what the team already knows.
- **List every new dependency** in the plan's Stack section with its reason and its approximate size for web.

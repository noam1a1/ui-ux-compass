# Performance Budget

A beautiful interface that stutters or loads slowly is a bad experience. Set a budget in the plan (section 13), especially when the direction includes heavy styles.

## Targets (Core Web Vitals, 75th percentile of real users)

- **LCP** (largest content visible): ≤ 2.5s
- **INP** (response to interactions): ≤ 200ms
- **CLS** (layout shift): ≤ 0.1
- Animations: a steady 60fps on a mid-range phone

## Heavy styles and their fallbacks

| Style / feature | Cost | Mitigation |
|---|---|---|
| Glass / Acrylic / Liquid Glass (`backdrop-filter`, SVG filters) | GPU per frame, worse while scrolling | Limit the number of blurred surfaces; smaller blur radius on mobile; opaque fallback on low-end devices or under `prefers-reduced-transparency` |
| Aurora / animated gradients / big blurs | Constant repaints | Static image or very slow animation; pause when off-screen; `will-change` only while animating |
| Immersive 3D / WebGL | JS bundle, GPU, battery | Lazy-load the scene after the main content; compressed models (Draco/meshopt, KTX2 textures); cap device pixel ratio at 1.5–2; poster image fallback; pause when the tab is hidden |
| Scrollytelling / parallax | Scroll handlers, layout thrash | Animate only `transform` and `opacity`; use GSAP/ScrollTrigger or CSS scroll timelines; no scroll hijacking |
| Grain / noise overlays | Large SVG filters | Tiled PNG texture |
| Glow / neon (many shadows) | Paint cost | Fewer layers; pseudo-element with a blurred background instead of stacked shadows |
| Video backgrounds | Bandwidth | Short, muted, compressed (AV1/H.264), poster image, no autoplay on data saver or reduced motion |
| Maximalism / collage (many images) | Bandwidth | Responsive images, AVIF/WebP, lazy loading below the fold |

## General practices

- **Images**: correct sizes (`srcset`/`sizes` or the framework's image component), AVIF/WebP, explicit width/height or `aspect-ratio` (prevents CLS), `loading="lazy"` below the fold, priority for the LCP image
- **Fonts**: 2–3 files at most where possible; variable fonts; subset to the scripts needed (Latin + Hebrew subsets); `font-display: swap`; preload the main text font; size-adjusted fallbacks to reduce layout shift
- **Motion**: only `transform` and `opacity`; avoid animating layout properties (width, height, top); `prefers-reduced-motion` disables non-essential motion
- **Skeletons** reserve exact space so content doesn't jump in
- **JavaScript**: code-split routes and heavy components; don't ship animation or 3D libraries to pages that don't use them
- **Eco / low-carbon styles**: a real budget (e.g. < 1MB per page) fits the brand's message

## Verifying

- Lighthouse (lab) in the browser or CI; PageSpeed Insights for field data on deployed sites
- Performance panel in DevTools with CPU throttling (4×) to simulate mid-range phones
- Test heavy styles on an actual phone when possible

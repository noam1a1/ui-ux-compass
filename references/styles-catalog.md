# Styles Catalog

About 95 visual styles grouped into families. Use it to propose directions (Phase 2) and to check a style the developer already picked against the vision and constraints.

Each entry has:
- **Fits**: products, audiences and moods it serves well
- **Avoid**: where it works against the product
- **Signature**: the concrete traits that make it recognizable (use these when specifying tokens and components)
- **Watch**: accessibility, performance or aging risks

## Contents

- [How to choose](#how-to-choose)
- [Product-type matrix](#product-type-matrix)
- [Combining styles](#combining-styles)
- A. [Glass & Translucency](#a-glass--translucency)
- B. [Soft & Tactile](#b-soft--tactile)
- C. [Flat & Systematic](#c-flat--systematic)
- D. [Minimal & Calm](#d-minimal--calm)
- E. [Dark](#e-dark)
- F. [Luxury & Editorial](#f-luxury--editorial)
- G. [Raw & Rebellious](#g-raw--rebellious)
- H. [Layout Systems](#h-layout-systems)
- I. [Color & Gradient](#i-color--gradient)
- J. [Metallic & Glossy](#j-metallic--glossy)
- K. [3D & Spatial](#k-3d--spatial)
- L. [Typography-Led](#l-typography-led)
- M. [Motion-Led](#m-motion-led)
- N. [Retro & Nostalgia](#n-retro--nostalgia)
- O. [Futuristic & Tech](#o-futuristic--tech)
- P. [Expressive & Playful](#p-expressive--playful)
- Q. [Organic & Natural](#q-organic--natural)
- R. [Geometric & Art Movements](#r-geometric--art-movements)
- S. [Accessibility-First](#s-accessibility-first)

---

## How to choose

1. **Start from the feel, not the trend.** Take the 3–5 adjectives from discovery ("calm, trustworthy, premium") and find the styles whose Fits line matches them.
2. **Filter by constraints.** Remove styles whose Watch line conflicts with a hard constraint: strict accessibility, low-end devices, a dense data product, an existing brand.
3. **Filter by lifespan.** Products meant to last years (banking, B2B, government) need styles that age slowly (Swiss, Minimalism, Material, Tech Minimalism). Campaign sites, launches and portfolios can use trendier styles.
4. **Pick 2–3 contrasting directions.** Proposing three near-identical minimal styles is not a real choice. Offer a safe option, a distinctive option, and something in between.
5. **Explain each one** in terms of this product's users, not in general terms.

## Product-type matrix

Starting points, not rules. The vision always overrides the matrix.

| Product type | Strong candidates | Use with care |
|---|---|---|
| B2B SaaS / productivity | Tech Minimalism, Swiss, Bento Grid, Card-Based, Micro-Interaction Design, Dark UI | Maximalism, Brutalism, heavy 3D |
| Developer tools | Terminal/CLI, Tech Minimalism, Dark UI, Data-Dense, Monochrome | Claymorphism, Kawaii |
| Admin / internal dashboard | Dashboard/Modular, Data-Dense, Material, Fluent, Flat | Glassmorphism (contrast), Parallax |
| Fintech / banking | Tech Minimalism, Swiss, Luxury Minimalism, Dark Luxe, Material You | Anti-Design, Glitch, Y2K |
| Healthcare / public services | High-Contrast, Flat, Material, Calm UI, Minimalism | Neumorphism, Glass, low-contrast palettes |
| AI product | AI/Futuristic SaaS, Aurora UI, Gradient Minimalism, Chat-First, Tech Minimalism | Skeuomorphism, Retro UI |
| Luxury / fashion e-commerce | Luxury Minimalism, Editorial Luxury, Oversized Typography, Dark Luxe | Corporate Memphis, Sticker UI |
| General e-commerce | Card-Based, Minimalism, Flat, Micro-Interaction Design | Anti-Grid, Brutalism on checkout |
| Portfolio / creative agency | Neo-Brutalism, Kinetic Typography, Scrollytelling, Immersive 3D, Anti-Grid, Experimental Typography | Material, Fluent (too generic) |
| Media / content / blog | Editorial Design, Typography-First, Swiss, Minimalism | Motion-First (distracts from reading) |
| Education / kids | Claymorphism, Kawaii, Hand-Drawn, Gamified, Soft 3D | Brutalism, Dark Luxe |
| Gaming / entertainment | Cyberpunk, FUI/HUD, Synthwave, Pixel Art, Immersive 3D, Neon/Glow | Ultra Minimalism |
| Wellness / meditation | Calm/Zen, Japandi, Organic, Eco/Natural, Soft 3D | Glitch, Data-Dense |
| Sustainability / nonprofit | Eco/Natural, Solarpunk, Organic, Editorial | Chrome, Cyberpunk |
| Product launch / landing page | Scrollytelling, Aurora, Bento Grid, Oversized Typography, Soft 3D | Data-Dense |
| Web3 / crypto | Holographic, Chrome, Dark UI, Neon/Glow, FUI/HUD | Corporate Memphis |
| Music / events / nightlife | Synthwave, Vaporwave, Maximalism, Kinetic Typography, Grainy Gradient | Corporate Memphis, Material |

## Combining styles

Most good directions combine layers:

- **One primary visual language** (e.g. Tech Minimalism, Neo-Brutalism, Glassmorphism)
- **One layout system** (e.g. Bento Grid, Card-Based, Editorial)
- **At most one accent**: motion (Micro-Interaction Design, Scrollytelling) or typography (Oversized, Kinetic)

Combinations that usually clash: Brutalism with Luxury Minimalism, Neumorphism with Maximalism, Data-Dense with Scrollytelling, Kawaii with Dark Luxe. Clashes can be intentional (anti-design does this on purpose), but say so in the plan.

Many styles work as a **theme layer** (Dark UI, Monochrome, Grainy Gradient) or an **interaction layer** (Micro-Interaction Design, Motion-First) on top of another style.

---

## A. Glass & Translucency

### Glassmorphism
Frosted, translucent panels floating over vivid, colorful backgrounds; depth comes from blur and layering.
- **Fits:** Modern consumer apps, landing pages, music and media players, widgets, overlays on photography.
- **Avoid:** Text-heavy or data-dense screens, strict accessibility requirements, low-end mobile audiences.
- **Signature:** `backdrop-filter: blur(12–24px)`; surfaces at 10–25% white or black; 1px semi-transparent light border; soft large shadows; saturated gradient or photo backgrounds behind.
- **Watch:** Contrast changes with whatever sits behind the panel, so test it on the worst background. Blur is expensive on low-end GPUs. Provide an opaque fallback when `prefers-reduced-transparency` is set or `backdrop-filter` isn't supported.

### Liquid Glass / Glass 2.0
The evolved glass look popularized by recent OS redesigns: glass that refracts, bends light at its edges and reacts to movement and content beneath it.
- **Fits:** Premium consumer apps, OS-like interfaces, media, product launches aiming at a current Apple-era feel.
- **Avoid:** Enterprise dashboards, content-heavy reading, products that must stay neutral for years.
- **Signature:** Specular edge highlights; lensing/refraction (SVG displacement filters or WebGL); dynamic tinting from the content behind; pill-shaped floating controls; controls that morph between states.
- **Watch:** Most expensive of the glass styles; refraction usually needs WebGL or SVG filters. Legibility of controls over busy content. Tied to a specific platform look, so it will date.

### Frosted Glass / Acrylic UI
A calmer, more functional glass (Microsoft's Acrylic/Mica): heavy blur plus noise texture and a tint, used mostly for chrome such as sidebars, title bars and menus.
- **Fits:** Desktop-like web apps, productivity tools, settings panels, apps that want depth without drama.
- **Avoid:** Primary content surfaces, marketing pages that need punch.
- **Signature:** High blur (30px+), a subtle noise layer (2–4% opacity), a tint color layered on top, glass used only on navigation and overlays.
- **Watch:** Same performance cost as glass. Keep the tint strong enough that text contrast is stable.

## B. Soft & Tactile

### Neumorphism / Soft UI
Elements that look extruded from or pressed into the same surface, created with paired light and dark shadows and almost no color contrast.
- **Fits:** Small, focused tools (calculators, smart-home controls, music players), concept pieces.
- **Avoid:** Almost any product with many controls or accessibility needs. Buttons don't look like buttons.
- **Signature:** Background and element share one color; two shadows (light top-left, dark bottom-right); inset shadows for pressed states; generous radii.
- **Watch:** Serious accessibility problems: very low contrast between controls and background, and unclear affordances. If used, add clear borders, focus rings and an accent color for primary actions.

### Claymorphism
Puffy, inflated 3D-looking elements that seem made of soft clay: rounded, bright, friendly.
- **Fits:** Kids and education, casual games, playful consumer apps, onboarding illustrations, fintech aimed at young users.
- **Avoid:** Serious B2B, luxury, data-heavy products.
- **Signature:** Large radii (24px+); double inner shadows (light top, dark bottom) plus a soft outer shadow; pastel or candy colors; often paired with 3D clay illustrations.
- **Watch:** Easy to overdo. Keep text on flat surfaces for legibility.

### Skeuomorphism
Interfaces that imitate real-world materials and objects: leather, paper, wood grain, real knobs and switches.
- **Fits:** Music production tools, games, niche nostalgic products, products where the physical metaphor helps (a synth, a notebook).
- **Avoid:** General web apps; it feels dated unless deliberate.
- **Signature:** Realistic textures, lighting and shadows; objects that mirror physical controls; ornate details.
- **Watch:** Heavy assets, hard to scale and to keep consistent. Metaphors can confuse when they break.

### Neo-Skeuomorphism
A modern, restrained take on skeuomorphism: realistic lighting and material hints on otherwise clean UI, with just enough physicality to make controls feel touchable.
- **Fits:** Hardware companion apps, audio apps, premium consumer tools, widgets.
- **Avoid:** Dense enterprise screens.
- **Signature:** Subtle gradients that imitate light; realistic toggles, dials and buttons; soft layered shadows; small texture hints; still minimal overall.
- **Watch:** Consistency. Every control needs the same light source and material logic.

### Tactile UI
Interfaces designed to feel physically responsive: pressable buttons with real "give", springy feedback and haptic-like motion. Closer to a behavior than a look.
- **Fits:** Mobile-first consumer apps, games, anything where feel is a selling point; pairs well with Claymorphism, Neo-Skeuomorphism and Neo-Brutalism.
- **Avoid:** Products where motion would slow down expert users.
- **Signature:** Press states that depress (translate/scale down 2–4%), spring easings, sound or haptics on native, bouncy toggles.
- **Watch:** Respect `prefers-reduced-motion`. Keep feedback fast (under 150ms to start).

## C. Flat & Systematic

### Flat Design
No depth effects: solid colors, simple shapes, crisp icons and clear typography.
- **Fits:** Almost anything that needs to be clear and fast: utilities, public services, admin tools, MVPs.
- **Avoid:** Products that need to feel premium or emotionally rich (add a stronger accent layer instead).
- **Signature:** Solid fills, no or minimal shadows, bold simple icons, clear color-coded states.
- **Watch:** Pure flat can hide affordances (what's clickable?). Most modern teams use "flat 2.0" with subtle shadows for elevation.

### Material Design
Google's design system: a paper-and-ink metaphor, elevation, grid-based layout and meaningful motion. Mature components and guidelines.
- **Fits:** Android apps, admin tools, products that need a proven system quickly, teams without a designer.
- **Avoid:** Brands that need a distinctive identity (it looks generic unless customized).
- **Signature:** Elevation scale, 8dp grid, FAB, ripple feedback, standard component shapes, Roboto-style typography.
- **Watch:** Recognizable as "default Google". Customize shape, color and type to stand out.

### Material You (M3)
Material Design 3: dynamic color derived from a seed or wallpaper, larger rounder shapes, tonal palettes and more expressive components.
- **Fits:** Android-first products, personal and consumer apps, products that want a friendly and current system.
- **Avoid:** Products that need a strict brand color everywhere (dynamic color can override it).
- **Signature:** Tonal palettes (primary/secondary/tertiary plus containers), large radii, pill buttons, surface tints instead of shadows.
- **Watch:** Check contrast of generated tonal pairs; they're designed for it, but custom seeds can break it.

### Apple Human Interface (HIG) style
The iOS/macOS visual language: clarity, deference to content, depth through translucency and hierarchy. Now includes Liquid Glass.
- **Fits:** iOS-first apps, web apps that want a native-Apple feel, premium consumer tools.
- **Avoid:** Android-first audiences (feels foreign), heavily branded experiences.
- **Signature:** SF-style typography, large titles, grouped inset lists, translucent bars, system colors, SF Symbols-style icons, generous touch targets.
- **Watch:** Don't imitate Apple branding or ship Apple's proprietary fonts or icons on the web without checking their license.

### Fluent Design
Microsoft's system: light, depth, motion, material (Acrylic/Mica) and scale, built for Windows and Microsoft 365.
- **Fits:** Productivity and enterprise tools, Microsoft ecosystem integrations, desktop-like web apps.
- **Avoid:** Consumer products that need warmth or playfulness.
- **Signature:** Acrylic/Mica surfaces, reveal highlights, Segoe-style typography, clear focus visuals, Fluent UI icon set.
- **Watch:** Can feel corporate. Fluent UI React gives accessible components out of the box.

### Swiss / International Style
Modernist graphic design: strict grids, asymmetric layouts, sans-serif typography, objective clarity and strong hierarchy.
- **Fits:** Corporate sites, portfolios, editorial pages, SaaS marketing, anything that needs authority and clarity.
- **Avoid:** Playful or cozy products.
- **Signature:** Visible grid logic, flush-left ragged-right text, Helvetica/Inter/Neue Haas-style type, big type contrast, a restrained palette often with one strong accent (red is classic), generous white space.
- **Watch:** Ages very well. Risk of feeling cold; warm it with photography or an accent color.

## D. Minimal & Calm

### Minimalism
Only what's needed: lots of white space, a limited palette, strong typography, few elements.
- **Fits:** Almost everything, especially premium products, portfolios, content products and tools that want focus.
- **Avoid:** Products whose users need lots of information at once (use Data-Dense instead).
- **Signature:** Generous spacing, 1–2 typefaces, restrained palette plus one accent, few decorations, clear hierarchy.
- **Watch:** Minimal is not empty. Hidden navigation and unlabelled icons hurt usability. Can be generic without a strong typographic voice.

### Ultra Minimalism
Minimalism pushed to the edge: nearly nothing on screen but type and space, often monochrome, sometimes hiding UI until needed.
- **Fits:** Portfolios, luxury brands, art projects, single-purpose tools.
- **Avoid:** Anything with many features or first-time users who need guidance.
- **Signature:** Tiny UI chrome, big empty areas, one typeface, hover-revealed controls, extreme restraint.
- **Watch:** Discoverability. Test that first-time users find the main actions.

### Monochrome UI
A single hue (or pure grayscale) across the whole interface; hierarchy comes from value, weight and space.
- **Fits:** Developer tools, editorial, fashion, photography portfolios (lets content carry color), focused productivity apps.
- **Avoid:** Products that need color-coded status everywhere (dashboards, monitoring), unless status colors are a deliberate exception.
- **Signature:** One hue's tonal scale, strong typographic hierarchy, borders and weight instead of color.
- **Watch:** Status (error, success) must still be distinguishable. Allow semantic colors as the exception, and never rely on color alone.

### Tech Minimalism
The clean, precise look of modern tech products (Linear, Vercel, Stripe era): neutral palettes, sharp type, subtle borders, fine detail.
- **Fits:** SaaS, developer tools, fintech, B2B, AI products, anything that wants to feel competent and fast.
- **Avoid:** Warm, emotional consumer brands, kids.
- **Signature:** Inter/Geist-style type, 1px hairline borders, subtle gradients or glows, tight 4px spacing grid, keyboard shortcuts visible, dark mode as a first-class citizen, restrained motion.
- **Watch:** Very common now, so it can look like every other startup. Add identity through one signature element (color, illustration, motion).

### Gradient Minimalism
Minimal layouts where soft gradients provide almost all of the color and personality.
- **Fits:** SaaS landing pages, AI products, apps that want minimal plus warmth.
- **Avoid:** Data-dense UI (gradients behind data hurt readability).
- **Signature:** Large soft gradient areas or accents, clean type, few elements, gradient buttons or highlights.
- **Watch:** Text over gradients needs contrast checks at both ends of the gradient. Banding on large areas, so add a little noise.

### Scandinavian / Nordic
Functional warmth: light neutral palettes, natural tones, clean type and a cozy, human feel.
- **Fits:** Lifestyle, home, furniture, wellness, family products, calm productivity.
- **Avoid:** High-energy entertainment, gaming.
- **Signature:** Off-white and warm grays, muted natural accents (sage, sand, clay), rounded sans, soft photography, simple line icons.
- **Watch:** Can look bland. Invest in photography and texture.

### Japandi Digital
Japanese minimalism meets Scandinavian warmth: calm, balanced, natural materials, intentional emptiness.
- **Fits:** Wellness, meditation, tea/coffee/craft brands, architecture, premium lifestyle.
- **Avoid:** Busy apps with many features.
- **Signature:** Muted earthy palette, generous negative space, asymmetric balance, thin elegant type (serif or light sans), natural textures, slow gentle motion.
- **Watch:** Low-contrast earthy palettes can fail WCAG, so check them.

### Calm / Zen UI
Interfaces designed to lower stress: slow pace, few choices at once, soft colors, no urgency patterns.
- **Fits:** Meditation, mental wellness, journaling, sleep, healthcare patient-facing apps.
- **Avoid:** Products where speed and density matter more than mood.
- **Signature:** One action per screen, soft palettes, slow easing (400–800ms), breathing-like animations, no red badges or countdowns, rounded shapes.
- **Watch:** Don't hide important information for the sake of calm. Respect reduced motion.

## E. Dark

### Dark UI / Dark Mode
Dark surfaces with light content. Either a theme option or the default identity.
- **Fits:** Developer tools, media and video, gaming, creative tools, dashboards used for long sessions, night use.
- **Avoid:** Long-form reading as the only mode, some older audiences; always offer light mode where reading matters.
- **Signature:** Dark grays (not pure #000, e.g. #0B0B0F to #1A1A1F), elevation shown by lighter surfaces instead of shadows, desaturated accents, off-white text (not pure white).
- **Watch:** Saturated colors vibrate on dark, so desaturate them. Check contrast of secondary text. Design both themes from tokens, not by inverting.

### Dark Luxe
Dark, rich and premium: deep blacks, metallic or jewel-tone accents, elegant type.
- **Fits:** Luxury brands, premium fintech cards, high-end hospitality, watches, cars, exclusive memberships.
- **Avoid:** Friendly mass-market products, kids.
- **Signature:** Near-black with warm or cool undertones, gold/champagne/emerald accents, serif or refined sans display type, slow reveals, fine hairlines.
- **Watch:** Gold on black often fails contrast at small sizes. Keep body text off-white.

### Neon / Glow UI
Dark backgrounds with glowing, electric accents: light as the main decorative element.
- **Fits:** Gaming, nightlife, music, esports, crypto, bold tech launches.
- **Avoid:** Calm or trust-heavy products (banking, health).
- **Signature:** Dark base, saturated neon accents (cyan, magenta, lime), glow via layered `box-shadow`/`text-shadow` or blur, gradient strokes.
- **Watch:** Glow on text reduces legibility; keep body text plain. Many large glows are expensive to render.

## F. Luxury & Editorial

### Luxury Minimalism
Restrained elegance: vast space, refined type, very few elements, high-quality imagery.
- **Fits:** Fashion, jewelry, real estate, boutique hotels, premium DTC brands.
- **Avoid:** Budget or mass-market products, dense catalogs that need filters everywhere.
- **Signature:** Thin or high-contrast serifs, wide letter-spacing on small caps labels, neutral palette (ivory, black, stone), full-bleed photography, slow fades.
- **Watch:** Thin light type fails contrast easily. Keep product and checkout flows clear and not just pretty.

### Editorial Design
Layouts inspired by magazines and newspapers: strong typographic hierarchy, columns, pull quotes and rich imagery.
- **Fits:** Media, blogs, long-form storytelling, brand journals, case studies.
- **Avoid:** Task-oriented apps and dashboards.
- **Signature:** Serif headlines with sans body (or the reverse), multi-column grids, drop caps, captions, pull quotes, varied image sizes, section rules.
- **Watch:** Multi-column layouts must collapse well on mobile. Reading comfort: 60–75 characters per line.

### Editorial Luxury
Editorial layout plus luxury restraint: fashion-magazine feel with big imagery and elegant type.
- **Fits:** Fashion houses, luxury e-commerce storytelling, art galleries, architecture studios.
- **Avoid:** Functional apps.
- **Signature:** Oversized serif headlines, asymmetric image placement, lots of white space, small elegant captions, slow scroll reveals.
- **Watch:** Heavy imagery, so optimize images aggressively.

### Art Deco
1920s glamour: geometric ornament, symmetry, gold lines, stepped forms and elegant display type.
- **Fits:** Hospitality, events, luxury spirits, theaters, weddings, heritage brands.
- **Avoid:** Modern tech and productivity.
- **Signature:** Symmetry, sunburst and fan motifs, thin gold/brass lines, black/cream/emerald palettes, geometric display fonts.
- **Watch:** Ornament can clutter UI; keep it to frames and headers.

## G. Raw & Rebellious

### Brutalism
Raw, unpolished web: default-looking elements, visible structure, harsh contrast, intentionally "undesigned".
- **Fits:** Art projects, indie publications, experimental portfolios, statements.
- **Avoid:** Commerce, finance, anything that needs trust or broad usability.
- **Signature:** System fonts, default blue links, raw borders, no rounding, stark black and white, dense text, unusual layouts.
- **Watch:** Easy to become actually unusable. Keep semantics and accessibility intact under the rough look.

### Neo-Brutalism
Brutalism made friendly and usable: thick black outlines, hard offset shadows, flat bright colors and bold type.
- **Fits:** Startups with personality, creative tools, portfolios, Gen-Z products, playful SaaS landing pages.
- **Avoid:** Luxury, healthcare, conservative finance.
- **Signature:** 2–4px black borders, hard shadows with no blur (e.g. `4px 4px 0 #000`), saturated flat colors (yellow, pink, lime, blue), chunky type, press states that shift the shadow.
- **Watch:** Very trendy. Loud colors can tire users in long sessions; keep app interiors calmer than marketing pages.

### Anti-Design
Deliberately breaking conventions (clashing colors, chaotic layouts, odd type) to provoke and stand out.
- **Fits:** Fashion campaigns, music, art, youth culture brands, one-off campaign sites.
- **Avoid:** Any product people need to use efficiently.
- **Signature:** Clashing palettes, overlapping elements, distorted type, unusual cursors, rule-breaking navigation.
- **Watch:** Keep the conversion path (buy, sign up) clear, and treat chaos as decoration.

### Anti-Grid
Layouts that escape the grid: elements float, overlap and break alignment on purpose.
- **Fits:** Portfolios, creative agencies, editorial features, galleries.
- **Avoid:** Forms, dashboards, e-commerce listings.
- **Signature:** Overlapping images and text, irregular positions, rotated elements, big spacing variation.
- **Watch:** Responsive behavior is hard; plan explicit mobile layouts. Keep reading order logical in the DOM.

### Glitch / Databending
Digital corruption as aesthetic: RGB splits, scanlines, pixel sorting, distortion.
- **Fits:** Music, gaming, cyber-security brands, tech events, art.
- **Avoid:** Anything where users might think the product is actually broken.
- **Signature:** Chromatic aberration, displaced slices, noise, flicker, corrupted type.
- **Watch:** Flicker can trigger photosensitive seizures. Never flash more than 3 times per second, and disable under reduced motion.

## H. Layout Systems

### Bento Grid
Content arranged in a grid of varied rectangular tiles, like a bento box. Each tile holds one idea.
- **Fits:** Feature showcases on landing pages, personal pages, dashboards, product overviews.
- **Avoid:** Linear content (articles), long forms.
- **Signature:** Rounded tiles of mixed sizes (1×1, 2×1, 2×2), consistent gaps, each tile with one visual plus a short label, subtle hover motion.
- **Watch:** Needs a planned mobile stacking order. Don't cram too much into one tile.

### Card-Based UI
Content in self-contained cards: flexible, scannable and responsive.
- **Fits:** Feeds, catalogs, e-commerce, dashboards, content libraries.
- **Avoid:** Content that needs comparison across rows (use tables).
- **Signature:** Consistent card anatomy (media, title, meta, actions), a clear clickable area, uniform spacing.
- **Watch:** Too many cards look like noise; group and prioritize. Define empty and loading (skeleton) cards.

### Dashboard / Modular UI
Screens made of modules or widgets (charts, KPIs, lists) that can be arranged and sometimes customized.
- **Fits:** Analytics, admin, monitoring, finance, CRM.
- **Avoid:** Marketing pages, simple consumer flows.
- **Signature:** KPI tiles, charts, filters bar, sidebar navigation, consistent widget chrome, drag-to-rearrange if customizable.
- **Watch:** Prioritize. Not everything deserves the top row. Each widget needs its own loading, empty and error state.

### Data-Dense / Utilitarian UI
Maximum information per screen for expert users: tables, compact rows, keyboard-driven.
- **Fits:** Trading, ops consoles, spreadsheets, logs, internal tools, power-user software.
- **Avoid:** Novice users, marketing.
- **Signature:** Compact spacing (4px grid, 28–32px rows), tabular numerals, monospace for data, sticky headers, dense tables with sorting and filtering, keyboard shortcuts.
- **Watch:** Tiny targets and text; offer density settings (compact/comfortable). Make sure density doesn't break zoom and screen readers.

### Chat-First / Conversational UI
The conversation is the main interface, with rich UI elements embedded in the thread.
- **Fits:** AI assistants, support, onboarding flows, booking, companions.
- **Avoid:** Tasks that are faster with direct manipulation (editing a table, browsing a catalog).
- **Signature:** Message thread, a composer with attachments, streaming responses, suggested replies/chips, embedded cards, clear typing/thinking states.
- **Watch:** Streaming and long waits need good loading states. Keep previous answers scannable, and design error and retry for failed messages.

## I. Color & Gradient

### Aurora UI
Soft, blurred, glowing color blobs drifting in the background like northern lights.
- **Fits:** AI and SaaS landing pages, hero sections, launches, apps that want atmosphere.
- **Avoid:** Busy data screens, strict brand-color environments.
- **Signature:** Large blurred gradient blobs (often animated slowly), dark or light base, content on clean surfaces above.
- **Watch:** Animated large blurs cost GPU; use static images or CSS with care on mobile. Check text contrast over the brightest spot.

### Mesh Gradient
Complex multi-point gradients that flow smoothly between several colors.
- **Fits:** Brand backgrounds, hero sections, cards, app icons, onboarding.
- **Avoid:** Behind body text.
- **Signature:** 3–5 colors blending organically, often as a static image or SVG, sometimes lightly animated.
- **Watch:** Export as optimized images or CSS layered radial gradients. Watch for banding.

### Grainy Gradient
Gradients with film-grain noise for a tactile, analog, less digital feel.
- **Fits:** Creative brands, music, editorial, modern SaaS that wants warmth.
- **Avoid:** Ultra-clean technical products (unless used subtly).
- **Signature:** Gradient plus a noise overlay (SVG `feTurbulence` or a PNG texture at 5–15% opacity).
- **Watch:** Noise can hurt text legibility; keep text on clean surfaces. Large SVG filters can be slow, so a tiled PNG is cheaper.

### Duotone
Images and surfaces rendered in two colors only: bold, graphic and brand-consistent.
- **Fits:** Brand campaigns, editorial, music, events, making mixed photography feel unified.
- **Avoid:** Product photos where true color matters (fashion, food e-commerce).
- **Signature:** Photos mapped to two brand colors, limited palettes, strong contrast.
- **Watch:** Ensure the two colors have enough contrast for any text on them.

### Holographic / Iridescent
Shifting rainbow sheens like holographic foil or soap bubbles.
- **Fits:** Web3, fashion drops, beauty, music, youth brands, collectibles.
- **Avoid:** Serious and trust-based products.
- **Signature:** Pastel rainbow gradients, angle-dependent shimmer (animated gradients, pointer-reactive), pearl and foil textures.
- **Watch:** Pointer-reactive effects need a static fallback on touch and reduced motion. Busy under text.

## J. Metallic & Glossy

### Chrome / Liquid Metal
Reflective chrome and molten-metal surfaces, often 3D-rendered.
- **Fits:** Fashion, music, Y2K revival, tech launches, bold brand moments.
- **Avoid:** Everyday app interiors.
- **Signature:** Mirror-like gradients, 3D chrome type or objects, liquid morphing shapes (WebGL/Spline), dark or pastel backgrounds.
- **Watch:** Mostly a hero or brand effect. Heavy 3D assets, so lazy-load them and provide static fallbacks.

### Glossy / Aqua UI
Shiny, jelly-like buttons and surfaces with highlights (the early Mac OS X Aqua look).
- **Fits:** Nostalgic brands, playful products, retro revivals.
- **Avoid:** Products that must look current and neutral.
- **Signature:** Glossy highlight bands on buttons, saturated blues and greens, drop shadows, pill shapes, reflections.
- **Watch:** Reads as dated unless it is clearly intentional.

## K. 3D & Spatial

### 3D UI
Interfaces that use real 3D objects (rendered or live) as core elements: product views, icons, scenes.
- **Fits:** Product showcases, configurators, games, launches, hardware products.
- **Avoid:** Simple forms and utilities.
- **Signature:** 3D renders or live models (three.js, Spline), depth, lighting, rotation on interaction.
- **Watch:** Asset weight and GPU load. Always have a poster image fallback.

### Soft 3D
Friendly, matte, pastel 3D illustrations and icons, like soft plastic or clay renders.
- **Fits:** Onboarding, SaaS marketing, fintech for young users, empty states, education.
- **Avoid:** Luxury, serious editorial.
- **Signature:** Rounded 3D icons and characters, pastel palettes, soft ambient shadows, used as illustration rather than interactive 3D.
- **Watch:** Keep a consistent illustration style; mixed 3D sources look cheap. Use WebP/AVIF.

### Immersive 3D / WebGL
The whole experience is a 3D scene: camera movement, interactive worlds, shaders.
- **Fits:** Award-style portfolios, brand experiences, product launches, games, museums.
- **Avoid:** Anything task-oriented, audiences on low-end devices or bad networks.
- **Signature:** Full-screen canvas, scroll- or pointer-driven camera, shaders, postprocessing, audio.
- **Watch:** Performance, accessibility (canvas content is invisible to screen readers, so provide an HTML layer), battery, SEO. Needs a lightweight fallback path.

### Spatial UI
Interfaces designed for or inspired by spatial computing (visionOS and similar): floating glass windows, depth, gaze and hand-friendly targets.
- **Fits:** XR apps, forward-looking brand experiences, OS-style web demos.
- **Avoid:** Standard web apps pretending to be spatial without a reason.
- **Signature:** Floating glass panels with depth, large rounded targets, parallax between layers, soft lighting.
- **Watch:** On flat screens, the depth effects are only decoration, so keep them light.

### Low-Poly
Faceted 3D geometry with visible polygons and flat shading.
- **Fits:** Indie games, outdoor and travel, playful tech, data art.
- **Avoid:** Premium realistic products.
- **Signature:** Triangulated surfaces, flat-shaded facets, limited palettes, gradient-lit polygons.
- **Watch:** Can feel dated (2014 era) unless paired with modern type and layout.

### Isometric
Illustrations and diagrams drawn in isometric projection: 3D-looking but technical and orderly.
- **Fits:** SaaS explainers, infrastructure and dev tools, games, maps, onboarding diagrams.
- **Avoid:** Emotional or photographic brands.
- **Signature:** 30° isometric grid, consistent light source, small detailed scenes, flat colors.
- **Watch:** Custom illustration takes effort; keep a single style across all illustrations.

## L. Typography-Led

### Kinetic Typography
Type that moves: letters animate, stretch, rotate or respond to scroll and pointer.
- **Fits:** Portfolios, brand launches, music, events, hero sections.
- **Avoid:** Body text, forms, anything users must read carefully.
- **Signature:** Animated headlines, split-letter animations, marquee text, scroll-scrubbed type.
- **Watch:** Reduced motion. Screen readers must still get the text once and in the right order (animate spans but keep an accessible label).

### Oversized Typography
Huge headlines that dominate the layout: type as the main visual.
- **Fits:** Landing pages, portfolios, fashion, editorial, bold SaaS marketing.
- **Avoid:** Dense apps.
- **Signature:** Display type at 8–20vw, tight leading, strong contrast with small body text, few images.
- **Watch:** Fluid sizing with `clamp()`. Long words overflow on mobile, especially in German and with Hebrew fonts, so test real copy.

### Typography-First
Design where typographic hierarchy does almost all of the work: few images, few decorations.
- **Fits:** Blogs, documentation, writing tools, portfolios, editorial products, minimal SaaS.
- **Avoid:** Visual products (photography, e-commerce) as the only approach.
- **Signature:** Carefully chosen type pairing, modular type scale, rhythm and spacing, meaningful use of weight and style.
- **Watch:** Font loading (FOUT/FOIT); subset fonts and use `font-display: swap`.

### Variable Typography
Uses variable fonts whose weight, width or other axes change smoothly, often responding to interaction.
- **Fits:** Brand sites, type-centric design, responsive headlines, playful interactions.
- **Avoid:** No real avoidance; it's a technique. Avoid gimmicky axis animation in apps.
- **Signature:** Weight or width that changes on hover or scroll, one variable file replacing many static weights.
- **Watch:** Hebrew and Arabic variable fonts exist but have fewer choices; check before promising.

### Experimental Typography
Type used as art: distorted, layered, custom letterforms, unusual compositions.
- **Fits:** Art, music, fashion, festivals, design studios.
- **Avoid:** Anything functional.
- **Signature:** Custom or distorted letterforms, overlapping text, text on paths, mixed fonts.
- **Watch:** Legibility and accessibility. Keep real, readable text available.

## M. Motion-Led

### Scrollytelling
A narrative told through scrolling: sections that reveal, transform and build a story step by step.
- **Fits:** Product launches, annual reports, data journalism, brand stories, case studies.
- **Avoid:** Pages users revisit to find information quickly.
- **Signature:** Pinned sections, step-based reveals, scroll-linked charts and visuals, chapter navigation.
- **Watch:** Don't hijack scroll speed. Must work without animation (reduced motion) and on mobile. Keep content in the DOM for SEO.

### Scroll-Driven Animation
Animations tied to scroll position (native CSS `animation-timeline: scroll()/view()` or JS).
- **Fits:** Landing pages, feature reveals, progress indicators, parallax-like effects.
- **Avoid:** Heavy use inside app screens.
- **Signature:** Elements that fade/slide/scale as they enter, progress bars, sticky transitions.
- **Watch:** Native CSS scroll timelines don't have full cross-browser support yet; feature-detect and fall back.

### Motion-First UI
Motion is part of the identity: transitions between states and screens are designed as carefully as the screens themselves.
- **Fits:** Consumer apps, premium tools, portfolios, onboarding.
- **Avoid:** Expert tools where speed matters more than delight.
- **Signature:** Shared-element transitions (View Transitions API), choreographed entrances, spring physics, consistent motion tokens.
- **Watch:** Motion must never block input. Keep durations short in app flows (150–300ms), and respect reduced motion.

### Micro-Interaction Design
Small, purposeful feedback moments: a button that confirms, a like that pops, a toggle that clicks.
- **Fits:** Almost every product; it's a layer, not a look.
- **Avoid:** Overusing it. Not every hover needs an animation.
- **Signature:** Hover/press/success feedback, animated icons, inline validation, subtle state transitions (100–200ms).
- **Watch:** Consistency. Define a small set of motion tokens and reuse them.

### Parallax
Layers moving at different speeds while scrolling to create depth.
- **Fits:** Storytelling pages, travel, games, portfolios.
- **Avoid:** Apps and content-heavy pages.
- **Signature:** Background/foreground speed difference, layered illustrations, hero depth.
- **Watch:** Can cause motion sickness, so disable under reduced motion. Use transforms only for performance.

## N. Retro & Nostalgia

### Retro UI
Interfaces borrowing from old operating systems and early web (Windows 95, classic Mac, early 2000s portals).
- **Fits:** Nostalgic products, games, indie tools, playful portfolios.
- **Avoid:** Serious modern products (unless used as a joke or campaign).
- **Signature:** Beveled windows, pixel or bitmap fonts, gray chrome, title bars, classic dialogs.
- **Watch:** Keep modern usability underneath: responsive, accessible, readable sizes.

### Y2K
Turn-of-the-millennium optimism: chrome, bubbles, bright blues, translucent plastics and futuristic type.
- **Fits:** Fashion, music, youth brands, beauty, events.
- **Avoid:** B2B, finance.
- **Signature:** Chrome and bubble type, iridescence, translucent colored plastics, stars and sparkles, tech-optimist motifs.
- **Watch:** Busy; keep functional areas clean.

### Frutiger Aero
Mid-2000s glossy optimism: sky blue, green nature, water bubbles, glossy glass and bright gradients.
- **Fits:** Nostalgia-driven brands, playful tech, eco-tech with a retro twist.
- **Avoid:** Products that must feel current and serious.
- **Signature:** Aqua and grass-green gradients, glossy surfaces, bubbles, clouds, lens flares, humanist sans (Frutiger-like).
- **Watch:** Recognized mostly by younger audiences as nostalgia; make sure the audience gets it.

### Vaporwave
Ironic 80s/90s internet nostalgia: pastel pinks and teals, Greek statues, grids, glitchy retro computing.
- **Fits:** Music, art, merch, niche communities.
- **Avoid:** Practically any mainstream product.
- **Signature:** Pink/teal/purple gradients, marble busts, palm trees, wireframe grids, Japanese text as decoration, VHS artifacts.
- **Watch:** Using Japanese text as decoration can be meaningless or wrong, so check it with a speaker.

### Synthwave
80s retro-futurism in neon: sunset gradients, chrome, wireframe grids, night drives.
- **Fits:** Music, gaming, events, retro tech brands.
- **Avoid:** Calm or trust products.
- **Signature:** Magenta/purple/orange sunsets, neon grid horizons, chrome type, dark backgrounds, glow.
- **Watch:** Glow and neon contrast issues, same as Neon UI.

### Retro-Futurism
The future as imagined in the past: space-age optimism, atomic-era curves, 60s/70s sci-fi interfaces.
- **Fits:** Space and science brands, entertainment, creative agencies, events.
- **Avoid:** Everyday utilities.
- **Signature:** Rounded capsule shapes, warm oranges and teals, retro sci-fi type, atomic motifs, analog dials.
- **Watch:** Easy to overdecorate; keep the motif to the brand layer.

### Pixel Art UI
Interfaces built from visible pixels: bitmap fonts, sprites, 8/16-bit aesthetics.
- **Fits:** Indie games, gaming communities, playful tools, retro campaigns.
- **Avoid:** Content-heavy reading.
- **Signature:** Bitmap fonts, crisp pixel edges (`image-rendering: pixelated`), limited palettes, sprite icons, chunky borders.
- **Watch:** Pixel fonts at small sizes are hard to read; use them for headings and a normal font for body text.

### Dithering / 1-bit
Images and gradients rendered with dithering patterns, often in 1-bit black/white or a tiny palette: early Mac and e-ink vibes.
- **Fits:** Indie tools, creative portfolios, low-energy/eco sites, tech art, retro brands.
- **Avoid:** Photo-dependent commerce.
- **Signature:** Dithered images (Bayer/Floyd-Steinberg), 1-bit palettes, pixel-perfect lines, monospace or bitmap type.
- **Watch:** Dithering can shimmer when scaled; render at integer scales.

## O. Futuristic & Tech

### Cyberpunk UI
High-tech dystopia: neon on black, glitch, angular frames, dense data overlays.
- **Fits:** Games, esports, security products, sci-fi brands, hackathons.
- **Avoid:** Friendly consumer products, healthcare.
- **Signature:** Neon yellow/cyan/magenta on black, clipped/angled corners (`clip-path`), monospace, scanlines, glitch accents.
- **Watch:** Contrast, flicker (same as Glitch), and readability of angled layouts.

### Terminal / CLI Style
Interfaces that look like a command line: monospace, prompts, blinking cursors, text-first.
- **Fits:** Developer tools, dev portfolios, docs, hacker-culture brands, AI agents.
- **Avoid:** Non-technical audiences.
- **Signature:** Monospace everywhere, dark background, green/amber or modern palette, prompt characters, keyboard-first, ASCII accents.
- **Watch:** Don't make users type commands when a button is better. Keep real semantics (buttons, links) under the terminal look.

### FUI / HUD
Fictional user interfaces from sci-fi films: heads-up displays, targeting reticles, dense animated telemetry.
- **Fits:** Games, sci-fi brands, data visualization showpieces, automotive and aerospace concepts.
- **Avoid:** Real productivity where clarity matters.
- **Signature:** Thin lines, brackets and corner marks, numbers everywhere, radial gauges, cyan/orange on dark, constant subtle animation.
- **Watch:** Decorative data can mislead users; label what's real. Heavy constant animation drains battery.

### AI / Futuristic SaaS
The current AI-product look: dark or clean bases, glowing gradients, sparkle icons, orbs and a sense of intelligence.
- **Fits:** AI products, LLM tools, modern SaaS launches.
- **Avoid:** Products that want to stand apart from the AI crowd.
- **Signature:** Gradient glows (purple/blue/teal), animated orbs or particles, "sparkle" iconography, chat composers, streaming text, Tech Minimalism underneath.
- **Watch:** Extremely common in 2025–2026. Differentiate with a distinctive color, type or illustration choice.

### Blueprint / Technical Drawing
Engineering drawings as UI: grid paper, construction lines, annotations, measurement marks.
- **Fits:** Engineering, architecture, hardware, dev tools, "how it works" pages.
- **Avoid:** Emotional consumer brands.
- **Signature:** Blue or dark grid backgrounds, thin white/cyan lines, dimension annotations, monospace labels, exploded diagrams.
- **Watch:** Thin lines at small sizes; keep interactive elements clearly distinct from decoration.

## P. Expressive & Playful

### Maximalism
More is more: rich color, layered patterns, many type styles, abundant imagery.
- **Fits:** Fashion, art, music, food and culture brands, campaigns.
- **Avoid:** Productivity, anything where focus matters.
- **Signature:** Dense compositions, bold clashing palettes, patterns, many fonts, stickers and ornaments.
- **Watch:** Clear hierarchy is still necessary. The main action must be the loudest thing on screen.

### Digital Maximalism
Maximalism native to screens: gradients, 3D, motion, emoji, stacked effects all at once.
- **Fits:** Youth brands, creator platforms, entertainment, NFTs and drops.
- **Avoid:** Sustained-use apps.
- **Signature:** 3D objects, animated gradients, stickers, big type, many effects layered, playful cursors.
- **Watch:** Performance budget and cognitive load.

### Collage / Mixed Media
Cut-out photos, paper textures, tape, scribbles and type combined like a scrapbook.
- **Fits:** Creative brands, editorial features, fashion, food, zines, portfolios.
- **Avoid:** Clean tech products.
- **Signature:** Cut-out images with rough edges, paper and tape textures, handwritten notes, layered compositions.
- **Watch:** Asset-heavy; plan an image pipeline. Hard to keep consistent across many screens.

### Hand-Drawn / Doodle
Sketchy lines, doodles and hand-lettering that make the interface feel human and informal.
- **Fits:** Education, kids, creative tools, note-taking, friendly startups, whiteboards.
- **Avoid:** Formal and luxury products.
- **Signature:** Sketchy borders (e.g. Rough.js), hand-drawn icons, handwritten accent font, imperfect shapes.
- **Watch:** Keep body text in a readable font, with handwriting only for accents.

### Sticker UI
UI elements styled like stickers: die-cut white borders, slight rotation, playful layering.
- **Fits:** Social apps, youth products, creator tools, playful marketing.
- **Avoid:** Serious products.
- **Signature:** White outline around shapes, drop shadows, slight rotation, badge-like labels, collectible feel.
- **Watch:** Rotated text is harder to read; keep important text straight.

### Comic / Pop Art
Comic-book and pop-art energy: halftone dots, bold outlines, speech bubbles and primary colors.
- **Fits:** Entertainment, games, kids, food brands, campaigns.
- **Avoid:** Formal products.
- **Signature:** Halftone patterns, thick outlines, CMYK primaries, speech and action bubbles, bold condensed type.
- **Watch:** Halftone under text reduces legibility.

### Memphis Design
80s Memphis Group: squiggles, confetti, clashing geometric shapes and bold patterns.
- **Fits:** Events, youth brands, creative agencies, playful campaigns.
- **Avoid:** Serious and data products.
- **Signature:** Squiggles, dots, triangles, zigzags, bold pastels and primaries, black outlines.
- **Watch:** Keep patterns in decorative zones.

### Corporate Memphis
The flat illustration style of big tech: people with oversized limbs, flat colors, simple shapes (sometimes called "Alegria").
- **Fits:** Friendly SaaS onboarding, HR and people tools, explainers.
- **Avoid:** Brands that want distinctiveness; it's widely seen as generic now.
- **Signature:** Flat vector people, disproportionate bodies, bright flat palette, no outlines.
- **Watch:** Perceived as dated and generic by design-aware audiences; consider a custom illustration style instead.

### Kawaii
Japanese "cute" aesthetic: pastel colors, round faces, mascots and soft shapes.
- **Fits:** Kids, casual games, stationery and lifestyle, social apps, fan communities.
- **Avoid:** Serious products and adult professional tools.
- **Signature:** Pastels, rounded everything, mascot characters with faces, sparkles and hearts, bubbly type.
- **Watch:** Pastel-on-white contrast; keep text dark enough.

### Gamified UI
Game mechanics in non-game products: progress, streaks, levels, rewards, celebrations.
- **Fits:** Education, fitness, habit tracking, onboarding, community products.
- **Avoid:** Serious tasks where games trivialize the stakes (health decisions, finance); dark patterns.
- **Signature:** Progress bars and rings, XP and levels, badges, streak counters, confetti moments, mascots.
- **Watch:** Avoid manipulative patterns (guilt streaks, fake urgency). Celebrations must be skippable and respect reduced motion.

## Q. Organic & Natural

### Organic Design
Soft, flowing, nature-inspired shapes and layouts: curves instead of boxes.
- **Fits:** Wellness, beauty, food, eco brands, creative portfolios.
- **Avoid:** Data-dense tools.
- **Signature:** Curved section dividers, flowing shapes, natural palettes, rounded type, hand-crafted textures.
- **Watch:** Curved layouts must still align content well on small screens.

### Blob Design
Amorphous blob shapes as backgrounds, masks and decorations, sometimes animated.
- **Fits:** Friendly SaaS, health and wellness, education, startups.
- **Avoid:** Formal or luxury brands.
- **Signature:** SVG blobs (often morphing), blob-masked images, soft colors.
- **Watch:** Slow morphing is fine; fast morphing distracts.

### Eco / Natural UI
Visual language of sustainability: earth tones, natural textures, honest materials.
- **Fits:** Sustainability, outdoor, organic food, nonprofits, green energy.
- **Avoid:** High-tech flashy products.
- **Signature:** Greens, browns, sand; paper and fiber textures; leaf and plant motifs; humanist type; lightweight pages (low-carbon design).
- **Watch:** Practice what it preaches: lightweight pages, efficient media, dark-mode friendly.

### Solarpunk
Optimistic eco-futurism: nature and technology in harmony, bright and hopeful.
- **Fits:** Climate tech, green startups, future-city projects, games, education.
- **Avoid:** Corporate conservative brands.
- **Signature:** Bright greens and golds, art-nouveau-inspired curves, plants integrated with tech, sunlight, hand-drawn futurism.
- **Watch:** Illustration-heavy; budget for custom art.

### Paper / Cutout Style
Layered paper look: cut-out shapes with soft shadows that stack like craft paper.
- **Fits:** Education, kids, storytelling, food, handmade brands, onboarding.
- **Avoid:** Technical tools.
- **Signature:** Layered flat shapes with soft drop shadows, paper texture, torn or cut edges, depth via stacking.
- **Watch:** Many layered shadows can be heavy on long pages.

## R. Geometric & Art Movements

### Geometric Design
Circles, squares, triangles and lines as the main visual language: precise and structured.
- **Fits:** Tech, architecture, education, brand identities, finance.
- **Avoid:** Organic or emotional brands.
- **Signature:** Pure shapes, grids, strict alignment, bold flat colors, geometric sans type.
- **Watch:** Can feel cold; add warmth through color.

### Abstract Geometric
Geometric shapes composed abstractly: overlapping, rotating, generative.
- **Fits:** Creative agencies, brand backgrounds, events, art-tech.
- **Avoid:** Using it as the main content in apps.
- **Signature:** Overlapping translucent shapes, generative patterns, bold compositions, often animated.
- **Watch:** Keep it behind or around content, never under text without a solid surface.

### Bauhaus
The Bauhaus school: primary colors, basic shapes, function-driven layout, bold sans type.
- **Fits:** Design studios, museums, education, creative tools, bold brands.
- **Avoid:** Luxury and soft wellness.
- **Signature:** Red/yellow/blue plus black, circles/squares/triangles, strong grids, geometric sans, asymmetric balance.
- **Watch:** Primary colors on white need contrast checks (yellow especially).

### Line / Outline UI
Everything drawn with thin, consistent strokes: icons, illustrations, even surfaces.
- **Fits:** Minimal tech, architecture, documentation, elegant brands.
- **Avoid:** Products for low-vision users without an alternative, very playful brands.
- **Signature:** 1–1.5px strokes, outline icons (Lucide/Phosphor), outlined cards and buttons, few fills.
- **Watch:** Thin lines have weak visual weight; primary actions need fills. Check 3:1 contrast for UI boundaries.

## S. Accessibility-First

### High-Contrast / Accessibility-First
Design where accessibility is the aesthetic: strong contrast, large targets, clear focus and plain structure.
- **Fits:** Government, healthcare, education, older audiences, any product with legal accessibility requirements. Also a great base layer for everything else.
- **Avoid:** Nothing. At minimum, offer it as a mode.
- **Signature:** Contrast of 7:1 for body text (AAA) or at least 4.5:1, 44px+ targets, thick visible focus rings, underlined links, clear labels, no information by color alone.
- **Watch:** Can look plain; add personality through type and layout, not low-contrast color.

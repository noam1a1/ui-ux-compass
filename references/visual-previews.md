# Visual Previews

Only build previews if the developer asked for them in discovery. Some developers can judge a direction from a description, others need to see it. Previews are **throwaway exploration**, not project code, so they don't cross the approval gate.

## What to build

One self-contained HTML page that shows **the same sample UI in each proposed direction**, side by side (desktop) or stacked (mobile), so the comparison is fair.

For each direction, render a small "specimen" made from this product's real context (its name, its main object, its real copy), not generic lorem:

1. **Header strip**: direction name and its 3–5 signature traits
2. **A hero or page title** in the direction's typography
3. **A primary and a secondary button**, including hover and focus states
4. **A card or list item** representing the product's main object (a task, a product, a transaction)
5. **A form field** with a label, and an error state
6. **An empty state** using that direction's illustration or icon style and copy
7. **A loading state** (skeleton) in that direction
8. **The color palette and type scale** as small swatches

If the product is dark-first or has dark mode, show both themes or add a toggle. If the product is RTL, build the previews in RTL with real copy in that language.

## How to build

- One HTML file with inline CSS (and minimal inline JS for toggles). No build step.
- Use CSS variables per direction (`.direction-a { --bg: ...; --radius: ... }`) so each specimen is driven by its draft tokens. That becomes the starting point for real tokens later.
- Keep it realistic: the effects must be achievable in the recommended stack (don't show a WebGL effect you won't build).
- Label clearly: "Direction A: Tech Minimalism + Bento", and so on, with a one-line "why" under each.

## How to deliver

- If the environment can publish or open an HTML page (an artifact tool, a local file the developer can open in a browser, a dev server), use that and give the developer the link or path.
- Otherwise, save it to `docs/ui-ux-previews.html` in the project and tell the developer to open it.

## After the preview

Ask the developer to pick a direction, mix elements ("A's colors with B's typography"), or reject all. Record the decision and the reason in the plan's Design Direction section, and link the preview file.

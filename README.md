# UI/UX Compass

**An agent skill that makes Claude understand before it designs, and plan before it builds.**

Most AI-generated interfaces look fine in the happy path and fall apart everywhere else: the empty list, the slow network, the first-time user, the error screen, the phone in RTL. UI/UX Compass changes the order of work. It interviews you only as much as needed, picks a design direction from a catalog of about 95 visual styles, maps every screen and every state, and hands you a Markdown plan. **No code is written until you approve it.**

## How it works

```
 Orient ──> Discover ──> Direction ──> Architecture ──> Plan (.md) ──> ✋ Approval ──> Build + Verify
```

| Phase | What happens |
|---|---|
| **0. Orient** | Detects whether this is a new project, a broad improvement or a scoped change. For existing projects it audits the code first: stack, tokens, components, state handling, accessibility, RTL. |
| **1. Discover** | An adaptive interview. It asks only what it can't learn from the code or your brief, in 1–3 short rounds. Non-critical gaps become explicit assumptions you can correct. It confirms the plan's language and whether you want visual previews. |
| **2. Direction** | Proposes 2–3 contrasting style directions (e.g. *Tech Minimalism + Bento Grid + Micro-interactions*) with reasons, risks and a recommendation. Optional side-by-side visual previews. Recommends a stack for new projects. |
| **3. Architecture** | Design tokens, screen inventory, Mermaid user flows, and a per-screen states table (loading, empty, error, partial, offline…), plus real UX copy, accessibility, RTL/i18n and a performance budget. |
| **4. Plan** | A structured `docs/ui-ux-plan.md` in your language, with assumptions and open questions called out. |
| **5. Approval gate** | You approve, request changes, or approve only some milestones. |
| **6. Build & verify** | Implements milestone by milestone, verifies with screenshots (mobile/tablet/desktop × light/dark, optional RTL), checks the states and accessibility checklists, and reports at each checkpoint. |

Small requests get a proportionally small process. "Make this button less flat" won't trigger a 20-page plan.

## What's inside

```
ui-ux-compass/
├── SKILL.md                      # The workflow
├── references/
│   ├── styles-catalog.md         # ~95 styles: fits / avoid / signature / risks + product-type matrix
│   ├── states-checklist.md       # Every state and detail a screen can need
│   ├── plan-template.md          # The plan's fixed structure
│   ├── audit-checklist.md        # Auditing existing frontends
│   ├── design-tokens.md          # Token layers, scales, formats
│   ├── accessibility.md          # WCAG 2.2 AA + style-specific risks
│   ├── rtl-i18n.md               # RTL (Hebrew/Arabic) and localization done right
│   ├── ux-copy.md                # Voice, tone and copy patterns
│   ├── stack-guide.md            # Stack and library recommendations per style
│   ├── performance.md            # Performance budget and heavy-style fallbacks
│   ├── visual-previews.md        # Building side-by-side direction previews
│   └── qa-verification.md        # Verifying each milestone
├── scripts/
│   └── capture_screens.py        # Playwright screenshots + overflow, console-error & touch-target checks
└── examples/
    └── example-plan.md           # A filled-in plan for a fictional app
```

## Highlights

- **Style catalog.** About 95 styles across 19 families, from Glassmorphism and Liquid Glass to Neo-Brutalism, Swiss, Japandi, Frutiger Aero, Solarpunk, Terminal/CLI and more. Each entry says where the style fits, where to avoid it, its concrete signature traits, and its accessibility and performance risks.
- **States-first design.** Empty (first use, no results, all done), loading timing rules, errors, partial data, offline, permissions, and the screens people forget.
- **RTL built in.** Logical CSS, mirroring rules, bidi text, Hebrew and Arabic font pairing, gendered copy.
- **Stack-agnostic.** React, Vue, Svelte, Angular, Astro, plain HTML, React Native, Flutter, SwiftUI, Compose. It works with what you have and recommends what fits when you start fresh.
- **Verification.** It doesn't stop at "it compiles": it takes screenshots and runs automated checks.

## Installation

### Claude Code
```bash
# Personal (all projects)
git clone https://github.com/<your-username>/ui-ux-compass ~/.claude/skills/ui-ux-compass

# Or per project
git clone https://github.com/<your-username>/ui-ux-compass .claude/skills/ui-ux-compass
```

### Claude apps (Claude.ai / Desktop)
Download the repository as a ZIP (or a `.skill` package from Releases) and upload it under **Settings → Capabilities → Skills**.

### Optional: screenshot verification
```bash
pip install playwright
python -m playwright install chromium
```

## Usage

Just describe what you want. The skill triggers on design and frontend requests:

- "I'm starting a habit-tracking app for students, help me design it"
- "Our admin dashboard looks generic and messy, can you improve the UX?"
- "Which style fits a luxury jewelry store?"
- "תעצב לי דף נחיתה למוצר AI בעברית"

## Contributing

Contributions are welcome: new styles, better checklists, framework notes, translations of the example plan.
Please keep catalog entries in the same format (**Fits / Avoid / Signature / Watch**).

## License

[MIT](LICENSE) © 2026 Noam

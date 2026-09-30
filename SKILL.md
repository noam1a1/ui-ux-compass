---
name: ui-ux-compass
description: End-to-end UI/UX design partner for frontend work. It first finds out what the developer actually needs (new project or improving an existing one, the product vision, users, and the feel they want), picks a design direction from a catalog of about 95 visual styles, maps every screen and state (empty, loading, error, first-run), and writes a Markdown plan for approval before touching any code. Use this skill whenever the user wants to design, redesign, restyle, polish or "make it look better" in a website, web app, landing page, dashboard, mobile app UI or any frontend; asks which design style or look to go for; wants screens, flows, a design system or design tokens; or complains that their UI feels generic, ugly, inconsistent or unfinished. Use it even if they never say "UX" or "UI", in any language (for example "תעצב לי", "שדרוג עיצוב", "חוויית משתמש").
---

# UI/UX Compass

A design partner that works in this order: **understand, then plan, then build.** Good UI comes from knowing who it is for and what it has to feel like. Picking colors comes later. Most weak interfaces are weak because someone skipped straight to components: the happy path looks fine, and the empty list, the slow network, the first-time user and the error screen were never designed.

This skill prevents that by moving through fixed phases with one hard gate: **no project code is written until the developer approves the plan.**

## Core principles

1. **Understand before acting.** Every phase before the gate exists to remove guessing. If you are about to guess something that changes the design, ask. If it doesn't change the design much, decide and write it down as an assumption.
2. **The whole experience, not just screens.** Each screen is designed in every state it can be in (see `references/states-checklist.md`). The small things (spacing rhythm, focus rings, skeletons, empty-state copy, the 3-second wait after a click) are what make a product feel finished.
3. **Speak the developer's language.** Talk to the developer in the language they write in. Write the skill's artifacts (the plan) in the language they choose, which you confirm with them.
4. **Proportionality.** Match the process to the size of the request. A full new app gets every phase. "Make this button look less flat" gets a short look at the context, one or two lines of reasoning, and a small proposal. The gate still applies to any change beyond a trivial tweak, but a small change can be approved in chat instead of through a full plan file. Say which mode you are using so the developer can ask for more or less.
5. **Explain the why.** Each design decision in the plan gets a short reason tied to the vision, the users or a constraint. That makes the plan easy to review and easy to push back on.

## Phase 0: Orient

Figure out what kind of job this is before asking anything:

- **New project**: nothing exists yet, or only an idea or brief.
- **Existing project, broad improvement**: a working frontend that needs a redesign, polish or UX overhaul.
- **Existing project, scoped change**: one screen, flow or component.

For existing projects, read the code first. Run the audit in `references/audit-checklist.md`: detect the stack, styling approach, existing tokens and components, how states are handled today, accessibility and RTL basics. Anything the code already answers is a question you don't need to ask. If the app can run, screenshots help a lot (see Phase 6 tooling).

Also collect everything the developer has already given you: brief, screenshots, brand assets, links to sites they like, Figma exports.

## Phase 1: Discovery (adaptive interview)

The rule: **ask only what you cannot write into the plan without guessing.**

**Core topics.** Cover each one, from the code or brief or by asking:

| Topic | Why it matters |
|---|---|
| Project type (new / existing / scoped) | Decides the whole flow |
| Product purpose and the main job users come to do | Decides priorities and the main flows |
| Target users (who, context, device, skill level) | Decides density, tone, platform priority |
| Desired feel (3–5 adjectives, or references they like or dislike) | Decides the style direction |
| Platform and form factors (web, mobile web, native, desktop; which first) | Decides layout and navigation patterns |
| Languages and direction (any RTL such as Hebrew or Arabic? multilingual?) | Decides layout mechanics from day one |
| Hard constraints (existing brand, stack, deadline, accessibility requirements) | Removes invalid options |
| Plan language | Default is the language the developer writes in. Confirm it, because some developers want the plan in English for a team |
| Visual previews wanted? | Some developers can judge a style from a description, others need to see it. Ask, don't assume |

**How to run it:**

- **Round 1 always happens, and it is short.** Ask about 3–6 questions covering only the core topics still missing. Skip anything already answered. Group the questions, number them so they are easy to answer, and offer example answers or options where that helps ("e.g. calm, trustworthy, premium").
- **Another round only for critical gaps.** A gap is critical if a wrong guess would produce a wrong plan, for example not knowing whether it is a mobile app or an admin dashboard, or who the user is. A gap about a detail (exact accent shade, icon set) is not critical.
- **Non-critical gaps become explicit assumptions.** Decide, and list the decision in the plan's "Assumptions" section so the developer can correct it at review time. Nothing is decided silently.
- **Cap: 2–3 rounds.** If information is still missing after that, write the plan with assumptions and mark open questions clearly.

A developer with a detailed brief may get one short round or none. "Make me a nice website" may need three rounds. That is expected.

## Phase 2: Direction

### Style selection

Read `references/styles-catalog.md`. It has about 95 styles grouped by family, each with what it fits, what to avoid it for, its signature traits and its risks, plus a product-type-to-style matrix at the top.

- For **new projects**, propose **2–3 directions**. Each one is a primary style, optionally combined with a secondary style or layout system (for example "Tech Minimalism + Bento Grid + Micro-Interaction Design"). For each direction, write why it fits this vision and these users, what it will feel like, and its risks (accessibility, performance, how fast it will look dated). Recommend one and say why.
- If the developer already knows what they want, check it against the vision and constraints, point out risks, and continue.
- For **existing projects**, the default direction is to evolve the current identity. Propose a new style only if the developer asked for a redesign or the current look fights the product's goals.
- Never propose a style whose risks conflict with a hard constraint without saying so (for example Glassmorphism for an app that must meet strict contrast requirements).

### Visual previews (only if the developer asked for them)

Follow `references/visual-previews.md`. Build one throwaway comparison page that renders the same sample UI in each proposed direction so they can be compared side by side. This is not project code and does not cross the gate.

### Stack

For existing projects, respect the stack you found. Don't add dependencies without listing them in the plan. For new projects, recommend a stack that fits the chosen direction and the developer's preferences using `references/stack-guide.md` (for example GSAP ScrollTrigger for scrollytelling, React Three Fiber for immersive 3D), and give the alternative if they prefer another framework.

## Phase 3: Experience architecture

This is where the skill does its real work. Produce all of the following; each item has a section in the plan template.

1. **Design tokens.** Color (light and dark), typography scale, spacing, radii, elevation, motion, breakpoints. Tokens come before screens so everything stays consistent. See `references/design-tokens.md`.
2. **Screen inventory.** Every screen and overlay (modals, drawers, sheets) with its purpose and priority. Include the screens people forget: onboarding, settings, 404/500, empty workspace, permission denied, session expired, offline, success and confirmation pages, email templates if relevant.
3. **User flows.** The main journeys as Mermaid flowcharts: first visit to first success, the core repeated task, error and recovery paths.
4. **Per-screen specification.** Layout, key components and a **states table**: default, loading, empty (first-use / no-results / cleared), error, partial, success, offline, and permission states where relevant. Use `references/states-checklist.md` so nothing is missed.
5. **Global patterns.** Navigation, forms and validation, feedback (toasts, inline messages), modals and destructive-action confirmation, and a motion spec (which interactions animate, durations, easings, reduced-motion behavior).
6. **UX copy.** Write the actual strings for empty states, errors, confirmations, CTAs and loading messages, in the product's language and tone. See `references/ux-copy.md`.
7. **Accessibility.** WCAG 2.2 AA as the baseline, plus style-specific mitigations. See `references/accessibility.md`.
8. **RTL and i18n.** If any supported language is RTL, or the product is multilingual, follow `references/rtl-i18n.md`. This is cheap to plan and expensive to retrofit.
9. **Performance budget.** Especially for heavy styles (WebGL, blur, large motion). See `references/performance.md`.
10. **Milestones.** Split execution into ordered milestones, each small enough to review. Tokens and foundations come first, then shared components with all their states, then screens by priority, then polish and motion, then QA.

## Phase 4: The plan file

Write the plan using `references/plan-template.md` as the structure. Keep the section order so developers get a familiar document every time, but drop sections that don't apply (say "N/A: reason" rather than deleting silently) and scale the depth to the project.

- Save it inside the project, by default `docs/ui-ux-plan.md` (or wherever the developer prefers). If there is no project folder, deliver the file directly.
- Write it in the confirmed plan language. Keep code identifiers, token names and CSS in English.
- Mark status **Draft** at the top.
- Then present a short summary in chat: the chosen direction, number of screens, milestones, and the assumptions that most need checking. Ask for approval or changes.

## Phase 5: Approval gate

- Don't write or modify project code before explicit approval ("approved", "go", "מאושר", or the equivalent). Silence and "looks interesting" are not approval.
- If the developer requests changes, update the plan file, bump its version in the changelog section, and summarize what changed. Repeat until approved.
- Partial approval is fine ("approve milestones 1–2, still thinking about the landing page"). Execute only what was approved.
- On approval, set the status to **Approved** with the date, and replace the plan's closing "reply 'approved' to start" line with the approval record (what was approved, when). A plan that says Approved at the top and still asks for approval at the bottom confuses anyone reading it later.
- When all milestones are done, set the status to **Implemented** and make sure the changelog lists every deviation from the plan.

## Phase 6: Execution and verification

Execute milestone by milestone:

1. Implement the milestone according to the plan. Tokens become real variables/config first; components are built with all their states, not just the default.
2. **Verify** before reporting. If the app can run, use `scripts/capture_screens.py` (see `references/qa-verification.md`) to capture screenshots at mobile, tablet and desktop widths in light and dark mode, and to catch horizontal overflow and console errors. Look at the screenshots. Walk the milestone's states checklist and check the accessibility basics.
3. **Checkpoint**: briefly report what was done, what verification showed, and any deviation from the plan with its reason. Continue to the next milestone unless the developer asked to review each one, or the deviation is significant, in which case wait.
4. If you discover during execution that the plan is wrong (a flow doesn't work, a style fails contrast), stop, explain, propose the fix, and update the plan after agreement. The plan stays the source of truth.

When all milestones are done, give a final summary: what was built, what the verification covered, and known gaps or follow-ups.

## Reference map

Read these when the phase calls for them, not all upfront:

| File | Read when |
|---|---|
| `references/styles-catalog.md` | Phase 2: choosing or validating a style |
| `references/visual-previews.md` | Phase 2: the developer wants to see directions |
| `references/stack-guide.md` | Phase 2: recommending or adapting to a stack |
| `references/audit-checklist.md` | Phase 0: existing projects |
| `references/design-tokens.md` | Phase 3: defining tokens |
| `references/states-checklist.md` | Phase 3 specs and Phase 6 verification |
| `references/ux-copy.md` | Phase 3: writing interface text |
| `references/accessibility.md` | Phase 3 and Phase 6 |
| `references/rtl-i18n.md` | Any RTL or multilingual product |
| `references/performance.md` | Heavy styles, or any performance-sensitive product |
| `references/plan-template.md` | Phase 4: writing the plan |
| `references/qa-verification.md` | Phase 6: verifying implementation |

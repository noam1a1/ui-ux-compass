# Plan Template

Use this structure for the plan file (default path `docs/ui-ux-plan.md`). Keep the section order so every plan feels familiar. If a section doesn't apply, keep the heading and write "N/A: <reason>". Scale depth to the project: a scoped change might fill sections 1, 2, 7, 8 and 14 briefly, while a new app fills everything.

Write in the confirmed plan language. Keep code identifiers, token names, file paths and CSS in English. In RTL languages, the Markdown renders fine, but keep code blocks LTR.

---

```markdown
# UI/UX Plan: <Project name>

> **Status:** Draft | Approved (<date>) | Implemented (<date>)  ·  **Version:** 0.1  ·  **Mode:** New project | Existing: broad improvement | Existing: scoped change
> **Plan language:** <language>  ·  **Visual previews:** Yes (<link/path>) | No

## 1. Summary
Three to five sentences: what we're building or improving, for whom, the chosen direction, and the scope of work.

## 2. Vision & Users
- **Product purpose:** the main job users come to do
- **Primary users:** who, context of use, device, expertise
- **Secondary users:** (if any)
- **Desired feel:** 3–5 adjectives, and what it must NOT feel like
- **Success looks like:** how we'll know the UX works (e.g. first task completed in < 2 min, fewer support tickets on X)

## 3. Current State (existing projects only)
- **Stack detected:** framework, styling, component library, icons, animation libs
- **What works:** keep these
- **Problems found:** prioritized list
  | # | Problem | Where | Impact | Type (Critical / Quick win / Structural) |
- **Screenshots:** paths or links if captured

## 4. Design Direction
- **Chosen direction:** primary style + layout system + accent (e.g. "Tech Minimalism + Bento Grid + Micro-Interaction Design")
- **Why it fits:** tied to the vision and users
- **Signature elements:** the 3–5 concrete traits that will define the look
- **Alternatives considered:** each with one line on why it wasn't chosen
- **Risks & mitigations:** accessibility, performance, aging

## 5. Stack & Tooling
- Framework / styling / component primitives / icons / animation / charts
- **New dependencies:** each with its reason (none added without approval)
- **Alternatives** if the developer prefers another stack

## 6. Design Tokens
Color (light & dark), typography scale, spacing, radii, elevation, motion, breakpoints, z-index.
Include the actual values, and the format they'll be implemented in (CSS variables / Tailwind theme / JSON).

## 7. Screens & Flows
### 7.1 Screen inventory
| # | Screen / overlay | Purpose | Priority (P0/P1/P2) | Milestone |
### 7.2 User flows
Mermaid flowcharts for: first visit to first success, the core repeated task, error and recovery.

## 8. Screen Specifications
One subsection per screen:
### 8.x <Screen name>
- **Purpose & primary action**
- **Layout:** structure per breakpoint (mobile / tablet / desktop)
- **Key components**
- **States:**
  | State | Design | Copy |
  |---|---|---|
  | Default | ... | ... |
  | Loading | ... | ... |
  | Empty: first use | ... | ... |
  | Empty: no results | ... | ... |
  | Error | ... | ... |
  | (others as relevant) | | |
- **Interactions & motion**
- **Notes:** edge cases (long content, permissions, etc.)

## 9. Global Patterns
Navigation · Forms & validation · Feedback (toasts, inline) · Modals & confirmation · Motion spec (durations, easings, reduced motion) · Icons & imagery

## 10. UX Copy
Voice & tone in 2–3 lines, plus a table of key strings (empty states, errors, confirmations, CTAs) not already listed in section 8.

## 11. Accessibility
Target level (WCAG 2.2 AA by default), key requirements, style-specific mitigations, how it will be checked.

## 12. Internationalization & RTL
Languages, direction strategy, fonts per script, formatting (dates, numbers, currency), mirroring rules. "N/A: single LTR language" if so.

## 13. Performance Budget
Core Web Vitals targets, heavy features and their fallbacks, image/font strategy.

## 14. Milestones
| # | Milestone | Includes | Done when |
|---|---|---|---|
| 1 | Foundations | tokens, fonts, base layout, theme switch | tokens in code, both themes render |
| 2 | Core components | ... with all states | ... |
| ... | | | |
| N | Polish & QA | motion, screenshots, a11y pass | checklist passes |
**Checkpoint preference:** report after each milestone and continue | wait for review after each milestone

## 15. Verification Plan
How each milestone will be checked: screenshots (viewports, themes, RTL), states checklist, accessibility checks, performance checks.

## 16. Assumptions
Decisions made without explicit input. **Please confirm or correct.**
| # | Assumption | Why | Impact if wrong |

## 17. Open Questions
Items that still need an answer, with the default we'll use if there's no answer.

## 18. Changelog
| Version | Date | Change |
|---|---|---|
| 0.1 | <date> | Initial draft |

---
**Approval:** reply "approved" (or approve specific milestones) to start implementation.
```

After approval, replace that last line with the record, for example:
`**Approved:** 2026-09-30, milestones 1–5.`
and after implementation:
`**Implemented:** 2026-10-02. Deviations are listed in the changelog.`

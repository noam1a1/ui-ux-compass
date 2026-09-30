# UX Copy

Interface text is part of the design. An empty state with a good illustration and bad copy is still a bad empty state. In Phase 3, write the actual strings, in the product's language, and put them in the plan's screen specs and copy section.

## Voice and tone

Derive the voice from the vision's adjectives, and write it down in 2–3 lines in the plan. For example: "Friendly and direct. Short sentences. Light humor in empty states and celebrations, never in errors or payment flows."

Tone shifts with the situation, while the voice stays the same:
- **Success**: warm, brief
- **Error**: calm, clear, helpful; no blame, no jokes
- **Destructive actions**: serious and precise
- **Onboarding / empty**: encouraging, focused on value

## Principles

- **Clear before clever.** A clever line that needs a second read is a bad line.
- **Front-load the meaning.** Users scan, so put the important words first.
- **Use the user's words**, not internal jargon ("Project", not "Workspace entity").
- **Buttons say what they do**: verb + object ("Create invoice", "Delete 3 files"), not "OK", "Submit", "Yes".
- **Consistent terms**: pick one word per concept (delete vs remove, sign in vs log in) and use it everywhere.
- **Sentence case** for UI text in Latin scripts (easier to read than Title Case).
- **Numbers as digits** in UI ("3 files", not "three files").
- **Gendered languages** (Hebrew, Arabic): decide on an approach. Options: plural address (commonly used in Hebrew UI), gender-neutral phrasing, infinitive forms ("להתחבר", "לשמור"), or personalization if the user's preference is known. Write it in the plan.

## Patterns and templates

### Empty states
Structure: **what goes here** + **why it's useful** + **one action**.
- First use: "No projects yet. Projects keep your files and tasks together. [Create project]"
- No results: "No results for 'invoice 2024'. Try a different spelling or [clear filters]."
- All done: "You're all caught up."

### Errors
Structure: **what happened** + **why (if known and useful)** + **how to fix it**.
- "We couldn't save your changes. Check your connection and try again. [Retry]"
- Field level: "Enter an email address like name@example.com", not "Invalid input".
- Never show raw error codes alone; include them in small text for support if useful.
- Don't blame the user ("You entered a wrong password" → "That password doesn't match this account").

### Confirmation dialogs (destructive)
- Title: the action and object, as a question: "Delete 'Marketing Q3'?"
- Body: the consequence: "This deletes the project and its 24 files for everyone. This can't be undone."
- Buttons: "Delete project" (destructive style) and "Cancel".

### Success
- Brief, and say what happens next if it isn't obvious: "Invoice sent to dana@example.com."
- For reversible actions, offer Undo in the same toast.

### Loading
- Short actions need no text.
- Long waits: say what's happening: "Analyzing 1,240 rows…"; for very long waits, set expectations ("This usually takes about a minute").
- AI and streaming: "Thinking…" and similar; allow Stop.

### Onboarding
- One idea per step, and let people skip.
- Show value before asking for effort (let them try before sign-up where possible).

### Permissions and paywalls
- Explain why and what they get: "Upgrade to Pro to export more than 3 reports a month. [See plans]"
- For browser permissions, ask in context with a pre-prompt explaining the benefit.

## In the plan

Each screen spec's states table has a Copy column. Section 10 has the voice summary plus shared strings (global errors, toasts, confirmation dialogs). Write copy in every language the product ships in, or at least in the primary one, marking where translation is needed.

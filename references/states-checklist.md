# States & Details Checklist

Every screen, widget and component can be in more states than the happy path. Use this list in Phase 3 to fill in each screen's states table, and in Phase 6 to check the implementation. Mark a state "N/A" when it truly can't happen. Don't just skip it.

## 1. Data states (for every screen or widget that shows data)

| State | What to design | Notes |
|---|---|---|
| **Default / populated** | The normal view with realistic data | Design with real-length data, not "Lorem" or perfect 5-item lists |
| **Loading (first load)** | Skeleton matching the final layout | Skeletons for content areas; spinners only for small inline actions |
| **Loading (refresh / pagination)** | Keep existing content visible and show a subtle indicator | Never blank the screen on refresh |
| **Empty: first use** | Explain what will be here, why it's valuable, and one clear action to start | This is onboarding: illustration or icon, a short line of copy, a primary CTA |
| **Empty: no results** | Say what was searched or filtered and offer a way out (clear filters, check spelling, broaden) | Show the active query or filters |
| **Empty: cleared / done** | A positive "all done" state (inbox zero, all tasks complete) | A small moment of delight fits here |
| **Error: failed to load** | What went wrong in plain words, plus a retry action | Keep any cached content if you have it |
| **Partial** | Some data loaded and some failed, or some fields missing | Show what you have and mark what's missing inline |
| **Offline** | Banner or inline notice; show cached data; queue actions if supported | Don't show a generic error |
| **Stale** | Data may be outdated ("updated 5 min ago", refresh) | Important for dashboards and finance |

### Loading timing guide
- **< 100ms**: show nothing, it feels instant.
- **100ms–1s**: subtle indicator (button spinner, progress bar at the top). Delay showing it by about 150–300ms to avoid flicker.
- **1–10s**: skeleton or a clear progress indicator, with the layout reserved to avoid layout shift.
- **> 10s**: determinate progress if possible, an explanation of what's happening, and let the user keep working or cancel.
- AI or streaming responses: show thinking/typing state immediately, then stream. Allow stopping.

## 2. Quantity states

- **Zero / one / many / too many** items. What does the list look like with 1 item? With 10,000? (pagination, virtualization, "show more")
- **Long content**: long names, long emails, long words (German, URLs), long titles in RTL. Truncate with a tooltip, wrap, or line-clamp, and decide per field.
- **Short content**: a one-character name, a missing avatar (initials fallback), a missing image (placeholder).
- **Numbers**: large numbers (1,234,567 → 1.2M?), negative values, zero, decimals, currency and locale formatting.

## 3. Interactive states (every interactive component)

- **Default, hover, focus-visible, active/pressed, disabled, loading, selected/checked**
- **Focus-visible** must be clearly visible (a 2px+ ring with 3:1 contrast). Don't remove outlines without replacing them.
- **Disabled**: explain why when possible (tooltip or helper text). Consider hiding instead of disabling when the action is never available to this user.
- **Loading on buttons**: keep the button width stable, show a spinner, prevent double submit.
- **Touch**: no hover on touch devices, so don't hide essential actions behind hover.

## 4. Forms

- Labels always visible (placeholders are not labels)
- Required and optional marking (mark the rarer of the two)
- Inline validation timing: validate on blur or submit, not on every keystroke while typing (except for positive feedback like password strength)
- Error messages next to the field, saying how to fix it; move focus to the first error on submit, plus an error summary for long forms
- Success state after submit (what happens next?)
- Autosave or unsaved-changes warning for long forms
- Correct input types and `autocomplete` attributes (email, tel, one-time-code, etc.) for mobile keyboards and autofill
- Submit disabled state vs always-enabled with validation (prefer always enabled plus clear errors)

## 5. Feedback & system messages

- **Success**: toast or inline confirmation for completed actions; a quiet confirmation for frequent actions
- **Undo** instead of confirm for reversible destructive actions (delete → toast with Undo)
- **Confirm dialog** for irreversible actions: name the object, state the consequence, make the destructive button explicit ("Delete project", not "OK")
- **Optimistic UI** where safe, with rollback and an error message if the server fails
- **Toasts**: position, duration (5–8s, longer if they contain an action), stacking, don't auto-dismiss errors
- **Notifications and badges**: counts, "99+", and a way to clear them

## 6. App-level states & screens people forget

- First visit / onboarding (and skipping it)
- Signed out / session expired (preserve the user's work, redirect back after login)
- Permission denied / not available on your plan (explain and offer the upgrade or request path)
- 404 not found (helpful: search, home, recent items)
- 500 / something went wrong (apologize, retry, status page, support)
- Maintenance mode
- Rate limited / too many attempts
- Email verification pending
- Feature flags / beta states
- Account deletion and data export flows
- Cookie / consent banner (without covering primary actions)
- Transactional emails and notifications, if the product sends them

## 7. Layout & visual details

- **Spacing rhythm**: all spacing from the token scale; consistent padding inside cards and sections
- **Alignment**: text baselines, icon and text vertical centering, grid edges
- **Empty space**: intentional, not leftover. Sections breathe equally, and nothing floats in a half-empty screen on large monitors (use max-widths)
- **Responsive**: 320px minimum width, tablet, desktop, wide (1440+) and ultra-wide (use a max content width)
- **Orientation** and on-screen keyboard overlap on mobile (inputs not hidden behind the keyboard)
- **Safe areas** on mobile (notch, home indicator): `env(safe-area-inset-*)`
- **Sticky elements** don't cover content or focus targets
- **Scroll**: restore scroll position on back; avoid nested scroll traps
- **Dark mode**: every state above in both themes; images and illustrations that work on both
- **Print styles** where relevant (invoices, reports)
- **Favicon, app icons, social preview (OG) image, page titles**

## 8. Motion details

- Entrance and exit of overlays (modal, drawer, toast)
- State transitions (expand/collapse, tab switch, list add/remove)
- Page and route transitions (keep them short; the View Transitions API where supported)
- Consistent motion tokens (durations and easings)
- A `prefers-reduced-motion` alternative for every non-essential animation (usually a fade or no animation)

# RTL & Internationalization

Read this when the product supports any right-to-left language (Hebrew, Arabic, Persian, Urdu) or more than one language. Planning for direction and localization from day one is cheap. Retrofitting it means touching every component.

## Direction basics

- Set `dir="rtl"` and `lang="he"` (or `ar`, etc.) on `<html>`. For multilingual apps, set them per locale, and set `dir="auto"` on user-generated content fields.
- **Use logical CSS properties everywhere**, never physical ones:
  - `margin-inline-start` / `-end` instead of `margin-left` / `-right`
  - `padding-inline`, `inset-inline-start`, `border-inline-start`
  - `text-align: start` / `end` instead of `left` / `right`
  - Flexbox and Grid already follow direction; `row` flows right-to-left in RTL
- **Tailwind**: use `ms-*`, `me-*`, `ps-*`, `pe-*`, `start-*`, `end-*`, `text-start`, `text-end`, `border-s`, `rounded-s-*`. Use `rtl:` / `ltr:` variants only for real exceptions (for example `rtl:rotate-180` on a directional icon)
- **Component libraries**: check RTL support (MUI and Mantine need direction config; Radix/shadcn mostly follow `dir`; some carousels and date pickers need explicit RTL options)
- **Native**: Flutter `Directionality` / `TextDirection`; React Native `I18nManager`; SwiftUI and Compose handle leading/trailing automatically if you use leading/trailing rather than left/right

## What to mirror and what not to

**Mirror:**
- Layout (sidebars, navigation order, breadcrumbs)
- Directional icons: back/forward arrows, chevrons, "next" and "previous", reply, undo/redo (usually), progress direction, sliders, carousels
- Text alignment, form label positions, checkbox/radio positions
- Swipe gestures (swipe "forward" goes left in RTL)

**Don't mirror:**
- Logos and brand marks
- Media playback controls (play ▶ stays pointing right in most conventions)
- Clocks, circular refresh/reload icons (clockwise stays clockwise)
- Checkmarks, plus/minus, search magnifier (commonly left as is)
- Numbers and charts' numeric axes. Numbers are written left to right even in RTL text; time-series charts in RTL products are commonly kept left-to-right, so decide per product and document it
- Code, URLs, email addresses, phone numbers (keep them LTR)

## Bidirectional text

- Mixed Hebrew/English strings with numbers or punctuation can reorder unexpectedly. Wrap embedded LTR runs (usernames, product codes, URLs, phone numbers) in `<bdi>` or `<span dir="ltr">`
- For inputs that take LTR data (email, URL, phone, code), set `dir="ltr"` on the input, keeping the label aligned to the page direction
- Punctuation at the end of mixed strings is the classic bug; test real strings

## Typography for Hebrew and Arabic

- **Hebrew fonts** (Google Fonts, free): Heebo, Assistant, Rubik, Noto Sans Hebrew, IBM Plex Sans Hebrew, Open Sans (Hebrew subset), Secular One and Karantina (display), Frank Ruhl Libre and David Libre (serif), Suez One, Varela Round
- **Arabic fonts**: Noto Sans/Kufi/Naskh Arabic, IBM Plex Sans Arabic, Cairo, Tajawal, Almarai, Readex Pro
- Pair each Latin font with a script font of similar weight and x-height, or use a family that covers both scripts (Rubik, Heebo, IBM Plex, Noto)
- **No letter-spacing** on Hebrew or Arabic (it breaks Arabic joining and looks wrong in Hebrew). Uppercase styles don't exist in these scripts, so "small caps label" patterns need an alternative (weight or color)
- Slightly larger line-height (Arabic especially: 1.6–1.8 for body)
- Italic doesn't really exist in Hebrew; use weight or color for emphasis
- Oversized or kinetic typography styles: check that the Hebrew/Arabic font has the weights and the character the style needs; many display styles depend on Latin-only fonts

## Localization

- **No hardcoded strings**: all UI text goes through an i18n layer (i18next, next-intl, vue-i18n, FormatJS/react-intl, Flutter intl, etc.)
- **Text expansion**: German and Finnish run 30–40% longer than English; Hebrew is often shorter. Design buttons and labels to flex, and test with the longest language
- **Plurals and gender**: Hebrew and Arabic have grammatical gender and complex plurals. Use ICU MessageFormat (`{count, plural, ...}`, `{gender, select, ...}`), and never concatenate strings
- **Formatting**: `Intl.DateTimeFormat`, `Intl.NumberFormat` (currency ₪ placement, decimal separators), `Intl.RelativeTimeFormat`. Week start (Sunday in Israel), date order (DD/MM/YYYY in Israel)
- **Hebrew calendar or Hijri** dates if the audience needs them
- **Images with text or direction** (screenshots, arrows in illustrations) need localized versions
- **Language switcher**: show language names in their own language ("עברית", "English"), not flags

## Testing

- Screenshot every key screen in each direction (`scripts/capture_screens.py --rtl` forces `dir="rtl"` for a quick check)
- Test with real translated copy, not machine-reversed English
- Check: icons mirrored correctly, no physical-margin leftovers (search the code for `left`, `right`, `ml-`, `mr-`, `pl-`, `pr-`), mixed-text strings, forms with LTR inputs

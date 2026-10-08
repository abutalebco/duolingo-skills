# Arabic (العربية) — worksheet guide

| Field | Value |
|---|---|
| Code | ar |
| Script | Arabic (right-to-left) |
| Direction | right-to-left |
| Reading aid | transliteration |
| Typst fonts | Noto Naskh Arabic, Amiri (+ DejaVu Sans fallback) |
| Typst lang/region | ar |
| Cell grid | No (ruled lines) |
| Duolingo status | established course |

## Teach and drill (pick content from here)

- Letter forms: isolated / initial / medial / final
- Short vowel marks (harakat) on beginner words; remove gradually
- Sun and moon letters with ال
- Root-and-pattern system (k-t-b)
- Dual and broken plurals

## How to fill entries

`text` = Arabic with harakat for beginners. `roman` = transliteration. `meaning` = English. `note` = gender/plural/root.

## Pitfalls

- Arabic is connected script: never split into one-letter cells; use ruled lines (grid = false)
- Set direction RTL; the trace row starts at the right edge
- Duolingo teaches Modern Standard Arabic (MSA); dialect forms (Egyptian etc.) go in `note` only

## Layout behaviour

- Words: ruled line with the word faded 3×, then blank ruled line(s).
- Sentences: one faded sentence line, then blank ruled line(s). Keep sentences ≲ 60 characters or the trace shrinks to fit.
- Right-to-left: trace starts at the right edge; do not reverse strings manually, store them in logical order.

## Starter section ideas

Greetings & introductions · Numbers 1–20 · Food & drink · Family · Places & directions · Time & days · Everyday verbs · Short sentences / mini dialogues

## Arabic specifics
- **Layout**: RTL ruled lines, trace first, then blank; template flips alignment automatically when `dir` is `rtl`.
- **Fonts**: `Noto Naskh Arabic` or `Amiri` (readable, handwriting-like); fall back to DejaVu Sans only for emergencies (poor shaping for harakat).
- **Letter drills**: use `type: "words"` with `text` = single letter and `note` listing its four forms.
- **Numbers**: Arabic text uses Eastern Arabic-Indic digits (١٢٣) in many materials; state which set you use and stay consistent.


## Quality checklist

- Every `text` is natural and correct; no machine-looking literal translations.
- Diacritics/special letters verified (see Pitfalls).
- Fonts render every glyph (no tofu boxes) — preview page 1 before delivering.
- Sentences are short, useful, and reuse words from earlier sections.

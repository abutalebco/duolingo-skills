# Yiddish (ייִדיש) — worksheet guide

| Field | Value |
|---|---|
| Code | yi |
| Script | Hebrew script (right-to-left) |
| Direction | right-to-left |
| Reading aid | YIVO transliteration |
| Typst fonts | Noto Sans Hebrew (+ DejaVu Sans fallback) |
| Typst lang/region | yi |
| Cell grid | No (ruled lines) |
| Duolingo status | verify on duolingo.com/courses before building (newer/incubator/limited course) |

## Teach and drill (pick content from here)

- YIVO orthography: ײַ ײ אַ אָ ײ װ ױ
- Germanic grammar in Hebrew script
- Loshn-koydesh vs Germanic spelling
- Articles der/di/dos

## How to fill entries

`text` = natural Yiddish (with correct diacritics). `meaning` = English. Use `note` for grammar flags (plural, case, irregular form). Show the article (der/di/dos) inside `text` for every noun, e.g. "der …".

## Pitfalls

- Use YIVO standard spelling; do not mix Hebrew-pointed forms
- RTL ruled lines

## Layout behaviour

- Words: ruled line with the word faded 3×, then blank ruled line(s).
- Sentences: one faded sentence line, then blank ruled line(s). Keep sentences ≲ 60 characters or the trace shrinks to fit.
- Right-to-left: trace starts at the right edge; do not reverse strings manually, store them in logical order.

## Starter section ideas

Greetings & introductions · Numbers 1–20 · Food & drink · Family · Places & directions · Time & days · Everyday verbs · Short sentences / mini dialogues


## Quality checklist

- Every `text` is natural and correct; no machine-looking literal translations.
- Diacritics/special letters verified (see Pitfalls).
- Fonts render every glyph (no tofu boxes) — preview page 1 before delivering.
- Sentences are short, useful, and reuse words from earlier sections.

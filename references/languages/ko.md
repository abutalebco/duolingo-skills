# Korean (한국어) — worksheet guide

| Field | Value |
|---|---|
| Code | ko |
| Script | Hangul |
| Direction | left-to-right |
| Reading aid | Revised Romanization |
| Typst fonts | Noto Sans CJK KR (+ DejaVu Sans fallback) |
| Typst lang/region | ko |
| Cell grid | Yes (1 character per cell, tian-zi style) |
| Duolingo status | established course |

## Teach and drill (pick content from here)

- Hangul letters (14 consonants, 10 vowels) then syllable blocks
- Batchim (final consonants) and pronunciation changes (연음, 비음화)
- Particles 은/는, 이/가, 을/를, 에, 에서
- Polite -요 and formal -ㅂ니다 endings
- Sino-Korean vs native Korean numbers

## How to fill entries

`text` = Hangul. `reading` omitted (Hangul is the reading). `roman` = Revised Romanization as pronounced. `meaning` = English.

## Pitfalls

- Each syllable block is one cell; spaces between words (띄어쓰기) are real and show as empty cells
- Romanize what is pronounced for `roman`, not letter-by-letter, and say so once in the sheet subtitle
- Use Hangul only in `text`; no hanja

## Layout behaviour

- Words: first row = faded copies of the word, then blank cells; `rows` adds more blank rows.
- Sentences: for every row of characters, a faded row followed by a blank row directly beneath it.

## Starter section ideas

Greetings & introductions · Numbers 1–20 · Food & drink · Family · Places & directions · Time & days · Everyday verbs · Short sentences / mini dialogues

- **Cells**: one syllable block per cell; default 1.15 cm. Spaces between words consume one empty cell, which doubles as a word-gap marker.


## Quality checklist

- Every `text` is natural and correct; no machine-looking literal translations.
- Diacritics/special letters verified (see Pitfalls).
- Fonts render every glyph (no tofu boxes) — preview page 1 before delivering.
- Sentences are short, useful, and reuse words from earlier sections.

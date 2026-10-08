# Japanese (日本語) — worksheet guide

| Field | Value |
|---|---|
| Code | ja |
| Script | Hiragana + Katakana + Kanji |
| Direction | left-to-right |
| Reading aid | kana reading + romaji (Hepburn) |
| Typst fonts | Noto Sans CJK JP (+ DejaVu Sans fallback) |
| Typst lang/region | ja |
| Cell grid | Yes (1 character per cell, tian-zi style) |
| Duolingo status | established course |

## Teach and drill (pick content from here)

- Hiragana and katakana first (46 + 46 base signs, then dakuten/handakuten, small ya/yu/yo, small tsu)
- Kanji introduced gradually, school grade-1/2 kanji first, always with kana reading
- Particles は (wa), を (o), へ (e): romanize by pronunciation, not by spelling
- Long vowels (おう, えい, ー) and doubled consonants (っ)
- Counters and polite -ます/です forms before plain forms

## How to fill entries

`text` = natural Japanese (kanji + kana as a native would write it). `reading` = full hiragana reading. `roman` = Hepburn romaji. For single kanji, put on-yomi/kun-yomi in `note`.

## Pitfalls

- No spaces between words in Japanese sentences; never insert any
- Use Japanese punctuation 。、「」 and full-width forms, not ASCII . ,
- Never invent stroke order; if shown, take it from KanjiVG (CC BY-SA 3.0) and credit it
- Keep one reading per entry; put alternate readings (音読み/訓読み) in `note`

## Layout behaviour

- Words: first row = faded copies of the word, then blank cells; `rows` adds more blank rows.
- Sentences: for every row of characters, a faded row followed by a blank row directly beneath it.

## Starter section ideas

Greetings & introductions · Numbers 1–20 · Food & drink · Family · Places & directions · Time & days · Everyday verbs · Short sentences / mini dialogues

## Japanese specifics
- **Cells**: 1 character per cell (kana, kanji, 、 and 。 each take a cell). Default cell 1.15 cm; use 1.3 cm for kanji sections, 1.0 cm for kana drills.
- **Font**: `Noto Sans CJK JP` is the safe default. A textbook-style font (教科書体, e.g. "UD Digi Kyokasho", "Klee One") shows real handwriting shapes and is better for tracing when installed; always keep the Noto fallback.
- **Progression** (use as section order): hiragana rows → katakana rows → dakuten & combos → grade-1 kanji words → particles/sentences → numbers & counters → daily-life sentences.
- **Sentence length**: 6–14 characters per sentence keeps one trace row + one blank row per card.
- **Kana charts**: use `type: "words"` with `text` = one kana, `roman` = romaji, `rows: 2` for extra rewrite space.


## Quality checklist

- Every `text` is natural and correct; no machine-looking literal translations.
- Diacritics/special letters verified (see Pitfalls).
- Fonts render every glyph (no tofu boxes) — preview page 1 before delivering.
- Sentences are short, useful, and reuse words from earlier sections.

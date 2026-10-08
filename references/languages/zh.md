# Chinese (Mandarin) (中文) — worksheet guide

| Field | Value |
|---|---|
| Code | zh |
| Script | Hanzi (Simplified by default) |
| Direction | left-to-right |
| Reading aid | pinyin with tone marks |
| Typst fonts | Noto Sans CJK SC (+ DejaVu Sans fallback) |
| Typst lang/region | zh/CN |
| Cell grid | Yes (1 character per cell, tian-zi style) |
| Duolingo status | established course |

## Teach and drill (pick content from here)

- Pinyin with tone marks (not numbers); learn all four tones plus neutral
- Radicals and component reuse (氵 water, 口 mouth, 女 woman, 木 tree)
- Measure words (个, 本, 杯, 只) with every noun they commonly pair with
- High-frequency characters first (HSK 1 ordering is a good backbone)
- Question forms: 吗, 什么, 哪儿, 几, 多少

## How to fill entries

`text` = Hanzi. `reading` = pinyin with tone marks, syllables separated by spaces for sentences and joined for words (xuéshēng). `meaning` = English.

## Pitfalls

- Pinyin tone-mark placement: a > e > o; in iu/ui the mark goes on the last vowel
- Write base tones in `reading`; mention sandhi (你好 nǐ hǎo is spoken ní hǎo, 不 bù→bú) in `note`
- Use Chinese punctuation 。，？！ and no spaces inside Chinese sentences
- Do not mix Simplified and Traditional; Traditional = set `config_override` (see vocab-schema.md)
- Never invent stroke order; use Make Me a Hanzi (LGPL / Arphic) or Hanzi Writer data if needed and credit it

## Layout behaviour

- Words: first row = faded copies of the word, then blank cells; `rows` adds more blank rows.
- Sentences: for every row of characters, a faded row followed by a blank row directly beneath it.

## Starter section ideas

Greetings & introductions · Numbers 1–20 · Food & drink · Family · Places & directions · Time & days · Everyday verbs · Short sentences / mini dialogues

## Chinese specifics
- **Cells**: 1 hanzi per cell on a tian zi ge (田字格: dashed cross). Default 1.15 cm; use 1.3 cm for complex characters.
- **Fonts**: `Noto Sans CJK SC` (Simplified), `Noto Sans CJK TC` (Traditional, Taiwan forms). A kaiti (楷体) font such as "KaiTi" or "AR PL UKai" is better for tracing handwriting; keep Noto fallback.
- **Progression**: numbers & greetings → pronouns/to be (是) → family & food → verbs with 想/要/喜欢 → time/place → measure words → short dialogues.
- **Pinyin layout**: `reading` is shown in orange under the character(s); sentences show pinyin once above the grid, never per character.


## Quality checklist

- Every `text` is natural and correct; no machine-looking literal translations.
- Diacritics/special letters verified (see Pitfalls).
- Fonts render every glyph (no tofu boxes) — preview page 1 before delivering.
- Sentences are short, useful, and reuse words from earlier sections.

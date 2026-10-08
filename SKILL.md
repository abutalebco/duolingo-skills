---
name: duolingo-skills
description: Build printable language-learning practice sheets (PDF or Typst) where every word or sentence sits on a green rounded "card" with a faded trace copy and blank space underneath to rewrite it from memory. Covers every real language on Duolingo (Japanese, Chinese, Korean, Spanish, French, German, Arabic, Hindi, Thai, Russian, and 35+ more; fictional languages like Klingon are excluded) with per-language guides, a shared design guide, and vocab JSON data. Use this skill whenever the user wants vocabulary sheets, handwriting or character-writing practice, kana/kanji/hanzi/hangul trace sheets, tian-zi-ge grids, a "write it again" worksheet, a Duolingo-style study PDF, or asks an agent to design, extend, or generate language-learning PDFs or Typst scripts, even if they never say "worksheet" or name this skill. Especially strong for Japanese and Chinese writing practice.
---

# Language practice worksheets

Turns a list of words and sentences into a PDF where each item has: the target text, its reading (kana / pinyin / romanization), the meaning, then a **faded trace row** and **blank space** to rewrite it. Visual style comes from a Duolingo-like infographic: light green page, thick green rounded cards, bold rounded type, orange accents.

## Quick start

```bash
pip install typst --break-system-packages        # once; bundles the Typst compiler
python scripts/build.py assets/vocab/ja.json -o japanese.pdf
python scripts/build.py assets/vocab/zh.json -o chinese.pdf --cell 1.3 --rows 2
```

Always **look at page 1** (rasterize with `pdftoppm -r 60 -png`) before delivering. Missing glyphs show as empty boxes.

## Workflow

1. **Identify the language(s).** Read `references/languages-index.md` for the code, script, direction and status. Then read `references/languages/<code>.md` for that language's drill focus, entry conventions and pitfalls. Do this even for languages you know well: the guide fixes repo-wide conventions (romanization system, which variant, which font).
2. **Write or extend the vocab JSON** following `references/vocab-schema.md`. Start from `assets/vocab/<code>.json` if it exists. Sections are `words` (short cards) or `sentences` (full-width cards). Keep ~10–15 items per section; order from easy to hard; reuse earlier words in later sentences.
3. **Pick layout options** only if the user asked or the content demands it: `--cell` (cm), `--rows` (blank rows per word), `--copies` (faded repeats per word).
4. **Build**: `scripts/build.py` (Typst first, reportlab fallback). Add `--project-dir DIR` when the user wants the editable `.typ` source too. Deliver the PDF and, if requested, the `.typ` project.
5. **Check the render** (page 1 + a sentence page). Fix fonts via `references/typst-guide.md`; fix content via the language guide's checklist.

## Rules that matter (and why)

- **Never write fictional-language courses** (Klingon, High Valyrian...). The user excluded them; every other real language, including constructed-but-real Esperanto and Latin, is in scope.
- **One reading system per language**, as stated in its guide, so sheets stay consistent across a user's whole repo and match what Duolingo teaches.
- **Correct, natural content beats volume.** The user will memorize what is printed; double-check diacritics, tone marks, particles, and gender/article. If unsure of a form, leave it out or flag it in `note`.
- **Do not invent stroke order, pitch accent or tone sandhi data.** Link or credit an open dataset (KanjiVG, Make Me a Hanzi) if the user wants stroke order.
- **Design stays inside `references/design-guide.md`.** Do not copy Duolingo's actual owl or logo; the bundled `assets/mascot.svg` is an original stand-in the user can replace.
- **CJK uses a cell grid, everything else ruled lines.** Connected/complex scripts (Arabic, Hebrew, Devanagari, Thai, Bengali, Tamil, Telugu, Gurmukhi) must never be split into per-letter cells.

## Files

| Path | Read when |
|---|---|
| `references/languages-index.md` | choosing/validating a language and its code |
| `references/languages/<code>.md` | writing content for that language (47 guides) |
| `references/vocab-schema.md` | creating or validating vocab JSON |
| `references/design-guide.md` | changing the look, or building a new layout from scratch |
| `references/typst-guide.md` | fonts, RTL, editing the template, hand-writing `.typ` |
| `references/pdf-fallback.md` | Typst unavailable; what the fallback can and cannot do |
| `assets/template.typ` | the reusable Typst design (entry cards, grids, ruled lines) |
| `assets/languages.json` | registry: fonts, direction, grid mode per language |
| `assets/vocab/*.json` | starter vocab (ja, zh, ko, es) |
| `scripts/build.py` | JSON → PDF |

## Adding a language that isn't there

Add an entry to `assets/languages.json` (copy a similar one), create `references/languages/<code>.md` using an existing guide as the model, and add a row to `references/languages-index.md`. Use `grid: true` only for scripts written one square block per character (Han, Hangul, kana).

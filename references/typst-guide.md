# Typst guide (template internals, fonts, hand-written scripts)

## How the build works

`scripts/build.py` merges `assets/languages.json[lang]` into the vocab JSON as `config`, copies `template.typ` + `mascot.svg` + `data.json` + a 2-line `main.typ` into a temp folder, and compiles:

```typst
#import "template.typ": render
#render(json("data.json"))
```

Engines tried in order: Python package `typst` (`pip install typst`), then the `typst` CLI, then the reportlab fallback.

To hand-edit and compile yourself: `python scripts/build.py vocab.json --project-dir ./proj` then `typst compile proj/main.typ out.pdf` (add `--font-path DIR` for custom fonts).

## Fonts

Typst picks the first font in a list that has each glyph, so lists work as fallbacks. The template uses `ui-font` (Quicksand, Nunito, DejaVu Sans) for UI text and `config.fonts + DejaVu Sans` for target-language text.

| Script | Typst font names (install at least one) |
|---|---|
| Latin / Cyrillic / Greek / Vietnamese | Nunito, Quicksand, Noto Sans |
| Japanese | Noto Sans CJK JP (tracing: UD Digi Kyokasho, Klee One) |
| Chinese (Simplified) | Noto Sans CJK SC (tracing: KaiTi, AR PL UKai) |
| Chinese (Traditional / Cantonese) | Noto Sans CJK TC / HK |
| Korean | Noto Sans CJK KR |
| Arabic / Yiddish-Hebrew | Noto Naskh Arabic, Amiri / Noto Sans Hebrew |
| Devanagari, Bengali, Tamil, Telugu, Gurmukhi, Thai | Noto Sans <Script> |

Check what Typst sees with the CLI: `typst fonts` (the Python package does not ship a CLI; install the CLI from github.com/typst/typst releases, or just check `fc-list | grep -i "noto sans cjk"` on Linux). If glyphs show as boxes, install the font or pass `--font-path`. Typst warns "unknown font family" on stderr but still renders with fallbacks.

## Useful template knobs (top of `template.typ`)

- Colors: `green`, `ink`, `card-a/b`, `trace-c`, `orange`.
- Layout: cell size via `options.cell` (cm), rows via `options.rows`, trace copies via `options.copies`.
- Practice shapes: `cell`, `word-practice`, `sentence-practice`, `ruled`. Each is a pure function; reuse them in new layouts.

## Gotchas learned the hard way

- `str.clusters()` splits by grapheme cluster, which is right for kana with combining marks, Hangul, and emoji; use it, not `.codepoints()`.
- `layout(a => ...)` is how cells auto-fit the card width; `measure()` inside it is what shrinks long alphabetic sentences.
- `block(breakable: false)` keeps cards whole; if one card is taller than a page, Typst overflows; keep sentences short.
- RTL: pass `dir: rtl` on `text` and flip `place` alignment; never reverse the string in the data.
- No `@preview` packages: the sandbox/network may block them. The template is dependency-free on purpose; do not add packages (e.g. rubby for furigana) unless the user's machine is online and they ask.
- Use `#set text(lang: ..., region: ...)` so CJK glyph variants (JP vs SC vs TC) are right.

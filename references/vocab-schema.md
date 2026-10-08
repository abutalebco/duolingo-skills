# Vocab JSON schema

```json
{
  "lang": "ja",                       // required: code from languages.json
  "title": "Japanese",                // optional: big title (default = language name)
  "subtitle": "Starter: kana, words & sentences",   // optional: pill + footer
  "options": {"cell": 1.15, "rows": 1, "copies": 3, "intro": true},   // optional, CLI flags override
  "config_override": {"fonts": ["Noto Sans CJK TC"], "region": "TW"},  // optional (e.g. Traditional Chinese)
  "sections": [
    {
      "title": "Everyday words",      // required
      "type": "words",                // required: "words" | "sentences"
      "note": "Optional line under the banner",
      "items": [
        {
          "text": "学生",              // required: the thing to practice
          "reading": "がくせい",        // optional: kana / pinyin / Jyutping (orange)
          "roman": "gakusei",         // optional: romanization (green italic)
          "meaning": "student",       // optional: English
          "note": "grade-1 kanji + 生" // optional: grammar flag, gender, plural, root...
        }
      ]
    }
  ]
}
```

## Field conventions

- `text`: exactly what a native would write. No spaces for ja/zh/yue; keep real spaces for ko and alphabetic languages.
- `reading` vs `roman`: use `reading` for the pronunciation script that belongs to the language (kana for ja, pinyin for zh, Jyutping for yue) and `roman` for an additional Latin transliteration (romaji, Revised Romanization, transliteration). If the language needs only one, use `reading` for Chinese, `roman` for everything else.
- `meaning`: English by default. If the user wants another instruction language, use that language everywhere in the file.
- `note`: short (≤ 40 characters ideal; it sits under the meaning).

## Limits that keep the layout intact

- Words: ≤ 6 characters for CJK (≥ 3 faded copies fit in one 13-cell row), ≤ 18 characters for alphabetic text.
- Sentences: CJK any length (rows wrap, ~13 chars per row); alphabetic ≲ 60 characters (trace auto-shrinks; longer gets unreadably small, split into two entries).
- ≤ 15 items per section so a section reads as one study block.

## Validation

`scripts/build.py` rejects unknown language codes, section types other than `words`/`sentences`, and items without `text`. It does not check linguistic correctness: follow the language guide's checklist.

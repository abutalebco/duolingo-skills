# AGENTS.md

Agents: read `SKILL.md` first. It holds the workflow and rules; everything else is linked from its file table.

Minimum path for a request like "make a <language> practice sheet":
1. `references/languages-index.md` → language code.
2. `references/languages/<code>.md` → conventions and pitfalls.
3. Write vocab JSON per `references/vocab-schema.md` (start from `assets/vocab/<code>.json` if present).
4. `pip install typst` then `python scripts/build.py <vocab.json> -o <out.pdf>`.
5. Rasterize page 1 and check for missing glyphs before delivering.

Rules: real languages only (no Klingon etc.); follow `references/design-guide.md`; never copy Duolingo's mascot, logo or name onto sheets.

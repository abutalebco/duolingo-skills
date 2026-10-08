# Design guide (shared by every language)

Source of the look: a green infographic with rounded boxes, a huge rounded title, alternating text/mascot cards, and orange accents. The goal is a **friendly, high-contrast, low-clutter study sheet** that prints well on A4.

## Palette

| Token | Hex | Used for |
|---|---|---|
| green | `#58CC02` | title, card borders, section banners, badges, practice-cell borders |
| green-dark | `#3F8F00` | subtitles, notes, footer |
| ink | `#2E5A0C` | main text (never pure black: keeps the green mood, still AA contrast on the light cards) |
| page-bg | `#F2FCE6` | page fill |
| card-a / card-b | `#DCEFB5` / `#E8F8D2` | alternating card fills (mimics the alternating boxes in the reference) |
| trace | `#B4D386` | faded characters to trace over |
| guide | `#A9D07A` | dashed cross/baseline guides |
| orange | `#E08700` | readings (kana/pinyin), subtitle pill, mascot beak/feet |
| white | `#FFFFFF` | the practice area inside each card |

Contrast rules: body text on cards ≥ 4.5:1 (ink on card-a passes). Trace text is *intentionally* faint; it must still be visible when printed on a laser printer. If a printer washes it out, darken `trace` to `#9CC468`, not black.

## Typography

- UI/headings: a rounded geometric sans: **Quicksand** or **Nunito** (free, Google Fonts). Fallback DejaVu Sans. Title 38 pt bold in green; section banner 15 pt bold white on green.
- Target-language text: bold, 30 pt (CJK words) / 24 pt (alphabetic words) / 17–19 pt (sentences).
- Reading line: orange, bold, 11 pt. Romanization: green-dark italic 10.5 pt. Meaning: ink bold 12 pt, right-aligned on word cards, under the sentence on sentence cards. Notes: 9 pt green-dark.

## Page anatomy (A4 portrait, margins 1.3 cm sides / 1.2 top / 1.5 bottom)

1. **Header**: big green title (left), orange pill with native name + subtitle underneath, mascot (right, ~2.5 cm).
2. **"How to practice" card** (optional): three columns: Say it / Trace it / Recall it.
3. **Section banner**: full-width green rounded bar with white title (sticky: never orphaned at page bottom). Optional one-line note under it.
4. **Entry cards**, one per word/sentence:
   - 2.2 pt green border, 14 pt corner radius, 10 pt padding, 10 pt gap between cards, never split across pages.
   - Top row: numbered green circle badge → target text (+ reading, romanization) → meaning.
   - Bottom: white rounded practice area.
5. **Footer**: centered, 8.5 pt: language · subtitle · page number.

## Practice area

- **CJK / Hangul (grid)**: square cells (default 1.15 cm, 3 pt gutter) with a dashed cross (tian zi ge) and 1 pt green border.
  - *Word card*: row of faded copies of the word (default 3 where they fit), remaining cells blank; `rows` adds extra blank rows.
  - *Sentence card*: for each row of characters, a faded row, then a blank row of the same length directly under it. The learner traces, then rewrites with the model right above.
- **Alphabetic and complex scripts (ruled)**: 1.05 cm line with solid baseline and dashed x-height guide. Word card: word faded 3×; sentence card: one faded sentence line (auto-shrinks up to ~60 chars); then blank line(s). RTL scripts start at the right edge.

## Density & page budget

Aim for 6–8 word cards or 4–5 sentence cards per page. If items spill, reduce `--rows` first, `--cell` second (never below 0.9 cm for kanji/hanzi; handwriting needs space).

## Do / Don't

- Do alternate card fills, keep generous rounded corners, keep one accent color (orange) for readings only.
- Do keep text left-aligned (right-aligned for RTL); center only titles and footer.
- Don't add clip-art per card, gradients, drop shadows, or more than the 3 accent colors; print cost and clutter.
- Don't copy Duolingo's owl, logo, wordmark, or the "Duolingo" name onto sheets. The look is inspired by it; the sheets are the user's own study materials. Use `assets/mascot.svg` (original) or a user-provided image.
- Don't put reading/romanization *inside* the practice cells; cells hold only the target characters.

## Variants an agent may offer (only if asked)

- Print-saver: `--no-intro`, white page background (`page-bg` → `#FFFFFF`), trace `#9CC468`.
- Large-print: `--cell 1.4 --rows 1`.
- Drill sheet (kana charts): `type: words`, one character per entry, `--rows 2 --copies 2`.

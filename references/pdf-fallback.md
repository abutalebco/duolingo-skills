# PDF fallback (reportlab)

`scripts/build_pdf_fallback.py` runs only when Typst isn't available (or `--fallback`). It draws the same cards with simpler typography.

Supported: left-to-right Latin/Cyrillic/Greek (needs a Latin TTF, auto-found: DejaVu/Arial) and CJK via reportlab's built-in CID fonts (HeiseiKakuGo-W5 ja, STSong-Light zh, MSung-Light yue, HYSMyeongJo-Medium ko).

Not supported: RTL and complex scripts (Arabic, Hebrew, Yiddish, Hindi, Bengali, Tamil, Telugu, Punjabi, Thai). The script exits with a message; install Typst instead.

Caveats:
- CID fonts are **not embedded**; the viewer must have a CJK font (desktop viewers do; some previewers and the sandbox's poppler do not, so glyphs may look blank there).
- No mascot image, fixed Latin font, no auto-shrink of long sentences.
- Prefer `pip install typst`; it is one command and gives the real design.

Override the Latin/reading font: `FALLBACK_FONT=/path/font.ttf python scripts/build.py ... --fallback`.

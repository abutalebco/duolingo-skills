"""reportlab fallback for build.py (used only when Typst is unavailable).

Supports CJK (grid cells) and left-to-right alphabetic scripts that the chosen
TTF covers. NOT supported: right-to-left or complex shaping (Arabic, Hebrew,
Hindi, Thai, ...). Use Typst for those.

Set FALLBACK_FONT=/path/to/font.ttf to choose the Latin/reading font.
"""
import os
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GREEN, DARK, INK = HexColor("#58CC02"), HexColor("#3F8F00"), HexColor("#2E5A0C")
BG, CARD_A, CARD_B = HexColor("#F2FCE6"), HexColor("#DCEFB5"), HexColor("#E8F8D2")
TRACE, GUIDE, ORANGE = HexColor("#B4D386"), HexColor("#A9D07A"), HexColor("#E08700")

# reportlab cannot embed CFF-based OpenType (Noto CJK), so CJK uses its built-in CID fonts.
# They are NOT embedded: the PDF viewer must have a CJK font installed (all desktop viewers do).
CID_FONT = {"ja": "HeiseiKakuGo-W5", "zh": "STSong-Light", "yue": "MSung-Light", "ko": "HYSMyeongJo-Medium"}
LATIN_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "C:/Windows/Fonts/arial.ttf",
    "/Library/Fonts/Arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def register(cfg):
    """Return (target_font, latin_font) names. latin_font covers readings/meanings."""
    latin = "Helvetica"
    env = os.environ.get("FALLBACK_FONT")
    for p in ([env] if env else []) + LATIN_PATHS:
        if p and Path(p).exists():
            pdfmetrics.registerFont(TTFont("L", p)); latin = "L"; break
    if cfg["grid"]:
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        name = CID_FONT.get(cfg["code"], "STSong-Light")
        pdfmetrics.registerFont(UnicodeCIDFont(name))
        return name, latin
    if cfg["dir"] == "rtl" or ("Latin" not in cfg["script"] and cfg["script"] not in ("Cyrillic", "Greek")):
        raise SystemExit("reportlab fallback cannot shape this script; install typst (pip install typst)")
    if latin == "Helvetica":
        raise SystemExit("No Latin TTF found; set FALLBACK_FONT=/path/to/font.ttf")
    return latin, latin


def rrect(c, x, y, w, h, r, fill, stroke=GREEN, lw=2):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1)


def cell(c, x, y, s, ch, font):
    c.setFillColor(white); c.setStrokeColor(GREEN); c.setLineWidth(1)
    c.roundRect(x, y, s, s, 2, fill=1, stroke=1)
    c.setStrokeColor(GUIDE); c.setLineWidth(.4); c.setDash(2, 2)
    c.line(x, y + s / 2, x + s, y + s / 2); c.line(x + s / 2, y, x + s / 2, y + s); c.setDash()
    if ch:
        c.setFillColor(TRACE); c.setFont(font, s * .68)
        c.drawCentredString(x + s / 2, y + s * .2, ch)


def build(data, out):
    cfg, o = data["config"], {"cell": 1.15, "rows": 1, "copies": 3, "intro": True}
    o.update(data.get("options", {}))
    TF, LF = register(cfg)
    c = __import__("reportlab.pdfgen.canvas", fromlist=["Canvas"]).Canvas(str(out), pagesize=A4)
    W, H = A4
    M, s = 1.3 * cm, o["cell"] * cm
    inner = W - 2 * M - 2 * 14
    per = max(1, int((inner + 3) // (s + 3)))
    state = {"y": H - 1.2 * cm, "n": 0}

    def page():
        c.setFillColor(BG); c.rect(0, 0, W, H, fill=1, stroke=0)
        state["y"] = H - 1.2 * cm

    def new_page():
        c.showPage(); page()

    page()
    c.setFillColor(GREEN); c.setFont(LF, 34)
    c.drawString(M, state["y"] - 34, data.get("title", cfg["name"]))
    c.setFillColor(ORANGE); c.setFont(LF, 11)
    c.drawString(M, state["y"] - 54, f'{cfg["name"]} · {data.get("subtitle", "practice")}')
    state["y"] -= 70

    for sec in data["sections"]:
        if state["y"] < 6 * cm:
            new_page()
        rrect(c, M, state["y"] - 22, W - 2 * M, 22, 8, GREEN)
        c.setFillColor(white); c.setFont(LF, 13); c.drawString(M + 10, state["y"] - 16, sec["title"])
        state["y"] -= 30
        for it in sec["items"]:
            state["n"] += 1
            txt = it["text"]
            words = sec["type"] == "words"
            chars = list(txt)
            if cfg["grid"]:
                if words:
                    row = []
                    for _ in range(o["copies"]):
                        if len(row) + len(chars) <= per:
                            row += chars
                    rows = [row + [None] * (per - len(row))] + [[None] * per for _ in range(o["rows"] - 1)]
                else:
                    rows = []
                    for i in range(0, len(chars), per):
                        ch = chars[i:i + per]
                        rows += [ch, [None] * len(ch)]
                prac_h = len(rows) * (s + 3) + 8
            else:
                rows = None
                prac_h = (1 + o["rows"]) * 1.0 * cm + 8
            card_h = 14 + 34 + prac_h + 14
            if state["y"] - card_h < 1.5 * cm:
                new_page()
            top = state["y"]
            rrect(c, M, top - card_h, W - 2 * M, card_h, 12, CARD_A if state["n"] % 2 else CARD_B)
            c.setFillColor(GREEN); c.circle(M + 22, top - 24, 10, fill=1, stroke=0)
            c.setFillColor(white); c.setFont(LF, 10); c.drawCentredString(M + 22, top - 28, str(state["n"]))
            c.setFillColor(INK); c.setFont(TF, 22 if words else 15); c.drawString(M + 40, top - 28, txt)
            sub = "  ".join(x for x in (it.get("reading"), it.get("roman")) if x)
            c.setFillColor(ORANGE); c.setFont(LF, 9.5); c.drawString(M + 40, top - 42, sub)
            if it.get("meaning"):
                c.setFillColor(INK); c.setFont(LF, 11); c.drawRightString(W - M - 14, top - 28, it["meaning"])
            py = top - 14 - 34
            rrect(c, M + 8, py - prac_h, W - 2 * M - 16, prac_h, 8, white, HexColor("#CFE8A6"), 1)
            if rows:
                y = py - 4 - s
                for r in rows:
                    for i, ch in enumerate(r):
                        cell(c, M + 14 + i * (s + 3), y, s, ch, TF)
                    y -= s + 3
            else:
                lines = [("  ".join([txt] * o["copies"]) if words else txt)] + [None] * o["rows"]
                y = py - 1.0 * cm
                for t in lines:
                    c.setStrokeColor(GREEN); c.setLineWidth(1); c.line(M + 14, y, W - M - 14, y)
                    if t:
                        c.setFillColor(TRACE); c.setFont(TF, 17 if words else 13)
                        c.drawString(M + 16, y + 3, t)
                    y -= 1.0 * cm
            state["y"] = top - card_h - 8
    c.save()

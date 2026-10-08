#!/usr/bin/env python3
"""Build a language practice worksheet PDF from a vocab JSON file.

  python scripts/build.py assets/vocab/ja.json -o ja.pdf
  python scripts/build.py my-words.json -o out.pdf --cell 1.3 --rows 2 --copies 2
  python scripts/build.py assets/vocab/zh.json --project-dir ./zh-typst   # keep .typ project too

Engine order: `typst` python package -> `typst` CLI -> reportlab fallback.
Typst is preferred (best typography, RTL, complex scripts). The fallback only
supports left-to-right scripts and CJK; it exists so a PDF is always produced.
"""
import argparse, json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

MAIN_TYP = '#import "template.typ": render\n#render(json("data.json"))\n'


def load(data_path: Path, args) -> dict:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    registry = json.loads((ASSETS / "languages.json").read_text(encoding="utf-8"))
    code = data["lang"]
    if code not in registry:
        sys.exit(f"Unknown lang '{code}'. Known: {', '.join(sorted(registry))}")
    cfg = dict(registry[code])
    cfg.update(data.get("config_override", {}))  # e.g. Traditional Chinese fonts/region
    data["config"] = cfg
    opts = data.setdefault("options", {})
    for k in ("cell", "rows", "copies"):
        v = getattr(args, k)
        if v is not None:
            opts[k] = v
    if args.no_intro:
        opts["intro"] = False
    for sec in data["sections"]:
        if sec["type"] not in ("words", "sentences"):
            sys.exit(f"Section '{sec.get('title')}': type must be 'words' or 'sentences'")
        for it in sec["items"]:
            if "text" not in it:
                sys.exit(f"Item without 'text' in section '{sec['title']}'")
    return data


def write_project(proj: Path, data: dict):
    proj.mkdir(parents=True, exist_ok=True)
    (proj / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    (proj / "main.typ").write_text(MAIN_TYP, encoding="utf-8")
    for f in ("template.typ", "mascot.svg"):
        shutil.copy(ASSETS / f, proj / f)


def compile_typst(proj: Path, out: Path, font_paths):
    try:
        import typst  # pip install typst
        typst.compile(str(proj / "main.typ"), output=str(out), font_paths=[str(p) for p in font_paths])
        return True
    except ImportError:
        pass
    exe = shutil.which("typst")
    if exe:
        cmd = [exe, "compile", str(proj / "main.typ"), str(out)]
        for p in font_paths:
            cmd += ["--font-path", str(p)]
        subprocess.run(cmd, check=True)
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("vocab", type=Path)
    ap.add_argument("-o", "--out", type=Path)
    ap.add_argument("--cell", type=float, help="practice cell size in cm (default 1.15)")
    ap.add_argument("--rows", type=int, help="blank practice rows per card (default 1)")
    ap.add_argument("--copies", type=int, help="faded trace copies per word (default 3)")
    ap.add_argument("--no-intro", action="store_true")
    ap.add_argument("--font-path", action="append", default=[], type=Path)
    ap.add_argument("--project-dir", type=Path, help="write the Typst project here and keep it")
    ap.add_argument("--fallback", action="store_true", help="force reportlab fallback")
    args = ap.parse_args()

    data = load(args.vocab, args)
    out = args.out or Path(args.vocab.stem + ".pdf")
    out = out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    if not args.fallback:
        if args.project_dir:
            proj = args.project_dir.resolve()
            write_project(proj, data)
            ok = compile_typst(proj, out, args.font_path)
        else:
            with tempfile.TemporaryDirectory() as td:
                proj = Path(td)
                write_project(proj, data)
                ok = compile_typst(proj, out, args.font_path)
        if ok:
            print(f"Built {out} with Typst")
            return
        print("Typst not available (pip install typst); using reportlab fallback", file=sys.stderr)

    sys.path.insert(0, str(Path(__file__).parent))
    from build_pdf_fallback import build
    build(data, out)
    print(f"Built {out} with reportlab fallback")


if __name__ == "__main__":
    main()

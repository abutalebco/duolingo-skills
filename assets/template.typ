// Language practice worksheet template — green, rounded "card" look.
// main.typ:  #import "template.typ": render
//            #render(json("data.json"))
// data.json = vocab file + merged "config" (see references/vocab-schema.md)

#let green = rgb("#58CC02")
#let green-dark = rgb("#3F8F00")
#let ink = rgb("#2E5A0C")
#let page-bg = rgb("#F2FCE6")
#let card-a = rgb("#DCEFB5")
#let card-b = rgb("#E8F8D2")
#let trace-c = rgb("#B4D386")
#let guide-c = rgb("#A9D07A")
#let orange = rgb("#E08700")
#let ui-font = ("Quicksand", "Nunito", "DejaVu Sans")

// ---------- practice primitives ----------
#let dashed = (paint: guide-c, thickness: 0.5pt, dash: "dashed")

// One square practice cell with dashed cross guides (tian zi ge style).
// ch = none -> blank; ch = string -> faded trace character.
#let cell(ch, size) = box(
  width: size, height: size, fill: white, stroke: 1pt + green, radius: 3pt, clip: true, {
    place(top + left, line(start: (0pt, size / 2), end: (size, size / 2), stroke: dashed))
    place(top + left, line(start: (size / 2, 0pt), end: (size / 2, size), stroke: dashed))
    if ch != none {
      place(center + horizon, text(size: size * 0.72, fill: trace-c, top-edge: "bounds", bottom-edge: "bounds")[#ch])
    }
  })

// items: array of none (blank cell) | string (trace) | auto (no cell)
#let cell-grid(items, size, per-row, font, lang, region) = {
  set text(font: font, lang: lang, region: region)
  grid(
    columns: (size,) * per-row, column-gutter: 3pt, row-gutter: 3pt,
    ..items.map(c => if c == auto { [] } else { cell(c, size) }),
  )
}

// Word: first row = faded copies of the word then blanks; extra rows blank.
#let word-practice(word, size, rows, copies, font, lang, region) = layout(a => {
  let gut = 3pt
  let per = calc.max(1, calc.floor((a.width + gut) / (size + gut)))
  let cs = word.clusters()
  let row = ()
  for i in range(copies) { if row.len() + cs.len() <= per { row += cs } }
  if row.len() == 0 { row = cs.slice(0, calc.min(cs.len(), per)) }
  row += (none,) * (per - row.len())
  cell-grid(row + (none,) * (per * (rows - 1)), size, per, font, lang, region)
})

// Sentence: per chunk of per-row chars -> faded row, then blank row under it.
#let sentence-practice(txt, size, font, lang, region) = layout(a => {
  let gut = 3pt
  let per = calc.max(1, calc.floor((a.width + gut) / (size + gut)))
  let cs = txt.clusters()
  let out = ()
  let i = 0
  while i < cs.len() {
    let chunk = cs.slice(i, calc.min(i + per, cs.len()))
    let pad = (auto,) * (per - chunk.len())
    out += chunk + pad
    out += (none,) * chunk.len() + pad
    i += per
  }
  cell-grid(out, size, per, font, lang, region)
})

// Ruled writing line for alphabetic scripts; txt = faded trace or none.
#let ruled(txt, h, is-rtl, font, lang, region, tsize) = layout(a => {
  let w = a.width
  let t = if txt == none { none } else {
    text(size: tsize, font: font, lang: lang, region: region, bottom-edge: "baseline")[#txt]
  }
  let f = if t == none { 1 } else { calc.min(1, w / measure(t).width) }
  box(width: w, height: h, {
    place(top + left, dy: h * 0.76, line(length: w, stroke: 1pt + green))
    place(top + left, dy: h * 0.50, line(length: w, stroke: dashed))
    if t != none {
      place(if is-rtl { right + bottom } else { left + bottom }, dy: -(h * 0.24),
        text(size: tsize * f, fill: trace-c, font: font, lang: lang, region: region, bottom-edge: "baseline", dir: if is-rtl { rtl } else { ltr })[#txt])
    }
  })
})

#let badge(n) = box(width: 22pt, height: 22pt, radius: 11pt, fill: green,
  align(center + horizon, text(fill: white, weight: "bold", size: 11pt)[#n]))

#let pill(body, fill: orange) = box(fill: fill, radius: 10pt, inset: (x: 9pt, y: 4pt),
  text(fill: white, weight: "bold", size: 10.5pt)[#body])

// ---------- one entry card ----------
#let entry(n, item, kind, cfg, o, tone) = {
  let font = cfg.fonts + ("DejaVu Sans",)
  let lang = cfg.lang
  let region = cfg.at("region", default: none)
  let is-rtl = cfg.dir == "rtl"
  let cjk = cfg.grid
  let size = o.cell * 1cm
  let tdir = if is-rtl { rtl } else { ltr }
  let txt = item.text
  let reading = item.at("reading", default: none)
  let roman = item.at("roman", default: none)
  let meaning = item.at("meaning", default: none)
  let note = item.at("note", default: none)
  let big = if kind == "words" { if cjk { 30pt } else { 24pt } } else { if cjk { 19pt } else { 17pt } }
  let target = text(font: font, lang: lang, region: region, dir: tdir, size: big, weight: "bold", fill: ink)[#txt]
  let sub = {
    if reading != none { text(fill: orange, weight: "bold", size: 11pt, font: font)[#reading] }
    if reading != none and roman != none { h(8pt) }
    if roman != none { text(fill: green-dark, size: 10.5pt, style: "italic", font: font)[#roman] }
  }
  let mean = if meaning != none { text(weight: "bold", size: 12pt, fill: ink)[#meaning] }
  let notes = if note != none { text(size: 9pt, fill: green-dark)[#note] }

  block(width: 100%, breakable: false, fill: tone, stroke: 2.2pt + green, radius: 14pt,
    inset: 10pt, above: 10pt, below: 0pt, {
    if kind == "words" {
      grid(columns: (auto, auto, 1fr), column-gutter: 12pt, align: horizon,
        badge(n),
        stack(spacing: 4pt, target, sub),
        align(right, stack(spacing: 3pt, mean, notes)))
    } else {
      grid(columns: (auto, 1fr), column-gutter: 12pt, align: horizon,
        badge(n),
        stack(spacing: 5pt, align(if is-rtl { right } else { left }, target), sub, mean, notes))
    }
    v(7pt)
    block(fill: white, radius: 8pt, inset: 6pt, width: 100%, stroke: 1pt + rgb("#CFE8A6"), {
      if cjk {
        if kind == "words" { word-practice(txt, size, o.rows, o.copies, font, lang, region) }
        else { sentence-practice(txt, size, font, lang, region) }
      } else {
        let lh = 1.05cm
        let tsize = if kind == "words" { 20pt } else { 15pt }
        let trace = if kind == "words" {
          range(o.copies).map(_ => txt).join(h(1.4em))
        } else { txt }
        ruled(trace, lh, is-rtl, font, lang, region, tsize)
        for _ in range(o.rows) { ruled(none, lh, is-rtl, font, lang, region, tsize) }
      }
    })
  })
}

// ---------- document ----------
#let render(data) = {
  let cfg = data.config
  let o = (cell: 1.15, rows: 1, copies: 3, intro: true) + data.at("options", default: (:))
  set page(paper: "a4", margin: (x: 1.3cm, top: 1.2cm, bottom: 1.5cm), fill: page-bg,
    footer: context align(center, text(size: 8.5pt, fill: green-dark, font: ui-font)[#cfg.name · #data.at("subtitle", default: "practice") · page #counter(page).display()]))
  set text(font: ui-font + cfg.fonts, fill: ink, size: 11pt)
  set par(leading: 0.55em)

  grid(columns: (1fr, auto), align: horizon, column-gutter: 10pt,
    stack(spacing: 9pt,
      text(size: 38pt, weight: "bold", fill: green)[#data.at("title", default: cfg.name)],
      pill([#cfg.native · #data.at("subtitle", default: "practice")])),
    image("mascot.svg", height: 2.5cm))

  if o.intro {
    block(width: 100%, breakable: false, fill: card-a, stroke: 2.2pt + green, radius: 14pt, inset: 12pt, above: 12pt, below: 0pt, {
      text(size: 14pt, weight: "bold", fill: green-dark)[How to practice]
      v(4pt)
      grid(columns: (1fr,) * 3, column-gutter: 10pt,
        [*1. Say it* \ Read the word aloud, then the meaning.],
        [*2. Trace it* \ Write over the faded characters.],
        [*3. Recall it* \ Cover the card and fill the blanks from memory.])
    })
  }

  let n = 0
  for sec in data.sections {
    block(sticky: true, width: 100%, fill: green, radius: 12pt, inset: (x: 12pt, y: 7pt), above: 16pt, below: 0pt,
      text(fill: white, weight: "bold", size: 15pt)[#sec.title])
    if "note" in sec { v(3pt); text(size: 9.5pt, fill: green-dark)[#sec.note] }
    for item in sec.items {
      n += 1
      entry(n, item, sec.type, cfg, o, if calc.odd(n) { card-a } else { card-b })
    }
  }
}

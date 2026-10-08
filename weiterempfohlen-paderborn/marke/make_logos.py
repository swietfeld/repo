import io, glob
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb

from pathlib import Path
BASE = str(Path(__file__).resolve().parent.parent) + "/"
FONTS = BASE + "render/fonts/"
OUT = BASE + "marke/logos/"
INK, PAPER, MUSTARD, PETROL = "#1F2A2B", "#F6F1E7", "#F2C14E", "#417572"

def load(prefix, wght):
    for p in sorted(glob.glob(FONTS + prefix + "*.woff2")):
        f = TTFont(p)
        if ord("W") in f.getBestCmap():
            f = instancer.instantiateVariableFont(f, {"wght": wght})
            f.flavor = None
            buf = io.BytesIO(); f.save(buf); data = buf.getvalue()
            tt = TTFont(io.BytesIO(data))
            face = hb.Face(data); font = hb.Font(face)
            return tt, font
    raise SystemExit("font not found " + prefix)

BRIC = load("3y9H6as8", 800)
DMS = load("rP2Yp2yw", 700)

def shape(fnt, text, size, x, y, tracking=0):
    tt, font = fnt
    upem = tt["head"].unitsPerEm; s = size / upem
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    paths = []; pen_x = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        sp = SVGPathPen(gs)
        tp = TransformPen(sp, (s, 0, 0, -s, x + (pen_x + pos.x_offset) * s, y - pos.y_offset * s))
        gs[name].draw(tp)
        paths.append((info.cluster, sp.getCommands()))
        pen_x += pos.x_advance + tracking / s
    width = pen_x * s
    return paths, width

def width_of(fnt, text, size, tracking=0):
    return shape(fnt, text, size, 0, 0, tracking)[1]

def wordmark_paths(size, x, y, text_color, dot_color):
    word = "Weiterempfohlen."
    paths, w = shape(BRIC, word, size, x, y)
    main = "".join(d for c, d in paths if word[c] != ".")
    dot = "".join(d for c, d in paths if word[c] == ".")
    return f'<path d="{main}" fill="{text_color}"/><path d="{dot}" fill="{dot_color}"/>', w

def symbol(cx, cy, r, circle, arrow):
    k = r / 50.0
    sw = 10 * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{circle}"/>'
            f'<path d="M{cx-22*k} {cy}H{cx+20*k}M{cx+5*k} {cy-15*k}L{cx+21*k} {cy}L{cx+5*k} {cy+15*k}" '
            f'fill="none" stroke="{arrow}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')

def svg(w, h, body, bg=None):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{rect}{body}</svg>\n'

def save(name, content):
    open(OUT + name, "w").write(content)

# Wordmark
size = 200
tt = BRIC[0]; upem = tt["head"].unitsPerEm
asc = tt["OS/2"].sCapHeight * size / upem if hasattr(tt["OS/2"], "sCapHeight") else size * 0.7
pad = 40
_, w = wordmark_paths(size, 0, 0, INK, MUSTARD)
H = asc + 0.25 * size + 2 * pad
base_y = pad + asc
W = w + 2 * pad
for fname, tc, dc in [("wortmarke_dunkel.svg", INK, MUSTARD), ("wortmarke_hell.svg", PAPER, MUSTARD),
                      ("wortmarke_einfarbig_dunkel.svg", INK, INK), ("wortmarke_einfarbig_hell.svg", PAPER, PAPER)]:
    body, _ = wordmark_paths(size, pad, base_y, tc, dc)
    save(fname, svg(W, H, body))

# Symbol (Zeichen)
for fname, c, a in [("zeichen.svg", MUSTARD, INK), ("zeichen_dunkel.svg", INK, MUSTARD)]:
    save(fname, svg(400, 400, symbol(200, 200, 200, c, a)))

# Kombination: Zeichen + Wortmarke
r = asc * 0.62
sx = pad + r
gap = 0.35 * size
for fname, tc in [("logo_kombi_dunkel.svg", INK), ("logo_kombi_hell.svg", PAPER)]:
    body, _ = wordmark_paths(size, pad + 2 * r + gap, base_y, tc, MUSTARD)
    cy = base_y - asc / 2
    sym = symbol(sx, cy, r, MUSTARD, INK)
    save(fname, svg(W + 2 * r + gap, H, sym + body))

# Aufkleber (rund, 1000 x 1000)
D = 1000; c = D / 2
body = f'<circle cx="{c}" cy="{c}" r="{c}" fill="{MUSTARD}"/><circle cx="{c}" cy="{c}" r="{c-44}" fill="none" stroke="{INK}" stroke-width="6"/>'
top = "PADERBORN EMPFIEHLT"; tsize = 44; trk = 6
tw = width_of(DMS, top, tsize, trk)
p, _ = shape(DMS, top, tsize, c - tw / 2, 290, trk)
body += f'<path d="{"".join(d for _, d in p)}" fill="{INK}"/>'
w2 = width_of(BRIC, "empfohlen.", 100)
wsize = 100 * 680 / w2
l1w = width_of(BRIC, "Weiter", wsize)
p1, _ = shape(BRIC, "Weiter", wsize, c - l1w / 2, 470)
body += f'<path d="{"".join(d for _, d in p1)}" fill="{INK}"/>'
word2 = "empfohlen."
p2, _ = shape(BRIC, word2, wsize, c - 340, 470 + wsize * 0.98)
body += f'<path d="{"".join(d for cl, d in p2)}" fill="{INK}"/>'
yr = "2027"; ysize = 44
yw = width_of(DMS, yr, ysize, trk)
p, _ = shape(DMS, yr, ysize, c - yw / 2, 760, trk)
body += f'<path d="{"".join(d for _, d in p)}" fill="{INK}"/>'
body += f'<path d="M{c-60} 840H{c+52}M{c+20} 808L{c+56} 840L{c+20} 872" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
save("aufkleber.svg", svg(D, D, body))
print("ok", round(W), round(H))

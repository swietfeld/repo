# Baut die City.Team-Fassung der Pitch-Website.
# Aufruf aus dem Ordner weiterempfohlen-bielefeld: python3 website-cityteam/build.py [QR-Ziel-URL]
# Erzeugt website-cityteam/weiterempfohlen-cityteam.html (zum Veröffentlichen, Bilder unter img/)
# und website-cityteam/local.html (Vorschau, Bilder unter img-web/).
import re, sys, base64, os
import segno
from PIL import Image

D = 'website-cityteam/'
# Ziel des QR-Codes auf dem Sticker: die Beispiel-Porträtseite. Nach dem Hochladen der Seite die echte Adresse übergeben.
QR_URL = sys.argv[1] if len(sys.argv) > 1 else 'https://unikat.media/vorschau/weiterempfohlen-city-tea-a3afrhrc/#portraet'

# Bilder als WebP
os.makedirs(D + 'img-web', exist_ok=True)
for name, w, q in [('hero', 1920, 62), ('ort-baeckerei', 700, 78)]:
    im = Image.open(f'{D}img/{name}.jpg').convert('RGB')
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(f'{D}img-web/{name}.webp', 'WEBP', quality=q, method=6)

# Wortmarke aus dem Logo-Paket
wm = re.findall(r'd="([^"]*)"', open('marke/logos/wortmarke_dunkel.svg').read())

# QR-Code als ein Pfad
qr = segno.make(QR_URL, error='m')
m = [list(r) for r in qr.matrix]
n = len(m)

def qr_path(x, y, size):
    cell = size / n
    return ''.join(f'M{x + c * cell:.2f} {y + r * cell:.2f}h{cell:.2f}v{cell:.2f}h-{cell:.2f}z'
                   for r in range(n) for c in range(n) if m[r][c])

F = "font-family=\"'DM Sans',Arial,sans-serif\""
FM = "font-family=\"'Bricolage Grotesque','DM Sans',Arial,sans-serif\""
PINK, DEEP = '#CD017E', '#8A0052'
VARIANT = sys.argv[2] if len(sys.argv) > 2 else 'A'

def arc(pid, r=150):
    return f'<path id="t{pid}" d="M{200 - r} 200A{r} {r} 0 0 1 {200 + r} 200" fill="none"/>'

def sticker(pid, name, v=None):
    """Sticker-Varianten. A: Klar (pink, rund). B: Minimal (weiß, pinker Rand). C: Kachel (abgerundetes Quadrat). D: Wortmarke groß."""
    v = v or VARIANT
    nm = name.upper()
    if v == 'A':
        return ('<circle cx="200" cy="200" r="199" fill="#FFFFFF"/>'
                f'<circle cx="200" cy="200" r="186" fill="{PINK}"/>'
                f'<defs>{arc(pid)}</defs>'
                f'<text {F} font-weight="800" font-size="22" letter-spacing="5" fill="#FFFFFF"><textPath href="#t{pid}" startOffset="50%" text-anchor="middle">BIELEFELD EMPFIEHLT</textPath></text>'
                '<rect x="138" y="94" width="124" height="124" rx="18" fill="#FFFFFF"/>'
                f'<path d="{qr_path(148, 104, 104)}" fill="{DEEP}"/>'
                f'<text x="200" y="270" text-anchor="middle" {FM} font-weight="800" font-size="40" letter-spacing="-1.2" fill="#FFFFFF">Weiterempfohlen.</text>'
                f'<text x="200" y="304" text-anchor="middle" {F} font-weight="700" font-size="15" letter-spacing="2.6" fill="#FFFFFF" fill-opacity=".88">{nm}</text>')
    if v == 'B':
        return (f'<circle cx="200" cy="200" r="199" fill="{PINK}"/>'
                '<circle cx="200" cy="200" r="188" fill="#FFFFFF"/>'
                f'<defs>{arc(pid, 152)}</defs>'
                f'<text {F} font-weight="800" font-size="20" letter-spacing="5" fill="{PINK}"><textPath href="#t{pid}" startOffset="50%" text-anchor="middle">BIELEFELD EMPFIEHLT</textPath></text>'
                f'<path d="{qr_path(146, 96, 108)}" fill="{PINK}"/>'
                f'<text x="200" y="268" text-anchor="middle" {FM} font-weight="800" font-size="40" letter-spacing="-1.2" fill="#161214">Weiterempfohlen<tspan fill="{PINK}">.</tspan></text>'
                f'<text x="200" y="302" text-anchor="middle" {F} font-weight="700" font-size="14" letter-spacing="2.6" fill="#5B5157">{nm}</text>')
    if v == 'C':
        return ('<rect x="0" y="0" width="400" height="400" rx="78" fill="#FFFFFF"/>'
                f'<rect x="12" y="12" width="376" height="376" rx="68" fill="{PINK}"/>'
                f'<text x="200" y="96" text-anchor="middle" {FM} font-weight="800" font-size="40" letter-spacing="-1.2" fill="#FFFFFF">Weiterempfohlen.</text>'
                f'<text x="200" y="128" text-anchor="middle" {F} font-weight="700" font-size="15" letter-spacing="2.6" fill="#FFFFFF" fill-opacity=".9">{nm}</text>'
                '<rect x="44" y="152" width="312" height="204" rx="40" fill="#FFFFFF"/>'
                f'<path d="{qr_path(140, 168, 120)}" fill="{DEEP}"/>'
                f'<text x="200" y="336" text-anchor="middle" {F} font-weight="800" font-size="14" letter-spacing="4" fill="{PINK}">BIELEFELD EMPFIEHLT</text>')
    if v == 'E':  # Zweiton: oben Pink, unten Weiß
        return ('<circle cx="200" cy="200" r="199" fill="#FFFFFF"/>'
                f'<defs><clipPath id="c{pid}"><circle cx="200" cy="200" r="188"/></clipPath></defs>'
                f'<circle cx="200" cy="200" r="188" fill="#FFFFFF" stroke="{PINK}" stroke-width="3"/>'
                f'<rect x="0" y="0" width="400" height="196" fill="{PINK}" clip-path="url(#c{pid})"/>'
                f'<text x="200" y="104" text-anchor="middle" {F} font-weight="800" font-size="15" letter-spacing="4" fill="#FFFFFF" fill-opacity=".9">BIELEFELD EMPFIEHLT</text>'
                f'<text x="200" y="160" text-anchor="middle" {FM} font-weight="800" font-size="38" letter-spacing="-1.2" fill="#FFFFFF">Weiterempfohlen.</text>'
                f'<path d="{qr_path(150, 212, 100)}" fill="{DEEP}"/>'
                f'<text x="200" y="346" text-anchor="middle" {F} font-weight="700" font-size="13" letter-spacing="2.6" fill="{PINK}">{nm}</text>')
    if v == 'F':  # Stempel: pinker Ring, oben und unten Bogenschrift, weiße Mitte
        return ('<circle cx="200" cy="200" r="199" fill="#FFFFFF"/>'
                f'<circle cx="200" cy="200" r="188" fill="{PINK}"/>'
                '<circle cx="200" cy="200" r="134" fill="#FFFFFF"/>'
                f'<defs><path id="u{pid}" d="M46 200A154 154 0 0 1 354 200" fill="none"/><path id="d{pid}" d="M34 200A166 166 0 0 0 366 200" fill="none"/></defs>'
                f'<text {FM} font-weight="800" font-size="32" letter-spacing="1" fill="#FFFFFF"><textPath href="#u{pid}" startOffset="50%" text-anchor="middle">Weiterempfohlen.</textPath></text>'
                f'<text {F} font-weight="800" font-size="17" letter-spacing="4.5" fill="#FFFFFF"><textPath href="#d{pid}" startOffset="50%" text-anchor="middle">BIELEFELD EMPFIEHLT</textPath></text>'
                '<circle cx="54" cy="236" r="4" fill="#FFFFFF"/><circle cx="346" cy="236" r="4" fill="#FFFFFF"/>'
                f'<path d="{qr_path(146, 112, 108)}" fill="{DEEP}"/>'
                f'<text x="200" y="258" text-anchor="middle" {F} font-weight="800" font-size="13" letter-spacing="2.4" fill="{PINK}">{nm}</text>')
    # D: Wortmarke groß, QR klein
    return ('<circle cx="200" cy="200" r="199" fill="#FFFFFF"/>'
            f'<circle cx="200" cy="200" r="186" fill="{PINK}"/>'
            f'<text x="200" y="104" text-anchor="middle" {F} font-weight="800" font-size="15" letter-spacing="4" fill="#FFFFFF" fill-opacity=".9">BIELEFELD EMPFIEHLT</text>'
            f'<text x="200" y="166" text-anchor="middle" {FM} font-weight="800" font-size="62" letter-spacing="-2" fill="#FFFFFF">Weiter-</text>'
            f'<text x="200" y="222" text-anchor="middle" {FM} font-weight="800" font-size="62" letter-spacing="-2" fill="#FFFFFF">empfohlen.</text>'
            '<rect x="152" y="240" width="96" height="96" rx="14" fill="#FFFFFF"/>'
            f'<path d="{qr_path(160, 248, 80)}" fill="{DEEP}"/>'
            f'<text x="200" y="360" text-anchor="middle" {F} font-weight="700" font-size="12" letter-spacing="2.4" fill="#FFFFFF" fill-opacity=".9">{nm}</text>')

STICKERS = [('stk', 'Konditorei Knigge'), ('stk-mode', 'Sinn für Mode'), ('stk-pizza', "Nonna's Pizzeria"),
            ('stk-buch', 'Buchhandlung'), ('stk-wein', 'Weinhandlung'), ('stk-blumen', 'Blumenladen')]
symbols = ''.join(f'<symbol id="{pid}" viewBox="0 0 400 400">{sticker(pid.replace("-", ""), nm)}</symbol>' for pid, nm in STICKERS)
sticker_knigge = sticker('k', 'Konditorei Knigge')
variants = {v: sticker('v' + v, 'Konditorei Knigge', v) for v in 'ABEF'}

def b64(f): return base64.b64encode(open('website/fonts/' + f, 'rb').read()).decode()
head = ('<link rel="preload" as="image" href="img/hero.webp" fetchpriority="high">\n<style>'
        "@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:300 800;font-stretch:75% 100%;font-display:block;"
        f"src:url(data:font/woff2;base64,{b64('bricolage.woff2')}) format('woff2')}}"
        "@font-face{font-family:'DM Sans';font-style:normal;font-weight:400 800;font-display:block;"
        f"src:url(data:font/woff2;base64,{b64('dm-sans.woff2')}) format('woff2')}}"
        '</style>')

s = open(D + 'src.html').read()
s = s.replace('%%HEAD%%', head).replace('%%STICKERS%%', symbols).replace('%%WM_LETTERS%%', wm[0]).replace('%%WM_DOT%%', wm[1])
assert '%%' not in s and 'fonts.googleapis' not in s
open(D + 'weiterempfohlen-cityteam.html', 'w').write(s)
loc = s.replace('img/', 'img-web/')
open(D + 'local.html', 'w').write('<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + loc + '</body></html>')
# Paket für die Vorschau auf unikat.media (WordPress): index.html und img/ auf oberster Ebene
import shutil, zipfile
dist = D + 'dist/'
shutil.rmtree(dist, ignore_errors=True); os.makedirs(dist + 'img')
open(dist + 'index.html', 'w').write('<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + s + '</body></html>')
for f in os.listdir(D + 'img-web'): shutil.copy(D + 'img-web/' + f, dist + 'img/' + f)
with zipfile.ZipFile(D + 'Weiterempfohlen_CityTeam_Website.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(dist):
        for f in files: z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), dist))
# Sticker als eigene Datei (Schriften als Text, für Vorschau und Abstimmung)
open(D + 'sticker-knigge.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="1000" height="1000">' + sticker_knigge + '</svg>')
open(D + 'sticker-varianten.html', 'w').write('<!doctype html><html><head><meta charset="utf-8">' + head.replace('<link rel="preload" as="image" href="img/hero.webp" fetchpriority="high">', '') + '<style>body{margin:0;background:#F7F3F5;font-family:DM Sans,Arial,sans-serif}.g{display:grid;grid-template-columns:repeat(4,1fr);gap:40px;padding:48px}.g div{display:grid;gap:14px;justify-items:center}.g svg{width:100%;filter:drop-shadow(0 14px 22px rgba(120,0,70,.3))}.g b{font-size:22px}</style></head><body><div class="g">' + ''.join(f'<div><svg viewBox="0 0 400 400">{variants[v]}</svg><b>Variante {v}</b></div>' for v in 'ABEF') + '</div></body></html>')
print(len(s), 'Zeichen · QR-Ziel:', QR_URL, '· QR-Version', qr.version)

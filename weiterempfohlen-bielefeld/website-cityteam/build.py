# Baut die City.Team-Fassung der Pitch-Website.
# Aufruf aus dem Ordner weiterempfohlen-bielefeld: python3 website-cityteam/build.py [QR-Ziel-URL]
# Erzeugt website-cityteam/weiterempfohlen-cityteam.html (zum Veröffentlichen, Bilder unter img/)
# und website-cityteam/local.html (Vorschau, Bilder unter img-web/).
import re, sys, base64, os
import segno
from PIL import Image

D = 'website-cityteam/'
# Ziel des QR-Codes auf dem Sticker: die Beispiel-Porträtseite. Nach dem Hochladen der Seite die echte Adresse übergeben.
QR_URL = sys.argv[1] if len(sys.argv) > 1 else 'https://unikat.media/vorschau/bielefelder-konzept-jfyedk53/#portraet'

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

QRP = qr_path(146, 100, 108)
F = "font-family=\"'DM Sans',Arial,sans-serif\""
FM = "font-family=\"'Bricolage Grotesque','DM Sans',Arial,sans-serif\""

def sticker(pid, name):
    """Runder Aufkleber: weißer Stanzrand, Pink mit Verlauf und Glanz, Bogentext, QR-Feld, Wortmarke, Namensband."""
    nm = name.upper()
    fs = 16 if len(nm) <= 16 else 14
    return (
        f'<defs>'
        f'<radialGradient id="g{pid}" cx="34%" cy="28%" r="80%"><stop offset="0" stop-color="#F03A9E"/><stop offset=".55" stop-color="#CD017E"/><stop offset="1" stop-color="#94005B"/></radialGradient>'
        f'<linearGradient id="h{pid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".42"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
        f'<clipPath id="c{pid}"><circle cx="200" cy="200" r="186"/></clipPath>'
        f'<path id="t{pid}" d="M50 200A150 150 0 0 1 350 200"/>'
        f'</defs>'
        '<circle cx="200" cy="200" r="199" fill="#FFFFFF"/>'
        '<circle cx="200" cy="200" r="198.5" fill="none" stroke="#1A0010" stroke-opacity=".10"/>'
        f'<circle cx="200" cy="200" r="186" fill="url(#g{pid})"/>'
        '<circle cx="200" cy="200" r="174" fill="none" stroke="#FFFFFF" stroke-opacity=".6" stroke-width="2.2" stroke-dasharray="1 7" stroke-linecap="round"/>'
        f'<text {F} font-weight="800" font-size="24" letter-spacing="5" fill="#FFFFFF"><textPath href="#t{pid}" startOffset="50%" text-anchor="middle">BIELEFELD EMPFIEHLT</textPath></text>'
        '<circle cx="66" cy="200" r="4" fill="#FFFFFF" fill-opacity=".85"/><circle cx="334" cy="200" r="4" fill="#FFFFFF" fill-opacity=".85"/>'
        '<rect x="136" y="90" width="128" height="128" rx="20" fill="#FFFFFF"/>'
        f'<path d="{QRP}" fill="#8A0052"/>'
        f'<text x="200" y="266" text-anchor="middle" {FM} font-weight="800" font-size="40" letter-spacing="-1.2" fill="#FFFFFF">Weiterempfohlen<tspan fill="#FFC6E5">.</tspan></text>'
        '<path d="M72 300L92 292L92 330L72 322L80 311Z" fill="#7A0049"/><path d="M328 300L308 292L308 330L328 322L320 311Z" fill="#7A0049"/>'
        '<path d="M86 288H314L322 311L314 334H86L78 311Z" fill="#FFFFFF"/>'
        f'<text x="200" y="{317 if fs == 16 else 316}" text-anchor="middle" {F} font-weight="800" font-size="{fs}" letter-spacing="2.4" fill="#B0006C">{nm}</text>'
        f'<text x="200" y="358" text-anchor="middle" {F} font-weight="700" font-size="10.5" letter-spacing="3.2" fill="#FFFFFF" fill-opacity=".85">CITY.TEAM BIELEFELD</text>'
        f'<g clip-path="url(#c{pid})"><ellipse cx="130" cy="96" rx="190" ry="96" transform="rotate(-28 130 96)" fill="url(#h{pid})"/></g>'
    )

STICKERS = [('stk', 'Konditorei Knigge'), ('stk-mode', 'Sinn für Mode'), ('stk-pizza', "Nonna's Pizzeria"),
            ('stk-buch', 'Buchhandlung'), ('stk-wein', 'Weinhandlung'), ('stk-blumen', 'Blumenladen')]
symbols = ''.join(f'<symbol id="{pid}" viewBox="0 0 400 400">{sticker(pid.replace("-", ""), nm)}</symbol>' for pid, nm in STICKERS)
sticker_knigge = sticker('k', 'Konditorei Knigge')

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
print(len(s), 'Zeichen · QR-Ziel:', QR_URL, '· QR-Version', qr.version)

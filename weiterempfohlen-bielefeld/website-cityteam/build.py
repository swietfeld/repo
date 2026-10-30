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

# QR-Code als ein Pfad, in einem weißen Feld mitten im Sticker
qr = segno.make(QR_URL, error='m')
m = [list(r) for r in qr.matrix]
n = len(m)
box, pad = 144, 10
cell = (box - 2 * pad) / n
x0, y0 = 128 + pad, 112 + pad
d = ''.join(f'M{x0 + c * cell:.2f} {y0 + r * cell:.2f}h{cell:.2f}v{cell:.2f}h-{cell:.2f}z'
            for r in range(n) for c in range(n) if m[r][c])
sticker = (
    '<circle cx="200" cy="200" r="200" fill="#CD017E"/>'
    '<circle cx="200" cy="200" r="186" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
    '<path id="stkTop" d="M56 200A144 144 0 0 1 344 200" fill="none"/>'
    '<path id="stkBot" d="M46 200A154 154 0 0 0 354 200" fill="none"/>'
    '<text font-family="\'DM Sans\',Arial,sans-serif" font-weight="800" font-size="27" letter-spacing="4" fill="#FFFFFF">'
    '<textPath href="#stkTop" startOffset="50%" text-anchor="middle">BIELEFELD EMPFIEHLT</textPath></text>'
    '<text font-family="\'DM Sans\',Arial,sans-serif" font-weight="700" font-size="17" letter-spacing="3" fill="#FFFFFF">'
    '<textPath href="#stkBot" startOffset="50%" text-anchor="middle">KONDITOREI KNIGGE</textPath></text>'
    f'<rect x="128" y="112" width="{box}" height="{box}" rx="14" fill="#FFFFFF"/>'
    f'<path d="{d}" fill="#7A0049"/>'
    '<text x="200" y="304" text-anchor="middle" font-family="\'Bricolage Grotesque\',\'DM Sans\',Arial,sans-serif" font-weight="800" font-size="38" letter-spacing="-1" fill="#FFFFFF">Weiterempfohlen.</text>'
)

def b64(f): return base64.b64encode(open('website/fonts/' + f, 'rb').read()).decode()
head = ('<link rel="preload" as="image" href="img/hero.webp" fetchpriority="high">\n<style>'
        "@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:300 800;font-stretch:75% 100%;font-display:block;"
        f"src:url(data:font/woff2;base64,{b64('bricolage.woff2')}) format('woff2')}}"
        "@font-face{font-family:'DM Sans';font-style:normal;font-weight:400 800;font-display:block;"
        f"src:url(data:font/woff2;base64,{b64('dm-sans.woff2')}) format('woff2')}}"
        '</style>')

s = open(D + 'src.html').read()
s = s.replace('%%HEAD%%', head).replace('%%STICKER%%', sticker).replace('%%WM_LETTERS%%', wm[0]).replace('%%WM_DOT%%', wm[1])
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
open(D + 'sticker-knigge.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="1000" height="1000">' + sticker + '</svg>')
print(len(s), 'Zeichen · QR-Ziel:', QR_URL, '· QR-Version', qr.version)

# Baut website/weiterempfohlen.html (zum Veröffentlichen) und website/local.html (Vorschau) aus website/src.html.
# Aufruf aus dem Ordner weiterempfohlen-bielefeld: python3 website/build.py
import re, base64
L='marke/logos/'
def ds(f): return re.findall(r'd="([^"]*)"', open(L+f).read())
wm=ds('wortmarke_dunkel.svg'); km=ds('logo_kombi_dunkel.svg')
st=open(L+'aufkleber.svg').read()
st_inner=re.search(r'<svg[^>]*>(.*)</svg>', st, re.S).group(1)
def b64(f): return base64.b64encode(open('website/fonts/'+f,'rb').read()).decode()
# Hero-Foto früh anfordern, Schriften direkt in der Seite, damit nichts nachlädt
head=('<link rel="preload" as="image" href="img/hero.webp" media="(min-width: 901px)" fetchpriority="high">\n'
      '<link rel="preload" as="image" href="img/hero-m.webp" media="(max-width: 900px)" fetchpriority="high">\n'
      '<style>'
      "@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:300 800;font-stretch:75% 100%;font-display:block;"
      f"src:url(data:font/woff2;base64,{b64('bricolage.woff2')}) format('woff2')}}"
      "@font-face{font-family:'DM Sans';font-style:normal;font-weight:400 700;font-display:block;"
      f"src:url(data:font/woff2;base64,{b64('dm-sans.woff2')}) format('woff2')}}"
      '</style>')
s=open('website/src.html').read()
s=s.replace('%%HEADPERF%%',head)
s=s.replace('%%WM_LETTERS%%',wm[0]).replace('%%WM_DOT%%',wm[1])
s=s.replace('%%KOMBI_ARROW%%',km[0]).replace('%%KOMBI_LETTERS%%',km[1]).replace('%%KOMBI_DOT%%',km[2])
s=s.replace('%%STICKER%%',st_inner)
assert '%%' not in s and 'fonts.googleapis' not in s
open('website/weiterempfohlen.html','w').write(s)
# lokale Vorschau, nutzt die WebP-Dateien aus website/img-web
loc=s.replace('img/','img-web/')
open('website/local.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+loc.split('<svg width="0"')[0]+'</head><body><svg width="0"'+loc.split('<svg width="0"',1)[1]+'</body></html>')
print(len(s))

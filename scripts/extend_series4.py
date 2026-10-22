"""Gezielte, wiederholbare Ergänzung; niemals den veralteten Gesamtgenerator starten."""
from pathlib import Path
import hashlib, html, json, re, sys, unicodedata
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools/python'))
import qrcode
from breeds_series4 import SERIES4

BASE = 'https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
REQUESTED = 'Altsteirer|Andalusier|Appenzeller Barthühner|Appenzeller Spitzhauben|Bergische Kräher|Bergische Schlotterkämme|Brabanter|Brakel|Breda|Dorking|Friesenhühner|Holländer Haubenhühner|Houdan|Kastilianer|Kraienköppe|La Flèche|Minorka|Nackthalshühner|Paduaner|Penedesenca|Bantam|Deutsche Zwerg-Lachshühner|Federfüßige Zwerghühner|Holländische Zwerghühner|Ko Shamo|Ohiki|Serama|Tuzo|Zwerg-Brakel|Zwerg-Kraienköppe'.split('|')

def normalized(name):
    name = name.casefold().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    name = ''.join(c for c in unicodedata.normalize('NFKD', name) if not unicodedata.combining(c))
    return re.sub('[^a-z0-9]', '', name)

def sortkey(name):
    return ''.join(c for c in unicodedata.normalize('NFKD', name.casefold()) if not unicodedata.combining(c))

def cards(text):
    return re.findall(r'<article class="card">.*?</article>', text, re.S)

def name(card):
    return html.unescape(re.search(r'<h3>(.*?)</h3>', card).group(1))

def render(b, template):
    e = html.escape
    facts = [('Herkunft',b['origin']),('Tiergruppe',b['group']),('Gewicht Hahn',b['weights'][0]),('Gewicht Henne',b['weights'][1]),('Jährliche Legeleistung',b['laying']),('Eiergewicht und Schalenfarbe',b['egg'])]
    content = '<a class="back" href="index.html">← Zurück zum Rasselexikon</a><section class="info"><h2>Auf einen Blick</h2><div class="facts">'
    content += ''.join(f'<div class="fact"><strong>{k}</strong>{e(v)}</div>' for k,v in facts)
    content += '</div><p>Gewichte sind Zuchtrichtwerte beziehungsweise ausdrücklich bezeichnete Orientierungswerte. Bruteier-Mindestgewichte sind keine durchschnittlichen Eigewichte. Jahreslegezahlen hängen von Linie, Alter und Haltung ab; ältere Rassetafeln liefern keine aktuelle Leistungsmessung.</p></section>'
    for key, title in [('history','Herkunft und historische Entwicklung'),('appearance','Körperbau und Rassemerkmale'),('colors','Farbenschläge und Belegstand'),('nature','Charakter und Verhalten'),('husbandry','Haltung und Besonderheiten'),('use','Nutzung und Zuchtzweck'),('fact','Schon gewusst?')]:
        content += f'<section class="info"><h2>{title}</h2><p>{e(b[key])}</p></section>'
    content += '<section class="info sources"><h2>Quellen und Weiterlesen</h2><p>Eigenständig formuliertes Rasseporträt. Recherchestand: 22. Oktober 2026. Historische Standardfassungen und belegte Farbbeispiele sind im Text als solche gekennzeichnet.</p><ul>'
    content += ''.join(f'<li><a href="{e(url)}">{e(label)}</a></li>' for label,url in b['sources'])
    content += '</ul></section><a class="back" href="index.html">← Alle Rassen entdecken</a>'
    result = re.sub(r'<title>.*?</title>',f'<title>{e(b["name"])} | Rasselexikon RGZV Hagen</title>',template)
    result = re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{e(b["short"])}">',result)
    result = re.sub(r'<h1>.*?</h1><p>.*?</p>',f'<h1>{e(b["name"])}</h1><p>{e(b["short"])}</p>',result)
    return re.sub(r'(<main id="inhalt">).*?(</main>)',lambda m:m[1]+content+m[2],result,flags=re.S)

def main():
    index = (ROOT/'lexikon.html').read_text(encoding='utf-8')
    existing = cards(index)
    names = [normalized(name(c)) for c in existing]
    assert len(set(names)) == len(names), 'Doppelte vorhandene Namen'
    urls = [re.search(r'href="([^"]+)"',c).group(1) for c in existing]
    assert len(set(urls)) == len(urls), 'Doppelte vorhandene URLs'
    template = (ROOT/'bantam.html').read_text(encoding='utf-8')
    before = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.glob('*.html') if p.name not in {'index.html','lexikon.html'} and p.stem not in {b['slug'] for b in SERIES4}}
    finderpath=ROOT/'assets/finder-data.js'
    findertext=finderpath.read_text(encoding='utf-8')
    finder=json.loads(findertext.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    additions=[]
    for b in SERIES4:
        target=ROOT/(b['slug']+'.html')
        rendered=render(b,template)
        if target.exists():
            assert target.read_text(encoding='utf-8')==rendered, f'Vorhandene Seite wird nicht überschrieben: {target}'
        else:
            assert normalized(b['name']) not in names, b['name']
            additions.append(b['name'])
            assert not (ROOT/'qr-codes'/f'{b["slug"]}.png').exists()
            target.write_text(rendered,encoding='utf-8')
        if normalized(b['name']) not in names:
            card=f'<article class="card"><span class="badge">Zwerghuhn</span><h3>{html.escape(b["name"])}</h3><p>{html.escape(b["short"])}</p><a class="button" href="{b["slug"]}.html" aria-label="{html.escape(b["name"])}: Rasse entdecken">Rasse entdecken</a></article>'
            pattern=r'(<section id="zwerghuehner"><h2>Zwerghühner</h2><div class="cards">)(.*?)(</div></section>)'
            index,n=re.subn(pattern,lambda m:m[1]+m[2]+card+m[3],index,flags=re.S)
            assert n==1
        if b['slug']+'.html' not in {r['url'] for r in finder}:
            finder.append(dict(name=b['name'],description=b['short'],url=b['slug']+'.html',group=b['group'],traits={'space':None},specialist=False))
        qrpath=ROOT/'qr-codes'/f'{b["slug"]}.png'
        if not qrpath.exists():
            qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=12,border=4)
            qr.add_data(BASE+b['slug']+'.html');qr.make(fit=True)
            qr.make_image(fill_color='black',back_color='white').save(qrpath)
    # Keep each card byte-for-byte, changing only its order within its existing group.
    index=re.sub(r'(<div class="cards">)(.*?)(</div>)',lambda m:m[1]+''.join(sorted(cards(m[2]),key=lambda c:sortkey(name(c))))+m[3],index,flags=re.S)
    index=re.sub(r'(<span id="rassen-gesamt"[^>]*>).*?(</span>)',r'\1…\2',index)
    for card in cards(index):
        url=re.search(r'href="([^"]+)"',card)[1]
        if url not in {r['url'] for r in finder}:
            finder.append(dict(name=name(card),description=html.unescape(re.search(r'<p>(.*?)</p>',card)[1]),url=url,group=html.unescape(re.search(r'<span class="badge">(.*?)</span>',card)[1]),traits={'space':None},specialist=False))
    (ROOT/'lexikon.html').write_text(index,encoding='utf-8')
    finderpath.write_text(findertext.split('window.FINDER_BREEDS = ',1)[0]+'window.FINDER_BREEDS = '+json.dumps(finder,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    for filename,digest in before.items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest,filename
    reportpath=ROOT/'scripts/series4-inventory.json'
    if not reportpath.exists():
        report=dict(before=len(existing),after=len(cards(index)),added=additions,already_present=[n for n in REQUESTED if n not in additions],preserved_pages=before,qr_urls={b['slug']:BASE+b['slug']+'.html' for b in SERIES4},note='Tuzo bleibt gemäß BDRG als Großhuhn eingeordnet. Ko Gunkei = Ko Shamo; Twentse Krielen = Zwerg-Kraienköppe.')
        reportpath.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(additions)} ergänzt; {len(cards(index))} Rassen insgesamt.')

if __name__=='__main__':
    main()

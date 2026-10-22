"""Prüft den zentralen Katalog gegen alle tatsächlichen Rassedateien (nur Standardbibliothek)."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {'Großhuhn', 'Zwerghuhn', 'Taube', 'Wachtel', 'Gans', 'Ente'}

def name_key(value):
    value=value.strip().casefold().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('œ','oe').replace('æ','ae')
    value=''.join(c for c in unicodedata.normalize('NFKD',value) if not unicodedata.combining(c))
    key=re.sub('[^a-z0-9]', '', value)
    aliases={'kogunkei':'koshamo','twentsekrielen':'zwergkraienkoeppe',
        'malayen':'malaien','modernesenglischeskaempferhuhn':'moderneenglischekaempfer',
        'zwergbielefelderkennhuehner':'bielefelderzwergkennhuehner',
        'deutschezwergsperber':'zwergdeutschesperber',
        'hollaendischeweisshauben':'hollaenderhaubenhuehner',
        'faverollesfranzoesischertyp':'faverolles','franzoesischefaverolles':'faverolles',
        'katalanier':'prat','araucanas':'araucana','zwergaraucanas':'zwergaraucana',
        'croadlangshan':'croadlangschan','deutschelangshan':'deutschelangschan',
        'zwergcroadlangshan':'zwergcroadlangschan','plymouthrock':'plymouthrocks',
        'jerseygiant':'jerseygiants','dominique':'dominikaner','cornish':'indischekaempfer'}
    return aliases.get(key,key)

class BreedPage(HTMLParser):
    def __init__(self):
        super().__init__(); self.h1=[]; self.in_h1=False; self.fact=False
        self.strong=False; self.label=''; self.group=''
    def handle_starttag(self, tag, attrs):
        if tag=='h1': self.in_h1=True
        if tag=='div' and 'fact' in dict(attrs).get('class','').split(): self.fact=True; self.label=''
        if tag=='strong' and self.fact: self.strong=True
    def handle_endtag(self, tag):
        if tag=='h1': self.in_h1=False
        if tag=='strong': self.strong=False
        if tag=='div': self.fact=False
    def handle_data(self, data):
        if self.in_h1: self.h1.append(data)
        if self.strong: self.label+=data
        elif self.fact and self.label.strip() in {'Tiergruppe','Rassegruppe'}: self.group+=data.strip()

def check(root=ROOT):
    raw=(root/'assets/finder-data.js').read_text(encoding='utf-8')
    entries=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    files={}
    for path in root.glob('*.html'):
        page=BreedPage();page.feed(path.read_text(encoding='utf-8'))
        group={'Großhühner':'Großhuhn'}.get(page.group,page.group)
        if group in GROUPS:
            files[path.name]=(''.join(page.h1).strip(),group)
    decorations=[b for b in entries if b.get('group')=='Dekorationshuhn']
    entries=[b for b in entries if b.get('group')!='Dekorationshuhn']
    for b in decorations:
        page=BreedPage();page.feed((root/b['url']).read_text(encoding='utf-8'))
        assert page.group=='Dekorationshuhn',b['url']
    urls=set(); names=set()
    for b in entries:
        assert isinstance(b,dict), 'Ungültiger Datensatz'
        assert isinstance(b.get('url'),str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*\.html',b['url']),b
        assert isinstance(b.get('name'),str) and name_key(b['name']),b
        assert isinstance(b.get('description'),str) and b['description'].strip(),b
        assert b.get('group') in GROUPS,b
        assert b['url'] not in urls, f'Doppelte URL: {b["url"]}'
        assert name_key(b['name']) not in names, f'Doppelter Name: {b["name"]}'
        urls.add(b['url']); names.add(name_key(b['name']))
        assert b['url'] in files, f'Keine gültige Rassedatei: {b["url"]}'
        title,group=files[b['url']]
        assert name_key(title)==name_key(b['name']) and group==b['group'],b['url']
    assert urls==set(files), f'Katalog und Dateien weichen ab: {urls.symmetric_difference(files)}'
    index=(root/'index.html').read_text(encoding='utf-8')
    lexikon=(root/'lexikon.html').read_text(encoding='utf-8')
    assert '<article class="card">' not in index and 'assets/lexikon-suche.js' not in index,'Rassenliste auf Startseite'
    assert 'href="lexikon.html"' in index,'Lexikonlink fehlt'
    cards=re.findall(r'<article class="card">.*?</article>',lexikon,re.S)
    targets=[re.search(r'href="([^"]+)"',c)[1] for c in cards if re.search(r'<span class="badge">(.*?)</span>',c)[1] in GROUPS]
    assert len(targets)==len(set(targets)) and set(targets)==urls,'Navigation und Katalog weichen ab'
    assert not re.search(r'id="rassen-gesamt"[^>]*>\s*\d+',index),'Fest hinterlegte Rasseanzahl'
    assert index.index('assets/finder-data.js')<index.index('assets/rassen-bestand.js')<index.index('assets/rassen-gesamt.js')
    audit=json.loads((root/'scripts/series4-inventory.json').read_text(encoding='utf-8'))
    requested=audit['added']+audit['already_present']
    assert len(requested)==30 and all(name_key(n) in names for n in requested), 'Eine beauftragte Rasse fehlt'
    print(f'{len(files)} gültige, einzigartige Rassedateien; Katalog und Navigation vollständig; alle {len(requested)} angefragten Rassen vorhanden.')
    return len(files)

if __name__=='__main__': check()

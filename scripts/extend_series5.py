"""50 tatsächlich fehlende BDRG-Rassen integrieren; bestehende Seiten nie überschreiben."""
from pathlib import Path
import sys,json,re,html,unicodedata,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
import qrcode
from series5_texts import TEXTS
from check_catalog import name_key,GROUPS
BASE='https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
REGISTRY='https://www.bdrg.de/media/user_upload/Rassenverzeichnis_BDRG_2024.pdf'
TABLES={'bdrg-huehner':'https://www.bdrg.de/media/docs/Rassetafeln_Huehner.pdf','bdrg-zwerghuehner':'https://www.bdrg.de/media/docs/zwerghuehner_2011_A6.pdf'}
REQUESTED='Asil|Augsburger|Brabanter Bauernhühner|Buckeye|Campiner|Cubalaya|Denizli-Kräher|Dominikaner|Faverolles (französischer Typ)|Holländische Weißhauben|Indische Kämpfer|Jersey Giants|Jurlower Kräher|Kaulhühner|Langschan|Lütticher Kämpfer|Malayen|Marans|Modernes Englisches Kämpferhuhn|Niederrheiner|Ostfriesische Möwen|Plymouth Rocks|Polnische Grünleger|Redcaps|Shamo|Spanier|Sulmtaler|Sumatra|Thüringer Barthühner|Yokohama|Amerikanische Zwerg-Leghorn|Zwerg-Amrocks|Zwerg-Altsteirer|Zwerg-Andalusier|Zwerg-Araucana|Zwerg-Barnevelder|Zwerg-Bielefelder Kennhühner|Zwerg-Brahma|Zwerg-Deutsche Sperber|Zwerg-Dorking|Zwerg-Hamburger|Zwerg-Italiener|Zwerg-Lakenfelder|Zwerg-Langschan|Zwerg-Minorka|Zwerg-New Hampshire|Zwerg-Paduaner|Zwerg-Plymouth Rocks|Zwerg-Rheinländer|Zwerg-Vorwerkhühner'.split('|')
ALIASES={'Faverolles (französischer Typ)':'Faverolles','Holländische Weißhauben':'Holländer Haubenhühner','Malayen':'Malaien','Modernes Englisches Kämpferhuhn':'Moderne Englische Kämpfer','Zwerg-Bielefelder Kennhühner':'Bielefelder Zwerg-Kennhühner','Zwerg-Langschan':'Deutsche Zwerg-Langschan','Zwerg-Plymouth Rocks':'Zwerg-Plymouth-Rocks'}
UNVERIFIED={'Buckeye','Campiner','Jurlower Kräher','Polnische Grünleger'}

def load():
    rows=json.loads((ROOT/'scripts/breeds_series5.json').read_text(encoding='utf-8'))
    assert len(rows)==len(TEXTS)==50
    return [{**b,**TEXTS[b['name']]} for b in rows]

def sortkey(text):return ''.join(c for c in unicodedata.normalize('NFKD',text.casefold()) if not unicodedata.combining(c))
def card_name(card):return html.unescape(re.search(r'<h3>(.*?)</h3>',card)[1])
def cards(text):return re.findall(r'<article class="card">.*?</article>',text,re.S)
def hashes(paths):return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}

def render(b,template):
    e=html.escape
    egg_label='Bruteier-Mindestgewicht' if b['name'] in {'Deutsche Zwerg-Langschan','Zwerg-Paduaner','Zwerg-Holländer-Haubenhühner','Zwerg-Dorking','Zwerg-Augsburger'} else 'Eiergewicht laut Rassetafel'
    facts=[('Herkunft der Rasse beziehungsweise Zwergzucht',b['origin']),('Tiergruppe',b['group'])]
    if b['period']:facts.append(('Belegte zeitliche Einordnung',b['period']))
    facts += [('Gewicht Hahn',b['weights'][0]),('Gewicht Henne',b['weights'][1]),('Jährliche Legeleistung (Richtwert)',str(b['laying'])+' Eier'),(egg_label,str(b['egg_g'])+' g'),('Eierschalenfarbe',b['shell'])]
    content='<a class="back" href="index.html">← Zurück zum Rasselexikon</a><section class="info"><h2>Auf einen Blick</h2><div class="facts">'
    content+=''.join(f'<div class="fact"><strong>{e(k)}</strong>{e(v)}</div>' for k,v in facts)
    content+='</div><p>Die BDRG-Rassetafeln sind ältere Orientierungsquellen (Zwerghühner: Ausgabe 2011), keine aktuellen Leistungsmessungen. Neuere, ausdrücklich zugeordnete Sondervereinsangaben haben Vorrang. Jahreslegezahlen sind keine Garantie. Das Eiergewicht der Tafel wird nicht als gemessener Durchschnitt ausgegeben; ein Mindestbruteigewicht ist nur bei entsprechendem Quellenbeleg so bezeichnet.</p></section>'
    for key,title in [('history','Herkunft und Entwicklung'),('appearance','Rassemerkmale und Körperbau'),('nature','Charakter und Verhalten'),('husbandry','Haltung, Bewegung und Gefiederpflege'),('use','Verwendungszweck und züchterische Bedeutung')]:
        content+=f'<section class="info"><h2>{title}</h2><p>{e(b[key])}</p></section>'
    content+=f'<section class="info"><h2>Anerkannte Farbenschläge</h2><p>{e(b["colors"])}</p><p>Belegstand: BDRG-Verzeichnis 2024. Als Beispiele bezeichnete Angaben sind keine vollständige Farbliste; die verlinkte Standardquelle ist für weitere Farben maßgeblich.</p></section>'
    sources=[('BDRG: Anerkennung und Farbenschläge, PDF-Seite '+str(b['registry_page']),REGISTRY+'#page='+str(b['registry_page'])),('BDRG: Rassetafel, PDF-Seite '+str(b['table_page']),TABLES[b['table_file']]+'#page='+str(b['table_page']))]+b['extra_sources']
    content+='<section class="info sources"><h2>Quellen und Einordnung</h2><p>Recherchestand: 22. Oktober 2026. Eigenständig formuliertes Rasseporträt. Haltungshinweise sind praktische Ableitungen aus Körperbau und Gefieder; nicht belegte Quadratmeterzahlen, Flugweiten und individuelle Verhaltensgarantien werden nicht ergänzt.</p><ul>'
    content+=''.join(f'<li><a href="{e(url)}">{e(label)}</a></li>' for label,url in sources)
    content+='</ul></section><section class="info"><h2>Rasseschild drucken</h2><div class="downloads">'
    content+=f'<a class="button" href="output/pdf/a7/{b["slug"]}.pdf" download>A7-Rasseschild herunterladen</a><a href="schilder-drucken.html">Mehrere Schilder auswählen</a></div></section><a class="back" href="index.html">← Alle Rassen entdecken</a>'
    out=re.sub(r'<title>.*?</title>',f'<title>{e(b["name"])} | Rasselexikon RGZV Hagen</title>',template)
    out=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{e(b["short"])}">',out)
    out=re.sub(r'<h1>.*?</h1><p>.*?</p>',f'<h1>{e(b["name"])}</h1><p>{e(b["short"])}</p>',out)
    return re.sub(r'(<main id="inhalt">).*?(</main>)',lambda m:m[1]+content+m[2],out,flags=re.S)

def main():
    refresh='--refresh-new' in sys.argv
    rows=load();slugs={b['slug'] for b in rows};assert len(slugs)==50
    indexpath=ROOT/'index.html';index=indexpath.read_text(encoding='utf-8');original_cards=cards(index)
    finderpath=ROOT/'assets/finder-data.js';raw=finderpath.read_text(encoding='utf-8');prefix=raw.split('window.FINDER_BREEDS = ',1)[0]
    finder=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    oldnames={name_key(b['name']):b for b in finder};newnames={name_key(b['name']) for b in rows};assert len(newnames)==50
    reportpath=ROOT/'scripts/series5-audit.json'
    if reportpath.exists():
        audit=json.loads(reportpath.read_text(encoding='utf-8'))
    else:
        assert not newnames.intersection(oldnames),'Geplante Rasse bereits vorhanden'
        before=len([b for b in finder if b['group'] in GROUPS])
        snapshot=hashes(list(ROOT.glob('*.html'))+list((ROOT/'qr-codes').glob('*.png'))+list((ROOT/'schilder').glob('*.pdf'))+list((ROOT/'output/pdf/a7').glob('*.pdf')))
        requests=[];direct=set()
        for n in REQUESTED:
            canonical=ALIASES.get(n,n);key=name_key(canonical)
            if n in UNVERIFIED:status='Kein eindeutiger eigenständiger BDRG-Nachweis im ausgewerteten Verzeichnis; ersetzt'
            elif n=='Langschan':status='Unpräzise Sammelbezeichnung; Deutsche Langschan und Croad-Langschan bereits vorhanden; ersetzt'
            elif key in oldnames:status='Bereits vorhanden; ersetzt'
            else:
                assert key in newnames,n
                status='Neu aufgenommen';direct.add(canonical)
            requests.append(dict(requested=n,canonical=canonical,status=status))
        replacements=[b['name'] for b in rows if b['name'] not in direct]
        needs=[r for r in requests if r['status']!='Neu aufgenommen'];assert len(needs)==len(replacements)
        for request,replacement in zip(needs,replacements):request['replacement']=replacement
        audit=dict(before=before,added=50,after=before+50,requested=requests,new_names=[b['name'] for b in rows],directly_requested=sorted(direct),replacements=replacements,preserved_files=snapshot,original_cards=original_cards,approval='Nur BDRG-Rassen; 50 neue Einträge dürfen überwiegend Zwerghühner sein.')
    template=(ROOT/'bantam.html').read_text(encoding='utf-8')
    rendered={b['slug']:render(b,template) for b in rows}
    # Vollständige Prüfung vor der ersten Seitenmutation.
    for b in rows:
        path=ROOT/(b['slug']+'.html')
        if path.exists():
            if path.read_text(encoding='utf-8')!=rendered[b['slug']]:
                assert refresh and audit.get('new_page_hashes',{}).get(path.name)==hashlib.sha256(path.read_bytes()).hexdigest(),path
        else:assert name_key(b['name']) not in oldnames,b['name']
    for b in rows:
        path=ROOT/(b['slug']+'.html')
        if not path.exists() or refresh:path.write_text(rendered[b['slug']],encoding='utf-8')
        target=b['slug']+'.html'
        if target not in {x['url'] for x in finder}:
            # Ohne belegte Verhaltensmerkmale bleibt die Finderbewertung neutral.
            finder.append(dict(name=b['name'],description=b['short'],url=target,group=b['group'],traits={'space':None},specialist=False))
            group='huehner' if b['group']=='Großhuhn' else 'zwerghuehner'
            card=f'<article class="card"><span class="badge">{b["group"]}</span><h3>{html.escape(b["name"])}</h3><p>{html.escape(b["short"])}</p><a class="button" href="{target}" aria-label="{html.escape(b["name"])}: Rasse entdecken">Rasse entdecken</a></article>'
            pattern=r'(<section id="'+group+r'"><h2>.*?</h2><div class="cards">)(.*?)(</div></section>)'
            index,n=re.subn(pattern,lambda m:m[1]+m[2]+card+m[3],index,flags=re.S);assert n==1
        qrpath=ROOT/'qr-codes'/(b['slug']+'.png')
        if not qrpath.exists():
            qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=12,border=4);qr.add_data(BASE+target);qr.make(fit=True)
            qr.make_image(fill_color='black',back_color='white').save(qrpath)
    index=re.sub(r'(<div class="cards">)(.*?)(</div>)',lambda m:m[1]+''.join(sorted(cards(m[2]),key=lambda c:sortkey(card_name(c))))+m[3],index,flags=re.S)
    indexpath.write_text(index,encoding='utf-8');finderpath.write_text(prefix+'window.FINDER_BREEDS = '+json.dumps(finder,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    for file,digest in audit['preserved_files'].items():
        if file=='index.html':continue
        assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==digest,file
    audit['new_page_hashes']={b['slug']+'.html':hashlib.sha256((ROOT/(b['slug']+'.html')).read_bytes()).hexdigest() for b in rows}
    reportpath.write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{audit["before"]} + {audit["added"]} = {audit["after"]} gültige Rassen; 50 Seiten und QR-Codes integriert.')
if __name__=='__main__':main()

"""Belegte Leistungsdaten ergänzen; vorhandene Besuchertexte bleiben erhalten.

Die beiden Original-PDFs vorher nach tmp/pdfs/bdrg-{huehner,zwerghuehner}.pdf laden.
"""
from pathlib import Path
import sys,re,json,html,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from pypdf import PdfReader
PAGES={'Altsteirer':2,'Andalusier':4,'Appenzeller Barthühner':6,'Appenzeller Spitzhauben':7,'Bergische Kräher':13,'Bergische Schlotterkämme':14,'Brabanter':16,'Brakel':19,'Breda':20,'Dorking':34,'Friesenhühner':38,'Holländer Haubenhühner':40,'Houdan':41,'Kastilianer':45,'Kraienköppe':48,'La Flèche':50,'Minorka':58,'Nackthalshühner':60,'Paduaner':68,'Penedesenca':69,'Tuzo':93}
DWARFS={'Bantam':11,'Deutsche Zwerg-Lachshühner':27,'Federfüßige Zwerghühner':35,'Holländische Zwerghühner':41}

def main():
    raw=(ROOT/'assets/finder-data.js').read_text(encoding='utf-8')
    breeds={b['name']:b for b in json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))}
    records=[]
    for file,mapping,url in [('huehner',PAGES,'https://www.bdrg.de/media/docs/Rassetafeln_Huehner.pdf'),('zwerghuehner',DWARFS,'https://www.bdrg.de/media/docs/zwerghuehner_2011_A6.pdf')]:
        reader=PdfReader(ROOT/'tmp/pdfs'/f'bdrg-{file}.pdf')
        for name,page in mapping.items():
            text=reader.pages[page-1].extract_text()
            weight=re.search(r'Hahn\s+([^\n]+)\s+Henne\s+([^\n]+)',text)
            laying=re.search(r'Legeleistung:\s*(\d+)\s*Eier',text)
            color=re.search(r'Eierschalenfarbe:\s*(.*?)\s*Eiergewicht:',text,re.S)
            egg=re.search(r'Eiergewicht:\s*(\d+)\s*Gramm',text)
            assert all([weight,laying,color,egg]),name
            facts=[('Gewicht Hahn',weight[1].strip().rstrip('.')),('Gewicht Henne',weight[2].strip().rstrip('.')),('Jährliche Legeleistung (Richtwert)',laying[1]+' Eier'),('Eierschalenfarbe',' '.join(color[1].split()).rstrip('.')),('Eiergewicht laut Rassetafel',egg[1]+' g')]
            path=ROOT/breeds[name]['url'];original=path.read_text(encoding='utf-8')
            original=re.sub(r'<section class="info" id="leistungsdaten-bdrg">.*?</section>','',original,flags=re.S)
            section='<section class="info" id="leistungsdaten-bdrg"><h2>Gewichte und Leistungsrichtwerte</h2><p>Ergänzende Angaben aus der unten verlinkten älteren BDRG-Rassetafel. Das sind Zuchtrichtwerte, keine aktuelle Herdenmessung oder Leistungsgarantie. Werte verschiedener Quellen und Zuchtlinien können voneinander abweichen; das genannte Eiergewicht ist kein zugesichertes Durchschnittsgewicht.</p><div class="facts">'
            section+=''.join(f'<div class="fact"><strong>{html.escape(k)}</strong>{html.escape(v)}</div>' for k,v in facts)
            section+=f'</div><p>Quelle: <a href="{url}#page={page}">BDRG-Rassetafel, PDF-Seite {page}</a>. Geprüft am 22. Oktober 2026.</p></section>'
            # Insert before the closing main, leaving every existing paragraph untouched.
            assert original.count('</main>')==1,name
            path.write_text(original.replace('</main>',section+'</main>'),encoding='utf-8')
            records.append(dict(name=name,url=breeds[name]['url'],original_sha256=hashlib.sha256(original.encode('utf-8')).hexdigest(),source=url,page=page,facts=dict(facts)))
    (ROOT/'scripts/requested-facts-audit.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(records)} vorhandene Porträts um belegte Leistungsrichtwerte ergänzt; keine neue Rasse angelegt.')
if __name__=='__main__':main()

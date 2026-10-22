"""Inhalt, Bestandsschutz und optional Originalquellen/PDFs der 50er-Erweiterung prüfen."""
from pathlib import Path
import sys,json,re,hashlib,html,subprocess
ROOT=Path(__file__).resolve().parents[1]
from check_catalog import check,name_key,GROUPS
from series5_texts import TEXTS

def main():
    audit=json.loads((ROOT/'scripts/series5-audit.json').read_text(encoding='utf-8'))
    rows=json.loads((ROOT/'scripts/breeds_series5.json').read_text(encoding='utf-8'))
    count=check()
    assert audit['added']==len(rows)==len(TEXTS)==len(set(audit['new_names']))==50
    assert audit['after']==audit['before']+50 and count>=audit['after']
    assert sum(b['group']=='Großhuhn' for b in rows)==1
    assert sum(b['group']=='Zwerghuhn' for b in rows)==49
    assert len(audit['requested'])==50 and len(audit['replacements'])==42 and len(audit['directly_requested'])==8
    assert len(set(audit['replacements']))==42
    for key in ['history','appearance','nature','husbandry','use']:
        assert len({b[key] for b in TEXTS.values()})==50,('Identische Texte',key)
    index=(ROOT/'index.html').read_text(encoding='utf-8')
    for card in audit['original_cards']:assert card in index,'Vorhandene Karte verändert'
    raw=(ROOT/'assets/finder-data.js').read_text(encoding='utf-8')
    finder=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    records={b['url']:b for b in finder}
    for b in rows:
        t=TEXTS[b['name']];target=b['slug']+'.html';page=(ROOT/target).read_text(encoding='utf-8')
        assert f'<h1>{html.escape(b["name"])}</h1>' in page
        assert records[target]['group']==b['group']
        assert sum(len(t[k].split()) for k in ['history','appearance','nature','husbandry','use'])>=130,b['name']
        for key in ['history','appearance','nature','husbandry','use','colors']:
            assert html.escape(t[key]) in page,(b['name'],key)
        assert 'TODO' not in page and 'Platzhalter' not in page
        assert 'BDRG-Verzeichnis 2024' in page and '#page='+str(b['registry_page']) in page
        assert index.count('href="'+target+'"')==1,target
        assert (ROOT/'qr-codes'/(b['slug']+'.png')).is_file(),target
        assert (ROOT/'output/pdf/a7'/(b['slug']+'.pdf')).is_file(),target
    if '--preserved' in sys.argv:
        for file,digest in audit['preserved_files'].items():
            if file=='index.html':continue
            assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==digest,file
        old=subprocess.run(['git','show','HEAD:assets/finder-data.js'],capture_output=True,check=True).stdout.decode('utf-8')
        for b in json.loads(old.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';')):
            assert records[b['url']]==b,b['url']
    source_checks=0;pdf_codes=0
    if '--sources' in sys.argv or '--pdf' in sys.argv:
        sys.path.insert(0,str(ROOT/'.tools/python'))
        from pypdf import PdfReader
    if '--sources' in sys.argv:
        registry=PdfReader(ROOT/'tmp/pdfs/bdrg-verzeichnis.pdf')
        tables={f:PdfReader(ROOT/'tmp/pdfs'/(f+'.pdf')) for f in ['bdrg-huehner','bdrg-zwerghuehner']}
        for b in rows:
            rt=registry.pages[b['registry_page']-1].extract_text().replace('- \n','-').replace('-\n','-')
            assert any(name_key(line)==name_key(b['name']) for line in rt.splitlines()),b['name']
            st=tables[b['table_file']].pages[b['table_page']-1].extract_text()
            assert int(re.search(r'Legeleistung:\s*(\d+)',st)[1])==b['laying'],b['name']
            if 'egg_g' not in b.get('metric_override',{}):assert int(re.search(r'Eiergewicht:\s*(\d+)',st)[1])==b['egg_g'],b['name']
            if 'weights' not in b.get('metric_override',{}):
                w=re.search(r'Hahn\s+([^\n]+)\s+Henne\s+([^\n]+)',st)
                assert [w[1].strip(),w[2].strip()]==b['weights'],b['name']
            source_checks+=1
    if '--pdf' in sys.argv:
        from check_a7 import scan,decode,size,BASE
        from PIL import Image
        urls=[]
        for b in rows:
            target=BASE+b['slug']+'.html';urls.append(target)
            assert decode(Image.open(ROOT/'qr-codes'/(b['slug']+'.png')))==[target]
            p=ROOT/'output/pdf/a7'/(b['slug']+'.pdf');r=PdfReader(p);assert len(r.pages)==1;size(r.pages[0],74,105)
            assert decode(scan(p))==[target]
            # Keine Rastergrafiken: QR-Module liegen unmittelbar im Vektor-Seiteninhalt.
            for obj in r.pages[0]['/Resources'].get('/XObject',{}).values():assert obj.get_object().get('/Subtype')!='/Image'
            pdf_codes+=1
        r=PdfReader(ROOT/'output/pdf/erweiterung-50-a7.pdf');assert len(r.pages)==50
        for p in r.pages:size(p,74,105)
        p=ROOT/'output/pdf/erweiterung-50-a4.pdf';r=PdfReader(p);assert len(r.pages)==7
        found=[]
        for i,page in enumerate(r.pages):size(page,210,297);found+=decode(scan(p,i))
        assert sorted(found)==sorted(urls)
        assert len(set(found))==50
        scan(p,0,300/72).save(ROOT/'tmp/pdfs/series5-a4-preview.png')
        scan(ROOT/'output/pdf/a7/bergische-zwerg-schlotterkaemme.pdf',0,300/72).save(ROOT/'tmp/pdfs/series5-a7-preview.png')
    result=dict(before=audit['before'],added=50,after=count,new_large_fowl=1,new_bantams=49,directly_requested=8,replacements=42,source_checks=source_checks,pdf_codes=pdf_codes,old_files_preserved='--preserved' in sys.argv,unique_texts=True,all_30_previous_requested_present=True)
    if all(flag in sys.argv for flag in ['--preserved','--sources','--pdf']):
        (ROOT/'scripts/series5-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()

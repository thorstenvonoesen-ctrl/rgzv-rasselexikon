"""Abschlussprüfung: Bestandsschutz, Ergänzungen, Links und Browser-PDF-Ausgabe."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,json,re,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from pypdf import PdfReader
from check_a7 import scan,decode,size,BASE
from check_catalog import check

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for key in ['href','src']:
            if key in a:self.links.append(a[key])

def main():
    total=check();facts=json.loads((ROOT/'scripts/requested-facts-audit.json').read_text(encoding='utf-8'))
    pages=0
    # Alle ursprünglichen Besuchertexte bleiben vollständig erhalten.
    changed=[]
    for p in ROOT.glob('*.html'):
        if p.name in {'index.html','ausstellung.html','schilder-drucken.html'}:continue
        original=subprocess.run(['git','show','HEAD:'+p.name],capture_output=True).stdout.decode('utf-8')
        if not original:continue
        actual=re.sub(r'<section class="info" id="leistungsdaten-bdrg">.*?</section>','',p.read_text(encoding='utf-8'),flags=re.S)
        assert actual.replace('\r\n','\n')==original.replace('\r\n','\n'),p.name
        pages+=1
        if 'leistungsdaten-bdrg' in p.read_text(encoding='utf-8'):changed.append(p.name)
    assert len(changed)==len(facts)==25
    files={}
    for path in ROOT.glob('*.html'):
        parser=Links();parser.feed(path.read_text(encoding='utf-8'));files[path.name]=parser
    links=0
    for name,page in files.items():
        for url in page.links:
            u=urlsplit(url)
            if u.scheme or u.netloc:continue
            path=ROOT/unquote(u.path) if u.path else ROOT/name
            assert path.is_file(),(name,url)
            if u.fragment and path.suffix=='.html':assert unquote(u.fragment) in files[path.name].ids,(name,url)
            links+=1
    # Tatsächlich im Browser heruntergeladene PDFs, nicht nur Generatorausgaben.
    a7=ROOT/'tmp/project/auswahl-a7.pdf';a4=ROOT/'tmp/project/auswahl-a4.pdf'
    r=PdfReader(a7);assert len(r.pages)==8
    urls=[]
    for i,p in enumerate(r.pages):size(p,74,105);urls+=decode(scan(a7,i))
    r=PdfReader(a4);assert len(r.pages)==1;size(r.pages[0],210,297)
    assert sorted(decode(scan(a4)))==sorted(urls) and len(set(urls))==8
    for path in [a7,a4]:
        r=PdfReader(path);assert r.trailer['/Root']['/ViewerPreferences']['/PrintScaling']=='/None'
    result=dict(total=total,requested_present=30,new_breeds=0,supplemented_breeds=25,preserved_description_pages=pages,local_links=links,browser_selection_a7_pages=8,browser_selection_a4_pages=1,selection_codes=8,scale=1)
    (ROOT/'scripts/project-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()

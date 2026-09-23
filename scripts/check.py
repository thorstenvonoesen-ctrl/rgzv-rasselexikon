"""Unabhängiges Decodieren der PNGs und aller gerenderten PDF-QR-Codes."""
from pathlib import Path
import sys,json,re
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from breeds import BREEDS
from new_breeds import NEW_BREEDS
ORIGINAL_BREEDS=BREEDS
BREEDS=BREEDS+NEW_BREEDS
from PIL import Image,ImageOps,ImageDraw
import zxingcpp,pypdfium2 as pdfium,pdfplumber
from pypdf import PdfReader
BASE='https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
MM=72/25.4
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for k in ['href','src']:
            if k in a:self.links.append(a[k])
def scan(image): return sorted(r.text for r in zxingcpp.read_barcodes(image))
assert len(BREEDS)==41 and len({b['slug'] for b in BREEDS})==41
index=Links(); index.feed((ROOT/'index.html').read_text(encoding='utf-8'))
for b in BREEDS: assert index.links.count(b['slug']+'.html')==1,b['slug']
links_checked=0
html_paths=[p for p in ROOT.rglob('*') if p.suffix.lower() in {'.html','.htm'} and not any(part in {'.git','.tools','node_modules','tmp'} for part in p.relative_to(ROOT).parts)]
external_pdf_sources=[]
for path in html_paths:
    text=path.read_text(encoding='utf-8'); assert '\ufffd' not in text
    parser=Links(); parser.feed(text)
    for link in parser.links:
        u=urlsplit(link)
        assert not re.search(r'(^|/)(schilder|qr-codes|druckboegen)(/|$)',unquote(u.path),re.I),(path,link)
        if u.scheme and u.path.lower().endswith('.pdf'): external_pdf_sources.append((path.name,link))
        if u.scheme or u.netloc:continue
        target=path.parent/unquote(u.path) if u.path else path
        assert target.is_file(),(path,link)
        if u.fragment:
            p=Links(); p.feed(target.read_text(encoding='utf-8')); assert u.fragment in p.ids
        links_checked+=1
previews=[]
for b in BREEDS:
    slug=b['slug']; url=BASE+slug+'.html'
    assert scan(Image.open(ROOT/'qr-codes'/f'{slug}.png'))==[url],slug
    file=ROOT/'schilder'/f'{slug}.pdf'; page=PdfReader(file).pages[0]
    assert abs(float(page.mediabox.width)/MM-90)<.001
    assert abs(float(page.mediabox.height)/MM-60)<.001
    extracted=page.extract_text()
    assert re.sub(r'\s','',b['name']) in re.sub(r'\s','',extracted),slug
    with pdfplumber.open(file) as pdf:
        words=pdf.pages[0].extract_words()
        for w in words:
            assert w['x0']>=4.5*MM and w['x1']<=48.5*MM,(slug,w)
            assert w['top']>=2*MM and w['bottom']<=58*MM,(slug,w)
    doc=pdfium.PdfDocument(file)
    for dpi in [150,300]:
        rendered=doc[0].render(scale=dpi/72).to_pil()
        assert scan(rendered)==[url],(slug,dpi)
    rendered.save(ROOT/'tmp/pdfs'/f'{slug}.png')
    preview=ImageOps.contain(rendered,(540,360)); previews.append(preview)
montage=Image.new('RGB',(540*3,380*((len(previews)+2)//3)),'#dedede')
for i,im in enumerate(previews):montage.paste(im,((i%3)*540,(i//3)*380))
montage.save(ROOT/'tmp/pdfs/all-labels.png')
for start in range(0,len(NEW_BREEDS),8):
    selected=previews[len(ORIGINAL_BREEDS)+start:len(ORIGINAL_BREEDS)+start+8]
    overview=Image.new('RGB',(1080,380*((len(selected)+1)//2)),'#dedede')
    for i,im in enumerate(selected): overview.paste(im,((i%2)*540,(i//2)*380))
    overview.save(ROOT/'tmp/pdfs'/f'new-labels-{start//8+1}.png')
for selection,prefix,layout_name in [(ORIGINAL_BREEDS,'rasseschild-bogen','layout.json'),(NEW_BREEDS,'rasseschild-erweiterung','layout-erweiterung.json')]:
  layout=json.loads((ROOT/'scripts'/layout_name).read_text(encoding='utf-8'))
  assert len(layout['placements'])==len(selection)
  for n in range(1,(len(selection)+7)//8+1):
    file=ROOT/'druckboegen'/f'{prefix}-{n:02}.pdf'
    page=PdfReader(file).pages[0]
    assert abs(float(page.mediabox.width)/MM-210)<.001
    assert abs(float(page.mediabox.height)/MM-297)<.001
    doc=pdfium.PdfDocument(file); rendered=doc[0].render(scale=300/72).to_pil()
    expected=sorted(BASE+b['slug']+'.html' for b in selection[(n-1)*8:n*8])
    assert scan(rendered)==expected,(n,scan(rendered),expected)
    rendered.resize((840,1188)).save(ROOT/'tmp/pdfs'/f'{prefix}-{n}.png')
    # Confirm actual PDF text coordinates match the source plus translation.
    with pdfplumber.open(file) as merged:
        for p in [p for p in layout['placements'] if p['sheet']==n]:
            with pdfplumber.open(ROOT/'schilder'/f'{p["slug"]}.pdf') as original:
                chars=original.pages[0].chars
                for ch in chars:
                    x=ch['x0']+p['x_mm']*MM
                    top=ch['top']+(297-p['y_mm']-60)*MM
                    assert any(c['text']==ch['text'] and abs(c['x0']-x)<.02 and abs(c['top']-top)<.02 and abs(c['size']-ch['size'])<.001 for c in merged.pages[0].chars),(p['slug'],ch)
baseline_path=ROOT/'tmp/extension-baseline.json'
preserved=None
if baseline_path.exists():
    import hashlib
    baseline=json.loads(baseline_path.read_text(encoding='utf-8'))
    for name,digest in baseline.items(): assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    preserved=len(baseline)
report={'rasseseiten':41,'html_seiten_geprueft':len(html_paths),'qr_png':41,'einzel_pdf':41,'a4_bogen':6,'interne_links_geprueft':links_checked,'png_decodiert':41,'einzel_pdf_decodiert_150_und_300_dpi':82,'a4_qr_decodiert_300_dpi':41,'oeffentliche_interne_downloadlinks':0,'externe_pdf_quellenlinks':len(external_pdf_sources),'bestehende_dateien_unveraendert_sha256':preserved,'pdf_groessen':'90 x 60 mm / 210 x 297 mm','a4_originalgroesse':'Alle Textpositionen und Schriftgrößen mit Einzel-PDF verglichen; nur Translation, keine Skalierung.','textgrenzen':'Alle PDF-Wörter innerhalb des linken Bereichs; vollständige Rassenamen extrahiert.'}
(ROOT/'scripts/qa-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True,indent=2))

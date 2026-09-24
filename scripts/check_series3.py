"""Begrenzte Prüfung ausschließlich der zuletzt neu erzeugten Serie."""
from pathlib import Path
import sys, json, re
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from breeds_series3 import SERIES3
from PIL import Image, ImageOps
from pypdf import PdfReader
import pypdfium2 as pdfium
import zxingcpp
BASE='https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
MM=72/25.4
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.title=''; self.in_h1=False
    def handle_starttag(self,tag,attrs):
        if tag=='h1': self.in_h1=True
        for k,v in attrs:
            if k in {'href','src'}: self.links.append(v)
    def handle_endtag(self,tag):
        if tag=='h1': self.in_h1=False
    def handle_data(self,data):
        if self.in_h1: self.title+=data
def parse(path):
    p=Page(); p.feed(path.read_text(encoding='utf-8')); return p
def decode(im): return [r.text for r in zxingcpp.read_barcodes(im)]
created=json.loads((ROOT/'scripts/series3-created.json').read_text(encoding='utf-8'))
selected=[b for b in SERIES3 if b['slug'] in created]
index=parse(ROOT/'index.html')
previews=[]
for b in selected:
    slug=b['slug']; target=slug+'.html'; url=BASE+target
    p=parse(ROOT/target)
    assert p.title==b['name'],slug
    assert index.links.count(target)==1,slug
    for link in p.links:
        path=unquote(urlsplit(link).path)
        assert not re.search(r'(^|/)(schilder|qr-codes|druckboegen)(/|$)',path,re.I),(slug,link)
    assert decode(Image.open(ROOT/'qr-codes'/f'{slug}.png'))==[url],slug
    file=ROOT/'schilder'/f'{slug}.pdf'
    pdf=PdfReader(file); assert len(pdf.pages)==1
    page=pdf.pages[0]
    assert abs(float(page.mediabox.width)/MM-90)<.001,slug
    assert abs(float(page.mediabox.height)/MM-60)<.001,slug
    assert re.sub(r'\s','',b['name']) in re.sub(r'\s','',page.extract_text()),slug
    doc=pdfium.PdfDocument(file); im=doc[0].render(scale=150/72).to_pil()
    assert decode(im)==[url],slug
    previews.append(ImageOps.contain(im,(450,300)))
for start in range(0,len(previews),8):
    group=previews[start:start+8]
    canvas=Image.new('RGB',(900,310*((len(group)+1)//2)),'#ddd')
    for i,im in enumerate(group):canvas.paste(im,((i%2)*450,(i//2)*310))
    canvas.save(ROOT/'tmp/pdfs'/f'series3-{start//8+1}.png')
report=dict(new_html=len(selected),new_qr=len(selected),new_labels=len(selected),
    qr_decoded=len(selected),pdf_qr_decoded=len(selected),label_mm=[90,60],
    correct_page_titles=True,index_entries=True,public_print_links=0,
    public_deployment='Nicht Bestandteil dieses lokalen Prüflaufs.')
(ROOT/'scripts/series3-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True,indent=2))

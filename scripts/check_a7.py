"""Alle vorhandenen QR-PNGs und neue A7/A4-Ausgaben unabhängig prüfen."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from PIL import Image
from pypdf import PdfReader
import pypdfium2 as pdfium
import zxingcpp
from build_a7 import catalog,BASE,OUT,alphabetical
MM=72/25.4

def decode(im):return [r.text for r in zxingcpp.read_barcodes(im.convert('RGB'),formats=zxingcpp.BarcodeFormat.QRCode)]
def scan(path,page=0,scale=200/72):
    pdf=pdfium.PdfDocument(str(path));p=pdf[page];bitmap=p.render(scale=scale);im=bitmap.to_pil().copy();bitmap.close();p.close();pdf.close();return im
def size(page,w,h):
    assert abs(float(page.mediabox.width)/MM-w)<.001
    assert abs(float(page.mediabox.height)/MM-h)<.001

def main():
    breeds=catalog();layout=json.loads((ROOT/'scripts/a7-layout.json').read_text(encoding='utf-8'))
    for filename,digest in layout['qr_hashes'].items():
        path=ROOT/'qr-codes'/filename
        assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,filename
        assert decode(Image.open(path))==[BASE+path.stem+'.html'],filename
        assert (ROOT/(path.stem+'.html')).is_file()
    for b in breeds:
        path=OUT/b['url'].replace('.html','.pdf');reader=PdfReader(path)
        assert len(reader.pages)==1;size(reader.pages[0],74,105)
        assert reader.trailer['/Root']['/ViewerPreferences']['/PrintScaling']=='/None'
        text=reader.pages[0].extract_text().replace('\n','').replace(' ','')
        assert b['name'].replace(' ','') in text,b['name']
        assert 'RGZVHagenundUmgebung' in text and 'seit1903e.V.' in text
        assert 'Rasseentdecken' in text and 'DigitalesRasselexikon' in text
        facts=' · '.join(filter(None,(b['group'],b['detail'])))
        assert facts.replace(' ','') in text,b['url']
        assert reader.pages[0]['/Annots'][0].get_object()['/A']['/URI']==BASE+b['url']
        assert decode(scan(path))==[BASE+b['url']],path.name
    combined=PdfReader(OUT/'alle-rasseschilder-a7.pdf');assert len(combined.pages)==len(breeds)
    assert [b['name'] for b in breeds]==sorted((b['name'] for b in breeds),key=alphabetical)
    for b,p in zip(breeds,combined.pages):
        size(p,74,105)
        assert p['/Annots'][0].get_object()['/A']['/URI']==BASE+b['url']
    a4=OUT/'alle-rasseschilder-a4.pdf';reader=PdfReader(a4)
    assert len(reader.pages)==(len(breeds)+7)//8
    for i,p in enumerate(reader.pages):
        size(p,210,297)
        found=decode(scan(a4,i));expected=[BASE+b['url'] for b in breeds[i*8:i*8+8]]
        assert sorted(found)==sorted(expected),(i,found,expected)
    example=OUT/'beispiel-acht-rasseschilder-a4.pdf';r=PdfReader(example);assert len(r.pages)==1;size(r.pages[0],210,297)
    im=scan(example,scale=300/72);assert sorted(decode(im))==sorted(BASE+s+'.html' for s in layout['example'])
    (ROOT/'tmp/pdfs/a7-example-preview.png').parent.mkdir(parents=True,exist_ok=True);im.save(ROOT/'tmp/pdfs/a7-example-preview.png')
    scan(OUT/'deutsche-zwerg-lachshuehner.pdf',scale=300/72).save(ROOT/'tmp/pdfs/a7-single-preview.png')
    # Pro Schild die tatsächliche Drehmatrix und Position auf dem A4-Bogen prüfen.
    for i,p in enumerate(reader.pages):
        rotations=[]
        for args,op in p.get_contents().operations:
            if op!=b'cm':
                continue
            matrix=list(map(float,args))
            if any(abs(a-b)>1e-6 for a,b in zip(matrix[:4],[1,0,0,1])):
                rotations.append(matrix)
        count=min(8,len(breeds)-8*i)
        assert len(rotations)==count,i
        for cell,matrix in enumerate(rotations):
            expected=[0,-1,1,0,(cell%2)*105*MM,((4-cell//2)*74+.5)*MM]
            assert all(abs(a-b)<1e-4 for a,b in zip(matrix,expected)),(i,cell,matrix)
    from check_pdf_storage import check as check_storage
    check_storage()
    old=0
    result=dict(races=len(breeds),existing_pngs=len(layout['qr_hashes']),existing_sign_pdfs=old,new_a7_pdfs=len(breeds),a4_pages=len(reader.pages),a4_example_codes=8,qr_decode_dpi=200,example_dpi=300,dimensions_mm=[74,105],scale=1)
    (ROOT/'scripts/a7-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()

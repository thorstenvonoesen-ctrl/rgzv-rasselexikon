"""A7-Hochformat 74 x 105 mm; A4: acht gedrehte Schilder ohne Skalierung."""
from pathlib import Path
import sys,json,re,hashlib,tempfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
import qrcode
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
BASE='https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
OUT=ROOT/'output/pdf'
GROUPS={'Großhuhn','Zwerghuhn','Taube','Wachtel','Gans','Ente'}
pdfmetrics.registerFont(TTFont('A7Regular','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('A7Bold','C:/Windows/Fonts/arialbd.ttf'))

def catalog():
    raw=(ROOT/'assets/finder-data.js').read_text(encoding='utf-8')
    data=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    return sorted([b for b in data if b['group'] in GROUPS],key=lambda b:b['name'].casefold())

def title_lines(name,size):
    lines=[];line=''
    for word in re.findall(r'[^\s-]+-?|[^\s]+',name):
        trial=line+('' if not line or line.endswith('-') else ' ')+word
        if pdfmetrics.stringWidth(trial,'A7Bold',size)>66*mm and line:lines.append(line);line=word
        else:line=trial
    if line:lines.append(line)
    return lines

def draw_label(c,b):
    c.setFillColor(HexColor('#183b2b'))
    size=16
    while True:
        lines=title_lines(b['name'],size)
        if len(lines)<=3 and all(pdfmetrics.stringWidth(x,'A7Bold',size)<=66*mm for x in lines):break
        size-=.25
        assert size>=10,b['name']
    c.setFont('A7Bold',size)
    for i,line in enumerate(lines):c.drawCentredString(37*mm,(97-i*6)*mm,line)
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,border=4,box_size=1)
    url=BASE+b['url'];qr.add_data(url);qr.make(fit=True)
    matrix=qr.get_matrix();module=60*mm/len(matrix)
    c.setFillColorRGB(0,0,0)
    # Ruhezone ist im 60-mm-Quadrat enthalten; jedes Modul ist eine echte Vektorfläche.
    for row,values in enumerate(matrix):
        for col,on in enumerate(values):
            if on:c.rect(7*mm+col*module,22*mm+(len(matrix)-1-row)*module,module,module,stroke=0,fill=1)
    c.linkURL(url,(7*mm,22*mm,67*mm,82*mm),relative=0)
    c.setFillColor(HexColor('#183b2b'));c.setFont('A7Regular',8)
    c.drawCentredString(37*mm,12*mm,'RGZV Hagen und Umgebung')
    c.drawCentredString(37*mm,8*mm,'seit 1903 e. V.')
    return dict(name=b['name'],url=url,title_lines=lines,font_size=size)

def pdf(path,selection,a4=False):
    c=canvas.Canvas(str(path),pagesize=A4 if a4 else (74*mm,105*mm),invariant=1)
    c.setTitle('RGZV Hagen | Rasseschilder DIN A7');c.setAuthor('RGZV Hagen und Umgebung seit 1903 e. V.')
    c.setViewerPreference('PrintScaling','None')
    batch=8 if a4 else 1
    for start in range(0,len(selection),batch):
        for i,b in enumerate(selection[start:start+batch]):
            c.saveState()
            if a4:
                c.translate((i%2)*105*mm,((4-i//2)*74+.5)*mm);c.rotate(-90)
            draw_label(c,b);c.restoreState()
        if a4:
            c.setStrokeColor(HexColor('#a0aaa3'));c.setLineWidth(.25)
            c.line(105*mm,.5*mm,105*mm,296.5*mm)
            for y in [74.5,148.5,222.5]:c.line(0,y*mm,210*mm,y*mm)
        c.showPage()
    c.save()

def main():
    from io import BytesIO
    from check_catalog import check
    from pypdf import PdfReader,PdfWriter,Transformation
    from pypdf.generic import DictionaryObject,NameObject
    check();breeds=catalog();(OUT/'a7').mkdir(parents=True,exist_ok=True)
    (ROOT/'tmp/pdfs').mkdir(parents=True,exist_ok=True)
    layout_path=ROOT/'scripts/a7-layout.json'
    previous=json.loads(layout_path.read_text(encoding='utf-8')) if layout_path.exists() else {}
    entries={b['url']:b['name'] for b in breeds}
    expected={url.replace('.html','.pdf') for url in entries}
    existing={p.name for p in (OUT/'a7').glob('*.pdf')}
    before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'qr-codes').glob('*.png')}
    changed=[]
    with tempfile.TemporaryDirectory(prefix='a7-',dir=ROOT/'tmp/pdfs') as work:
        stage=Path(work)
        for b in breeds:
            filename=b['url'].replace('.html','.pdf');target=OUT/'a7'/filename
            if not target.exists() or previous.get('entries',{}).get(b['url'],b['name'])!=b['name']:
                pdf(stage/filename,[b]);changed.append(filename)
        totals=['alle-rasseschilder-a7.pdf','alle-rasseschilder-a4.pdf']
        refresh=bool(changed) or existing!=expected or previous.get('count')!=len(breeds) or any(not (OUT/f).is_file() for f in totals)
        if refresh:
            a7=PdfWriter();a4=PdfWriter();sheet=None
            for i,b in enumerate(breeds):
                filename=b['url'].replace('.html','.pdf')
                source=stage/filename if filename in changed else OUT/'a7'/filename
                page=PdfReader(source).pages[0];a7.add_page(page)
                if i%8==0:sheet=a4.add_blank_page(210*mm,297*mm)
                cell=i%8
                transform=Transformation().rotate(-90).translate((cell%2)*105*mm,((4-cell//2)*74+.5)*mm)
                sheet.merge_transformed_page(page,transform)
            grid=BytesIO();marks=canvas.Canvas(grid,pagesize=A4,invariant=1)
            marks.setStrokeColor(HexColor('#a0aaa3'));marks.setLineWidth(.25)
            marks.line(105*mm,.5*mm,105*mm,296.5*mm)
            for y in [74.5,148.5,222.5]:marks.line(0,y*mm,210*mm,y*mm)
            marks.showPage();marks.save();grid.seek(0)
            overlay=PdfReader(grid).pages[0]
            for sheet in a4.pages:sheet.merge_page(overlay)
            for writer,filename in [(a7,totals[0]),(a4,totals[1])]:
                writer._root_object[NameObject('/ViewerPreferences')]=DictionaryObject({NameObject('/PrintScaling'):NameObject('/None')})
                with (stage/filename).open('wb') as stream:writer.write(stream)
            for filename in totals:(OUT/filename).write_bytes((stage/filename).read_bytes())
        for filename in changed:(OUT/'a7'/filename).write_bytes((stage/filename).read_bytes())
    for filename in existing-expected:(OUT/'a7'/filename).unlink()
    assert before=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'qr-codes').glob('*.png')}
    previous.update(count=len(breeds),entries=entries,size_mm=[74,105],qr_hashes=before,a4_cells_mm=[105,74],rotation=-90,scale=1)
    layout_path.write_text(json.dumps(previous,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(breeds)} A7-Schilder zentral vorhanden; {len(changed)} ergänzt oder inhaltlich aktualisiert; Gesamtausgaben aktualisiert: {refresh}.')
if __name__=='__main__':main()

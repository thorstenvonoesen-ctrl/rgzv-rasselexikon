"""A7-Hochformat 74 x 105 mm; A4: acht gedrehte Schilder ohne Skalierung."""
from pathlib import Path
import sys,json,re,hashlib,tempfile,unicodedata
from html import unescape
from shutil import copyfile
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
OUT=ROOT/'A7-Rasseschilder'
LEGACY=ROOT/'output/pdf'
LAYOUT_VERSION=2
TOTALS=['alle-rasseschilder-a7.pdf','alle-rasseschilder-a4.pdf']
EXAMPLE='beispiel-acht-rasseschilder-a4.pdf'
EXTENSIONS=['erweiterung-50-a7.pdf','erweiterung-50-a4.pdf']
COLLECTIONS=[*TOTALS,EXAMPLE,*EXTENSIONS]
GROUPS={'Großhuhn','Zwerghuhn','Taube','Wachtel','Gans','Ente'}
pdfmetrics.registerFont(TTFont('A7Regular','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('A7Bold','C:/Windows/Fonts/arialbd.ttf'))

def catalog():
    raw=(ROOT/'assets/finder-data.js').read_text(encoding='utf-8')
    data=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    for breed in data:
        if breed['group'] in GROUPS:
            page=(ROOT/breed['url']).read_text(encoding='utf-8')
            match=re.search(r'<strong>Herkunft[^<]*</strong>(.*?)</div>',page,re.S)
            breed['origin']=' '.join(unescape(re.sub(r'<[^>]+>',' ',match[1])).split()) if match else ''
    return sorted((b for b in data if b['group'] in GROUPS),key=lambda b:alphabetical(b['name']))

def alphabetical(name):
    folded=unicodedata.normalize('NFD',name.casefold())
    return ''.join(c for c in folded if not unicodedata.combining(c)),name.casefold()

def wrapped(text,font,size):
    lines=[];line=''
    for word in re.findall(r'[^\s-]+-?|-',text):
        trial=line+('' if not line or line.endswith('-') else ' ')+word
        if line and pdfmetrics.stringWidth(trial,font,size)>62*mm:
            lines.append(line);line=word
        else:
            line=trial
    return lines+[line]

def fit(text,font,start,minimum,max_lines):
    for quarter_points in range(start*4,minimum*4-1,-1):
        size=quarter_points/4
        lines=wrapped(text,font,size)
        if len(lines)<=max_lines and all(pdfmetrics.stringWidth(line,font,size)<=62*mm for line in lines):
            return lines,size
    raise ValueError(f'Text passt nicht auf ein A7-Schild: {text}')

def caption(c,text,y,size,font='A7Regular'):
    c.setFont(font,size)
    c.drawCentredString(37*mm,y*mm,text)

def draw_label(c,b):
    c.setLineWidth(.45)
    c.roundRect(2*mm,2*mm,70*mm,101*mm,3*mm)
    lines,size=fit(b['name'],'A7Bold',15,10,3)
    for i,line in enumerate(lines):
        caption(c,line,(97-i*5.8 if len(lines)==3 else 95-i*6.5),size,'A7Bold')
    facts=' · '.join(filter(None,(b['group'],b['origin'])))
    lines,size=fit(facts,'A7Regular',10,8,2)
    for i,line in enumerate(lines):
        caption(c,line,81-i*4.2,size)
    caption(c,'Rasse entdecken',72,12,'A7Bold')
    caption(c,'QR-Code scannen und mehr erfahren',66,9.5)

    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,border=4,box_size=1)
    url=BASE+b['url'];qr.add_data(url);qr.make(fit=True)
    matrix=qr.get_matrix();module=42*mm/len(matrix)
    path=c.beginPath()
    for row,values in enumerate(matrix):
        for col,on in enumerate(values):
            if on:
                path.rect(16*mm+col*module,18*mm+(len(matrix)-1-row)*module,module,module)
    c.drawPath(path,stroke=0,fill=1)
    c.linkURL(url,(16*mm,18*mm,58*mm,60*mm),relative=0)
    caption(c,'RGZV Hagen und Umgebung',14,8.5)
    caption(c,'seit 1903 e.V.',9.8,8.5)
    caption(c,'Digitales Rasselexikon',5.6,8.5)

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
    check();breeds=catalog();OUT.mkdir(exist_ok=True)
    (LEGACY/'a7').mkdir(parents=True,exist_ok=True)
    (ROOT/'tmp/pdfs').mkdir(parents=True,exist_ok=True)
    layout_path=ROOT/'scripts/a7-layout.json'
    previous=json.loads(layout_path.read_text(encoding='utf-8')) if layout_path.exists() else {}
    entries={b['url']:[b['name'],b['group'],b['origin']] for b in breeds}
    layout_changed=previous.get('version')!=LAYOUT_VERSION
    expected={url.replace('.html','.pdf') for url in entries}
    existing={p.name for p in OUT.glob('*.pdf')}-set(COLLECTIONS)
    before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'qr-codes').glob('*.png')}
    changed=set()
    with tempfile.TemporaryDirectory(prefix='a7-',dir=ROOT/'tmp/pdfs') as work:
        stage=Path(work)
        for b in breeds:
            filename=b['url'].replace('.html','.pdf');target=OUT/filename
            if layout_changed or not target.exists() or previous.get('entries',{}).get(b['url'])!=entries[b['url']]:
                pdf(stage/filename,[b]);changed.add(filename)
        refresh=bool(changed) or existing!=expected or previous.get('count')!=len(breeds) or any(not (OUT/f).is_file() for f in COLLECTIONS)
        if refresh:
            a7=PdfWriter();a4=PdfWriter();sheet=None
            for i,b in enumerate(breeds):
                filename=b['url'].replace('.html','.pdf')
                source=stage/filename if filename in changed else OUT/filename
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
            for writer,filename in [(a7,TOTALS[0]),(a4,TOTALS[1])]:
                writer._root_object[NameObject('/ViewerPreferences')]=DictionaryObject({NameObject('/PrintScaling'):NameObject('/None')})
                with (stage/filename).open('wb') as stream:writer.write(stream)
            sample_urls={slug+'.html' for slug in previous['example']}
            pdf(stage/EXAMPLE,[b for b in breeds if b['url'] in sample_urls],a4=True)
            extension_urls={b['slug']+'.html' for b in json.loads((ROOT/'scripts/breeds_series5.json').read_text(encoding='utf-8'))}
            extension=[b for b in breeds if b['url'] in extension_urls]
            for filename,a4_mode in zip(EXTENSIONS,(False,True)):
                pdf(stage/filename,extension,a4=a4_mode)
            for filename in COLLECTIONS:
                (stage/filename).replace(OUT/filename)
        for filename in changed:(stage/filename).replace(OUT/filename)
    for filename in existing-expected:(OUT/filename).unlink()
    # Bestehende Direktlinks auf Rasseseiten und externe Lesezeichen erhalten.
    for filename in expected | set(COLLECTIONS):
        source=OUT/filename
        target=(LEGACY/'a7' if filename in expected else LEGACY)/filename
        if not target.exists() or source.read_bytes()!=target.read_bytes():
            copyfile(source,target)
    for path in (LEGACY/'a7').glob('*.pdf'):
        if path.name not in expected:
            path.unlink()
    assert before=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'qr-codes').glob('*.png')}
    previous.update(version=LAYOUT_VERSION,qr_mm=[16,18,42,42],count=len(breeds),entries=entries,size_mm=[74,105],qr_hashes=before,a4_cells_mm=[105,74],rotation=-90,scale=1)
    layout_path.write_text(json.dumps(previous,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(breeds)} A7-Schilder zentral vorhanden; {len(changed)} ergänzt oder inhaltlich aktualisiert; Gesamtausgaben aktualisiert: {refresh}.')
if __name__=='__main__':main()

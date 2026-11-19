"""A4-Wickelfalz: außen 97/100/100 mm, innen 100/100/97 mm.
Zweiseitige Druckdatei, Falzplan, 300-dpi-Renderings und unabhängiger QR-Scan.
"""
from pathlib import Path
import sys, json, shutil, zipfile, hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
from PIL import Image, ImageDraw, ImageFont
import pypdfium2 as pdfium

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
ASSETS=ROOT/'output/pdf/gefluegelzuchtbedarf-a4'
for filename in ['original-logo.png','Zuechterhaende-Schwarzweiss.png']:
    if not (HERE/filename).exists():shutil.copyfile(ASSETS/filename,HERE/filename)
sys.path.insert(0,str(ROOT/'.tools/python'))
import qrcode, zxingcpp
for name,file in [('Book','FRABK.TTF'),('Heavy','FRAHV.TTF'),('Medium','framd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
W,H=297*mm,210*mm
PAPER='#F5F3EE'; BLACK='#252A28'; RUST='#A8432F'; MUTED='#626662'
URL='gefluegelzuchtbedarf.myshopify.com'
LINK='https://'+URL
LOGO=HERE/'original-logo.png'
PHOTO=HERE/'Zuechterhaende-Schwarzweiss.png'
EXT=[(0,97),(97,100),(197,100)]
INT=[(0,100),(100,100),(200,97)]

def rect(c,x,y,w,h,color):
    c.setFillColor(HexColor(color));c.rect(x*mm,H-(y+h)*mm,w*mm,h*mm,stroke=0,fill=1)

def rule(c,x,y,w,color=RUST,weight=.7):
    c.setStrokeColor(HexColor(color));c.setLineWidth(weight)
    c.line(x*mm,H-y*mm,(x+w)*mm,H-y*mm)

def text(c,s,x,y,font='Book',size=11.5,color=BLACK,align='left',tracking=0):
    sw=pdfmetrics.stringWidth(s,font,size)+max(0,len(s)-1)*tracking
    xx=x*mm-(sw/2 if align=='center' else sw if align=='right' else 0)
    assert xx>=7*mm-.1 and xx+sw<=W-7*mm+.1,(s,xx/mm,(xx+sw)/mm)
    c.setFillColor(HexColor(color)); t=c.beginText()
    t.setFont(font,size);t.setCharSpace(tracking);t.setTextOrigin(xx,H-y*mm)
    t.textOut(s);c.drawText(t)
    return sw/mm

def pt(c,p,s,y,font='Book',size=11.5,color=BLACK,dx=8,align='left',tracking=0):
    x,w=p
    pos=x+dx if align=='left' else x+w/2
    sw=pdfmetrics.stringWidth(s,font,size)+max(0,len(s)-1)*tracking
    assert sw<=(w-16)*mm+.2,('Panelüberlauf',s,sw/mm,w-16)
    return text(c,s,pos,y,font,size,color,align,tracking)

def para(c,p,s,y,size=11.5,leading=5.8,color=BLACK):
    words=s.split(); lines=[]; line=''
    for word in words:
        trial=(line+' '+word).strip()
        if pdfmetrics.stringWidth(trial,'Book',size)>(p[1]-16)*mm:
            lines.append(line);line=word
        else:line=trial
    if line:lines.append(line)
    for line in lines:
        pt(c,p,line,y,size=size,color=color);y+=leading
    return y

def logo(c,p,y=12,width=82):
    x=p[0]+(p[1]-width)/2
    c.drawImage(ImageReader(str(LOGO)),x*mm,H-(y+width/2)*mm,width*mm,width/2*mm,mask='auto')

def qr(c,x,y,side=34):
    q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,border=4,box_size=12)
    q.add_data(LINK);q.make(fit=True);matrix=q.get_matrix();module=side*mm/len(matrix)
    rect(c,x,y,side,side,'#FFFFFF');c.setFillColor(HexColor('#000000'))
    for row,values in enumerate(matrix):
        for col,dark in enumerate(values):
            if dark:c.rect(x*mm+col*module,H-y*mm-(row+1)*module,module,module,stroke=0,fill=1)
    c.linkURL(LINK,(x*mm,H-(y+side)*mm,(x+side)*mm,H-y*mm),relative=0,thickness=0)

def start(c):
    rect(c,0,0,297,210,PAPER)
    c.setTitle('Zucht ist Herzblut | A4-Wickelfalz-Broschüre')
    c.setAuthor('Geflügelzuchtbedarf')
    c.setSubject('Fachhandel für Geflügelzucht und Hobbyhaltung | HERZBLUT10')

def outside(c):
    start(c)
    # Links: eingeschlagene Lasche, Mitte: Rückseite, rechts: Titel.
    p=EXT[0]
    pt(c,p,'AUS LEIDENSCHAFT.',18,'Medium',9,tracking=.8)
    for s,y in [('FÜR DIE,',40),('DIE MIT',52),('HERZBLUT',64),('ZÜCHTEN.',76)]:pt(c,p,s,y,'Heavy',27)
    rule(c,8,88,13,weight=2.5)
    y=para(c,p,'Wer Geflügel züchtet oder hält, weiß: Die tägliche Versorgung gehört genauso dazu wie die Freude an den Tieren.',105)
    y=para(c,p,'Wir bieten Zubehör für Tränken und Fütterung, für Brut und Aufzucht sowie für den Geflügelstall.',y+6)
    pt(c,p,'VOM ZÜCHTER.',177,'Heavy',18)
    pt(c,p,'FÜR DEN ZÜCHTER.',186,'Heavy',18)
    pt(c,p,'GEFLÜGELZUCHTBEDARF',199,'Medium',8.5,tracking=.5)
    p=EXT[1]
    pt(c,p,'DIREKT ZUM SHOP.',18,'Medium',9,tracking=.8)
    pt(c,p,'IHR GEFLÜGEL.',39,'Heavy',23)
    pt(c,p,'UNSER FACHGEBIET.',50,'Heavy',21)
    qr(c,128,67,38)
    pt(c,p,'Scannen und Sortiment entdecken.',118,size=10.5,align='center')
    pt(c,p,URL,130,'Medium',10.7,align='center')
    c.linkURL(LINK,(105*mm,H-135*mm,189*mm,H-123*mm),relative=0,thickness=0)
    rule(c,105,143,84,BLACK,.6)
    pt(c,p,'10 % RABATT',162,'Heavy',27,RUST,align='center')
    pt(c,p,'HERZBLUT10',177,'Heavy',24,align='center')
    pt(c,p,'Code beim Bezahlen eingeben.',190,size=10,align='center')
    p=EXT[2]
    logo(c,p,10,82)
    pt(c,p,'ZUCHT IST',63,'Heavy',31)
    pt(c,p,'HERZBLUT.',76,'Heavy',31)
    rule(c,205,87,13,weight=2.5)
    photo_w=48
    photo_h=photo_w*1916/821
    c.drawImage(ImageReader(str(PHOTO)),241*mm,H-(90+photo_h)*mm,photo_w*mm,photo_h*mm)
    text(c,'WIR HABEN',205,109,'Heavy',11)
    text(c,'DAS ZUBEHÖR.',205,116,'Heavy',11)
    text(c,'Für Züchter',205,153,size=10)
    text(c,'und Hobbyhalter.',205,159,size=10)
    text(c,'Zucht.',205,181,'Medium',10)
    text(c,'Aufzucht.',205,187,'Medium',10)
    text(c,'Haltung.',205,193,'Medium',10)

def inside(c):
    start(c)
    p=INT[0]
    pt(c,p,'01 / TÄGLICHE VERSORGUNG',18,'Medium',9,tracking=.5)
    pt(c,p,'TRÄNKEN.',40,'Heavy',29)
    pt(c,p,'FÜTTERN.',53,'Heavy',29)
    rule(c,8,66,13,weight=2.5)
    pt(c,p,'Gute Zucht lebt vom Alltag.',85,'Medium',14)
    para(c,p,'Füttern, Wasser bereitstellen, nach den Tieren sehen: Es sind die täglichen Handgriffe, die zur Geflügelhaltung gehören.',98)
    pt(c,p,'Tränken & Tränkesysteme',133,'Heavy',13)
    para(c,p,'Entdecken Sie Tränken und Zubehör für die Wasserversorgung Ihres Geflügels.',143)
    pt(c,p,'Fütterung & Futterzubehör',170,'Heavy',13)
    para(c,p,'Passendes Zubehör für die Fütterung im Zucht- und Hobbybestand.',180)
    p=INT[1]
    pt(c,p,'02 / VOM ERSTEN TAG AN',18,'Medium',9,tracking=.5)
    pt(c,p,'BRUT &',40,'Heavy',29)
    pt(c,p,'AUFZUCHT.',53,'Heavy',29)
    rule(c,108,66,13,weight=2.5)
    pt(c,p,'Kleine Anfänge.',85,'Medium',17)
    pt(c,p,'Große Leidenschaft.',94,'Medium',17)
    para(c,p,'Wenn aus Vorfreude neues Leben wird, beginnt eine besondere Zeit. Entdecken Sie Bedarf für Brut und Aufzucht.',109)
    pt(c,p,'Mit Blick auf Ihre Tiere.',149,'Heavy',13)
    para(c,p,'Unser Sortiment richtet sich an Menschen, die Geflügel mit Erfahrung, Geduld und Leidenschaft züchten und halten.',160)
    pt(c,p,'VOM ZÜCHTER FÜR DEN ZÜCHTER.',198,'Medium',9)
    p=INT[2]
    pt(c,p,'03 / STALL & GEFLÜGELZUBEHÖR',18,'Medium',8.7,tracking=.2)
    pt(c,p,'HALTUNG',40,'Heavy',29)
    pt(c,p,'MIT HERZ.',53,'Heavy',29)
    rule(c,208,66,13,weight=2.5)
    pt(c,p,'Für Ihren Geflügelstall.',85,'Medium',15)
    para(c,p,'Ob Zuchtbestand oder Hobbyhaltung: Entdecken Sie Stall- und Geflügelzubehör für den Alltag mit Ihren Tieren.',99)
    para(c,p,'Das Sortiment finden Sie in unserem Onlineshop. Einfach scannen und entdecken.',129)
    text(c,'IHR DANKESCHÖN:',208,161,'Medium',9,tracking=.4)
    text(c,'10 %',208,176,'Heavy',26,RUST)
    text(c,'RABATT',208,184,'Heavy',13,RUST)
    text(c,'HERZBLUT10',208,195,'Heavy',15)
    qr(c,254,163,32)
    text(c,'Code beim Bezahlen eingeben.',208,201,size=8.5)

def render_pdf(path,dpi,prefix):
    doc=pdfium.PdfDocument(str(path))
    images=[]
    for i in range(len(doc)):
        im=doc[i].render(scale=dpi/72).to_pil().convert('RGB')
        im.save(HERE/f'{prefix}-{i+1}.png',dpi=(dpi,dpi));images.append(im)
    return images

def guide(c):
    start(c)
    text(c,'DRUCKEN. FALTEN. FERTIG.',12,20,'Heavy',25)
    text(c,'A4 quer | beidseitig | 100 % / tatsächliche Größe | an der kurzen Kante wenden',12,31,size=12)
    text(c,'Blatt innen nach oben legen. Zuerst die schmale rechte Lasche nach links falten,',12,43,size=11)
    text(c,'danach das linke Feld nach rechts schließen. Endformat: 100 × 210 mm.',12,50,size=11)
    for y,title,panels,names in [(66,'SEITE 1 / AUSSEN',EXT,['Lasche','Rückseite / QR & Rabatt','Titelseite']),
                                 (121,'SEITE 2 / INNEN',INT,['Tränken / Fütterung','Brut / Aufzucht','Stall / Rabatt'])]:
        text(c,title,12,y,'Heavy',12)
        scale=273/297
        for i,((x,w),name) in enumerate(zip(panels,names)):
            xx=12+x*scale;ww=w*scale
            rect(c,xx,y+5,ww-.7,35,'#E4E2DC')
            text(c,name,xx+4,y+19,'Medium',10)
            text(c,f'{w} mm',xx+4,y+30,size=10)
        folds='97 und 197 mm ab linker Blattkante' if panels==EXT else '100 und 200 mm ab linker Blattkante'
        text(c,'Falzpositionen: '+folds,12,y+48,size=10)
    text(c,'Die Druckdatei enthält keine sichtbaren Falzlinien. Erst einen Duplex-Probedruck falten.',12,185,'Medium',11)
    text(c,'Bei manueller Papierzufuhr die Wenderichtung des eigenen Druckers beachten.',12,193,size=10.5)
    text(c,'Diese Anleitung ist ein separates Blatt und gehört nicht in die Broschüre.',12,201,size=10.5)

if __name__=='__main__':
    final=HERE/'Herzblut-Wickelfalz-A4-Duplex.pdf'
    c=canvas.Canvas(str(final),pagesize=(W,H),pageCompression=1)
    c.setViewerPreference('Duplex','DuplexFlipShortEdge')
    c.setViewerPreference('PrintScaling','None')
    for draw in [outside,inside]:draw(c);c.showPage()
    c.save()
    images=render_pdf(final,300,'Herzblut-Broschuere-300dpi')
    small=[]
    label_font=ImageFont.truetype('C:/Windows/Fonts/framd.ttf',24)
    for im,label in zip(images,['AUSSENSEITE  /  LASCHE - RÜCKSEITE - TITEL','INNENSEITE  /  TRÄNKEN - AUFZUCHT - STALL']):
        im.thumbnail((1485,1050))
        frame=Image.new('RGB',(1545,1120),'#DEDCD6');frame.paste(im,(30,55))
        ImageDraw.Draw(frame).text((30,16),label,font=label_font,fill=BLACK)
        small.append(frame)
    overview=Image.new('RGB',(1545,2240),'#DEDCD6')
    for i,im in enumerate(small):overview.paste(im,(0,i*1120))
    overview.save(HERE/'Broschuere-Uebersicht.png')
    instructions=HERE/'Druck-und-Falzplan.pdf'
    c=canvas.Canvas(str(instructions),pagesize=(W,H),pageCompression=1)
    guide(c);c.showPage();c.save()
    render_pdf(instructions,120,'Falzplan')
    reader=PdfReader(final)
    assert len(reader.pages)==2
    results={}
    for i,p in enumerate(reader.pages):
        assert abs(float(p.mediabox.width)-W)<.01 and abs(float(p.mediabox.height)-H)<.01
        assert 'HERZBLUT10' in p.extract_text()
        for dpi in [150,300]:
            doc=pdfium.PdfDocument(str(final));im=doc[i].render(scale=dpi/72).to_pil().convert('RGB')
            decoded=[r.text for r in zxingcpp.read_barcodes(im,formats=zxingcpp.BarcodeFormat.QRCode)]
            assert decoded==[LINK],(i,dpi,decoded)
            results[f'Seite {i+1}, {dpi} dpi']=decoded
    results['Falzbreiten außen']=[97,100,100]
    results['Falzbreiten innen']=[100,100,97]
    results['Motiv dpi']=821/(48/25.4)
    (HERE/'Pruefung.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print('A4 quer, 2 Druckseiten, 6 Felder, Falzbreiten und beide QR-Codes bei 150/300 dpi geprüft.')

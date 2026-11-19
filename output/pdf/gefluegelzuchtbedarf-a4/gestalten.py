"""Reproduzierbare A4-Anzeige. Ausführen mit Python + reportlab + pypdfium2 + Pillow.
Das Original-Logo wird ausschließlich proportional platziert, nicht verändert.
"""
from pathlib import Path
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'jtl-vorlagen/originale/Elegantes Geflügelzuchtbedarf-Logo mit Feder(1).png'
LOGO = HERE / 'original-logo.png'
if not LOGO.exists():
    shutil.copyfile(SOURCE, LOGO)
for name, file in [('Serif','BASKVILL.TTF'), ('Sans','GIL_____.TTF'), ('SansBold','GILB____.TTF')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts') / file)))
GREEN='#173E32'
CREAM='#F8F5EC'
GOLD='#A48A50'
INK='#233B32'
W,H=A4
URL='gefluegelzuchtbedarf.myshopify.com'

def box(c,x,y,w,h,color):
    c.setFillColor(HexColor(color)); c.rect(x*mm,H-(y+h)*mm,w*mm,h*mm,stroke=0,fill=1)

def line(c,x,y,x2,y2,color=GOLD,width=.55):
    c.setStrokeColor(HexColor(color)); c.setLineWidth(width)
    c.line(x*mm,H-y*mm,x2*mm,H-y2*mm)

def text(c,s,x,y,font='Sans',size=12,color=GREEN,align='left',tracking=0):
    c.setFillColor(HexColor(color))
    t=c.beginText();t.setFont(font,size);t.setCharSpace(tracking)
    sw=pdfmetrics.stringWidth(s,font,size)+max(0,len(s)-1)*tracking
    xx=x*mm-(sw/2 if align=='center' else sw if align=='right' else 0)
    t.setTextOrigin(xx,H-y*mm);t.textOut(s);c.drawText(t)
    assert xx >= 10*mm-0.1 and xx+sw <= W-10*mm+0.1, (s,xx,sw)

def logo(c,x,y,w):
    c.drawImage(ImageReader(str(LOGO)),x*mm,H-(y+w/2)*mm,w*mm,w/2*mm,mask='auto')

def setup(c):
    c.setTitle('Geflügelzuchtbedarf | Fachhandelsanzeige A4')
    c.setAuthor('Geflügelzuchtbedarf')
    c.setSubject('Vom Züchter für den Züchter')
    box(c,0,0,210,297,CREAM)

def assortment(c,y=226,center=105,color=INK,size=12):
    text(c,'Tränken und Tränkesysteme · Fütterung und Futterzubehör',center,y,size=size,color=color,align='center')
    text(c,'Brut- und Aufzuchtbedarf · Stall- und Geflügelzubehör',center,y+8,size=size,color=color,align='center')

def concept1(c):
    setup(c)
    logo(c,31,15,148)
    line(c,18,99,192,99)
    box(c,12,108,186,100,GREEN)
    text(c,'FÜR ZÜCHTER UND HOBBYHALTER',23,120,size=9,color='#D8C799',tracking=1.25)
    for s,y in [('Für die Zucht.',139),('Für den Stall.',155),('Für Ihr Geflügel.',171)]:
        text(c,s,23,y,'Serif',40,CREAM)
    line(c,23,182,41,182)
    text(c,'Das passende Zubehör für den Alltag mit Geflügel.',23,195,size=12.6,color=CREAM)
    assortment(c)
    line(c,18,246,192,246)
    text(c,'UNSER SORTIMENT ONLINE ENTDECKEN',105,259,size=9,tracking=1.0,align='center')
    text(c,URL,105,273,'SansBold',18,align='center')
    c.linkURL('https://'+URL,(18*mm,H-278*mm,192*mm,H-263*mm),relative=0,thickness=0)

def concept2(c):
    setup(c)
    box(c,12,12,14,273,GREEN)
    logo(c,49,20,128)
    text(c,'AUS DER PRAXIS. FÜR DIE PRAXIS.',40,110,size=9,tracking=1)
    for s,y in [('Zucht braucht',133),('Erfahrung.',151),('Und das richtige',176),('Zubehör.',194)]:
        text(c,s,40,y,'Serif',34)
    line(c,40,208,190,208)
    for s,y in [('Tränken und Tränkesysteme',219),('Fütterung und Futterzubehör',227),('Brut- und Aufzuchtbedarf',235),('Stall- und Geflügelzubehör',243)]:
        text(c,s,40,y,size=12)
    text(c,'Fachhandel für Züchter und Hobbyhalter',40,260,size=11)
    text(c,URL,40,276,'SansBold',14)

def concept3(c):
    setup(c)
    text(c,'FACHHANDEL FÜR GEFLÜGELZUCHT & HALTUNG',105,24,size=9,tracking=1,align='center')
    logo(c,31,39,148)
    line(c,88,126,122,126)
    text(c,'Mit Erfahrung',105,151,'Serif',38,align='center')
    text(c,'für Ihre Zucht.',105,167,'Serif',38,align='center')
    text(c,'Bedarf für Züchter und Hobbyhalter.',105,185,size=13,align='center')
    box(c,12,204,186,81,GREEN)
    text(c,'VON DER BRUT BIS ZUM STALL',105,219,size=9,color='#D8C799',tracking=1,align='center')
    assortment(c,235,color=CREAM,size=11)
    line(c,25,253,185,253)
    text(c,URL,105,270,'SansBold',17,CREAM,'center')

def render(path, dpi, target):
    doc=pdfium.PdfDocument(str(path))
    for i in range(len(doc)):
        im=doc[i].render(scale=dpi/72).to_pil()
        p=target if len(doc)==1 else target.with_name(target.stem+f'-{i+1}.png')
        im.save(p,dpi=(dpi,dpi))

if __name__=='__main__':
    final=HERE/'Werbeschild-A4.pdf'
    c=canvas.Canvas(str(final),pagesize=A4,pageCompression=1)
    concept1(c);c.showPage();c.save()
    concepts=HERE/'Drei-Designkonzepte.pdf'
    c=canvas.Canvas(str(concepts),pagesize=A4,pageCompression=1)
    for draw in [concept1,concept2,concept3]:
        draw(c);c.showPage()
    c.save()
    render(final,300,HERE/'Werbeschild-A4-300dpi.png')
    render(concepts,110,HERE/'Konzept.png')
    thumbs=[]
    for i,label in enumerate(['01 / FACHHANDEL','02 / EDITORIAL','03 / MARKENANZEIGE'],1):
        im=Image.open(HERE/f'Konzept-{i}.png').convert('RGB')
        im.thumbnail((490,694))
        frame=Image.new('RGB',(530,754),'#E5E4DE');frame.paste(im,((530-im.width)//2,45))
        ImageDraw.Draw(frame).text((20,16),label,fill=GREEN)
        thumbs.append(frame)
    overview=Image.new('RGB',(1590,754),'#E5E4DE')
    for i,im in enumerate(thumbs):overview.paste(im,(530*i,0))
    overview.save(HERE/'Konzeptvergleich.png')
    reader=PdfReader(final)
    assert len(reader.pages)==1
    p=reader.pages[0]
    assert abs(float(p.mediabox.width)-210*mm)<.01
    assert abs(float(p.mediabox.height)-297*mm)<.01
    extracted=p.extract_text()
    assert URL in extracted
    assert 'Für Ihr Geflügel.' in extracted
    print('A4, 1 Seite, URL und Text geprüft. Logo: %.1f dpi.'%(1774/(148/25.4)))
    print('Schriften:',list(p['/Resources']['/Font'].keys()))

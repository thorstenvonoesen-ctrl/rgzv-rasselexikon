"""Statische Seiten und Druckdateien erzeugen: python scripts/build.py."""
from pathlib import Path
import sys, html, json, re
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools/python'))
from breeds import BREEDS
from new_breeds import NEW_BREEDS
from breeds_series3 import SERIES3
ALL_BREEDS = BREEDS + NEW_BREEDS + SERIES3
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter, Transformation

BASE = 'https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/'
e = html.escape
for directory in ['qr-codes', 'schilder', 'druckboegen', 'tmp/pdfs']:
    (ROOT / directory).mkdir(parents=True, exist_ok=True)
font_dir = Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('Label', str(font_dir / 'arial.ttf')))
pdfmetrics.registerFont(TTFont('LabelBold', str(font_dir / 'arialbd.ttf')))

def shell(title, subtitle, content):
    return f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)} | Rasselexikon RGZV Hagen</title><meta name="description" content="{e(subtitle)}"><link rel="stylesheet" href="assets/style.css"></head>
<body><a class="skip" href="#inhalt">Zum Inhalt</a><header><div class="small">Digitales Rasselexikon</div><h1>{e(title)}</h1><p>{e(subtitle)}</p></header>
<main id="inhalt">{content}</main><footer><strong>RGZV Hagen und Umgebung seit 1903 e.V.</strong><br>Digitales Rasselexikon für Besucher unserer Ausstellungen</footer></body></html>
'''

def pages(selection):
    for b in selection:
        content = '<a class="back" href="index.html">← Zurück zum Rasselexikon</a><section class="info"><h2>Auf einen Blick</h2><div class="facts">'
        for key, value in [('Herkunft',b['origin']),('Tiergruppe',b['group'])]:
            content += f'<div class="fact"><strong>{key}</strong>{e(value)}</div>'
        if 'weights' in b:
            for key, value in [('Gewicht Hahn', b['weights'][0]), ('Gewicht Henne', b['weights'][1]), ('Eier', b['egg'])]:
                content += f'<div class="fact"><strong>{key}</strong>{e(value)}</div>'
        content += '</div>'
        if 'weights' in b:
            content += '<p>Gewichte sind Richtwerte für ausgewachsene Zuchttiere. Bruteier-Mindestgewichte bezeichnen die Untergrenze für die Zuchtauswahl, nicht das durchschnittliche Eigewicht. Legeleistungen sind Orientierungswerte und hängen auch von Alter, Linie und Haltung ab.</p>'
        content += '</section>'
        for key, title in [('history','Herkunft und Geschichte'),('appearance','Körperbau und Rassemerkmale'),('colors','Gefieder und Zeichnung'),('nature','Wesen und Eigenschaften'),('husbandry','Haltung und Alltag'),('use','Nutzung und Zuchtzweck'),('fact','Schon gewusst?')]:
            if key not in b: continue
            content += f'<section class="info"><h2>{title}</h2><p{chr(32)+"class=\"highlight\"" if key=="fact" else ""}>{e(b[key])}</p></section>'
        researched=b.get('researched','23. September 2026')
        content += f'<section class="info sources"><h2>Quellen und Weiterlesen</h2><p>Eigenständig formuliertes Besucherporträt auf Grundlage der folgenden Quellen. Recherchestand: {researched}. Genannte Farbenschläge sind Beispiele, keine vollständige Standardliste.</p><ul>'
        content += ''.join(f'<li><a href="{e(url)}">{e(label)}</a></li>' for label,url in b['sources'])
        content += f'</ul></section><a class="back" href="index.html">← Alle Rassen entdecken</a>'
        (ROOT / (b['slug']+'.html')).write_text(shell(b['name'],b['short'],content),encoding='utf-8')
    groups = [('huehner','Hühner','Großhuhn'),('zwerghuehner','Zwerghühner','Zwerghuhn'),('tauben','Tauben','Taube'),('wachteln','Wachteln','Wachtel')]
    content = f'<div class="info"><h2>Unsere Rassen entdecken</h2><p>Willkommen beim RGZV Hagen und Umgebung seit 1903 e.V. Lernen Sie {len(ALL_BREEDS)} Geflügelrassen kennen: ihre Herkunft, ihr Aussehen und ihre Besonderheiten.</p></div><nav class="groups" aria-label="Tiergruppen">'
    content += ''.join(f'<a href="#{slug}">{name}</a>' for slug,name,_ in groups)+'</nav>'
    for slug,name,group in groups:
        content += f'<section id="{slug}"><h2>{name}</h2><div class="cards">'
        for b in ALL_BREEDS:
            if b['group']==group:
                content += f'<article class="card"><span class="badge">{e(group)}</span><h3>{e(b["name"])}</h3><p>{e(b["short"])}</p><a class="button" href="{b["slug"]}.html" aria-label="{e(b["name"])}: Rasse entdecken">Rasse entdecken</a></article>'
        content += '</div></section>'
    (ROOT/'index.html').write_text(shell('Digitales Rasselexikon','RGZV Hagen und Umgebung seit 1903 e.V.',content),encoding='utf-8')

def wrap(text, font, size, width):
    # Hyphens are legal line breaks, retained at the end of a line.
    tokens = re.findall(r'[^\s-]+-?|[^\s]+',text)
    lines=[]; current=''
    for token in tokens:
        candidate=current+('' if current.endswith('-') or not current else ' ')+token
        if pdfmetrics.stringWidth(candidate,font,size)>width and current:
            lines.append(current); current=token
        else: current=candidate
    if current: lines.append(current)
    return lines

LAYOUT=[]
def label(b):
    url=BASE+b['slug']+'.html'
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=12,border=4)
    qr.add_data(url); qr.make(fit=True)
    qr.make_image(fill_color='black',back_color='white').save(ROOT/'qr-codes'/f'{b["slug"]}.png')
    c=canvas.Canvas(str(ROOT/'schilder'/f'{b["slug"]}.pdf'),pagesize=(90*mm,60*mm),invariant=1)
    c.setTitle(b['name']+' | Rasseschild 90 x 60 mm'); c.setAuthor('RGZV Hagen und Umgebung seit 1903 e.V.')
    c.setLineWidth(.35); c.roundRect(1.5*mm,1.5*mm,87*mm,57*mm,2.5*mm,stroke=1,fill=0)
    width=43*mm; size=13
    while True:
        lines=wrap(b['name'],'LabelBold',size,width)
        if len(lines)<=3 and all(pdfmetrics.stringWidth(x,'LabelBold',size)<=width for x in lines): break
        size-=.25
        assert size>=9
    c.setFont('LabelBold',size)
    for i,line in enumerate(lines): c.drawString(5*mm, (52*mm)-i*(size+2), line)
    name_bottom=52*mm-(len(lines)-1)*(size+2)
    meta=wrap(b['group']+' · '+b['origin'],'Label',7.3,width)
    meta_y=min(35*mm,name_bottom-12)
    c.setFont('Label',7.3)
    for i,line in enumerate(meta): c.drawString(5*mm,meta_y-i*9,line)
    assert meta_y-(len(meta)-1)*9>28*mm
    c.setFont('LabelBold',9); c.drawString(5*mm,24*mm,'Rasse entdecken')
    c.setFont('Label',8)
    c.drawString(5*mm,19.5*mm,'QR-Code scannen')
    c.drawString(5*mm,16*mm,'und mehr erfahren')
    c.setFont('Label',6.7)
    for i,line in enumerate(['RGZV Hagen und Umgebung','seit 1903 e.V.','Digitales Rasselexikon']): c.drawString(5*mm,(11-i*3)*mm,line)
    matrix=qr.get_matrix(); module=35*mm/len(matrix)
    # Full four-module white quiet zone is included in the 35 mm square.
    for row,values in enumerate(matrix):
        for col,on in enumerate(values):
            if on: c.rect(51*mm+col*module,12.5*mm+(len(matrix)-1-row)*module,module,module,stroke=0,fill=1)
    c.linkURL(url,(51*mm,12.5*mm,86*mm,47.5*mm),relative=0)
    c.showPage(); c.save()
    LAYOUT.append(dict(slug=b['slug'],url=url,name_lines=lines,font_size=size,qr_mm=[51,12.5,35,35],text_right_mm=48))

def sheets(selection, prefix, layout_name):
    placements=[]
    batches=(len(selection)+7)//8
    for batch in range(batches):
        overlay=ROOT/'tmp/pdfs'/f'marks-{batch}.pdf'
        c=canvas.Canvas(str(overlay),pagesize=A4,invariant=1)
        series='Ergänzung' if selection is NEW_BREEDS else 'Rasseschilder'
        c.setFont('Label',9); c.drawString(12*mm,284*mm,f'RGZV Hagen | {series} | Bogen {batch+1}/{batches}')
        c.setFont('Label',8); c.drawString(12*mm,278*mm,'90 x 60 mm je Schild | Tatsächliche Größe / 100 % | Keine Seitenanpassung')
        positions=[]
        for n,b in enumerate(selection[batch*8:batch*8+8]):
            x=(12+(n%2)*96)*mm; y=(210-(n//2)*65)*mm
            positions.append((b,x,y)); c.setLineWidth(.3)
            for px in [x,x+90*mm]:
                for py in [y,y+60*mm]:
                    dx=-1 if px==x else 1; dy=-1 if py==y else 1
                    c.line(px+dx*.5*mm,py,px+dx*2*mm,py)
                    c.line(px,py+dy*.5*mm,px,py+dy*2*mm)
        c.showPage(); c.save()
        page=PdfReader(overlay).pages[0]
        for b,x,y in positions:
            source=PdfReader(ROOT/'schilder'/f'{b["slug"]}.pdf').pages[0]
            page.merge_transformed_page(source,Transformation().translate(x,y))
            placements.append(dict(slug=b['slug'],sheet=batch+1,x_mm=x/mm,y_mm=y/mm,width_mm=90,height_mm=60,scale=1))
        writer=PdfWriter(); writer.add_page(page)
        with (ROOT/'druckboegen'/f'{prefix}-{batch+1:02}.pdf').open('wb') as f: writer.write(f)
    slugs={b['slug'] for b in selection}
    (ROOT/'scripts'/layout_name).write_text(json.dumps(dict(labels=[p for p in LAYOUT if p['slug'] in slugs],placements=placements),ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    modes=parser.add_mutually_exclusive_group()
    modes.add_argument('--reference-only',action='store_true')
    modes.add_argument('--extension-only',action='store_true',help='Nur die 20 neuen Rassen und die Übersicht erzeugen.')
    modes.add_argument('--series3-only',action='store_true',help='Nur fehlende Rassen der dritten Serie; keine A4-Bögen.')
    args=parser.parse_args()
    if args.reference_only:
        label(BREEDS[0])
        print('Ayam-Cemani-Referenz erzeugt.')
    elif args.series3_only:
        selection=[b for b in SERIES3 if not (ROOT/(b['slug']+'.html')).exists()]
        # Fail before writing if a supposedly missing page has existing print assets.
        for b in selection:
            assert not (ROOT/'schilder'/(b['slug']+'.pdf')).exists(), b['slug']
            assert not (ROOT/'qr-codes'/(b['slug']+'.png')).exists(), b['slug']
        if selection:
            pages(selection)
            for b in selection: label(b)
        (ROOT/'scripts/series3-created.json').write_text(json.dumps([b['slug'] for b in selection],indent=2),encoding='utf-8')
        print(f'{len(selection)} neue Seiten, QR-Codes und Schilder; keine A4-Bögen.')
    else:
        pages(NEW_BREEDS if args.extension_only else BREEDS[1:]+NEW_BREEDS)
        for b in (NEW_BREEDS if args.extension_only else ALL_BREEDS): label(b)
        if not args.extension_only: sheets(BREEDS,'rasseschild-bogen','layout.json')
        sheets(NEW_BREEDS,'rasseschild-erweiterung','layout-erweiterung.json')
        print('20 neue Rassen, QR-Codes und Schilder; 3 ergänzende A4-Bögen.' if args.extension_only else '41 Rassen, 41 QR-Codes, 41 Schilder, 6 A4-Bögen erzeugt.')

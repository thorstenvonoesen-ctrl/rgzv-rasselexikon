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
for directory in ['qr-codes', 'tmp/pdfs']:
    (ROOT / directory).mkdir(parents=True, exist_ok=True)
font_dir = Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('Label', str(font_dir / 'arial.ttf')))
pdfmetrics.registerFont(TTFont('LabelBold', str(font_dir / 'arialbd.ttf')))

def shell(title, subtitle, content):
    catalog_scripts = '<script src="assets/finder-data.js" defer></script><script src="assets/rassen-bestand.js" defer></script><script src="assets/rassen-gesamt.js" defer></script>' if title == 'Digitales Rasselexikon' else ''
    return f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)} | Rasselexikon RGZV Hagen</title><meta name="description" content="{e(subtitle)}"><link rel="stylesheet" href="assets/style.css">{catalog_scripts}</head>
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
    content = '<div class="info"><h2>Unsere Rassen entdecken</h2><p>Willkommen beim RGZV Hagen und Umgebung seit 1903 e.V. Lernen Sie <span data-rassen-anzahl>…</span> Geflügelrassen kennen: ihre Herkunft, ihr Aussehen und ihre Besonderheiten.</p></div><nav class="groups" aria-label="Tiergruppen">'
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

def label(b):
    """Kompatibilität: ausschließlich die zentrale A7-Sammlung verwenden."""
    from build_a7 import OUT,pdf
    qrpath=ROOT/'qr-codes'/(b['slug']+'.png')
    if not qrpath.exists():
        qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=12,border=4)
        qr.add_data(BASE+b['slug']+'.html');qr.make(fit=True)
        qr.make_image(fill_color='black',back_color='white').save(qrpath)
    target=OUT/'a7'/(b['slug']+'.pdf');target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists():pdf(target,[dict(name=b['name'],url=b['slug']+'.html')])

def sheets(selection=None,prefix=None,layout_name=None):
    """Alte Aufrufe erzeugen keine weiteren PDF-Sammlungen mehr."""
    from build_a7 import main
    main()

if __name__=='__main__':
    from build_a7 import main
    main()

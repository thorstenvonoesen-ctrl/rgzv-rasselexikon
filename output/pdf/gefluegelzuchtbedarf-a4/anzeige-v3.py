"""Bildgetragene Fachhandelsanzeige; Vektortext und unverändertes Original-Logo."""
from gestalten import *

PHOTO=HERE/'Hennenportraet.png'

def advertisement(c):
    setup(c)
    # Einzelmotiv, ohne Rahmen, Kästen oder Produktkacheln.
    c.drawImage(ImageReader(str(PHOTO)),92*mm,H-135*mm,106*mm,106*mm,mask='auto')
    text(c,'GEFLÜGEL IST LEIDENSCHAFT.',18,20,'Sans',9,GREEN,tracking=1)
    for s,y in [('Weil gute',49),('Zucht mit',64),('Fürsorge',79),('beginnt.',94)]:
        text(c,s,17,y,'Serif',38,GREEN)
    text(c,'Das Zubehör dazu',18,113,'Sans',12,GREEN)
    text(c,'finden Sie bei uns.',18,120,'Sans',12,GREEN)
    line(c,18,148,44,148,GOLD,.7)
    text(c,'Für das, was Ihnen am Herzen liegt.',18,165,'Serif',25,GREEN)
    text(c,'Ob Zucht oder Hobbyhaltung: Entdecken Sie Zubehör für',18,178,'Sans',13,GREEN)
    text(c,'Tränken und Fütterung, für Brut und Aufzucht sowie für',18,186,'Sans',13,GREEN)
    text(c,'Ihren Geflügelstall. Vom Züchter für den Züchter.',18,194,'Sans',13,GREEN)
    text(c,'Jetzt das Sortiment im Onlineshop entdecken.',18,210,'SansBold',13,GREEN)
    logo(c,50,223,110)
    text(c,URL,105,282,'SansBold',18,GREEN,'center')
    c.linkURL('https://'+URL,(15*mm,H-286*mm,195*mm,H-275*mm),relative=0,thickness=0)

if __name__=='__main__':
    target=HERE/'Werbeanzeige-Bildmotiv-A4.pdf'
    c=canvas.Canvas(str(target),pagesize=A4,pageCompression=1)
    advertisement(c);c.showPage();c.save()
    render(target,300,HERE/'Werbeanzeige-Bildmotiv-A4-300dpi.png')
    reader=PdfReader(target)
    assert len(reader.pages)==1 and URL in reader.pages[0].extract_text()
    im=Image.open(PHOTO)
    dpi=im.width/(106/25.4)
    assert dpi >= 300, f'Motivauflösung zu niedrig: {dpi:.1f} dpi'
    print(f'A4 geprüft. Motiv: {im.size}, effektiv {dpi:.1f} dpi. Logo unverändert.')

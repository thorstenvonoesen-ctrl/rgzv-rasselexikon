"""Überarbeitete Anzeige mit angebotsbezogener Hierarchie."""
from gestalten import *

def advertisement(c):
    setup(c)
    box(c,12,12,186,213,GREEN)
    text(c,'VOM ZÜCHTER FÜR DEN ZÜCHTER',24,28,'Sans',10,'#DBC995',tracking=1.1)
    text(c,'Alles für Ihre',23,55,'Serif',46,CREAM)
    text(c,'Geflügelzucht.',23,74,'Serif',46,CREAM)
    text(c,'Gut ausgestattet. Vom ersten Tag an.',24,92,'Sans',15,CREAM)
    line(c,24,106,186,106,'#A48A50',.7)
    text(c,'TRÄNKEN & TRÄNKESYSTEME',24,125,'SansBold',17,CREAM)
    text(c,'FÜTTERUNG & FUTTERZUBEHÖR',24,138,'SansBold',17,CREAM)
    text(c,'BRUT- & AUFZUCHTBEDARF',24,151,'SansBold',17,CREAM)
    text(c,'STALL- & GEFLÜGELZUBEHÖR',24,164,'SansBold',17,CREAM)
    text(c,'Für passionierte Züchter. Für Ihren Hobbybestand.',24,183,'Sans',12.4,CREAM)
    line(c,24,194,186,194,'#A48A50',.7)
    text(c,'Entdecken Sie das Zubehör für Ihren Stall.',24,208,'Serif',20,CREAM)
    logo(c,60,229,90)
    text(c,URL,105,282,'SansBold',18,align='center')
    c.linkURL('https://'+URL,(15*mm,H-286*mm,195*mm,H-275*mm),relative=0,thickness=0)

if __name__=='__main__':
    target=HERE/'Werbeanzeige-A4-V2.pdf'
    c=canvas.Canvas(str(target),pagesize=A4,pageCompression=1)
    advertisement(c);c.showPage();c.save()
    render(target,300,HERE/'Werbeanzeige-A4-V2-300dpi.png')
    reader=PdfReader(target)
    assert len(reader.pages)==1 and URL in reader.pages[0].extract_text()
    print('A4-Anzeige V2 gerendert. Original-Logo: 500 dpi.')

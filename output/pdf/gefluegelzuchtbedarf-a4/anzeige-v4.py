"""Neue Richtung: Schwarzweiß-Dokumentarmotiv, kräftige Grotesk, klare Anzeige."""
from gestalten import *
import hashlib
import zipfile

for name,file in [('Franklin','FRABK.TTF'),('FranklinHeavy','FRAHV.TTF'),('FranklinMedium','framd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
PAPER='#F5F3EE'
BLACK='#252A28'
RUST='#A8432F'
PHOTO=HERE/'Zuechterhaende-Schwarzweiss.png'

def advertisement(c, include_qr=False, include_discount=False):
    c.setTitle('Zucht ist Herzblut | Geflügelzuchtbedarf | A4')
    c.setAuthor('Geflügelzuchtbedarf')
    c.setSubject('Fachhandel für Züchter und Hobbyhalter')
    box(c,0,0,210,297,PAPER)
    im=Image.open(PHOTO)
    photo_w=min(86,im.width*25.4/300)
    photo_h=photo_w*im.height/im.width
    c.drawImage(ImageReader(str(PHOTO)),(198-photo_w)*mm,H-(12+photo_h)*mm,photo_w*mm,photo_h*mm)
    text(c,'FÜR ZÜCHTER & HOBBYHALTER',18,21,'FranklinMedium',8.7,BLACK,tracking=.65)
    text(c,'ZUCHT IST',16.8,44,'FranklinHeavy',44,BLACK)
    text(c,'HERZBLUT.',16.8,61,'FranklinHeavy',44,BLACK)
    box(c,18,73,13,1.4,RUST)
    text(c,'Wir haben',18,91,'FranklinMedium',23,BLACK)
    text(c,'das Zubehör.',18,101,'FranklinMedium',23,BLACK)
    for s,y in [('Von Tränken und Futterzubehör',122),
                ('über Brut- und Aufzuchtbedarf',129),
                ('bis zum Stallzubehör:',136),
                ('Entdecken Sie Ihren Fachhandel',147),
                ('für den Alltag mit Geflügel.',154)]:
        text(c,s,18,y,'Franklin',12,BLACK)
    text(c,'JETZT ONLINE ENTDECKEN',18,175,'FranklinHeavy',11,RUST,tracking=.3)
    # Das Leitmotiv wirkt als redaktionelle Signatur, nicht als Werbeversprechen.
    text(c,'VOM ZÜCHTER.',18,198,'FranklinHeavy',25,BLACK)
    text(c,'FÜR DEN ZÜCHTER.',18,210,'FranklinHeavy',25,BLACK)
    if include_discount:
        text(c,'10 % RABATT',156,195,'FranklinHeavy',22,RUST,'center')
        text(c,'HERZBLUT10',156,207,'FranklinHeavy',20,BLACK,'center')
        text(c,'Code beim Bezahlen eingeben.',156,216,'Franklin',9,BLACK,'center')
    line(c,18,224,192,224,BLACK,.65)
    logo(c,18,231,84)
    if include_qr:
        import sys
        sys.path.insert(0,str(ROOT/'.tools/python'))
        import qrcode
        qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,border=4,box_size=12)
        qr.add_data('https://'+URL);qr.make(fit=True)
        matrix=qr.get_matrix()
        side=32*mm
        module=side/len(matrix)
        x,y=162*mm,H-264*mm
        c.setFillColor(HexColor('#FFFFFF'));c.rect(x,y,side,side,stroke=0,fill=1)
        c.setFillColor(HexColor('#000000'))
        for row,values in enumerate(matrix):
            for col,dark in enumerate(values):
                if dark:
                    c.rect(x+col*module,y+side-(row+1)*module,module,module,stroke=0,fill=1)
        qr.make_image(fill_color='black',back_color='white').save(HERE/'Shop-QR.png')
        c.linkURL('https://'+URL,(x,y,x+side,y+side),relative=0,thickness=0)
        text(c,'DIREKT',119,245,'FranklinHeavy',12,BLACK)
        text(c,'ZUM SHOP.',119,252,'FranklinHeavy',12,BLACK)
        text(c,'Scannen und Sortiment entdecken.',119,272,'Franklin',9.8,BLACK)
    else:
        text(c,'IHR GEFLÜGEL.',119,243,'FranklinHeavy',12,BLACK)
        text(c,'UNSER FACHGEBIET.',119,250,'FranklinHeavy',12,BLACK)
        text(c,'Das Sortiment im Onlineshop.',119,265,'Franklin',10.5,BLACK)
    text(c,URL,105,283,'FranklinHeavy',18,BLACK,'center')
    c.linkURL('https://'+URL,(18*mm,H-287*mm,192*mm,H-277*mm),relative=0,thickness=0)
    return im.width/(photo_w/25.4)

if __name__=='__main__':
    final=HERE/'Werbeanzeige-Herzblut-A4.pdf'
    c=canvas.Canvas(str(final),pagesize=A4,pageCompression=1)
    dpi=advertisement(c);c.showPage();c.save()
    render(final,300,HERE/'Werbeanzeige-Herzblut-A4-300dpi.png')
    doc=PdfReader(final);p=doc.pages[0]
    assert len(doc.pages)==1
    assert abs(float(p.mediabox.width)-210*mm)<.01
    assert abs(float(p.mediabox.height)-297*mm)<.01
    assert URL in p.extract_text() and 'HERZBLUT.' in p.extract_text()
    assert dpi>=299.99
    if SOURCE.exists():
        assert hashlib.sha256(LOGO.read_bytes()).digest()==hashlib.sha256(SOURCE.read_bytes()).digest()
    print(f'A4, Shopadresse und Original-Logo geprüft. Motiv: {dpi:.1f} dpi.')

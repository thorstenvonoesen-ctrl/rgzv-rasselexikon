"""QR-Ergänzung der freigegebenen Herzblut-Anzeige; unabhängiger Scan der PDF."""
from pathlib import Path
import runpy
import sys
import json
import zipfile

HERE=Path(__file__).resolve().parent
base=runpy.run_path(str(HERE/'anzeige-v4.py'))
globals().update({k:v for k,v in base.items() if not k.startswith('__')})
sys.path.insert(0,str(ROOT/'.tools/python'))
import zxingcpp

if __name__=='__main__':
    final=HERE/'Werbeanzeige-Herzblut-A4-mit-QR.pdf'
    c=canvas.Canvas(str(final),pagesize=A4,pageCompression=1)
    advertisement(c,include_qr=True);c.showPage();c.save()
    preview=HERE/'Werbeanzeige-Herzblut-A4-mit-QR-300dpi.png'
    render(final,300,preview)
    expected='https://'+URL
    results={}
    for dpi in [150,300]:
        doc=pdfium.PdfDocument(str(final))
        im=doc[0].render(scale=dpi/72).to_pil().convert('RGB')
        decoded=[r.text for r in zxingcpp.read_barcodes(im,formats=zxingcpp.BarcodeFormat.QRCode)]
        assert decoded==[expected],(dpi,decoded)
        results[str(dpi)+' dpi']=decoded[0]
    p=PdfReader(final).pages[0]
    assert abs(float(p.mediabox.width)-210*mm)<.01
    assert abs(float(p.mediabox.height)-297*mm)<.01
    assert URL in p.extract_text()
    (HERE/'QR-Pruefung.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print('QR aus fertiger A4-PDF bei 150 und 300 dpi korrekt decodiert:',expected)

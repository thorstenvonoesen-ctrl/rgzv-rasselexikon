from pathlib import Path
import re
P=Path(__file__).parent
for f in (P/'analyse').rglob('*.txt'):
    s=f.read_text(encoding='utf8')
    print('\nFILE',f.name, f.parent.name)
    print('\n'.join(x for x in s.splitlines() if any(k in x for k in ['Identifier=Note','Identifier=Vat','Identifier=Total block','Identifier=Payment','@FontSize;','@PositionsColumnWidthVAT;'])))
    if 'Lieferanten' in f.parent.name:
        print('\n'.join(x for x in s.splitlines() if any(k in x for k in ['Identifier=','Position/','ObjectID='])))

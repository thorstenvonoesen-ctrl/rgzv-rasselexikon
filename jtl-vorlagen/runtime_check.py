"""Read-only List & Label 30 structural load, without JTL data provider."""
from pathlib import Path
import ctypes as C, os, json, zipfile
ROOT=Path(__file__).resolve().parent
runtime=Path(r'C:\Program Files\JTL-Software\JTL-Wawi')
cookie=os.add_dll_directory(str(runtime))
ll=C.WinDLL(str(runtime/'cxLL30.dll'))
ll.LlJobOpen.argtypes=[C.c_int]; ll.LlJobOpen.restype=C.c_int
ll.LlJobClose.argtypes=[C.c_int]
ll.LlProjectOpenW.argtypes=[C.c_int,C.c_uint,C.c_wchar_p,C.c_uint];ll.LlProjectOpenW.restype=C.c_int
ll.LlProjectClose.argtypes=[C.c_int];ll.LlProjectClose.restype=C.c_int
ll.LlDomGetProject.argtypes=[C.c_int,C.POINTER(C.c_void_p)];ll.LlDomGetProject.restype=C.c_int
result=[]
for folder in ['originale','output']:
    for f in sorted((ROOT/folder).glob('*.vlg')):
        with zipfile.ZipFile(f) as z:
            for name in z.namelist():
                if not name.endswith('.lst'):continue
                target=ROOT/'pruefung'/'runtime'/folder/f.stem/name
                target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(name))
                job=ll.LlJobOpen(0)
                row={'archive':f.name,'group':folder,'entry':name,'job_open_ok':job>0}
                if job>0:
                    # Read-only; no printer initialization; unknown JTL identifiers ignored.
                    code=ll.LlProjectOpenW(job,2,str(target),67108864|134217728)
                    row['project_open']=code
                    if code==0:
                        dom=C.c_void_p();row['dom_get_project']=ll.LlDomGetProject(job,C.byref(dom));row['dom_handle_present']=bool(dom.value)
                        ll.LlProjectClose(job)
                    ll.LlJobClose(job)
                result.append(row)
(ROOT/'pruefung/runtime-validierung.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
print(json.dumps(result,indent=2,ensure_ascii=False))

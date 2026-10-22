(() => {
  'use strict';
  const breeds=[...window.RASSE_BESTAND.entries].sort((a,b)=>a.name.localeCompare(b.name,'de'));
  const selected=new Set(), list=document.getElementById('schild-liste'),status=document.getElementById('druck-status');
  const search=document.getElementById('schild-suche');
  const buttons=['auswahl-a7','auswahl-a4'].map(id=>document.getElementById(id));
  const normal=s=>s.toLocaleLowerCase('de').replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  let busy=false;
  function update(){document.getElementById('auswahl-status').textContent=selected.size+' Schilder ausgewählt';buttons.forEach(b=>b.disabled=busy||!selected.size);}
  function render(){
    list.replaceChildren();
    for(const b of breeds.filter(b=>normal(b.name).includes(normal(search.value)))){
      const row=document.createElement('div');row.className='print-row';
      const label=document.createElement('label'),input=document.createElement('input');input.type='checkbox';input.checked=selected.has(b.url);input.value=b.url;
      input.addEventListener('change',()=>{input.checked?selected.add(b.url):selected.delete(b.url);update();});label.append(input,document.createTextNode(b.name));
      const link=document.createElement('a');link.href='output/pdf/a7/'+b.url.replace(/\.html$/,'.pdf');link.textContent='A7-PDF';link.download='';link.setAttribute('aria-label',b.name+': A7-PDF herunterladen');
      row.append(label,link);list.append(row);
    }
    if(!list.children.length)list.textContent='Keine passende Rasse gefunden.';
  }
  async function exportPDF(a4){
    busy=true;update();status.textContent='PDF wird zusammengestellt …';
    try{
      const {PDFDocument,degrees,rgb}=window.PDFLib, pdf=await PDFDocument.create(), mm=72/25.4;
      const selection=breeds.filter(b=>selected.has(b.url));
      let sheet;
      for(let i=0;i<selection.length;i++){
        const response=await fetch('output/pdf/a7/'+selection[i].url.replace(/\.html$/,'.pdf'));
        if(!response.ok)throw Error('Ein Schild konnte nicht geladen werden.');
        const source=await PDFDocument.load(await response.arrayBuffer());
        if(a4){
          if(i%8===0)sheet=pdf.addPage([210*mm,297*mm]);
          const embedded=await pdf.embedPage(source.getPage(0)),cell=i%8;
          sheet.drawPage(embedded,{x:(cell%2)*105*mm,y:((4-Math.floor(cell/2))*74+.5)*mm,rotate:degrees(-90)});
        }else{const [copy]=await pdf.copyPages(source,[0]);pdf.addPage(copy);}
      }
      if(a4)for(const page of pdf.getPages()){
        const line=(x1,y1,x2,y2)=>page.drawLine({start:{x:x1*mm,y:y1*mm},end:{x:x2*mm,y:y2*mm},thickness:.25,color:rgb(.63,.67,.64)});
        line(105,.5,105,296.5);[74.5,148.5,222.5].forEach(y=>line(0,y,210,y));
      }
      pdf.catalog.getOrCreateViewerPreferences().setPrintScaling(window.PDFLib.PrintScaling.None);
      const url=URL.createObjectURL(new Blob([await pdf.save()],{type:'application/pdf'}));
      const link=document.createElement('a');link.href=url;link.download='rgzv-rasseschilder-'+(a4?'a4':'a7')+'.pdf';link.click();setTimeout(()=>URL.revokeObjectURL(url),60000);
      status.textContent='PDF mit '+selection.length+' Schildern erstellt. Bitte in tatsächlicher Größe drucken.';
    }catch(error){status.textContent='PDF konnte nicht erstellt werden: '+error.message;}
    finally{busy=false;update();}
  }
  search.addEventListener('input',render);
  document.getElementById('alle-waehlen').addEventListener('click',()=>{breeds.forEach(b=>selected.add(b.url));render();update();});
  document.getElementById('keine-waehlen').addEventListener('click',()=>{selected.clear();render();update();});
  buttons[0].addEventListener('click',()=>exportPDF(false));buttons[1].addEventListener('click',()=>exportPDF(true));
  render();update();
})();

const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root=path.resolve(__dirname,'..');
const server=http.createServer((req,res)=>{
 const name=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
 const target=path.resolve(root,'.'+(name==='/'?'/index.html':name));
 if(!target.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}
 fs.readFile(target,(err,data)=>{if(err){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',({'.js':'text/javascript','.json':'application/json','.html':'text/html; charset=utf-8','.css':'text/css','.pdf':'application/pdf'})[path.extname(target)]||'application/octet-stream');res.end(data);});
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const base='http://127.0.0.1:'+server.address().port+'/';
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.clock.install({time:new Date('2026-10-22T12:00:00Z')});
  let layoutChecks=0;
  for(const width of [320,390,768,1280]){
   await page.setViewportSize({width,height:900});
   for(const file of ['index.html','ausstellung.html','rasse-finder.html','schilder-drucken.html']){
    await page.goto(base+file);await page.waitForLoadState('networkidle');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,file+' '+width);layoutChecks++;
   }
  }
  await page.goto(base);await page.waitForLoadState('networkidle');
  const raw=fs.readFileSync('assets/finder-data.js','utf8');
  const expected=JSON.parse(raw.split('window.FINDER_BREEDS = ')[1].trim().replace(/;$/,'')).filter(b=>['Großhuhn','Zwerghuhn','Taube','Wachtel','Gans','Ente'].includes(b.group)).length;
  assert.equal(await page.locator('#rassen-gesamt').innerText(),String(expected));
  assert.deepEqual((await page.locator('main h2').allTextContents()).slice(0,6),['1. Offene Rassetaubenschau 2027','Rassen entdecken','Welche Rasse passt zu mir?','Willkommen in der Welt des Rassegeflügels','Mehr vom RGZV Hagen','Alle Rassen im Überblick']);
  assert.equal(await page.locator('main').innerText().then(t=>t.includes('Lokalschau 2026')),false);
  assert.equal(await page.locator('#ausstellung-start a').count(),0);
  await page.locator('#lexikon-suche').fill('Kraienkoeppe');assert.equal(await page.locator('.cards .card:visible').count(),2);
  await page.locator('#lexikon-suche').fill('');
  fs.mkdirSync('tmp/project',{recursive:true});await page.setViewportSize({width:390,height:844});await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:'tmp/project/start-mobile.png',fullPage:false});
  await page.clock.setSystemTime(new Date('2027-01-31T12:00:00Z'));await page.reload();await page.waitForLoadState('networkidle');assert.equal(await page.locator('#ausstellung-start').isVisible(),false);
  await page.goto(base+'ausstellung.html');await page.waitForLoadState('networkidle');assert.equal(await page.locator('#kaefig-suche').count(),0);
  await page.clock.setSystemTime(new Date('2027-01-30T12:00:00Z'));
  const config=JSON.parse(fs.readFileSync('assets/veranstaltungen.json','utf8'));config.veranstaltungen[0].erkundungFreigegeben=true;
  const id=config.aktuelleVeranstaltung;
  await page.route('**/assets/veranstaltungen.json',r=>r.fulfill({json:config}));
  const data={veranstaltungId:id,rassen:[{name:'Orientalische Roller',slug:'orientalische-roller.html',kaefige:[{von:11,bis:15}]},{name:'Deutsche Modeneser',slug:'deutsche-modeneser.html',kaefige:[{von:20,bis:25}]}]};
  await page.route('**/assets/ausstellungen/'+id+'.json',r=>r.fulfill({json:data}));
  await page.goto(base);await page.waitForLoadState('networkidle');await page.getByRole('link',{name:'Ausstellung erkunden',exact:true}).click();
  await page.locator('#kaefig-suche').fill('12');assert.equal(await page.locator('.ausstellung-cards .card').count(),1);assert.equal(await page.locator('.ausstellung-cards h3').innerText(),'Orientalische Roller');
  await page.locator('.ausstellung-cards input[type=checkbox]').check();assert.equal(await page.locator('progress').getAttribute('value'),'1');
  await page.locator('#kaefig-suche').fill('999');assert.equal(await page.locator('.ausstellung-cards .card').count(),0);
  // Alte oder falsch zugeordnete Belegung darf niemals sichtbar werden.
  data.veranstaltungId='lokalschau-2026';await page.reload();await page.waitForLoadState('networkidle');assert.equal(await page.locator('#kaefig-suche').count(),0);
  await page.goto(base+'rasse-finder.html');
  for(let step=0;step<8;step++){
   await page.locator('#finder-content .finder-choice').first().click();
   const next=page.getByRole('button',{name:'Weiter',exact:true});if(await next.count() && await next.isEnabled())await next.click();
  }
  assert.equal(await page.locator('.finder-results .card').count(),3);
  await page.goto(base+'schilder-drucken.html');
  await page.locator('#schild-suche').fill('Kraienkoeppe');assert.equal(await page.locator('.print-row').count(),2);
  await page.locator('#schild-suche').fill('');
  const choices=page.locator('.print-row input');for(let i=0;i<8;i++)await choices.nth(i).check();
  for(const type of ['a7','a4']){
   const download=page.waitForEvent('download');await page.locator('#auswahl-'+type).click();const result=await download;
   await result.saveAs('tmp/project/auswahl-'+type+'.pdf');
   assert.match(await page.locator('#druck-status').innerText(),/8 Schildern erstellt/);
  }
  await page.screenshot({path:'tmp/project/drucken-mobile.png',fullPage:false});
  await page.locator('#alle-waehlen').click();assert.equal(await page.locator('#auswahl-status').innerText(),expected+' Schilder ausgewählt');
  let newPages=0,newSearches=0;
  if(fs.existsSync('scripts/breeds_series5.json')){
   const newBreeds=JSON.parse(fs.readFileSync('scripts/breeds_series5.json','utf8'));
   for(const b of newBreeds)assert.equal(await page.locator(`.print-row input[value="${b.slug}.html"]`).count(),1);
   // Zusätzlich eine echte Auswahl ausschließlich neuer Rassen herunterladen.
   await page.locator('#keine-waehlen').click();
   for(const b of newBreeds.slice(0,8))await page.locator(`.print-row input[value="${b.slug}.html"]`).check();
   for(const type of ['a7','a4']){
    const download=page.waitForEvent('download');await page.locator('#auswahl-'+type).click();await (await download).saveAs('tmp/project/neue-rassen-'+type+'.pdf');
    assert.match(await page.locator('#druck-status').innerText(),/8 Schildern erstellt/);
   }
   for(const width of [320,1280]){
    await page.setViewportSize({width,height:900});
    for(const b of newBreeds){
     await page.goto(base+b.slug+'.html');assert.equal(await page.locator('h1').innerText(),b.name);
     assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,b.name+' '+width);newPages++;
     if(width===320){
      await page.locator('a.back').first().click();await page.locator('#lexikon-suche').fill(b.name);
      assert.equal(await page.locator(`.cards a[href="${b.slug}.html"]`).isVisible(),true,b.name);newSearches++;
     }
    }
   }
   await page.goto(base+'bergische-zwerg-schlotterkaemme.html');await page.setViewportSize({width:390,height:844});await page.screenshot({path:'tmp/project/neue-rasse-mobile.png',fullPage:true});
  }
  assert.deepEqual(errors,[]);
  fs.writeFileSync('scripts/project-browser-results.json',JSON.stringify({layoutChecks,viewports:[320,390,768,1280],count:expected,eventOrder:true,expiredHidden:true,notReleasedHidden:true,wrongEventBlocked:true,cageSearch:true,breedSearch:true,finder:true,selectionPDFs:['a7','a4'],newPages,newSearches,errors},null,2));
  console.log('Startseite, Ablauf/Freigabe, Käfigsuche, Finder und beide PDF-Auswahlen erfolgreich geprüft.');
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});

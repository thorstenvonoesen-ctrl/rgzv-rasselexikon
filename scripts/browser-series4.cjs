const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage();const errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const added=['ko-shamo','ohiki','serama','zwerg-brakel','zwerg-kraienkoeppe'];
 let checks=0;
 for(const width of [320,390,768,1280]){
  await page.setViewportSize({width,height:844});
  for(const slug of ['index',...added,'rasse-finder']){
   await page.goto(pathToFileURL(path.resolve(slug+'.html')).href);
   if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Überlauf '+slug+' '+width);
   if(await page.locator('h1').count()!==1)throw Error('H1 '+slug);
   checks++;
  }
 }
 await page.goto(pathToFileURL(path.resolve('index.html')).href);
 if(await page.locator('#rassen-gesamt').innerText()!=='193')throw Error('Zähler');
 for(const slug of added){
  await page.locator(`a[href="${slug}.html"]`).click();
  if(await page.locator('h1').innerText()==='')throw Error('Navigation');
  await page.locator('a.back').first().click();
 }
 if(errors.length)throw Error(errors.join('\n'));
 fs.writeFileSync('scripts/series4-browser-results.json',JSON.stringify({viewportChecks:checks,newPageRoundTrips:5,counter:193,pageErrors:errors},null,2));
 await browser.close();console.log('28 Layoutprüfungen, fünf Navigationen und Gesamtzähler bestanden.');
})().catch(e=>{console.error(e);process.exit(1)});

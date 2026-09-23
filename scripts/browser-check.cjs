// PLAYWRIGHT_MODULE may point at the bundled Playwright installation.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
(async () => {
 const browser = await chromium.launch({channel:'msedge',headless:true});
 const page = await browser.newPage(); const failures=[]; const errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const files=fs.readdirSync('.').filter(f=>f.endsWith('.html'));
 for(const width of [320,390,768,1280]) {
  await page.setViewportSize({width,height:844});
  for(const file of files){
   await page.goto(pathToFileURL(path.resolve(file)).href);
   const result=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,h1:document.querySelectorAll('h1').length,broken:[...document.images].some(i=>!i.complete||!i.naturalWidth)}));
   if(result.overflow||result.h1!==1||result.broken)failures.push({width,file,...result});
   if(width===390&&['index.html','antwerpener-bartzwerge.html','deutsche-lachshuehner.html','vorwerkhuehner.html'].includes(file))await page.screenshot({path:`tmp/${file}-mobile.png`,fullPage:file!=='index.html'});
   if(width===1280&&['index.html','antwerpener-bartzwerge.html'].includes(file))await page.screenshot({path:`tmp/${file}-desktop.png`,fullPage:false});
  }
 }
 await page.goto(pathToFileURL(path.resolve('index.html')).href);
 const links=await page.locator('.card a').evaluateAll(as=>as.map(a=>a.href));
 for(const link of links){await page.goto(link);if(!await page.locator('h1').innerText())failures.push(link);await page.locator('a[href="index.html"]').first().click();if(!page.url().endsWith('/index.html'))failures.push('return link');}
 const report={pages:files.length,viewports:[320,390,768,1280],navigations:links.length,failures,errors};
 fs.writeFileSync('scripts/browser-results.json',JSON.stringify(report,null,2));
 await browser.close();console.log(report);if(failures.length||errors.length)process.exitCode=1;
})();

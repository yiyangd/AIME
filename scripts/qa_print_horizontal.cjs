/* Check actual KaTeX fragments in the saved, fully rendered print HTML. */
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {pathToFileURL}=require('node:url');
const deps=path.join(os.homedir(),'.cache','codex-runtimes','codex-primary-runtime','dependencies','node','node_modules');
const {chromium}=require(path.join(deps,'playwright'));
const browserRoot=path.join(os.homedir(),'AppData','Local','ms-playwright');
const exe=fs.readdirSync(browserRoot).filter(x=>x.startsWith('chromium_headless_shell-')).sort().reverse().map(x=>path.join(browserRoot,x,'chrome-headless-shell-win64','chrome-headless-shell.exe')).find(x=>fs.existsSync(x));
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:exe});
 try{
  const reports=[];
  for(const file of process.argv.slice(2)){
   const page=await browser.newPage();await page.goto(pathToFileURL(path.resolve(file)).href);await page.evaluate(()=>document.fonts.ready);
   const r=await page.evaluate(()=>{
    const failures=[];let math=0;
    for(const body of document.querySelectorAll('.content')){
     const b=body.getBoundingClientRect();
     for(const el of body.querySelectorAll('.katex,.katex .base')){
      math++;for(const r of el.getClientRects())if(r.left<b.left-2||r.right>b.right+2)failures.push({page:body.closest('.page').querySelector('.footer').textContent,text:el.textContent.slice(0,120),left:r.left-b.left,right:r.right-b.right});
     }
    }
    return {pages:document.querySelectorAll('.page').length,math_fragments:math,horizontal_overflows:failures};
   });
   reports.push({file,...r});await page.close();
  }
  console.log(JSON.stringify(reports,null,2));
  if(reports.some(r=>r.horizontal_overflows.length))process.exitCode=1;
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});

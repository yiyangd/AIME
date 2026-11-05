/* Native local KaTeX typesetting and measured A4 pagination for build_print.py. */
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
let playwright;
try {playwright=require('playwright');}
catch {playwright=require(process.env.AIME_PLAYWRIGHT_MODULE||path.join(require('node:os').homedir(),'.cache','codex-runtimes','codex-primary-runtime','dependencies','node','node_modules','playwright'));}
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const u=(p)=>pathToFileURL(p).href;
const base=spec.asset_root;
const html=`<!doctype html><html><head><meta charset="utf-8"><title>AIME ${spec.kind}</title>
<link rel="stylesheet" href="${u(path.join(base,'katex/katex.min.css'))}">
<style>
@page {size:A4;margin:0}*{box-sizing:border-box}html,body{margin:0;padding:0;color:#193850;font-family:Arial,'Microsoft YaHei',sans-serif;font-size:12pt;line-height:1.5}
.page{width:210mm;height:297mm;position:relative;padding:14mm 14mm 17mm;page-break-after:always;break-after:page;background:white;overflow:hidden}.page:last-child{break-after:auto;page-break-after:auto}
.header{height:29mm;border-bottom:.25mm solid #dce5ea;margin-bottom:6mm}.header .eyebrow{font-size:8pt;color:#e77835;font-weight:700;letter-spacing:1.2px;margin-bottom:3mm}.header h1{font-size:16pt;line-height:1.15;margin:0 0 2mm;color:#163e65}.subtitle{font-size:10.5pt;color:#647684}.content{height:223mm}.label{font-size:9pt;color:#447aa2;font-weight:700;margin-bottom:5mm}.block{margin:0 0 4mm;overflow-wrap:anywhere}.block.zh{font-size:11.5pt;line-height:1.6}.statement{font-size:12.5pt;line-height:1.6}.method-title{font-size:15pt;font-weight:700;color:#163e65}.example{padding:4mm;background:#edf4f8;border-left:1mm solid #e77835;font-size:12.5pt}.step{font-size:12.5pt;line-height:1.6;margin-bottom:5mm}.tip{font-size:11pt;padding:3mm;border:.25mm solid #dce5ea}.practice{font-size:9.5pt;color:#447aa2;border-top:.25mm solid #dce5ea;padding-top:4mm;line-height:1.7}.source-note{font-size:8pt;color:#647684;margin-bottom:2mm}.source-note a{color:#447aa2}.answer{font-size:16pt;color:#163e65;font-weight:700;border-bottom:.5mm solid #e77835;padding-bottom:3mm;margin-bottom:6mm}.working{font-size:10pt;color:#647684;border-top:.25mm solid #dce5ea;padding-top:5mm;margin-top:9mm}.footer{position:absolute;bottom:8mm;left:14mm;right:14mm;border-top:.2mm solid #dce5ea;padding-top:2mm;font-size:8pt;color:#647684;display:flex;justify-content:space-between}.diagram svg{display:block;max-width:100%;max-height:65mm;margin:auto}.katex{font-size:1.06em}.katex-display{overflow:visible;margin:.6em 0}.katex-error{color:red}
</style><script src="${u(path.join(base,'katex/katex.min.js'))}"></script><script src="${u(path.join(base,'katex/contrib/auto-render.min.js'))}"></script></head><body><main id="pages"></main><div id="measure" style="position:absolute;left:-10000px;top:0;width:182mm"></div></body></html>`;
fs.mkdirSync(path.dirname(spec.html),{recursive:true});fs.writeFileSync(spec.html,html);
(async()=>{
 const home=require('node:os').homedir();
 const browserRoot=path.join(home,'AppData','Local','ms-playwright');
 const installed=fs.existsSync(browserRoot)?fs.readdirSync(browserRoot).filter(x=>x.startsWith('chromium_headless_shell-')).sort().reverse():[];
 const found=installed.map(x=>path.join(browserRoot,x,'chrome-headless-shell-win64','chrome-headless-shell.exe')).find(x=>fs.existsSync(x));
 const executablePath=process.env.AIME_CHROMIUM||found;
 const browser=await playwright.chromium.launch({headless:true,...(executablePath?{executablePath}:{} )});
 try {
  const page=await browser.newPage({viewport:{width:1000,height:1200},deviceScaleFactor:1});
  await page.goto(u(spec.html));await page.evaluate(()=>document.fonts.ready);
  const result=await page.evaluate(async(spec)=>{
   const root=document.querySelector('#pages');const meas=document.querySelector('#measure');let number=0;const metadata=[];const mathErrors=[];
   const render=(el)=>renderMathInElement(el,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false},{left:'\\[',right:'\\]',display:true}],preProcess:math=>math.replace(/\),\s*\(/g,'),\\allowbreak ('),throwOnError:true,errorCallback:(msg,err)=>mathErrors.push({msg,error:String(err)})});
   function newPage(unit,continued=false){
    number++;const el=document.createElement('section');el.className='page';
    const head=document.createElement('header');head.className='header';
    const eye=document.createElement('div');eye.className='eyebrow';eye.textContent='STEMHUB / AIME '+spec.date_range;
    const h=document.createElement('h1');h.textContent=unit.header;
    const sub=document.createElement('div');sub.className='subtitle';sub.textContent=unit.subtitle;
    head.append(eye,h,sub);el.append(head);
    const body=document.createElement('div');body.className='content';
    const label=document.createElement('div');label.className='label';label.textContent=unit.label+(continued?'  (continued / 续)':'');body.append(label);el.append(body);
    const foot=document.createElement('footer');foot.className='footer';const f1=document.createElement('span');f1.textContent='AIME / '+spec.kind.replaceAll('_',' ');const f2=document.createElement('span');f2.textContent=String(number);foot.append(f1,f2);el.append(foot);root.append(el);
    const rec={body_page:number,unit_id:unit.id,section_id:unit.section_id,...(unit.method_id?{method_id:unit.method_id}:{}),continued,block_count:0,max_bottom_px:0};metadata.push(rec);return {el,body,rec};
   }
   for(const unit of spec.units){
    let current=newPage(unit);let first=true;
    for(let blockIndex=0;blockIndex<unit.blocks.length;blockIndex++){
     const markup=unit.blocks[blockIndex];
     meas.innerHTML=markup;const b=meas.firstElementChild;render(b);current.body.append(b);await document.fonts.ready;
     // A section/procedure/solution heading belongs with at least its next block.
     if(!first&&b.classList.contains('method-title')&&blockIndex+1<unit.blocks.length){
      const holder=document.createElement('div');holder.innerHTML=unit.blocks[blockIndex+1];const probe=holder.firstElementChild;render(probe);current.body.append(probe);await document.fonts.ready;
      const keepHere=probe.getBoundingClientRect().bottom<=current.body.getBoundingClientRect().bottom+0.5;probe.remove();
      if(!keepHere){b.remove();current=newPage(unit,true);current.body.append(b);}
     }
     const fits=()=>b.getBoundingClientRect().bottom<=current.body.getBoundingClientRect().bottom+0.5;
     if(!fits()){
      current.body.removeChild(b);
      if(first)throw new Error('An individual block exceeds an A4 page: '+unit.id+' '+b.textContent.slice(0,80));
      current=newPage(unit,true);current.body.append(b);
      if(!fits())throw new Error('An individual block exceeds an A4 continuation page: '+unit.id+' '+b.textContent.slice(0,80));
     }
     current.rec.block_count++;current.rec.max_bottom_px=Math.max(current.rec.max_bottom_px,b.getBoundingClientRect().bottom-current.el.getBoundingClientRect().top);first=false;
     // Display mathematics must stay within its available horizontal area.
     for(const math of b.querySelectorAll('.katex-display'))if(math.scrollWidth>math.clientWidth+2)throw new Error('Display math too wide: '+unit.id+' '+math.textContent.slice(0,100));
     const bounds=current.body.getBoundingClientRect();
     for(const math of b.querySelectorAll('.katex,.katex .base'))for(const r of math.getClientRects())if(r.left<bounds.left-2||r.right>bounds.right+2)throw new Error('Inline math too wide: '+unit.id+' '+math.textContent.slice(0,120));
    }
   }
   for(const body of root.querySelectorAll('.content'))if(body.lastElementChild?.classList.contains('method-title'))throw new Error('Orphan textbook heading at page end');
   meas.remove();return {pages:metadata,overflow_check:'passed measured A4 content bounds and heading continuation',math_errors:mathErrors};
  },spec);
  await page.evaluate(()=>document.fonts.ready);
  if(result.math_errors.length)throw new Error('KaTeX errors: '+JSON.stringify(result.math_errors));
  await page.pdf({path:spec.output,format:'A4',printBackground:true,preferCSSPageSize:true,margin:{top:0,right:0,bottom:0,left:0}});
  fs.writeFileSync(spec.metadata,JSON.stringify(result,null,2));
  fs.writeFileSync(spec.html,await page.content());
  console.log(JSON.stringify({kind:spec.kind,pages:result.pages.length,math_errors:result.math_errors.length}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});

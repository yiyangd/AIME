const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {pathToFileURL}=require('node:url');
const deps=path.join(os.homedir(),'.cache','codex-runtimes','codex-primary-runtime','dependencies','node','node_modules');
const {chromium}=require(path.join(deps,'playwright'));
const sharp=require(path.join(deps,'sharp'));
const root=path.resolve(__dirname,'..'),out=path.join(root,'tmp','knowledge-diagrams-qa');fs.mkdirSync(out,{recursive:true});
const diagrams=JSON.parse(fs.readFileSync(path.join(root,'data','knowledge_diagrams.json'),'utf8'));
const browsers=path.join(os.homedir(),'AppData','Local','ms-playwright');
const exe=fs.readdirSync(browsers).filter(x=>x.startsWith('chromium_headless_shell-')).sort().reverse().map(x=>path.join(browsers,x,'chrome-headless-shell-win64','chrome-headless-shell.exe')).find(x=>fs.existsSync(x));
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:exe});const tiles=[];const reports=[];
 try{
  const page=await browser.newPage({viewport:{width:640,height:340},deviceScaleFactor:1});
  for(const [id,d] of Object.entries(diagrams)){
   await page.goto(pathToFileURL(path.join(root,d.diagram_path)).href);await page.evaluate(()=>document.fonts.ready);
   const bounds=await page.evaluate(()=>{const svg=document.querySelector('svg'),box=svg.viewBox.baseVal;return [...svg.querySelectorAll('text')].map(x=>({text:x.textContent,box:x.getBBox()})).filter(x=>x.box.x<0||x.box.y<0||x.box.x+x.box.width>box.width||x.box.y+x.box.height>box.height).map(x=>x.text)});
   if(bounds.length)throw new Error(id+' text outside viewBox: '+bounds);
   const png=path.join(out,id+'.png');await page.screenshot({path:png});
   const tile=await sharp(png).resize(640,340,{fit:'contain',background:'#ffffff'}).png().toBuffer();tiles.push({input:tile,left:((tiles.length)%2)*640,top:Math.floor(tiles.length/2)*340});
   reports.push({method_id:id,svg:d.diagram_path,label_bounds:'pass',construction_check:d.construction_check});
  }
  await sharp({create:{width:1280,height:Math.ceil(tiles.length/2)*340,channels:3,background:'#ffffff'}}).composite(tiles).png().toFile(path.join(out,'contact-sheet.png'));
  fs.writeFileSync(path.join(out,'qa-receipt.json'),JSON.stringify({diagrams:reports,visual_review:'pending'},null,2));
  console.log('Rendered '+reports.length+' diagrams with all labels inside their viewBoxes.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});

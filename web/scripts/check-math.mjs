import fs from 'node:fs';
import katex from '../public/vendor/katex/katex.mjs';
const raw=JSON.parse(fs.readFileSync('src/data/workbook.json','utf8'));
let formulas=0;const errors=[];
function scan(value,path='content'){
 if(typeof value==='string'){
  if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(value))errors.push({path,error:'Control character in text'});
  for(const m of value.matchAll(/\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g)){
   formulas++;try{katex.renderToString(m[1]??m[2],{throwOnError:true,strict:'ignore',displayMode:!!m[1]});}
   catch(e){errors.push({path,formula:m[1]??m[2],error:e.message});}
  }
 }else if(Array.isArray(value))value.forEach((x,i)=>scan(x,`${path}[${i}]`));
 else if(value&&typeof value==='object')Object.entries(value).forEach(([k,v])=>scan(v,`${path}.${k}`));
}
scan(raw);fs.mkdirSync('reports',{recursive:true});fs.writeFileSync('reports/math-validation.json',JSON.stringify({formulas,errors},null,2));
console.log(JSON.stringify({formulas,errors:errors.length,firstErrors:errors.slice(0,12)}));if(errors.length)process.exitCode=1;

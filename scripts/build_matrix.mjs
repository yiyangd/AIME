import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const load=async f=>JSON.parse(await fs.readFile(path.join(root,f),'utf8'));
const [qs,tax,coverage]=await Promise.all([load('data/questions.json'),load('data/taxonomy.json'),load('output/qa/coverage.json')]);
if(!qs.length)throw Error('No authored questions');
const out=path.join(root,'output/matrix');await fs.mkdir(out,{recursive:true});
const qa=path.join(root,'output/qa/matrix');await fs.mkdir(qa,{recursive:true});
const wb=Workbook.create();
const names=['Matrix','Statistics','Problems','Tags','Taxonomy','Review'];
const sheets=Object.fromEntries(names.map(n=>[n,wb.worksheets.add(n)]));
const cat=new Map(tax.categories.map(c=>[c.id,c]));const sub=new Map(tax.subtypes.map(s=>[s.id,s]));
const col=n=>{let s='';for(;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function base(sh,rows,cols,title){
  sh.showGridLines=false;
  const area=sh.getRange(`A1:${col(cols)}${rows}`);
  area.format.font={name:'Arial',size:11,color:'#172554'};
  area.format.verticalAlignment='center';area.format.rowHeight=24;
  sh.getRange(`A1:${col(Math.min(4,cols))}1`).merge();sh.getRange('A1').values=[[title]];
  sh.getRange('A1').format.font={name:'Arial',size:17,bold:true,color:'#173d69'};
  sh.getRange('A1').format.rowHeight=34;
  sh.getRange(`A2:${col(Math.min(4,cols))}2`).merge();
  sh.getRange('A2').values=[['2000–2026 · AIME I/II · 主考唯一 / Unique primary']];
  sh.getRange('A2').format.font={name:'Arial',size:10,color:'#64748b'};
  sh.getRange(`A4:${col(cols)}4`).format={fill:'#173d69',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},rowHeight:36,wrapText:true,verticalAlignment:'center',horizontalAlignment:'center'};
  sh.freezePanes.freezeRows(4);
}
const primary=(q)=>sub.get(q.primary.subtype_id);
const label=(code)=>{const s=sub.get(code);return `${code} ${s.name_zh}\n${s.name_en}`;};
const detailRows=new Map(qs.map((q,i)=>[q.question_id,i+5]));
const detailEnd=col(20+2*tax.categories.length);
const detail=qs.map(q=>[q.question_id,q.exam_year,q.exam_form,q.number,q.practice_part,q.primary.category_id,q.primary.subtype_id,q.secondary.map(t=>t.subtype_id).join(' '),`|${[...new Set([q.primary.category_id,...q.secondary.map(t=>t.category_id)])].join('|')}|`,`|${[...new Set(q.secondary.map(t=>t.category_id))].join('|')}|`,q.answer,q.source_url,q.statement_en,q.statement_zh,q.primary.reason_en||'',q.primary.reason_zh||'',...tax.categories.map(c=>+q.secondary.some(t=>t.category_id===c.id)),...tax.categories.map(c=>+[q.primary,...q.secondary].some(t=>t.category_id===c.id)),q.corrected_answer_en||'',q.corrected_answer_zh||'',q.editorial_note_en||'',q.editorial_note_zh||'']);
base(sheets.Problems,qs.length+4,20+2*tax.categories.length,'AIME Problem Classification Detail / 逐题分类');
sheets.Problems.getRange(`A4:${detailEnd}4`).values=[['Question ID / 题号','Year / 年','Form / 卷','Q / 原号','Part','Primary topic / 主类','Primary code / 主型','Secondary codes / 次型','All topics / 涉及类','Secondary topics / 次类','Source key / 来源答案','Original source / 原题来源','English restatement','中文数学重述','Primary rationale','主分类理由',...tax.categories.map(c=>`${c.id} Secondary incidence / 次类涉及`),...tax.categories.map(c=>`${c.id} Either incidence / 主次涉及`),'Verified result if source differs','来源有误时的核算结果','Verification note','核对说明']];
sheets.Problems.getRange(`A5:${detailEnd}${qs.length+4}`).values=detail;
sheets.Problems.getRange(`A4:${detailEnd}${qs.length+4}`).format.wrapText=true;
sheets.Problems.getRange(`A5:${detailEnd}${qs.length+4}`).format.verticalAlignment='top';
sheets.Problems.getRange(`A5:${detailEnd}${qs.length+4}`).format.rowHeight=90;
sheets.Problems.getRange('A:A').format.columnWidth=25;sheets.Problems.getRange('B:K').format.columnWidth=12;
sheets.Problems.getRange('L:L').format.columnWidth=35;sheets.Problems.getRange('M:P').format.columnWidth=65;
sheets.Problems.getRange(`K5:K${qs.length+4}`).setNumberFormat('000');
sheets.Problems.getRange(`Q:${detailEnd}`).format.columnWidth=14;
sheets.Problems.getRange(`${col(17+2*tax.categories.length)}:${detailEnd}`).format.columnWidth=70;
sheets.Problems.tables.add(`A4:${detailEnd}${qs.length+4}`,true,'ProblemDetails');
sheets.Problems.freezePanes.freezeColumns(1);
let tagrows=[];
for(const q of qs)for(const [role,tags]of[['primary',[q.primary]],['secondary',q.secondary]])for(const t of tags){const s=sub.get(t.subtype_id);tagrows.push([q.question_id,role,t.category_id,t.subtype_id,s.name_en,s.name_zh,t.reason_en||'',t.reason_zh||'']);}
base(sheets.Tags,tagrows.length+4,8,'AIME Primary and Secondary Tags / 主次考点标签');
sheets.Tags.getRange('A4:H4').values=[['Question ID','Role / 主次','Topic','Subtype','English name','中文名称','Reason / English','理由 / 中文']];
sheets.Tags.getRange(`A5:H${tagrows.length+4}`).values=tagrows;
sheets.Tags.getRange(`A4:H${tagrows.length+4}`).format.wrapText=true;
sheets.Tags.getRange('A:D').format.columnWidth=23;sheets.Tags.getRange('E:F').format.columnWidth=42;sheets.Tags.getRange('G:H').format.columnWidth=75;
sheets.Tags.getRange(`A5:H${tagrows.length+4}`).format.rowHeight=65;
sheets.Tags.tables.add(`A4:H${tagrows.length+4}`,true,'ClassificationTags');
const dict=tax.subtypes.map(s=>[s.id,s.category_id,s.section_number,s.name_en,s.name_zh,s.definition_en,s.definition_zh,s.boundary_en,s.boundary_zh]);
if(dict.some(row=>row.some(x=>!x)))throw Error('The bilingual taxonomy has a missing field');
base(sheets.Taxonomy,dict.length+4,9,'AIME Topic and Subtype Dictionary / 分类词典');
sheets.Taxonomy.getRange('A4:I4').values=[['Code / 代码','Topic / 一级','Section / 小节','English name','中文名称','Definition / English','定义 / 中文','Boundary / English','分类边界 / 中文']];
sheets.Taxonomy.getRange(`A5:I${dict.length+4}`).values=dict;
sheets.Taxonomy.getRange('A:C').format.columnWidth=15;sheets.Taxonomy.getRange('D:E').format.columnWidth=44;sheets.Taxonomy.getRange('F:I').format.columnWidth=65;
sheets.Taxonomy.getRange(`A4:I${dict.length+4}`).format.wrapText=true;sheets.Taxonomy.getRange(`A5:I${dict.length+4}`).format.rowHeight=85;
sheets.Taxonomy.tables.add(`A4:I${dict.length+4}`,true,'SubtypeDictionary');
const reviewRows=qs.map(q=>[q.question_id,q.review?.author||'',q.review?.source_checked===true,q.review?.recomputed===true,`${q.review?.status||'pending'}\n${Array.isArray(q.review?.cross_review)?[...new Set(q.review.cross_review.map(r=>r.reviewer))].join(', '):q.review?.cross_review||''}`,q.unresolved_issues?.join('; ')||'None / 无',q.answer_status==='source_discrepancy'?'Source discrepancy documented / 来源差异已核实\nFull evidence in cell note / 完整证据见批注':'Independent source, mathematics, classification and language checks accepted.\n来源、数学、分类及语言独立审核通过。']);
base(sheets.Review,qs.length+4,7,'AIME Review Evidence / 审核记录');
sheets.Review.getRange('A4:G4').values=[['Question ID','Author','Source checked','Math checked','Cross review / 复审','Unresolved / 未决','Notes / 记录']];sheets.Review.getRange(`A5:G${qs.length+4}`).values=reviewRows;
sheets.Review.getRange('A:B').format.columnWidth=25;sheets.Review.getRange('C:D').format.columnWidth=18;sheets.Review.getRange('E:G').format.columnWidth=60;
sheets.Review.getRange(`A4:G${qs.length+4}`).format.wrapText=true;sheets.Review.getRange(`A5:G${qs.length+4}`).format.rowHeight=50;
sheets.Review.tables.add(`A4:G${qs.length+4}`,true,'ReviewEvidence');
for(let i=0;i<qs.length;i++){const q=qs[i],address=`E${i+5}`;wb.notes.add({id:`Review:${address}`,target:{cell:{sheetName:'Review',sheetId:sheets.Review.sheetId,address}},authorId:'',createdAt:'',body:{plainText:JSON.stringify({question_id:q.question_id,review:q.review,editorial_note_en:q.editorial_note_en,editorial_note_zh:q.editorial_note_zh},null,2)}});}
const stat=sheets.Statistics;const codes=[...tax.categories,...tax.subtypes];
base(stat,codes.length+7,7,'AIME Classification Statistics / 主次考点统计');
stat.getRange('A4:G4').values=[['Code / 代码','Name / 名称','Primary / 主考','Secondary / 次考','Either / 涉及','Primary share / 主考占比','Level / 层级']];
for(let i=0;i<codes.length;i++){
 const x=codes[i],r=i+5,isCat=cat.has(x.id),dc=isCat?'F':'G';
 stat.getRange(`A${r}:B${r}`).values=[[x.id,`${x.name_zh}\n${x.name_en}`]];
 stat.getRange(`G${r}`).values=[[isCat?'Topic / 一级':'Subtype / 二级']];
 stat.getRange(`C${r}`).formulas=[[`=COUNTIF(Problems!$${dc}$5:$${dc}$${qs.length+4},A${r})`]];
 const ci=tax.categories.findIndex(c=>c.id===x.id),secCol=col(17+ci),eitherCol=col(17+tax.categories.length+ci);
 stat.getRange(`D${r}`).formulas=[[isCat?`=SUM(Problems!$${secCol}$5:$${secCol}$${qs.length+4})`:`=COUNTIFS(Tags!$B$5:$B$${tagrows.length+4},"secondary",Tags!$D$5:$D$${tagrows.length+4},A${r})`]];
 stat.getRange(`E${r}`).formulas=[[isCat?`=SUM(Problems!$${eitherCol}$5:$${eitherCol}$${qs.length+4})`:`=C${r}+D${r}`]];
 stat.getRange(`F${r}`).formulas=[[`=C${r}/COUNTA(Problems!$A$5:$A$${qs.length+4})`]];
 if(isCat)stat.getRange(`A${r}:G${r}`).format.fill=x.color;
}
stat.getRange('A:A').format.columnWidth=13;stat.getRange('B:B').format.columnWidth=50;stat.getRange('C:G').format.columnWidth=20;
stat.getRange(`A5:G${codes.length+4}`).format.rowHeight=42;stat.getRange(`A4:G${codes.length+4}`).format.wrapText=true;stat.getRange(`F5:F${codes.length+4}`).setNumberFormat('0.0%');
const papers=[...new Set(qs.map(q=>q.paper_id))].sort((a,b)=>b.slice(5,9).localeCompare(a.slice(5,9))||a.localeCompare(b));
const matrix=sheets.Matrix;const end=col(papers.length+1);
base(matrix,19,papers.length+1,'AIME Primary / Secondary Matrix / 题型矩阵');
matrix.getRange(`A4:${end}4`).values=[['Original Q / 原题号',...papers.map(p=>p.replace('AIME-',''))]];
matrix.getRange('A5:A19').values=Array.from({length:15},(_,i)=>[i+1]);matrix.getRange('A:A').format.columnWidth=15;
matrix.getRange(`B:${end}`).format.columnWidth=37;matrix.getRange('A5:A19').format.rowHeight=145;
matrix.getRange(`B5:${end}19`).format.wrapText=true;matrix.getRange(`B5:${end}19`).format.verticalAlignment='top';
const matrixLinks=[];const rowHeights=Array(15).fill(100);
for(let pi=0;pi<papers.length;pi++)for(let n=1;n<=15;n++){
 const q=qs.find(q=>q.paper_id===papers[pi]&&q.number===n);if(!q)continue;
 const cell=matrix.getCell(n+3,pi+1);const text=`${q.answer_status==='source_discrepancy'?'[来源核对 / Source-key note]\n':''}主 / Primary: ${label(q.primary.subtype_id)}${q.secondary.length?'\n次 / Secondary: '+q.secondary.map(t=>label(t.subtype_id)).join('\n'):''}`;
 cell.values=[[text]];
 matrixLinks.push({ref:`${col(pi+2)}${n+4}`,location:`'Problems'!A${detailRows.get(q.question_id)}`});
 const lines=text.split('\n').reduce((sum,line)=>sum+Math.max(1,Math.ceil([...line].reduce((w,c)=>w+(/[\u3400-\u9fff]/.test(c)?2:1),0)/39)),0);
 rowHeights[n-1]=Math.max(rowHeights[n-1],lines*14+14);
 cell.format.fill=cat.get(q.primary.category_id).color;
 wb.notes.add({id:`Matrix:${col(pi+2)}${n+4}`,target:{cell:{sheetName:'Matrix',sheetId:matrix.sheetId,address:`${col(pi+2)}${n+4}`}},authorId:'',createdAt:'',body:{plainText:[q.question_id,...[q.primary,...q.secondary].map(t=>`${t.subtype_id}: ${t.reason_en||''}\n${t.reason_zh||''}`),q.editorial_note_en||'',q.editorial_note_zh||''].filter(Boolean).join('\n\n')}});
}
for(let n=1;n<=15;n++)matrix.getRange(`A${n+4}:${end}${n+4}`).format.rowHeight=rowHeights[n-1];
matrix.freezePanes.freezeColumns(1);matrix.tabColor='#173d69';stat.tabColor='#315c8a';
wb.recalculate();
const values=stat.getRange(`C5:F${codes.length+4}`).values;
for(let i=0;i<codes.length;i++){
 const code=codes[i].id,isCat=cat.has(code);
 const p=qs.filter(q=>(isCat?q.primary.category_id:q.primary.subtype_id)===code).length;
 const sec=qs.filter(q=>q.secondary.some(t=>(isCat?t.category_id:t.subtype_id)===code)).length;
 const union=qs.filter(q=>[q.primary,...q.secondary].some(t=>(isCat?t.category_id:t.subtype_id)===code)).length;
 for(const [j,v]of [p,sec,union].entries())if(values[i][j]!==v)throw Error(`Statistic mismatch ${code} ${j}: ${values[i][j]} != ${v}`);
}
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:30},maxChars:2000});
await fs.writeFile(path.join(qa,'formula-errors.ndjson'),errors.ndjson);
const summary=await wb.inspect({kind:'table',range:'Statistics!A4:G11',include:'values,formulas',tableMaxRows:8,tableMaxCols:7,maxChars:3000});
await fs.writeFile(path.join(qa,'statistics-inspection.ndjson'),summary.ndjson);
for(const n of names){
 const range=n==='Matrix'?`A1:${col(Math.min(4,papers.length+1))}8`:n==='Statistics'?'A1:G11':n==='Taxonomy'?'A1:I7':n==='Review'?'A1:G7':n==='Tags'?'A1:H7':'A1:H7';
 const blob=await wb.render({sheetName:n,range,scale:1,format:'png'});await fs.writeFile(path.join(qa,`${n}.png`),new Uint8Array(await blob.arrayBuffer()));
}
const file=await SpreadsheetFile.exportXlsx(wb);await file.save(path.join(out,'AIME_Matrix_Bilingual.xlsx'));
await fs.writeFile(path.join(qa,'internal-links.json'),JSON.stringify(matrixLinks));
// The runtime cannot calculate HYPERLINK; preserve readable labels and add native internal links.
execFileSync('python',[path.join(root,'scripts/xlsx_internal_links.py'),path.join(out,'AIME_Matrix_Bilingual.xlsx'),path.join(qa,'internal-links.json')],{stdio:'inherit'});
await fs.writeFile(path.join(qa,'build.json'),JSON.stringify({questions:qs.length,papers:papers.length,primary_subtypes:new Set(qs.map(q=>q.primary.subtype_id)).size,complete_coverage:coverage.complete_coverage,statistic_reconciliation:true,source_sha256:coverage.content_sha256},null,2));
console.log(`Exported bilingual Matrix: ${qs.length} questions / ${papers.length} papers; statistics reconciled.`);

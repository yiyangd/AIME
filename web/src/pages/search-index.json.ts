import {chapters,sections,questions,chapterUrl,sectionUrl,questionUrl} from '../lib/content';
export function GET(){return new Response(JSON.stringify([
 ...chapters.map(c=>({kind:'chapter',id:`Chapter ${c.id}`,title:c.titleEn,titleZh:c.titleZh,subtitle:`${c.questionCount} questions`,subtitleZh:`${c.questionCount}题`,href:chapterUrl(c.id),keywords:`${c.code} ${c.titleEn} ${c.titleZh}`})),
 ...sections.map(s=>({kind:'section',id:`Section ${s.id}`,title:s.titleEn,titleZh:s.titleZh,subtitle:`${s.questionIds.length} questions`,subtitleZh:`${s.questionIds.length}题`,href:sectionUrl(s),keywords:`${s.code} ${s.titleEn} ${s.titleZh}`})),
 ...questions.map(q=>{const s=sections.find(s=>s.id===q.sectionId)!;return {kind:'question',id:q.id,title:`${s.id}. ${s.titleEn}`,titleZh:`${s.id}. ${s.titleZh}`,subtitle:`${q.year} AIME ${q.form} · Part ${q.part}`,subtitleZh:`${q.year} AIME ${q.form} · ${q.part}组`,href:questionUrl(q),keywords:`${q.id} ${q.year} ${q.form} ${s.code} ${q.statementEn} ${q.statementZh}`}})
]),{headers:{'Content-Type':'application/json; charset=utf-8'}})}

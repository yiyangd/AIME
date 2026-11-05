from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'src/lib/content.ts';s=p.read_text(encoding='utf8')
s=s.replace('reviewStatus:string;image?', 'reviewStatus:string;answerStatus?:string;correctedAnswerEn?:string;correctedAnswerZh?:string;sourceAnswer?:string;editorialNoteEn?:string;editorialNoteZh?:string;image?')
p.write_text(s,encoding='utf8')
p=ROOT/'src/components/QuestionCard.astro';s=p.read_text(encoding='utf8')
old='<p class="answer-line"><span class="answer-choice"><Bi en="Answer" zh="答案" /> {q.answer.value}</span></p>'
new='''{q.answerStatus==='source_discrepancy'?<div class="editorial-answer"><p class="answer-line"><span class="answer-choice"><Bi en="Verified result under the stated conditions" zh="按原题条件核验的结果" /></span></p><p data-content-language="en"><MathText text={q.correctedAnswerEn||''}/></p><p data-content-language="zh" lang="zh"><MathText text={q.correctedAnswerZh||''}/></p><p class="historical-key"><Bi en={`Historical source key: ${q.sourceAnswer}`} zh={`历史来源答案键：${q.sourceAnswer}`}/></p><p class="editorial-note" data-content-language="en"><MathText text={q.editorialNoteEn||''}/></p><p class="editorial-note" data-content-language="zh" lang="zh"><MathText text={q.editorialNoteZh||''}/></p></div>:<p class="answer-line"><span class="answer-choice"><Bi en="Answer" zh="答案" /> {q.answer.value}</span></p>}'''
if old in s:s=s.replace(old,new)
elif 'editorial-answer' not in s:raise ValueError('Answer markup not found')
p.write_text(s,encoding='utf8')

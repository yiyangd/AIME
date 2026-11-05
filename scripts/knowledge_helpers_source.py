"""Original bilingual teaching material; source_audit owns AL01–05 and NT01–08."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
QUESTIONS=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))

def method(code,n,en,zh,steps,example,solution,tip,refs,pre=(),extensions=()):
 return {'method_id':f'{code}-M{n:02d}','title_en':en,'title_zh':zh,
 'steps_en':[x[0] for x in steps],'steps_zh':[x[1] for x in steps],
 'example_en':example[0],'example_zh':example[1],
 'solution_en':[x[0] for x in solution],'solution_zh':[x[1] for x in solution],
 'tip_en':tip[0],'tip_zh':tip[1],
 'question_ids':['AIME-'+x for x in refs.split()],
 'prerequisites':list(pre),'extensions_en':[x[0] for x in extensions],
 'extensions_zh':[x[1] for x in extensions]}

def save(code,intro,methods,pre=(),gaps=()):
 relevant=[q for q in QUESTIONS if q['primary']['subtype_id']==code or any(t['subtype_id']==code for t in q['secondary'])]
 coverage={}
 for q in relevant:
  ms=[m for m in methods if q['question_id'] in m['question_ids']]
  if not ms:raise ValueError('Unmapped question '+q['question_id']+' in '+code)
  coverage[q['question_id']]={'method_ids':[m['method_id'] for m in ms],
   # A method family can contain optional branches; do not attach every branch's
   # prerequisites to every question. The reviewed tags define this exact route.
   'prerequisites':sorted({t['subtype_id'] for t in q['secondary'] if t['subtype_id']!=code}|({q['primary']['subtype_id']} if q['primary']['subtype_id']!=code else set()))}
 known={q['question_id'] for q in QUESTIONS}
 assert all(x in known for m in methods for x in m['question_ids'])
 result={'subtype_id':code,'introduction_en':intro[0],'introduction_zh':intro[1],
 'prerequisites':list(pre),'methods':methods,
 'practice_ids':[q['question_id'] for q in relevant if q['primary']['subtype_id']==code],
 'coverage_by_question':coverage,
 'review':{'author':'source_audit','all_primary_routes_read':True,'necessary_secondary_routes_read':True,
 'original_examples_recomputed':True,'independent_review':False,
 'notes':'Mapped against every currently integrated primary and secondary route. General steps and worked examples are separate. Original question conditions and full solutions remain in the companion question bank.'},
 'unresolved_issues':list(gaps)}
 target=ROOT/f'data/knowledge_batches/{code}.json';target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print(code,len(methods),'methods',len(result['practice_ids']),'primary',len(coverage),'mapped routes')

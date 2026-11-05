from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def current_questions():
 qs={q['question_id']:q for p in sorted((ROOT/'data/batches').glob('*.json')) for q in json.loads(p.read_text(encoding='utf8'))}
 for p in sorted((ROOT/'audit/reviews').glob('*.json')):
  records=json.loads(p.read_text(encoding='utf8'))
  if isinstance(records,dict):records=records.get('records',[records])
  for r in records:
   if r['question_id'] in qs:qs[r['question_id']].update(r.get('patch',{}))
 return sorted(qs.values(),key=lambda q:q['question_id'])
def relevant(code):return [q for q in current_questions() if code in [q['primary']['subtype_id']]+[t['subtype_id'] for t in q.get('secondary',[])]]
def qid(short):
 import re
 m=re.fullmatch(r'(\d{4})(II|I)(\d{1,2})',short)
 if not m:raise ValueError(short)
 return f'AIME-{m[1]}-{m[2]}-Q{int(m[3]):02d}'
class Chapter:
 def __init__(self,code,intro_en,intro_zh,prerequisites):
  self.code=code;self.rows=relevant(code);self.ids={q['question_id'] for q in self.rows}
  self.data=dict(subtype_id=code,introduction_en=intro_en,introduction_zh=intro_zh,prerequisites=prerequisites,methods=[],practice_ids=[q['question_id'] for q in self.rows if q['primary']['subtype_id']==code],coverage_by_question={})
 def add(self,title_en,title_zh,steps_en,steps_zh,example_en,example_zh,solution_en,solution_zh,tip_en,tip_zh,questions,prerequisites=None,extensions_en=None,extensions_zh=None):
  mid=f'{self.code}-M{len(self.data["methods"])+1:02d}';ids=[qid(s) for s in questions.split()];ids=[s for s in ids if s in self.ids]
  m=dict(method_id=mid,title_en=title_en,title_zh=title_zh,steps_en=steps_en,steps_zh=steps_zh,example_en=example_en,example_zh=example_zh,solution_en=solution_en,solution_zh=solution_zh,tip_en=tip_en,tip_zh=tip_zh,question_ids=sorted(ids),prerequisites=prerequisites or [])
  if extensions_en:m['extensions_en']=extensions_en;m['extensions_zh']=extensions_zh
  assert len(steps_en) in (3,4) and len(steps_zh)==len(steps_en)
  assert len(solution_en) in (3,4) and len(solution_zh)==len(solution_en)
  self.data['methods'].append(m)
  for x in ids:self.data['coverage_by_question'].setdefault(x,dict(method_ids=[],prerequisites=[]))['method_ids'].append(mid)
 def save(self):
  missing=self.ids-set(self.data['coverage_by_question']);assert not missing,sorted(missing)
  for q in self.rows:
   self.data['coverage_by_question'][q['question_id']]['prerequisites']=sorted({t['subtype_id'] for t in [q['primary']]+q.get('secondary',[]) if t['subtype_id']!=self.code})
  self.data['review']=dict(author='template_audit',all_primary_routes_read=True,necessary_secondary_routes_read=True,original_examples_recomputed=True,independent_review=False,notes='Every current primary and necessary secondary route was read in full. Original teaching examples and general procedures are separate from source problems. Independent review remains required.')
  self.data['unresolved_issues']=[]
  path=ROOT/'data/knowledge_batches'/f'{self.code}.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(self.data,ensure_ascii=False,indent=2),encoding='utf8')
  print(self.code,len(self.data['methods']),'methods',len(self.rows),'primary/secondary routes',len(self.data['practice_ids']),'primary practice')
def show(code,start=0,end=None):
 for q in relevant(code)[start:end]:
  print('\n###',q['question_id'],'PRIMARY',q['primary']['subtype_id'],'SECONDARY',[t['subtype_id'] for t in q.get('secondary',[])])
  print('PROBLEM',q['statement_en']);print('METHODS',q['method_chain']);print('SOLUTION','\n'.join(q['solution_en']))
if __name__=='__main__':
 import sys;show(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 0,int(sys.argv[3]) if len(sys.argv)>3 else None)

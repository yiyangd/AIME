"""Geometry textbook authoring helpers; no question content is generated here."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
def questions():
 rows={q['question_id']:q for p in sorted((ROOT/'data/batches').glob('*.json')) for q in read(p)}
 for path in sorted((ROOT/'audit/reviews').glob('*.json')):
  rr=read(path)
  if isinstance(rr,dict):rr=rr.get('records',[rr])
  for r in rr:
   if r['question_id'] in rows:rows[r['question_id']].update(r.get('patch',{}))
 return sorted(rows.values(),key=lambda q:(q['exam_year'],q['exam_form'],q['number']))
class Section:
 def __init__(self,code,en,zh,prerequisites=()):
  self.code=code;self.rows=[q for q in questions() if code in [t['subtype_id'] for t in [q['primary']]+q['secondary']]]
  self.ids={q['question_id'] for q in self.rows}
  self.data=dict(subtype_id=code,introduction_en=en,introduction_zh=zh,prerequisites=list(prerequisites),methods=[],practice_ids=[q['question_id'] for q in self.rows if q['primary']['subtype_id']==code],coverage_by_question={})
 def add(self,en,zh,steps_en,steps_zh,example_en,example_zh,solution_en,solution_zh,tip_en,tip_zh,ids,prerequisites=(),extensions_en=(),extensions_zh=()):
  ids=[x if x.startswith('AIME-') else 'AIME-'+x for x in ids.split()] if isinstance(ids,str) else ids
  assert set(ids)<=self.ids,(self.code,set(ids)-self.ids)
  mid=f'{self.code}-M{len(self.data["methods"])+1:02}'
  assert 3<=len(steps_en)<=4 and len(steps_en)==len(steps_zh)
  assert 3<=len(solution_en)<=4 and len(solution_en)==len(solution_zh)
  self.data['methods'].append(dict(method_id=mid,title_en=en,title_zh=zh,steps_en=steps_en,steps_zh=steps_zh,example_en=example_en,example_zh=example_zh,solution_en=solution_en,solution_zh=solution_zh,tip_en=tip_en,tip_zh=tip_zh,question_ids=ids,prerequisites=list(prerequisites),extensions_en=list(extensions_en),extensions_zh=list(extensions_zh)))
  for x in ids:self.data['coverage_by_question'].setdefault(x,dict(method_ids=[],prerequisites=[]))['method_ids'].append(mid)
 def save(self):
  serialized=json.dumps(self.data,ensure_ascii=False)
  def texts(obj):
   if isinstance(obj,str):yield obj
   elif isinstance(obj,list):
    for v in obj:yield from texts(v)
   elif isinstance(obj,dict):
    for v in obj.values():yield from texts(v)
  for value in texts(self.data):assert not any(ord(c)<32 for c in value),repr(value)
  missing=self.ids-set(self.data['coverage_by_question']);assert not missing,sorted(missing)
  for q in self.rows:self.data['coverage_by_question'][q['question_id']]['prerequisites']=sorted({t['subtype_id'] for t in [q['primary']]+q['secondary'] if t['subtype_id']!=self.code})
  self.data.setdefault('review',dict(author='print_builder',all_primary_routes_read=True,necessary_secondary_routes_read=True,original_examples_recomputed=True,independent_review=False))
  self.data['unresolved_issues']=[]
  p=ROOT/'data/knowledge_batches'/f'{self.code}.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(self.data,ensure_ascii=False,indent=2),encoding='utf8')
  print(self.code,len(self.rows),'routes',len(self.data['methods']),'methods')
if __name__=='__main__':
 sys.stdout.reconfigure(encoding='utf8');code=sys.argv[1]
 for q in questions():
  tags=[t['subtype_id'] for t in [q['primary']]+q['secondary']]
  if code not in tags:continue
  print('\n'+q['question_id']+' ['+','.join(tags)+'] '+str(q.get('method_chain')))
  if '--full' in sys.argv or q['exam_year'] not in [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2018,2019,2023,2024,2025,2026]:
   print(q['statement_en']);print('\n'.join(q['solution_en']))

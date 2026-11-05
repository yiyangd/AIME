from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
REVIEW=ROOT/'audit/reviews/source_2000_2004_2020_2021.json'
KNOW=ROOT/'data/knowledge_requirements/template_audit.json'
AUTH=[]
for p in [ROOT/'data/batches/2000_2004.json',ROOT/'data/batches/2020_2021.json']:
 AUTH.extend(json.loads(p.read_text(encoding='utf8')))
BY={q['question_id']:q for q in AUTH}
class Review:
 def __init__(self,paper):
  self.paper=paper
  self.records=json.loads(REVIEW.read_text(encoding='utf8')) if REVIEW.exists() else []
  self.knowledge=json.loads(KNOW.read_text(encoding='utf8')) if KNOW.exists() else []
 def add(self,num,findings,methods,patch=None,verdict='pass'):
  year=self.paper[:4];form=self.paper[4:];qid=f'AIME-{year}-{form}-Q{num:02d}';q=BY[qid]
  record=dict(question_id=qid,reviewer='template_audit',verdict=verdict,source_checked=True,math_checked=True,classification_checked=True,language_checked=True,findings=findings)
  patch=patch or {}
  if methods:patch.setdefault('method_chain',[m[0] for m in methods])
  if patch:record['patch']=patch
  self.records=[r for r in self.records if r['question_id']!=qid]+[record]
  for entry in self.knowledge:
   for item in entry['methods']:
    item['question_ids']=[x for x in item['question_ids'] if x!=qid]
   entry['methods']=[x for x in entry['methods'] if x['question_ids']]
  self.knowledge=[x for x in self.knowledge if x['methods']]
  for method in methods:
   name_en,name_zh,*rest=method;prerequisites=rest[0] if rest else []
   section=patch.get('primary',q['primary'])['subtype_id'];entry=next((x for x in self.knowledge if x['subtype_id']==section),None)
   if not entry:entry=dict(subtype_id=section,methods=[]);self.knowledge.append(entry)
   item=next((x for x in entry['methods'] if x['name_en']==name_en),None)
   if not item:item=dict(name_en=name_en,name_zh=name_zh,question_ids=[],prerequisites=prerequisites);entry['methods'].append(item)
   if qid not in item['question_ids']:item['question_ids'].append(qid)
 def save(self):
  REVIEW.parent.mkdir(parents=True,exist_ok=True);REVIEW.write_text(json.dumps(sorted(self.records,key=lambda q:q['question_id']),ensure_ascii=False,indent=2),encoding='utf8')
  KNOW.parent.mkdir(parents=True,exist_ok=True);KNOW.write_text(json.dumps(sorted(self.knowledge,key=lambda x:x['subtype_id']),ensure_ascii=False,indent=2),encoding='utf8')
  print(f'{self.paper}: total accepted or flagged review records {len(self.records)}')

"""Persist explicitly supplied print_builder independent review judgments."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
REVIEW=ROOT/'audit/reviews/web_2005_2009_2019_2024_2026.json'
REQUIREMENTS=ROOT/'data/knowledge_requirements/print_builder.json'
def read(path):return json.loads(Path(path).read_text(encoding='utf8'))
def atomic_save(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8');tmp.replace(path)
def record_paper(paper,methods,findings=None,patches=None,needs_correction=()):
 rows=read(ROOT/f'data/batches/{paper}.json');assert len(rows)==len(methods)==15
 findings=findings or {};patches=patches or {}
 existing={x['question_id']:x for x in read(REVIEW)} if REVIEW.exists() else {}
 req_by={x['subtype_id']:x for x in read(REQUIREMENTS)} if REQUIREMENTS.exists() else {}
 for q,method in zip(rows,methods):
  assert q['review']['author']!='print_builder'
  num=q['number'];en,zh,prereq=method;patch=dict(patches.get(num,{}));patch.setdefault('method_chain',[en])
  inputs={kind:hashlib.sha256((ROOT/f'{folder}/{paper}.json').read_bytes()).hexdigest() for kind,folder in [('source','sources/records'),('authored','data/batches')]}
  existing[q['question_id']]={'question_id':q['question_id'],'reviewer':'print_builder','review_type':'separate_agent','source_checked':True,'math_checked':True,'classification_checked':True,'language_checked':True,'verdict':'needs_correction' if num in needs_correction else 'pass','findings':findings.get(num,[]),'input_hashes':inputs,'reviewed_input_sha256':hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode('utf8')).hexdigest(),'patch':patch}
  subtype=patch.get('primary',q['primary'])['subtype_id'];req=req_by.setdefault(subtype,{'subtype_id':subtype,'methods':[]})
  entry=next((x for x in req['methods'] if x['name_en']==en),None)
  if entry is None:entry={'name_en':en,'name_zh':zh,'question_ids':[],'prerequisites':prereq};req['methods'].append(entry)
  if q['question_id'] not in entry['question_ids']:entry['question_ids'].append(q['question_id'])
 atomic_save(REVIEW,sorted(existing.values(),key=lambda x:x['question_id']))
 atomic_save(REQUIREMENTS,sorted(req_by.values(),key=lambda x:x['subtype_id']))
 print(f'{paper}: 15 review records; {len(existing)} reviewed total')
if __name__=='__main__':
 import argparse,sys
 sys.stdout.reconfigure(encoding='utf-8')
 ap=argparse.ArgumentParser();ap.add_argument('paper');ap.add_argument('--from-number',type=int,default=1);args=ap.parse_args()
 source=read(ROOT/f'sources/records/{args.paper}.json');authored=read(ROOT/f'data/batches/{args.paper}.json')
 for s,q in zip(source,authored):
  if q['number']<args.from_number:continue
  print('\n## '+q['question_id']);print('SOURCE:',s['question_source_en']);print('EN:',q['statement_en']);print('ZH:',q['statement_zh'])
  print('CLASS:',q['primary']['subtype_id'],[t['subtype_id'] for t in q['secondary']]);print('ANSWER:',q['answer'])
  for lang in ['en','zh']:
   print(lang.upper()+':')
   for i,step in enumerate(q['solution_'+lang],1):print(str(i)+'. '+step)

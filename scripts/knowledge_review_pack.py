import argparse,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('code');a.add_argument('--start',type=int,default=0);a.add_argument('--count',type=int,default=5);a.add_argument('--routes',action='store_true');v=a.parse_args()
s=json.loads((R/'data/knowledge_batches'/f'{v.code}.json').read_text(encoding='utf8'));Q={q['question_id']:q for q in json.loads((R/'data/questions.json').read_text(encoding='utf8'))}
print(v.code,s['introduction_en'],s['introduction_zh'])
for m in s['methods'][v.start:v.start+v.count]:
 print('\n'+m['method_id']+' '+m['title_en']+' / '+m['title_zh'])
 for k in ['steps_en','steps_zh','example_en','example_zh','solution_en','solution_zh','tip_en','tip_zh','extensions_en','extensions_zh']:print(k+': '+json.dumps(m.get(k,[]),ensure_ascii=False))
 print('Question IDs: '+' '.join(m['question_ids']))
 if v.routes:
  for qid in m['question_ids']:print(qid+' '+str(Q[qid]['method_chain']))

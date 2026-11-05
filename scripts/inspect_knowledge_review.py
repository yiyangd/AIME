"""Compact read-only view of authored textbook content for independent review."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for code in sys.argv[1:]:
 s=json.loads((ROOT/'data/knowledge_batches'/f'{code}.json').read_text(encoding='utf8'))
 print('\n###',code, s['introduction_en'],s['introduction_zh'])
 for m in s['methods']:
  print('\n##',m['method_id'],m['title_en'],'/',m['title_zh'])
  for field in ['steps_en','steps_zh','example_en','example_zh','solution_en','solution_zh','tip_en','tip_zh','extensions_en','extensions_zh']:
   v=m.get(field,[])
   print(field+':', '\n'.join(v) if isinstance(v,list) else v)
  print('Routes:',','.join(m['question_ids']))
 print('Coverage:',len(s['coverage_by_question']))

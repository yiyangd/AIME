from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
slug=sys.argv[1]
source=json.loads((ROOT/f'sources/records/{slug}.json').read_text(encoding='utf-8'))
draft=json.loads((ROOT/f'data/batches/{slug}.json').read_text(encoding='utf-8'))
for a,s in zip(draft,source):
 print('\n###',a['question_id'],a['answer'],a['primary']['subtype_id'],[t['subtype_id'] for t in a['secondary']])
 print('SOURCE:',s['question_source_en'])
 print('EN:',a['statement_en'])
 print('ZH:',a['statement_zh'])
 for i,(en,zh) in enumerate(zip(a['solution_en'],a['solution_zh']),1):print(i,en,'\nZH',zh)

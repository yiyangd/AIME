"""Read-only review packet; contains source conditions and independently authored text."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
paper=sys.argv[1];selected={int(x) for x in sys.argv[2:]} if len(sys.argv)>2 else set(range(1,16))
source=json.loads((ROOT/f'sources/records/{paper}.json').read_text(encoding='utf8'))
path=ROOT/f'data/batches/{paper}.json'
if path.exists():authored=json.loads(path.read_text(encoding='utf8'))
else:
 authored=[]
 for path in (ROOT/'data/batches').glob('*.json'):
  authored.extend(q for q in json.loads(path.read_text(encoding='utf8')) if q['exam_year']==int(paper[:4]) and q['exam_form']==paper[4:])
by={q['number']:q for q in authored}
for s in source:
 if s['number'] not in selected:continue
 q=by[s['number']]
 print('\n###',q['question_id'],'KEY',q['answer'],'TAGS',q['primary']['subtype_id'],[t['subtype_id'] for t in q.get('secondary',[])])
 print('SOURCE CONDITIONS:',s['question_source_en'])
 print('EN RESTATEMENT:',q['statement_en'])
 print('ZH RESTATEMENT:',q['statement_zh'])
 print('EN SOLUTION:', '\n'.join(q['solution_en']))
 print('ZH SOLUTION:', '\n'.join(q['solution_zh']))
 print('FLAGS:',q.get('unresolved_issues'),q.get('review',{}).get('notes',''))

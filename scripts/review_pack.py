"""Readable comparison for a separate mathematical/editorial review; never marks a pass."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
paper=sys.argv[1]
source=json.loads((ROOT/f'sources/records/{paper}.json').read_text(encoding='utf8'))
rows=[]
for p in (ROOT/'data/batches').glob('*.json'):
    rows.extend(q for q in json.loads(p.read_text(encoding='utf8')) if q['paper_id']==source[0]['paper_id'])
rows.sort(key=lambda q:q['number'])
for s,q in zip(source,rows):
    print('\n###',q['question_id'],'source key',s['answer'],'tags',q['primary']['subtype_id'],[t['subtype_id'] for t in q['secondary']])
    print('ORIGINAL:',s['question_source_en'])
    print('RESTATED EN:',q['statement_en'])
    print('RESTATED ZH:',q['statement_zh'])
    for en,zh in zip(q['solution_en'],q['solution_zh']):print('EN:',en,'\nZH:',zh)
    if q.get('unresolved_issues'):print('ISSUES:',q['unresolved_issues'])

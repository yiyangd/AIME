import argparse,json
from knowledge_ge_helpers import questions
ap=argparse.ArgumentParser();ap.add_argument('code');ap.add_argument('--start',type=int,default=0);ap.add_argument('--count',type=int,default=12);a=ap.parse_args()
rows=[q for q in questions() if a.code in [t['subtype_id'] for t in [q['primary']]+q['secondary']]]
print(f'{a.code}: {len(rows)} current routes; showing {a.start}..{min(a.start+a.count,len(rows))-1}')
for q in rows[a.start:a.start+a.count]:
 print('\n'+q['question_id']+' '+str(q['method_chain']));print(q['statement_en']);print('\n'.join(q['solution_en']))

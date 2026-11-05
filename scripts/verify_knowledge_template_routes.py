"""Independent canonical route membership audit for the 16 reviewed chapters."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf8'))
byid={q['question_id']:q for q in questions}
reviews=json.loads((ROOT/'audit/knowledge_reviews/template_audit.json').read_text(encoding='utf8'))
report=[]
for receipt in reviews:
 code=receipt['subtype_id']
 chapter=json.loads((ROOT/'data/knowledge_batches'/f'{code}.json').read_text(encoding='utf8'))
 chapter.update(receipt['patch'])
 actual={q['question_id'] for q in questions if code in [q['primary']['subtype_id'],*[s['subtype_id'] for s in q.get('secondary',[])]]}
 covered=set(chapter['coverage_by_question'])
 assert actual==covered,(code,'route membership',actual-covered,covered-actual)
 primary={q['question_id'] for q in questions if q['primary']['subtype_id']==code}
 assert primary==set(chapter['practice_ids']),(code,'primary practice')
 methods={m['method_id']:m for m in chapter['methods']}
 for qid,route in chapter['coverage_by_question'].items():
  assert route['method_ids']
  assert all(qid in methods[mid]['question_ids'] for mid in route['method_ids']),(code,qid,'reverse method link')
 for mid,method in methods.items():
  assert set(method['question_ids'])<=actual,(mid,'extraneous route')
  assert all(mid in chapter['coverage_by_question'][qid]['method_ids'] for qid in method['question_ids']),(mid,'reverse coverage link')
 row=dict(subtype_id=code,methods=len(methods),routes=len(actual),primary=len(primary),passed=True,
          concrete_routes=[dict(question_id=qid,methods=chapter['coverage_by_question'][qid]['method_ids'],
            method_chain=byid[qid].get('method_chain',[])) for qid in sorted(actual)])
 report.append(row)
 print(code,len(methods),'methods',len(actual),'routes',len(primary),'primary')
out=ROOT/'output/qa/knowledge-template-route-audit.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(report),'chapters',sum(x['methods'] for x in report),'methods',sum(x['routes'] for x in report),'route assignments')

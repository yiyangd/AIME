"""Isolated real typesetting QA of all authored geometry knowledge methods."""
from collections import defaultdict
import build_print as p
from knowledge_ge_helpers import questions
p.WORK=p.ROOT/'tmp/geometry-knowledge-qa';p.OUT=p.WORK/'pdf'
p.WORK.mkdir(parents=True,exist_ok=True)
qs=questions();tax=p.read(p.ROOT/'data/taxonomy.json');groups=defaultdict(list)
for q in qs:groups[q['primary']['subtype_id']].append(q)
sections=[s for s in tax['subtypes'] if s['id'].startswith('GE')]
knowledge=[p.read(p.ROOT/f'data/knowledge_batches/{s["id"]}.json') for s in sections]
units=p.make_units('textbook',qs,sections,tax['categories'],knowledge,groups)
assert len(units)==sum(len(s['methods']) for s in knowledge)
assert all(u['id']==u['method_id'] for u in units)
body=p.render_body('textbook',units)
report=dict(sections=len(sections),methods=len(units),pages=len(body['pages']),math_errors=body['math_errors'],overflow_check=body['overflow_check'],visual_review='pending representative page inspection')
p.save(p.WORK/'qa-receipt.json',report);print(report)

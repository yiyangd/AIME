"""Isolated typesetting QA of the 66 independently reviewed CO/AL06 methods."""
from collections import defaultdict
import build_print as p
from review_knowledge_helpers import digest
from knowledge_ge_helpers import questions

p.WORK = p.ROOT/'tmp/reviewed-knowledge-print-qa'
p.OUT = p.WORK/'pdf'
p.WORK.mkdir(parents=True, exist_ok=True)
qs = questions()
tax = p.read(p.ROOT/'data/taxonomy.json')
groups = defaultdict(list)
for q in qs:
    groups[q['primary']['subtype_id']].append(q)
receipts = {r['subtype_id']:r for r in p.read(p.ROOT/'audit/knowledge_reviews/print_builder.json')}
codes = ['CO01','CO02','CO03','CO04','CO05','CO06','CO07','AL06']
sections = [s for s in tax['subtypes'] if s['id'] in codes]
knowledge = []
for code in codes:
    s = p.read(p.ROOT/f'data/knowledge_batches/{code}.json')
    s.update(receipts[code]['patch'])
    assert digest(s) == receipts[code]['content_sha256'], code
    knowledge.append(s)
units = p.make_units('textbook', qs, sections, tax['categories'], knowledge, groups)
assert len(units) == 66
body = p.render_body('textbook', units)
report = dict(sections=len(sections),methods=len(units),pages=len(body['pages']),math_errors=body['math_errors'],overflow_check=body['overflow_check'],review_receipt_hashes='all current',visual_review='pending representative page inspection')
p.save(p.WORK/'qa-receipt.json',report)
print(report)

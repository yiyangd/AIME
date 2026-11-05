"""Temporary real batch print QA; outputs remain under tmp/print-real-qa."""
import build_print as p
from collections import defaultdict
p.WORK=p.ROOT/'tmp/print-real-qa';p.OUT=p.WORK/'pdf';p.OUT.mkdir(parents=True,exist_ok=True)
p.register_fonts();p.setup_assets()
qs=p.read(p.ROOT/'data/batches/2022I.json');tax=p.read(p.ROOT/'data/taxonomy.json')
cats=tax['categories'];subs=tax['subtypes'];group=defaultdict(list)
for q in qs:group[q['primary']['subtype_id']].append(q)
subs=[s for s in subs if s['id'] in group]
for arr in group.values():arr.sort(key=lambda q:(q['practice_part'],q['exam_year'],q['exam_form'],q['number']))
qs=[q for s in subs for q in group[s['id']]]
for kind in ['workbook','solutions_en','solutions_zh']:p.build_book(kind,qs,subs,cats,[],group)
p.matrix_pdf(qs,subs,cats,'bilingual')
print('Real batch render QA generated under tmp; contest data unchanged.')

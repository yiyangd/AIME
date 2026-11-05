"""Math-render and measured-layout check for print_builder's authored cohort."""
from collections import defaultdict
import build_print as p
p.WORK=p.ROOT/'tmp/print-author-qa';p.OUT=p.WORK/'pdf'
p.WORK.mkdir(parents=True,exist_ok=True);p.OUT.mkdir(exist_ok=True)
p.setup_assets()
qs=[]
for year in [2010,2011,2012,2013,2014,2018,2023]:
 for form in ['I','II']:qs+=p.read(p.ROOT/f'data/batches/{year}{form}.json')
tax=p.read(p.ROOT/'data/taxonomy.json');group=defaultdict(list)
for q in qs:group[q['primary']['subtype_id']].append(q)
sections=[s for s in tax['subtypes'] if s['id'] in group]
for records in group.values():records.sort(key=lambda q:(q['practice_part'],q['exam_year'],q['exam_form'],q['number']))
report={}
for kind in ['workbook','solutions_en','solutions_zh']:
 units=p.make_units(kind,qs,sections,tax['categories'],[],group)
 layout=p.render_body(kind,units)
 report[kind]={'questions':len(units),'pages':len(layout['pages']),'math_errors':layout['math_errors'],'overflow_check':layout['overflow_check']}
p.save(p.WORK/'qa-receipt.json',report)
print(report)

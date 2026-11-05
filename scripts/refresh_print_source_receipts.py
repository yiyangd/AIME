"""Refresh source receipts only when current canonical data produces identical units.

This handles edits outside a book's actual printed content. It never changes PDFs.
"""
from collections import defaultdict
import build_print as p

questions=p.read(p.ROOT/'data/questions.json')
tax=p.read(p.ROOT/'data/taxonomy.json')
categories=sorted(tax['categories'],key=lambda c:c.get('order',0))
sections=sorted(tax['subtypes'],key=lambda s:(next(i for i,c in enumerate(categories) if c['id']==s['category_id']),s.get('order',s['id'])))
groups=defaultdict(list)
for q in questions:groups[q['primary']['subtype_id']].append(q)
for qs in groups.values():qs.sort(key=lambda q:(q['practice_part'],q['exam_year'],q.get('exam_form',''),q['number']))
sections=[s for s in sections if s['id'] in groups]
for ci,ca in enumerate(categories,1):
    for si,s in enumerate([s for s in sections if s['category_id']==ca['id']],1):s.setdefault('section_number',f'{ci}.{si}')
questions=[q for s in sections for q in groups[s['id']]]
p.DATE_RANGE=f'{min(q["exam_year"] for q in questions)}-{max(q["exam_year"] for q in questions)}'
knowledge=p.read(p.ROOT/'data/knowledge.json')
wb=p.read(p.WORK/'workbook/layout_manifest.json')['locations']
hashes={name:p.sha(p.ROOT/'data'/name) for name in ['questions.json','taxonomy.json','knowledge.json','knowledge_diagrams.json']}
reports=[]
for kind in ['workbook','solutions_en','solutions_zh','textbook']:
    units=p.make_units(kind,questions,sections,categories,knowledge,groups,wb)
    spec=p.read(p.WORK/kind/'render-spec.json')
    assert spec['date_range']==p.DATE_RANGE
    assert units==spec['units'],f'{kind}: current-data content differs; rebuild required'
    m=p.read(p.WORK/kind/'layout_manifest.json')
    assert p.sha(p.ROOT/m['output'])==m['sha256']
    if kind!='textbook':
        expected=[(q['question_id'],q['primary']['subtype_id'],q['practice_part']) for q in questions]
        assert [(x['question_id'],x['subtype_id'],x['practice_part']) for x in m['placements']]==expected
    reports.append(dict(kind=kind,pdf_sha256=m['sha256'],current_data_render_units='identical',frontmatter_dependencies='same taxonomy,question count,section groups,date range and locations'))
book_receipt=p.read(p.WORK/'question_books_receipt.json')
book_receipt['canonical_inputs']={name:hashes[name] for name in ['questions.json','taxonomy.json']}
book_receipt['source_update_verification']='Current canonical data regenerates exactly the saved units of all four printed books; PDFs are unchanged unless separately rebuilt.'
for book in book_receipt['books']:
    m=p.read(p.WORK/book['kind']/'layout_manifest.json')
    book.update(sha256=m['sha256'],body_pages=m['body_pages'],pdf_pages=m['pdf_pages'],overflow_check=m['overflow_check'])
p.save(p.WORK/'question_books_receipt.json',book_receipt)
textbook=p.read(p.WORK/'textbook_receipt.json')
assert all(textbook['canonical_inputs'][name]==hashes[name] for name in ['taxonomy.json','knowledge.json','knowledge_diagrams.json'])
textbook['canonical_inputs']=hashes
textbook['source_update_verification']='Current-data textbook units exactly match saved render spec after English-only question wording changes.'
p.save(p.WORK/'textbook_receipt.json',textbook)
for kind in ['workbook','solutions_en','solutions_zh','textbook']:
    path=p.WORK/f'build_receipt_{kind}.json'
    if path.exists():
        r=p.read(path);r['source_hashes']={name:hashes[name] for name in ['questions.json','taxonomy.json']};r['source_update_verification']='Current-data units identical to saved render spec.';p.save(path,r)
p.save(p.WORK/'source_update_verification.json',dict(canonical_inputs=hashes,reports=reports))
print('Verified identical current-data units for all four books and refreshed source receipts.')

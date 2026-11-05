"""Structural QA for question placements, links, splits and the documented erratum."""
import hashlib
import json
import subprocess
from pathlib import Path
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
qids={q['question_id'] for q in read(ROOT/'data/questions.json')}
build=read(ROOT/'output/print/question_books_receipt.json')
assert build['canonical_inputs']['questions.json']==sha(ROOT/'data/questions.json')
reports=[]
for kind in ['workbook','solutions_en','solutions_zh']:
    m=read(ROOT/f'output/print/{kind}/layout_manifest.json')
    r=PdfReader(ROOT/m['output'])
    assert len(r.pages)==m['pdf_pages'] and sha(ROOT/m['output'])==m['sha256']
    assert {p['question_id'] for p in m['placements']}==qids
    assert len(m['placements'])==len(qids)==810
    for p in m['placements']:
        assert p['physical_page']==m['front_pages']+p['body_page']
        assert m['locations'][p['question_id']]==p['body_page']
        assert r.page_labels[p['physical_page']-1]==str(p['body_page'])
    splits=read(ROOT/f'output/print/{kind}/section_manifest.json')
    assert len(splits)==44
    split_pages=[]
    for s in splits:
        assert len(PdfReader(ROOT/s['output']).pages)==s['page_count']
        split_pages.extend(s['source_physical_pages'])
    assert sorted(split_pages)==list(range(m['front_pages']+1,m['pdf_pages']+1))
    links=0
    for page in r.pages[:m['front_pages']]:
        for annot in page.get('/Annots',[]):
            a=annot.get_object()
            if a.get('/Subtype')=='/Link':
                dest=a.get('/Dest')
                assert dest and isinstance(dest[0],int) and m['front_pages']<=dest[0]<len(r.pages)
                links+=1
    assert links>=44
    erratum=None
    if kind.startswith('solutions_'):
        own=[p for p in m['pages'] if p['unit_id']=='AIME-2016-I-Q09']
        text='\n'.join(r.pages[p['physical_page']-1].extract_text() for p in own)
        assert '728.365125470659' in text and '744' in text
        erratum=dict(physical_pages=[p['physical_page'] for p in own],corrected_result_and_historical_key_present=True)
    reports.append(dict(kind=kind,questions=810,sections=44,pdf_pages=len(r.pages),toc_links=links,split_pages_complete=True,page_labels_and_placements='pass',erratum=erratum))
out=dict(question_sha256=sha(ROOT/'data/questions.json'),reports=reports,visual_review='Corrected-result pages inspected in both languages; final full-pack montage/representative inspection remains separate.')
horizontal=subprocess.run(['node',str(ROOT/'scripts/qa_print_horizontal.cjs')]+[str(ROOT/f'output/print/{kind}/body.html') for kind in ['workbook','solutions_en','solutions_zh']],capture_output=True,text=True,cwd=ROOT)
assert horizontal.returncode==0,horizontal.stdout+'\n'+horizontal.stderr
hreport=json.loads(horizontal.stdout)
(ROOT/'output/print/question_books_horizontal_qa.json').write_text(json.dumps(hreport,ensure_ascii=False,indent=2),encoding='utf8')
out['horizontal_math_fragments']='all three books pass'
(ROOT/'output/print/question_books_structural_qa.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(out,ensure_ascii=False))

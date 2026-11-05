"""Build the reviewed textbook only after the question and knowledge freeze."""
import hashlib,json,subprocess,sys
from pathlib import Path
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
inputs={name:sha(ROOT/'data'/name) for name in ['questions.json','taxonomy.json','knowledge.json','knowledge_diagrams.json']}
knowledge=read(ROOT/'data/knowledge.json')
assert len(knowledge)==44 and all(s['review'].get('independent_review') is True for s in knowledge)
method_ids={m['method_id'] for s in knowledge for m in s['methods']}
assert len(method_ids)==sum(len(s['methods']) for s in knowledge)
question_build=read(ROOT/'output/print/question_books_receipt.json')
assert all(question_build['canonical_inputs'][name]==inputs[name] for name in question_build['canonical_inputs'])
wb=read(ROOT/'output/print/workbook/layout_manifest.json')
assert len(wb['placements'])==810 and len(wb['locations'])==810
subprocess.run([sys.executable,str(ROOT/'scripts/build_print.py'),'--only','textbook'],check=True,cwd=ROOT)
assert inputs=={name:sha(ROOT/'data'/name) for name in inputs}
m=read(ROOT/'output/print/textbook/layout_manifest.json')
assert not m['math_errors'] and set(m['method_locations'])==method_ids
pdf=PdfReader(ROOT/m['output'])
assert len(pdf.pages)==m['pdf_pages']
for mid,loc in m['method_locations'].items():
    page=pdf.pages[loc['physical_page']-1]
    assert mid in page.extract_text(),mid
    assert pdf.page_labels[loc['physical_page']-1]==str(loc['body_page'])
splits=read(ROOT/'output/print/textbook/section_manifest.json')
assert len(splits)==44
pages=[]
for s in splits:
    assert len(PdfReader(ROOT/s['output']).pages)==s['page_count']
    pages.extend(s['source_physical_pages'])
assert sorted(pages)==list(range(m['front_pages']+1,m['pdf_pages']+1))
receipt=dict(canonical_inputs=inputs,sections=44,methods=len(method_ids),body_pages=m['body_pages'],pdf_pages=m['pdf_pages'],output=m['output'],sha256=m['sha256'],method_page_anchors='all verified against printed method IDs',section_splits='44 complete',math_errors=m['math_errors'],overflow_check=m['overflow_check'],visual_review='pending final whole-book montage/representative page inspection')
(ROOT/'output/print/textbook_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(receipt,ensure_ascii=False))

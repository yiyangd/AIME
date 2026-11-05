"""Record only the English PDF/render version actually inspected by source_audit."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'output/solutions/AIME_2000-2026_solutions_en.pdf'
PDF_SHA='e665c9bb44d4cd05faa39a0c0ce028e2869253562ef5d636e9bc3e47012bcb53'
QUESTION_SHA='2eb9bf48ae0b5f70d00970d3d33b32deb037d1212bb456323c2defda84411476'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(PDF)==PDF_SHA,'English PDF changed: inspect the new render before recording visual approval'
assert sha(ROOT/'data/questions.json')==QUESTION_SHA,'Canonical questions changed'
folder=ROOT/'output/qa/rendered/solutions_en/AIME_2000-2026_solutions_en'
contacts=sorted(folder.glob('contact-*.jpg'));assert len(contacts)==13
comparison=json.loads((ROOT/'output/qa/solutions-en-render-comparison.json').read_text(encoding='utf-8'))
assert comparison=={'compared_pages':830,'changed_pages':[202,203,346],'pixel_identical_other_pages':827}
high_resolution=[1,2,3,18,19,197,198,202,203,319,327,346,684,728,828]
report=dict(reviewer='source_audit',reviewed_at=datetime.now(timezone.utc).isoformat(),status='passed',pdf=PDF.relative_to(ROOT).as_posix(),pdf_sha256=PDF_SHA,canonical_questions_sha256=QUESTION_SHA,physical_pages=830,body_pages=812,
contact_sheet_review=dict(sheets=13,covered_physical_pages=[1,830],all_sheets_visually_inspected=True,render_source_pdf_sha256='36ee231c5e1c02cf5067ba3a7a381037ec55e67a5d71a43112fe192330ab2c6a',files={p.name:sha(p) for p in contacts}),
final_render_comparison=dict(comparison,renderer='Poppler pdftoppm at35dpi',meaning='827 final page PNGs are byte-identical to the previously inspected contact-sheet source pages; all3 changed final pages were rendered at130dpi and visually inspected.'),
high_resolution_pages=high_resolution,final_changed_pages_inspected=[202,203,346],checks=['cover and bilingual atlas alignment','all16 contents pages in contact sheets; first and last contents pages at full resolution','original diagram detail','headers/footers and body numbering','long proof continuations on197–198','corrected result and historical key distinction on202–203','dense geometry/discrete arguments','LaTeX glyphs and long formulas','no clipping, text collisions or overprinting seen'],
resolved_findings=[dict(question_id='AIME-2016-I-Q09',finding='Missing English spaces adjoining744',resolved=True),dict(question_id='AIME-2022-I-Q14',finding='Plain-text vector algebra and degree expressions',resolved=True)],unresolved_findings=[],limitation='Contact sheets establish whole-book layout review; detailed legibility was sampled at high resolution. This visual receipt is separate from the mathematical data reviews.')
out=ROOT/'output/qa/solutions-en-visual-review.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for rel in ['output/print/build_receipt_solutions_en.json','output/print/solutions_en/layout_manifest.json']:
 path=ROOT/rel;data=json.loads(path.read_text(encoding='utf-8'))
 data['visual_review']='passed: source_audit checked13 contact sheets covering830 pages and15 full-resolution sample pages; final3 changed pages rechecked,827 others pixel-identical'
 data['visual_review_pdf_sha256']=PDF_SHA;data['visual_review_record']='output/qa/solutions-en-visual-review.json'
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded exact final English visual approval:',PDF_SHA)

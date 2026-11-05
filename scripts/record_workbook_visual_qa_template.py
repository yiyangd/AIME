"""Receipt for the manually inspected final workbook render set."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'output/workbook/AIME_2000-2026_workbook.pdf'
folder=ROOT/'output/qa/rendered/workbook/AIME_2000-2026_workbook'
contacts=sorted(folder.glob('contact-*.jpg'))
details=[1,2,3,18,19,148,536,608,716,828]
receipt={
 'reviewer':'template_audit','pdf':str(pdf.relative_to(ROOT)),
 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'physical_pages':828,'all_page_pngs':len(list(folder.glob('p-*.png'))),
 'contact_sheets_visually_inspected':[str(p.relative_to(ROOT)) for p in contacts],
 'high_resolution_pages_visually_inspected':details,
 'high_resolution_renders':[str((folder/f'detail-{p:04d}.png').relative_to(ROOT)) for p in details],
 'findings':[
  'All13 contact sheets covering physical pages1–828 were visually screened. No blank unintended page, displaced header/footer, visible overlap, truncated page block, or inconsistent section transition was found.',
  'Full-resolution cover preserves the established AMC8 palette, curves, STEMHUB mark and geometric decoration. It correctly states2000–2026,810 problems and44 sections.',
  'The full-resolution atlas has six chapter boxes and44 bilingual subtype entries, with aligned numbering and clear English/Chinese hierarchy.',
  'First and last contents pages show the three practice parts, I/II paper labels, individual printed body-page numbers and coherent section numbers. The final listed question is bodypage810.',
  'First body page has readable bilingual text, sharp original nine-square diagram, human-readable source link and ample working space.',
  'Additional high-resolution pages148,536,608 inspect long polynomial, multiline modular recurrence and factorial-base summations. Formula glyphs, subscripts, line breaks and margins are readable and unclipped.',
  'Page716 confirms the original16-vertex graph is sharp and separated from text and working area. Page828 confirms the final long bilingual logical-deduction statement fits with stable footer and bodypage810.',
  'The one-question-per-page whitespace is intentional working area, consistent across the practice workbook. No layout correction is required.'
 ],
 'limitations':'The contact sheets establish whole-book visual layout screening; detailed glyph legibility was checked on the ten named full-resolution pages. Mathematical content and physical-page links are covered by separate independent-review and print-link receipts.',
 'passed':True
}
assert len(contacts)==13 and receipt['all_page_pngs']==828
out=ROOT/'audit/workbook-visual-qa-template.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf8')
print('Recorded13 contact sheets,828 pages,10 full-resolution pages; passed')

"""Rebuild current matrices and compare every page to root's reviewed renders."""
import hashlib,json,subprocess,sys
from pathlib import Path
from PIL import Image,ImageChops

ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prior=read(ROOT/'output/print/build_receipt_matrix.json')
poppler=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
subprocess.run([sys.executable,str(ROOT/'scripts/build_print.py'),'--only','matrix'],check=True,cwd=ROOT)
current=read(ROOT/'output/print/build_receipt_matrix.json');reports=[]
old={Path(m['path']).stem:m for m in prior['matrix']}
for m in current['matrix']:
    source=ROOT/m['path'];stem=source.stem
    baseline=ROOT/'output/qa/rendered/matrix'/stem
    fresh=ROOT/'tmp/final-matrix-refresh'/stem;fresh.mkdir(parents=True,exist_ok=True)
    subprocess.run([str(poppler),'-r','35','-png',str(source),str(fresh/'p')],check=True,capture_output=True)
    before=sorted(baseline.glob('p-*.png'));after=sorted(fresh.glob('p-*.png'))
    assert len(before)==len(after)==m['pages']
    for a,b in zip(before,after):
        aa=Image.open(a).convert('RGB');bb=Image.open(b).convert('RGB')
        assert aa.size==bb.size and ImageChops.difference(aa,bb).getbbox() is None,(a,b)
    m['visual_review']='passed: every newly rebuilt page is pixel-identical to the all-page renders inspected by root; see output/qa/matrix-refresh-verification.json'
    reports.append(dict(path=m['path'],prior_pdf_sha256=old[stem]['sha256'],final_pdf_sha256=sha(source),pages=m['pages'],pixel_identical_pages=m['pages'],review_receipt='audit/final-root-visual-qa.json'))
(ROOT/'output/print/build_receipt_matrix.json').write_text(json.dumps(current,ensure_ascii=False,indent=2),encoding='utf8')
out=dict(question_sha256=sha(ROOT/'data/questions.json'),matrices=reports,total_pixel_identical_pages=sum(r['pages'] for r in reports),status='pass')
(ROOT/'output/qa/matrix-refresh-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(out,ensure_ascii=False))

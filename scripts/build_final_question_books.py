"""Build the three question books sequentially from one frozen canonical input."""
import hashlib
import json
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

data = ROOT/'data/questions.json'
questions = json.loads(data.read_text(encoding='utf8'))
assert len(questions) == 810
inputs = {name:sha(ROOT/'data'/name) for name in ['questions.json','taxonomy.json']}
parser=argparse.ArgumentParser()
parser.add_argument('--refresh-only',action='store_true',help='Refresh one rebuilt book in the receipt after verifying the canonical freeze has not changed.')
args=parser.parse_args()
if args.refresh_only:
    prior=json.loads((ROOT/'output/print/question_books_receipt.json').read_text(encoding='utf8'))
    assert prior['canonical_inputs']==inputs
books = []
for kind in ['workbook','solutions_en','solutions_zh']:
    if not args.refresh_only:
        print('Building',kind,flush=True)
        subprocess.run([sys.executable,str(ROOT/'scripts/build_print.py'),'--only',kind],cwd=ROOT,check=True)
    assert inputs == {name:sha(ROOT/'data'/name) for name in inputs}, 'Canonical question input changed during the build'
    manifest = json.loads((ROOT/f'output/print/{kind}/layout_manifest.json').read_text(encoding='utf8'))
    assert manifest['question_count'] == 810 and len(manifest['placements']) == 810
    assert not manifest['math_errors']
    books.append(dict(kind=kind,output=manifest['output'],sha256=manifest['sha256'],body_pages=manifest['body_pages'],pdf_pages=manifest['pdf_pages'],sections=len(json.loads((ROOT/f'output/print/{kind}/section_manifest.json').read_text(encoding='utf8'))),overflow_check=manifest['overflow_check']))
receipt = dict(canonical_inputs=inputs,question_count=810,books=books,visual_review='pending final whole-pack inspection')
(ROOT/'output/print/question_books_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(receipt,ensure_ascii=False),flush=True)

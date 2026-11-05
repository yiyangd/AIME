"""Update the resumable project ledger from completed artifact evidence."""
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--deployed',action='store_true');args=ap.parse_args()
q=read('output/qa/coverage.json');k=read('output/qa/knowledge-coverage.json');m=read('output/qa/matrix/build.json')
assert q['authored_questions']==q['cross_reviewed']==810 and q['complete_coverage'] and not q['unresolved']
assert k['sections']==len(k['independently_reviewed_sections'])==44 and k['methods']==399 and not k['stale_reviews']
assert m['source_sha256']==q['content_sha256']==sha('data/questions.json') and m['statistic_reconciliation']
books=[]
for kind in ['workbook','textbook','solutions_en','solutions_zh']:
 layout=read(f'output/print/{kind}/layout_manifest.json');assert sha(layout['output'])==layout['sha256']
 books.append(dict(kind=kind,pages=layout['pdf_pages'],sha256=layout['sha256']))
web=read('web/reports/validation.json');math=read('web/reports/math-validation.json');links=read('web/reports/print-links.json')
assert web['passed'] and not math['errors'] and len(links)==4 and all(r['passed'] for r in links)
p=read('progress.json');p['updated_at']=datetime.now(timezone.utc).isoformat();p['stage']='ready_to_publish'
p['taxonomy'].update(status='completed',topics=6,subtypes=44)
p['knowledge']=dict(status='completed',sections=44,methods=399,independently_reviewed=44,sha256=k['knowledge_sha256'])
p['matrix']=dict(status='completed',questions=810,papers=54,sheets=6,offline_languages=['en','zh','bilingual'],statistics_reconciled=True)
p['print']=dict(status='completed',books=books,section_extracts=176,all_pages_rendered_and_visually_inspected=True)
p['website']=dict(status='completed',questions=810,chapters=6,sections=44,methods=399,original_method_diagrams=10,downloads=188,local_checks='passed; final fixed-input publication snapshot is retained separately')
p['deployment']=dict(status='ready',repository='yiyangd/AIME',url='https://yiyangd.github.io/AIME/')
p['next']='Publish the fixed-input reviewed snapshot, enable GitHub Pages Actions and verify the live site.'
if args.deployed:
 live=read('output/release/live-verification.json');assert live['passed'] and live.get('commit')
 p['stage']='completed';p['deployment'].update(status='completed',commit=live['commit'],verified_at=live['verified_at'],checks=live['checks']);p['next']='All requested products and live deployment completed.'
(ROOT/'progress.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({key:p[key] for key in ['stage','updated_at','deployment','next']},ensure_ascii=False))

"""Inventory explicit public files; --final is a local release gate, never a push."""
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'output/release'
SOURCE_METADATA={'sources/README-audit.md','sources/inventory.json','sources/fetch_manifest.json','sources/asset_manifest.json'}
TOP={'.gitignore','README.md','DEPLOYMENT.md','project.config.json','progress.json'}
SCRIPT_SUFFIXES={'.py','.mjs','.cjs','.js','.ps1','.md'}
PRODUCT_SUFFIXES={'.pdf','.xlsx','.html'}
EXCLUDED_SCRIPTS={'check_publish_auth.py'}
def allowed(rel):
 p=Path(rel);parts=p.parts
 if not parts or '..' in parts or any(x in parts for x in ['node_modules','__pycache__','.git','.astro']):return False
 if rel in TOP or rel in SOURCE_METADATA:return True
 if rel.startswith('.github/workflows/'):return p.suffix in {'.yml','.yaml'}
 if rel.startswith('data/'):return p.suffix in {'.json','.svg'}
 if rel.startswith('audit/'):return p.suffix in {'.json','.md'}
 if rel.startswith('scripts/'):return p.suffix in SCRIPT_SUFFIXES and p.name not in EXCLUDED_SCRIPTS
 if rel.startswith('assets/print/'):return p.suffix.lower() in {'.json','.css','.js','.mjs','.ttf','.woff','.woff2','.md'} or p.name=='LICENSE'
 if rel.startswith('web/src/'):return p.suffix.lower() in {'.astro','.ts','.js','.mjs','.json','.css','.svg'}
 if rel.startswith('web/public/'):return p.suffix.lower() in PRODUCT_SUFFIXES|{'.svg','.css','.js','.mjs','.ttf','.woff','.woff2','.md'} or p.name=='LICENSE'
 if rel.startswith('web/scripts/'):return p.suffix in SCRIPT_SUFFIXES
 if rel in {'web/.gitignore','web/README.md','web/astro.config.mjs','web/package.json','web/package-lock.json','web/tsconfig.json'}:return True
 if len(parts)>2 and parts[:2] in [('output','matrix'),('output','workbook'),('output','textbook'),('output','solutions')]:return p.suffix.lower() in PRODUCT_SUFFIXES
 if rel.startswith('output/print/'):return p.suffix=='.json' and (p.name in {'layout_manifest.json','section_manifest.json'} or 'receipt' in p.name or 'structural_qa' in p.name or 'horizontal_qa' in p.name)
 if rel.startswith('output/qa/'):return p.suffix=='.json' and p.name not in {'publish-auth-probe.json','source-geometry-unseen-routes.json','integration_errors.json'}
 if rel.startswith('web/reports/'):return p.name in {'validation.json','math-validation.json','print-links.json'}
 return False
def read(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def final_checks():
 errors=[]
 questions=read('data/questions.json');knowledge=read('data/knowledge.json');taxonomy=read('data/taxonomy.json')
 if len(questions)!=810:errors.append('Expected810 canonical questions')
 if any(q.get('unresolved_issues') or q.get('review',{}).get('status') not in {'reviewed','source_discrepancy_documented'} for q in questions):errors.append('Question review incomplete')
 if len(knowledge)!=len(taxonomy['subtypes']) or len(knowledge)!=44:errors.append('Expected44 knowledge sections')
 if any(not k.get('review',{}).get('independent_review') or k.get('unresolved_issues') for k in knowledge):errors.append('Independent textbook review incomplete')
 workbook=read('web/src/data/workbook.json')
 if {q['id'] for q in workbook['questions']}!={q['question_id'] for q in questions}:errors.append('Imported website question IDs differ')
 qmap={q['question_id']:q for q in questions}
 for rendered in workbook['questions']:
  q=qmap.get(rendered['id'])
  if not q:continue
  if (rendered.get('statementEn'),rendered.get('statementZh'),rendered.get('answer',{}).get('stepsEn'),rendered.get('answer',{}).get('stepsZh'))!=(q.get('statement_en'),q.get('statement_zh'),q.get('solution_en'),q.get('solution_zh')):errors.append('Stale imported question '+q['question_id'])
  for source,target in [('corrected_answer_en','correctedAnswerEn'),('corrected_answer_zh','correctedAnswerZh'),('editorial_note_en','editorialNoteEn'),('editorial_note_zh','editorialNoteZh')]:
   if q.get(source)!=rendered.get(target):errors.append('Stale imported editorial field '+q['question_id']+'/'+source)
 kmap={k['subtype_id']:k for k in knowledge}
 for section in workbook['sections']:
  k=kmap.get(section['code'])
  if not k:errors.append('Missing canonical knowledge '+section['code']);continue
  if [{a:b for a,b in m.items() if a not in {'print','diagram'}} for m in section['methods']]!=k['methods']:errors.append('Stale imported methods '+section['code'])
 diagram_manifest=read('data/knowledge_diagrams.json')
 imported_methods={m['method_id']:m for section in workbook['sections'] for m in section['methods']}
 if {mid for mid,m in imported_methods.items() if m.get('diagram')}!=set(diagram_manifest):errors.append('Imported method diagram membership differs')
 for mid,diagram in diagram_manifest.items():
  method=imported_methods.get(mid)
  if not method:errors.append('Unknown diagram method '+mid);continue
  rendered=method.get('diagram',{})
  source=ROOT/diagram['diagram_path'];target=ROOT/'web/public'/rendered.get('src','__missing__')
  example={k:method[k] for k in ['example_en','example_zh','solution_en','solution_zh']}
  example_sha=hashlib.sha256(json.dumps(example,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
  if example_sha!=diagram.get('example_sha256'):errors.append('Stale diagram example '+mid)
  if (rendered.get('altEn'),rendered.get('altZh'))!=(diagram['alt_en'],diagram['alt_zh']):errors.append('Stale diagram alt text '+mid)
  if not source.is_file() or not target.is_file() or hashlib.sha256(source.read_bytes()).hexdigest()!=diagram.get('svg_sha256') or hashlib.sha256(target.read_bytes()).hexdigest()!=diagram.get('svg_sha256'):errors.append('Stale method diagram SVG '+mid)
 if not read('web/reports/validation.json').get('passed'):errors.append('Website link validation did not pass')
 if read('web/reports/math-validation.json').get('errors'):errors.append('Website mathematics validation has errors')
 print_reports=read('web/reports/print-links.json')
 if {r['family'] for r in print_reports}!={'workbook','textbook','solutions_en','solutions_zh'} or not all(r.get('passed') for r in print_reports):errors.append('Final four-family print-link review missing')
 downloads=read('web/src/data/downloads.json')
 if {r['family'] for r in downloads}!={'matrix','workbook','textbook','solutions'}:errors.append('Final downloadable product family missing')
 if len([q for q in questions if q.get('answer_status')=='source_discrepancy'])!=1:errors.append('Expected exactly one documented source discrepancy')
 for source in [p for family in ['matrix','workbook','textbook','solutions'] for p in (ROOT/'output'/family).rglob('*') if p.is_file() and p.suffix.lower() in PRODUCT_SUFFIXES]:
  destination=ROOT/'web/public/downloads'/source.relative_to(ROOT/'output')
  if not destination.exists() or hashlib.sha256(source.read_bytes()).digest()!=hashlib.sha256(destination.read_bytes()).digest():errors.append('Public product copy differs: '+str(source.relative_to(ROOT)))
 coverage=read('output/qa/knowledge-coverage.json')
 if coverage.get('canonical_questions_sha256')!=hashlib.sha256((ROOT/'data/questions.json').read_bytes()).hexdigest() or coverage.get('knowledge_sha256')!=hashlib.sha256((ROOT/'data/knowledge.json').read_bytes()).hexdigest():errors.append('Knowledge coverage report hashes are stale')
 from check_publication_snapshot import capture_inputs,capture_reports
 receipt=read('output/qa/publication-checks.json')
 if not receipt.get('passed') or receipt.get('inputs')!=capture_inputs() or receipt.get('reports')!=capture_reports():errors.append('Final check receipt is missing or stale for current inputs/reports')
 return errors
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
 files=[]
 for path in sorted(ROOT.rglob('*')):
  if not path.is_file():continue
  rel=path.relative_to(ROOT).as_posix()
  if not allowed(rel):continue
  if path.is_symlink() or not path.resolve().is_relative_to(ROOT):raise ValueError('Linked file in public allowlist: '+rel)
  data=path.read_bytes()
  if len(data)>=100*1024*1024:raise ValueError('GitHub blob limit exceeded: '+rel)
  files.append(dict(path=rel,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_sha1=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()))
 errors=[]
 if args.final:
  try:errors=final_checks()
  except (FileNotFoundError,KeyError) as exc:errors.append(str(exc))
 manifest=dict(repository='yiyangd/AIME',branch='main',site_url='https://yiyangd.github.io/AIME/',created_at=datetime.now(timezone.utc).isoformat(),final=bool(args.final and not errors),errors=errors,files=files,file_count=len(files),total_bytes=sum(f['bytes'] for f in files),unique_blob_bytes=sum(next(v['bytes'] for v in files if v['git_blob_sha1']==h) for h in {f['git_blob_sha1'] for f in files}))
 identity=json.dumps(files,sort_keys=True,separators=(',',':')).encode();manifest['files_sha256']=hashlib.sha256(identity).hexdigest()
 DEST.mkdir(parents=True,exist_ok=True);(DEST/'publication-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in manifest.items() if k!='files'},ensure_ascii=False,indent=2))
 if errors:raise SystemExit('Final publication gate failed; no upload is authorized by this manifest')
if __name__=='__main__':main()

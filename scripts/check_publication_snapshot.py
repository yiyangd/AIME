"""Run final web/print checks and bind their reports to exact current input hashes."""
import hashlib,json,os,shutil,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def hashes(paths):return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths)) if p.is_file()}
def capture_inputs():
 paths=[ROOT/p for p in ['data/questions.json','data/taxonomy.json','data/knowledge.json','web/package.json','web/package-lock.json','web/astro.config.mjs','web/tsconfig.json','.github/workflows/pages.yml']]
 for folder in ['web/src','web/public','web/scripts']:
  paths.extend(p for p in (ROOT/folder).rglob('*') if p.is_file())
 for family in ['matrix','workbook','textbook','solutions']:
  paths.extend(p for p in (ROOT/'output'/family).rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.xlsx','.html'})
 paths.extend(p for p in (ROOT/'output/print').rglob('*.json') if p.name in {'layout_manifest.json','section_manifest.json'})
 return hashes(paths)
def capture_reports():
 paths=[ROOT/p for p in ['web/reports/validation.json','web/reports/math-validation.json','web/reports/print-links.json','output/qa/coverage.json','output/qa/knowledge-coverage.json']]
 paths.extend((ROOT/'output/print').glob('*receipt*.json'))
 paths.extend((ROOT/'output/qa').glob('*visual*.json'))
 return hashes(paths)
def main():
 before=capture_inputs();commands=[];passed=False;failure=None
 npm=shutil.which('npm.cmd' if os.name=='nt' else 'npm')
 if not npm:raise SystemExit('npm is required for final website checks')
 try:
  for task in ['check','check-math','build','validate']:
   cmd=[npm,'run',task];print('Running npm run '+task,flush=True)
   subprocess.run(cmd,cwd=ROOT/'web',check=True);commands.append('npm run '+task)
  subprocess.run([sys.executable,'scripts/verify-print-links.py'],cwd=ROOT/'web',check=True);commands.append('python scripts/verify-print-links.py')
  if capture_inputs()!=before:raise RuntimeError('Publication input changed during final checks; rerun after the freeze')
  passed=True
 except (subprocess.CalledProcessError,RuntimeError) as exc:failure=str(exc)
 receipt=dict(passed=passed,created_at=datetime.now(timezone.utc).isoformat(),commands=commands,inputs=before,reports=capture_reports(),failure=failure)
 output=ROOT/'output/qa/publication-checks.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'passed':passed,'input_files':len(before),'completed_checks':commands,'failure':failure},ensure_ascii=False))
 if not passed:raise SystemExit(1)
if __name__=='__main__':main()

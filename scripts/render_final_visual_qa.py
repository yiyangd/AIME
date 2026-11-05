"""Render every final question-book page with Poppler and build contact sheets."""
import argparse,json,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
POPPLER=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
ap=argparse.ArgumentParser();ap.add_argument('kind',choices=['workbook','solutions_en','solutions_zh','textbook','matrix']);a=ap.parse_args()
if a.kind=='matrix':
 files=sorted((ROOT/'output/matrix').glob('*.pdf'))
else:
 files=[ROOT/json.loads((ROOT/f'output/print/{a.kind}/layout_manifest.json').read_text(encoding='utf8'))['output']]
out=ROOT/'output/qa/rendered'/a.kind;out.mkdir(parents=True,exist_ok=True);report=[]
for source in files:
 target=out/source.stem;target.mkdir(parents=True,exist_ok=True)
 subprocess.run([str(POPPLER),'-r','35','-png',str(source),str(target/'p')],check=True,capture_output=True)
 imgs=sorted(target.glob('p-*.png'));n=len(PdfReader(source).pages);assert len(imgs)==n
 for start in range(0,n,64):
  batch=imgs[start:start+64];w,h=248,370;sheet=Image.new('RGB',(8*w,8*h),'#d9dee6');d=ImageDraw.Draw(sheet)
  for i,path in enumerate(batch):
   im=Image.open(path).convert('RGB');im.thumbnail((w-8,h-22))
   x=(i%8)*w+(w-im.width)//2;y=(i//8)*h+18;sheet.paste(im,(x,y));d.text(((i%8)*w+8,(i//8)*h+3),str(start+i+1),fill='black')
  sheet.save(target/f'contact-{start+1:04d}-{min(n,start+64):04d}.jpg',quality=88)
 for page in ([1,2,min(3,n),min(18,n),min(19,n)] if a.kind!='matrix' else range(1,min(n,3)+1)):
  subprocess.run([str(POPPLER),'-f',str(page),'-l',str(page),'-r','110','-png','-singlefile',str(source),str(target/f'detail-{page:04d}')],check=True,capture_output=True)
 report.append({'pdf':str(source.relative_to(ROOT)),'pages':n,'all_pages_rendered':len(imgs),'contact_sheets':len(list(target.glob('contact-*.jpg')))})
 print(json.dumps(report[-1]),flush=True)
(out/'render-report.json').write_text(json.dumps(report,indent=2),encoding='utf8')

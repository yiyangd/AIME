"""Check imported PDF anchors against real files, manifests and printed question IDs."""
from pathlib import Path
import json,re,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2]; WEB=ROOT/'web'
data=json.loads((WEB/'src/data/workbook.json').read_text(encoding='utf8'))
qmap={q['id']:q for q in data['questions']}; smap={s['code']:s for s in data['sections']}
report=[]; readers={}
def published(value):
 p=Path(value);p=p if p.is_absolute() else ROOT/p
 return WEB/'public/downloads'/p.relative_to(ROOT/'output')
def pdf(path):
 if path not in readers:readers[path]=PdfReader(path)
 return readers[path]
for kind in ['workbook','textbook','solutions_en','solutions_zh']:
 folder=ROOT/'output/print'/kind;mp=folder/'layout_manifest.json'
 if not mp.exists():continue
 manifest=json.loads(mp.read_text(encoding='utf8'));main=published(manifest['output'])
 assert main.is_file(),main
 reader=pdf(main);qcount=0;methodcount=0;sectioncount=0
 assert len(reader.pages)==manifest['pdf_pages'],(kind,'main page count')
 for q in manifest.get('placements',[]):
  ref=qmap[q['question_id']]['print'][kind]
  assert ref['physicalPage']==q['physical_page'] and ref['bodyPage']==q['body_page']
  assert int(ref['href'].split('#page=')[1])==q['physical_page']
  assert q['physical_page']==manifest['front_pages']+q['body_page']
  text=reader.pages[q['physical_page']-1].extract_text()
  assert q['question_id'] in text,(kind,q['question_id'],'printed ID missing at URL anchor')
  qcount+=1
 for mid,p in manifest.get('method_locations',{}).items():
  methods=[m for s in data['sections'] for m in s['methods'] if m['method_id']==mid]
  assert len(methods)==1,(kind,mid)
  ref=methods[0]['print'][kind]
  assert ref['physicalPage']==p['physical_page'] and ref['bodyPage']==p['body_page']
  assert 1<=p['physical_page']<=len(reader.pages)
  text=reader.pages[p['physical_page']-1].extract_text()
  assert mid in text,(kind,mid,'printed method ID missing at URL anchor')
  methodcount+=1
 split=folder/'section_manifest.json'
 if split.exists():
  for section in json.loads(split.read_text(encoding='utf8')):
   ref=smap[section['subtype_id']]['print'][kind]
   splitpdf=published(section['output'])
   assert splitpdf.is_file(),splitpdf
   assert ref['href'].split('#')[0]==splitpdf.relative_to(WEB/'public').as_posix()
   assert len(pdf(splitpdf).pages)==section['page_count']==ref['pageCount']
   assert len(section['source_physical_pages'])==section['page_count']
   sectioncount+=1
 report.append(dict(family=kind,pdf_sha256=hashlib.sha256(main.read_bytes()).hexdigest(),layout_manifest_sha256=hashlib.sha256(mp.read_bytes()).hexdigest(),pdf_pages=len(reader.pages),question_anchors=qcount,method_anchors=methodcount,section_files=sectioncount,passed=True))
out=WEB/'reports/print-links.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))

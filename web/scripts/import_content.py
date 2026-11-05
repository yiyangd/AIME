"""Import the canonical AIME pack without reading any external source project."""
from pathlib import Path
import json, collections, shutil,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
WEB=ROOT/'web'
def read(name,default):
 p=ROOT/'data'/name
 return json.loads(p.read_text(encoding='utf-8-sig')) if p.exists() else default
def array(value,key):return value.get(key,[]) if isinstance(value,dict) else value
tax=read('taxonomy.json',{'categories':[],'subtypes':[]})
qs=array(read('questions.json',[]),'questions')
knowledge=array(read('knowledge.json',[]),'sections')
if isinstance(knowledge,dict):knowledge=list(knowledge.values())
kmap={k.get('subtype_id',k.get('section_id','')):k for k in knowledge}
knowledge_diagrams=read('knowledge_diagrams.json',{})

def diagram_asset(relative):
 source=ROOT/relative
 if not source.exists():raise FileNotFoundError(source)
 if not source.resolve().is_relative_to((ROOT/'data/diagrams').resolve()):raise ValueError('Only original data/diagrams assets may enter the public site')
 if source.suffix.lower()!='.svg':raise ValueError('Original diagram assets must be SVG')
 destination=WEB/'public/diagrams'/source.name;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,destination)
 svg=source.read_text(encoding='utf8');box=re.search(r'viewBox=[\"\']([\d\s.\-]+)[\"\']',svg)
 dims=box.group(1).split() if box else ['0','0','720','400']
 return dict(src='diagrams/'+source.name,width=int(float(dims[2])),height=int(float(dims[3])))

def method_for_web(method):
 result=dict(method,print=method_print.get(method.get('method_id',''),{}))
 diagram=knowledge_diagrams.get(method.get('method_id',''))
 if diagram:
  if diagram.get('example_sha256'):
   example={k:method[k] for k in ['example_en','example_zh','solution_en','solution_zh']}
   digest=hashlib.sha256(json.dumps(example,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
   if digest!=diagram['example_sha256']:raise ValueError('Stale method diagram for '+method['method_id'])
  if diagram.get('svg_sha256') and hashlib.sha256((ROOT/diagram['diagram_path']).read_bytes()).hexdigest()!=diagram['svg_sha256']:raise ValueError('Diagram SVG hash mismatch for '+method['method_id'])
  result['diagram']=dict(diagram_asset(diagram['diagram_path']),altEn=diagram['alt_en'],altZh=diagram['alt_zh'])
 return result
# Publish final deliverables recursively; render inputs and source material stay private.
downloads=[];published={}
for family in ['matrix','workbook','textbook','solutions']:
 folder=ROOT/'output'/family
 if not folder.exists():continue
 for source in sorted(folder.rglob('*')):
  if not source.is_file() or source.suffix.lower() not in ['.pdf','.xlsx','.html']:continue
  relative=source.relative_to(folder);href=(Path('downloads')/family/relative).as_posix()
  destination=WEB/'public'/href;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,destination)
  published[source.resolve()]=href
  downloads.append(dict(name=source.stem.replace('_',' '),href=href,family=family,format=source.suffix[1:].upper(),bytes=source.stat().st_size,section='sections' in relative.parts))
def published_href(value):
 if not value:return None
 path=Path(value)
 if not path.is_absolute():path=ROOT/path
 return published.get(path.resolve())
question_print={};section_print={};method_print={}
for kind in ['workbook','textbook','solutions_en','solutions_zh']:
 folder=ROOT/'output/print'/kind;manifest=folder/'layout_manifest.json'
 if not manifest.exists():continue
 layout=json.loads(manifest.read_text(encoding='utf8'));main=published_href(layout.get('output'))
 if not main:continue
 for p in layout.get('pages',[]):
  code=p.get('section_id');unit=p.get('method_id') or p.get('unit_id')
  ref=dict(href=main+'#page='+str(p['physical_page']),bodyPage=p['body_page'],physicalPage=p['physical_page'])
  if code:section_print.setdefault(code,{}).setdefault(kind,ref)
  if unit:method_print.setdefault(unit,{}).setdefault(kind,ref)
 for q in layout.get('placements',[]):
  question_print.setdefault(q['question_id'],{}).setdefault(kind,dict(href=main+'#page='+str(q['physical_page']),bodyPage=q['body_page'],physicalPage=q['physical_page']))
 for mid,p in layout.get('method_locations',{}).items():
  method_print.setdefault(mid,{})[kind]=dict(href=main+'#page='+str(p['physical_page']),bodyPage=p['body_page'],physicalPage=p['physical_page'])
 splits=folder/'section_manifest.json'
 if splits.exists():
  for p in json.loads(splits.read_text(encoding='utf8')):
   href=published_href(p.get('output'))
   if href:section_print.setdefault(p['subtype_id'],{}).setdefault(kind,{}).update(href=href,pageCount=p.get('page_count'))
categories=sorted(tax['categories'],key=lambda c:c.get('order',0))
active={q['primary']['subtype_id'] for q in qs}
subtypes=sorted([s for s in tax['subtypes'] if s['id'] in active],key=lambda s:(next(c.get('order',0) for c in categories if c['id']==s['category_id']),s.get('order',s['id'])))
cmap={c['id']:i+1 for i,c in enumerate(categories)}
chapters=[];sections=[];questions=[]
for c in categories:
 members=[s for s in subtypes if s['category_id']==c['id']]
 if not members:continue
 chapters.append(dict(id=cmap[c['id']],code=c['id'],titleEn=c['name_en'],titleZh=c['name_zh'],questionCount=sum(q['primary']['category_id']==c['id'] for q in qs),sectionCount=len(members)))
for s in subtypes:
 members=sorted([q for q in qs if q['primary']['subtype_id']==s['id']],key=lambda q:(q['exam_year'],q['exam_form'],q['number']))
 kn=kmap.get(s['id'],{})
 secid=str(s.get('section_number',s['id']))
 sections.append(dict(id=secid,slug=s['id'].lower(),chapterId=cmap[s['category_id']],code=s['id'],titleEn=s['name_en'],titleZh=s['name_zh'],questionIds=[q['question_id'] for q in members],partCounts=dict(collections.Counter(q.get('practice_part','A' if q['number']<=5 else 'B' if q['number']<=10 else 'C') for q in members)),definitionEn=kn.get('introduction_en',s.get('definition_en','')),definitionZh=kn.get('introduction_zh',s.get('definition_zh','')),methods=[method_for_web(m) for m in kn.get('methods',[])],prerequisites=kn.get('prerequisites',[]),print=section_print.get(s['id'],{})))
 for q in members:
  image=q.get('diagram') or q.get('image')
  if image and not isinstance(image,dict):image=None
  diagram_path=q.get('diagram_path')
  if diagram_path:
   image=diagram_asset(diagram_path)
  questions.append(dict(id=q['question_id'],year=q['exam_year'],form=q['exam_form'],number=q['number'],chapterId=cmap[s['category_id']],sectionId=secid,part=q.get('practice_part','A' if q['number']<=5 else 'B' if q['number']<=10 else 'C'),statementEn=q.get('statement_en',''),statementZh=q.get('statement_zh',''),sourceUrl=q.get('source_url','https://live.poshenloh.com/past-contests'),answer=dict(value=str(q.get('answer','')).zfill(3),stepsEn=q.get('solution_en',[]),stepsZh=q.get('solution_zh',[])),secondary=[t['subtype_id'] if isinstance(t,dict) else t for t in q.get('secondary',[])],reasonEn=q['primary'].get('reason_en',''),reasonZh=q['primary'].get('reason_zh',''),reviewStatus=q.get('review',{}).get('status',''),**({'image':image} if image and image.get('src') else {})))
  if q.get('answer_status')=='source_discrepancy':
   questions[-1].update(answerStatus='source_discrepancy',correctedAnswerEn=q['corrected_answer_en'],correctedAnswerZh=q['corrected_answer_zh'],sourceAnswer=str(q.get('source_answer',q['answer'])),editorialNoteEn=q['editorial_note_en'],editorialNoteZh=q['editorial_note_zh'])
  questions[-1]['print']=question_print.get(q['question_id'],{})
for s in sections:
 for part in 'ABC':s['partCounts'].setdefault(part,0)
target=WEB/'src/data/workbook.json';target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(dict(chapters=chapters,sections=sections,questions=questions),ensure_ascii=False,indent=2),encoding='utf-8')
(WEB/'src/data/downloads.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Imported {len(questions)} questions, {len(chapters)} chapters, {len(sections)} sections; {len(downloads)} downloads.')

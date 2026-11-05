"""Rebuild AIME print products from the shared, editable bilingual data.

Uses ReportLab for vector covers, atlas, contents and matrices. Chromium prints
locally bundled KaTeX mathematics; pypdf assembles linked, bookmarked books.
No raw source problem text or images are included in the public products.
"""
from __future__ import annotations
import argparse, csv, hashlib, html, json, math, os, re, shutil, subprocess, sys
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf'; WORK=ROOT/'output/print'; ASSETS=ROOT/'assets/print'
W,H=A4; M=39.7
BLUE=colors.HexColor('#163E65'); MID=colors.HexColor('#447AA2')
ORANGE=colors.HexColor('#E77835'); INK=colors.HexColor('#193850')
MUTED=colors.HexColor('#647684'); RULE=colors.HexColor('#DCE5EA')
PALE=colors.HexColor('#EDF4F8'); CREAM=colors.HexColor('#FFFDFA')
PARTS={'A':'Q1-Q5','B':'Q6-Q10','C':'Q11-Q15'}
DATE_RANGE='2000-2026'

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qid(q):return q['question_id']
def qlabel(q):return f"{q['exam_year']} {q.get('exam_form','')} Q{q['number']:02}"
def sname(s,lang):return s.get('name_'+lang,s.get('title_'+lang,s['id']))
def steps(q,lang):
    v=q.get('solution_'+lang,[])
    if isinstance(v,dict):v=v.get('steps',[])
    return [v] if isinstance(v,str) else v
def paragraph(c,text,x,top,width,size=10,font='Body',color=INK,leading=None):
    p=Paragraph(text,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.35,textColor=color,wordWrap='CJK'))
    _,h=p.wrap(width,10000)
    if c:p.drawOn(c,x,H-top-h)
    return h
def text(c,t,x,top,size=10,font='Body',color=INK):
    c.setFont(font,size);c.setFillColor(color);c.drawString(x,H-top,t)
def line(c,x1,t1,x2,t2,col=RULE,width=.6):
    c.setStrokeColor(col);c.setLineWidth(width);c.line(x1,H-t1,x2,H-t2)

def register_fonts():
    for name,filename in [('Body','arial.ttf'),('Bold','arialbd.ttf'),('Serif','times.ttf'),('Serif-Bold','timesbd.ttf'),('Italic','timesi.ttf'),('ZH','msyh.ttc'),('ZH-Bold','msyhbd.ttc')]:
        pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/filename),subfontIndex=0))

def setup_assets():
    ASSETS.mkdir(parents=True,exist_ok=True)
    if not (ASSETS/'katex/katex.min.js').exists():
        candidates=[ROOT/'node_modules/katex/dist',Path('D:/AMC8_Codex/output/AMC10_AMC12_A_Day1_English_Full_v2/source/vendor/node_modules/katex/dist')]
        source=next((p for p in candidates if (p/'katex.min.js').exists()),None)
        if source is None:raise FileNotFoundError('Install KaTeX locally or set up assets/print/katex before printing.')
        shutil.copytree(source,ASSETS/'katex',dirs_exist_ok=True)
    manifest={'katex':'assets/print/katex','license':'assets/print/katex/LICENSE','purpose':'Local mathematical typesetting; no network dependency'}
    license_path=Path('D:/AMC8_Codex/output/AMC10_AMC12_A_Day1_English_Full_v2/source/vendor/node_modules/katex/LICENSE')
    if license_path.exists() and not (ASSETS/'katex/LICENSE').exists():shutil.copy2(license_path,ASSETS/'katex/LICENSE')
    save(ASSETS/'manifest.json',manifest)

def cover(c,subtitle,zh,counts):
    """Editable vector interpretation of the AMC8 orange/navy STEMHUB cover."""
    c.setFillColor(CREAM);c.rect(0,0,W,H,fill=1,stroke=0)
    # Broad blue and orange diagonals preserve the reference cover's geometry.
    p=c.beginPath();p.moveTo(0,H*.20);p.curveTo(W*.25,H*.29,W*.56,H*.35,W,H*.60)
    p.lineTo(W,H*.20);p.curveTo(W*.72,-40,W*.22,H*.09,0,H*.02);p.close()
    c.setFillColor(BLUE);c.drawPath(p,fill=1,stroke=0)
    p=c.beginPath();p.moveTo(0,H*.85);p.curveTo(W*.10,H*.77,-15,H*.44,W*.46,H*.28)
    p.lineTo(W*.38,H*.21);p.curveTo(W*.02,H*.42,-20,H*.48,0,H*.85);p.close()
    c.setFillColor(ORANGE);c.drawPath(p,fill=1,stroke=0)
    c.setFillColor(colors.HexColor('#0B2E50'));c.rect(0,0,W,H*.12,fill=1,stroke=0)
    # Infinity mark and brand are vector text and paths.
    c.setStrokeColor(colors.HexColor('#00A7E8'));c.setLineWidth(1)
    for shift in [0,2,4]:
        p=c.beginPath();p.moveTo(W-99,H-50-shift);p.curveTo(W-90,H-31-shift,W-70,H-31-shift,W-59,H-50-shift)
        p.curveTo(W-47,H-69-shift,W-29,H-69-shift,W-22,H-50-shift)
        p.curveTo(W-29,H-31-shift,W-47,H-31-shift,W-59,H-50-shift)
        p.curveTo(W-70,H-69-shift,W-90,H-69-shift,W-99,H-50-shift);c.drawPath(p)
    text(c,'STEMHUB',W-96,85,13,'Body',colors.HexColor('#00A7E8'))
    c.setFont('Serif-Bold',112);c.setFillColor(BLUE);c.drawCentredString(W/2,H-287,'AIME')
    line(c,122,323,177,323,BLUE,1);line(c,W-177,323,W-122,323,BLUE,1)
    text(c,'STEMHUB',196,330,18,'Serif-Bold',BLUE)
    text(c,'自研教材',304,329,14,'ZH-Bold',BLUE)
    c.setFillColor(BLUE);c.setFont('Bold',12);c.drawCentredString(W/2,H-365,subtitle.upper())
    c.setFont('ZH',10.8);c.drawCentredString(W/2,H-389,zh)
    text(c,'Think Deeply.',126,443,22,'Italic',BLUE)
    text(c,'Solve Beautifully.',126,468,22,'Italic',BLUE)
    line(c,130,485,161,485,ORANGE,3)
    text(c,'启发思维，优雅解题',130,512,13,'ZH-Bold',BLUE)
    # Circle, triangle, coordinate parabola, cube, all scalable vectors.
    c.setStrokeColor(colors.white);c.setLineWidth(.75)
    cx,cy,r=470,236,79;c.circle(cx,cy,r,fill=0,stroke=1)
    pts=[(470,315),(401,196),(539,196)]
    for a,b in [(0,1),(1,2),(2,0)]:c.line(*pts[a],*pts[b])
    c.setDash(3,3);c.line(470,315,470,157);c.setDash()
    c.setFillColor(ORANGE)
    for x,y in pts:c.circle(x,y,2.5,fill=1,stroke=0)
    c.setFillColor(colors.white);c.setFont('Italic',12)
    for (x,y),t in zip(pts,['A','B','C']):c.drawString(x+4,y+5,t)
    # The lower-left wire cube.
    a=[(50,108),(105,137),(160,103),(106,73),(50,54),(105,25),(160,51),(106,83)]
    c.setStrokeColor(colors.white)
    for i,j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,7),(2,6),(3,5)]:c.line(*a[i],*a[j])
    c.setStrokeColor(ORANGE);c.setLineWidth(.8);c.line(315,47,315,160);c.line(235,62,400,62)
    p=c.beginPath();p.moveTo(255,150);p.curveTo(285,28,345,28,375,150);c.drawPath(p)
    c.setFillColor(colors.white);c.setFont('Bold',12);c.drawRightString(W-35,35,DATE_RANGE)
    c.setFont('Body',8);c.drawRightString(W-35,20,f"{counts['questions']} problems  /  {counts['sections']} sections")
    c.showPage()

def atlas_plan(categories,sections):
    pages=[];cols=[[],[]];heights=[0,0];capacity=H-150
    for cat in categories:
        ss=[s for s in sections if s['category_id']==cat['id']]
        for start in range(0,len(ss),24):
            subset=ss[start:start+24];hh=43+len(subset)*20+9
            idx=min(range(2),key=lambda x:heights[x])
            if heights[idx]+hh>capacity:
                pages.append(cols);cols=[[],[]];heights=[0,0];idx=0
            cols[idx].append((cat,subset));heights[idx]+=hh
    if any(cols):pages.append(cols)
    return pages

def atlas(c,categories,sections,question_count,plan):
  for page_index,columns in enumerate(plan):
    text(c,'The Mathematics Atlas',M,60,23,'Bold',BLUE)
    text(c,'章节与考点总览',M,83,12.8,'ZH',ORANGE)
    text(c,f"{len(categories):02} CHAPTERS   {len(sections):02} SECTIONS",W-240,52,9,'Bold',MID)
    colw=(W-2*M-16)/2
    for ix,items in enumerate(columns):
        top=106;x=M+ix*(colw+16)
        for cat,ss in items:
            hh=43+len(ss)*20
            c.setStrokeColor(RULE);c.setFillColor(colors.white);c.roundRect(x,H-top-hh,colw,hh,7,fill=1,stroke=1)
            text(c,str(categories.index(cat)+1).zfill(2),x+10,top+21,12,'Bold',ORANGE)
            paragraph(c,escape(sname(cat,'en')),x+37,top+7,colw-45,10,'Bold',BLUE)
            text(c,sname(cat,'zh'),x+37,top+33,9,'ZH',MID)
            yy=top+46
            for s in ss:
                text(c,s['section_number'],x+11,yy,8,'Bold',ORANGE)
                paragraph(c,escape(sname(s,'en')),x+39,yy-9,colw-47,8.1,'Body',INK,10)
                text(c,sname(s,'zh'),x+39,yy+10,7.8,'ZH',MUTED)
                yy+=20
            top+=hh+9
    line(c,M,H-34,W-M,H-34)
    text(c,'AIME  /  '+DATE_RANGE,M,H-20,8,'Bold',MID)
    c.setFont('Body',8);c.setFillColor(MUTED);c.drawRightString(W-M,20,f'{question_count} problems; English and Chinese')
    c.showPage()

def toc_plan(categories,sections,groups,locations,kind):
    pages=[];items=[];top=99;last=None
    def fresh():
        nonlocal items,top
        if items:pages.append(items)
        items=[];top=99
    for s in sections:
        if not groups.get(s['id']):continue
        cat=next(c for c in categories if c['id']==s['category_id'])
        if top+115>H-50:fresh()
        if cat['id']!=last:
            items.append({'kind':'chapter','category':cat,'top':top});top+=43;last=cat['id']
        label=f"Section {s['section_number']}. {sname(s,'en')} ({s['id']})"
        hh=paragraph(None,escape(label),M,top,W-2*M-30,10.3,'Bold')
        first=groups[s['id']][0]
        target=qid(first) if kind!='textbook' else s['id']
        items.append({'kind':'section','section':s,'text':label,'target':target,'top':top,'height':hh});top+=hh+3
        items.append({'kind':'zh','text':sname(s,'zh'),'top':top});top+=18
        if kind=='textbook':top+=9;continue
        for part in PARTS:
            qs=[q for q in groups[s['id']] if q['practice_part']==part]
            if not qs:continue
            if top+43>H-45:fresh()
            items.append({'kind':'part','part':part,'top':top});top+=17
            for start in range(0,len(qs),3):
                if top+16>H-45:fresh()
                for j,q in enumerate(qs[start:start+3]):items.append({'kind':'question','question':q,'target':qid(q),'index':j,'top':top})
                top+=17
            top+=5
        top+=10
    fresh();return pages

def draw_toc(c,plan,locations,atlas_count=1):
    links=[]
    for pi,items in enumerate(plan):
        text(c,'Contents',M,57,21,'Bold');text(c,'目录',M+112,57,13,'ZH')
        c.setFont('Body',8.5);c.setFillColor(MUTED);c.drawRightString(W-M,H-57,f'{pi+1} / {len(plan)}')
        line(c,M,73,W-M,73)
        for it in items:
            top=it['top'];kind=it['kind']
            if kind=='chapter':
                ca=it['category'];text(c,sname(ca,'en'),M,top+12,12,'Bold');text(c,sname(ca,'zh'),M,top+29,10,'ZH')
            elif kind=='section':
                paragraph(c,escape(it['text']),M,top,W-2*M-30,10.3,'Bold')
                c.setFont('Body',9);c.setFillColor(INK);c.drawRightString(W-M,H-top-11,str(locations[it['target']]))
                links.append({'front_page':1+atlas_count+pi,'target':it['target'],'rect':[M,H-top-it['height'],W-M,H-top]})
            elif kind=='zh':text(c,it['text'],M,top+10,9,'ZH',MUTED)
            elif kind=='part':text(c,f"Part {it['part']} ({PARTS[it['part']]})",M+8,top+10,9,'Bold')
            elif kind=='question':
                cw=(W-2*M-20)/3;x=M+10+it['index']*cw
                text(c,qlabel(it['question']),x,top+9,8.6)
                c.setFont('Body',8);c.setFillColor(MUTED);c.drawRightString(x+cw-9,H-top-9,str(locations[it['target']]))
                links.append({'front_page':1+atlas_count+pi,'target':it['target'],'rect':[x,H-top-13,x+cw-5,H-top+1]})
        text(c,'Click a section or question to open its page.',M,H-26,8,'Body',MUTED)
        c.showPage()
    return links

def block(text_,cls='prose'):
    return f'<div class="block {cls}">{html.escape(str(text_))}</div>'
def steps_blocks(vals):
    result=[]
    for i,v in enumerate(vals,1):
        if isinstance(v,dict):v=v.get('text',v.get('content',str(v)))
        result.append(block(f'{i}. {v}','step'))
    return result

def diagram_block(record):
    """Only original, project-owned diagrams are printable, never raw sources."""
    svg=record.get('diagram_svg')
    if record.get('diagram_path'):
        diagram=(ROOT/record['diagram_path']).resolve()
        allowed=(ROOT/'data/diagrams').resolve()
        if not diagram.is_relative_to(allowed) or diagram.suffix.lower()!='.svg':
            raise ValueError(f'Printable diagram must be an original SVG in data/diagrams: {diagram}')
        if record.get('svg_sha256') and sha(diagram)!=record['svg_sha256']:
            raise ValueError(f'Diagram changed after its construction check: {diagram}')
        svg=diagram.read_text(encoding='utf-8-sig')
    return '<div class="block diagram">'+svg+'</div>' if svg else None

def make_units(kind,questions,sections,categories,knowledge,groups,wb_locations=None):
    units=[];sd={s['id']:s for s in sections};cd={c['id']:c for c in categories}
    if kind=='textbook':
        kd={k['subtype_id']:k for k in knowledge}
        diagram_manifest=read(ROOT/'data/knowledge_diagrams.json') if (ROOT/'data/knowledge_diagrams.json').exists() else {}
        for s in sections:
            if s['id'] not in groups:continue
            if s['id'] not in kd:raise ValueError(f"Missing textbook content {s['id']}")
            k=kd[s['id']];methods=k.get('methods',[])
            if not methods:raise ValueError(f"No textbook methods for {s['id']}")
            for mi,m in enumerate(methods):
                method_id=m.get('method_id',f"{s['id']}-M{mi+1:02}")
                title=m.get('title_en',sname(s,'en'));zh=m.get('title_zh',sname(s,'zh'))
                bs=[]
                if mi==0:
                    for lang in ['en','zh']:
                        if k.get('introduction_'+lang):bs.append(block(k['introduction_'+lang],'prose '+lang))
                bs.append(block(title,'method-title'));bs.append(block(zh,'zh'))
                for lang in ['en','zh']:
                    vals=m.get('steps_'+lang,[])
                    if vals:
                        bs.append(block('Procedure' if lang=='en' else '通用步骤','method-title'))
                        bs+=steps_blocks(vals)
                if m.get('example_en'):bs.append(block('Example. '+m['example_en'],'example en'))
                if m.get('example_zh'):bs.append(block('例题：'+m['example_zh'],'example zh'))
                diagram_record=dict(m)
                if method_id in diagram_manifest:
                    extra=diagram_manifest[method_id]
                    example_sha=hashlib.sha256(json.dumps({key:m[key] for key in ['example_en','example_zh','solution_en','solution_zh']},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
                    if extra.get('example_sha256')!=example_sha:raise ValueError(f'Stale example diagram: {method_id}')
                    diagram_record.update(extra)
                diagram=diagram_block(diagram_record)
                if diagram:bs.append(diagram)
                for lang in ['en','zh']:
                    vals=m.get('solution_'+lang,[])
                    if vals:
                        bs.append(block('Worked solution' if lang=='en' else '例题解析','method-title'))
                        bs+=steps_blocks(vals)
                if m.get('tip_en'):bs.append(block(m['tip_en'],'tip en'))
                if m.get('tip_zh'):bs.append(block(m['tip_zh'],'tip zh'))
                for lang in ['en','zh']:
                    extra=m.get('extensions_'+lang,[])
                    if isinstance(extra,str):extra=[extra]
                    for value in extra:bs.append(block(value,'tip '+lang))
                refs=m.get('question_ids',m.get('practice_ids',[]))
                if not refs and len(methods)==1:refs=k.get('practice_ids',[qid(q) for q in groups[s['id']]])
                if refs:
                    route=[]
                    for r in refs:
                        route.append(r+(f" (WB p. {wb_locations[r]})" if wb_locations and r in wb_locations else ''))
                    bs.append(block('Practice / 配套练习: '+', '.join(route),'practice'))
                units.append({'id':method_id,'method_id':method_id,'section_id':s['id'],'header':f"Section {s['section_number']}  {sname(s,'en')}",'subtitle':sname(s,'zh'),'label':f"Method {mi+1} / 方法 {mi+1}  [{method_id}]",'blocks':bs})
        return units
    for s in sections:
        for q in groups.get(s['id'],[]):
            bs=[]
            if kind=='workbook':
                for lang in ['en','zh']:
                    if not q.get('statement_'+lang):raise ValueError(f"Missing {lang} statement for {qid(q)}")
                    bs.append(block(q['statement_'+lang],'statement '+lang))
                diagram=diagram_block(q)
                if diagram:bs.append(diagram)
                bs.append(block('Mathematical statement reworded for this bilingual edition. 原数学条件的双语重述。','source-note'))
                if q.get('source_url'):bs.append(f'<div class="block source-note"><a href="{html.escape(q["source_url"],quote=True)}">Source / 原题来源</a></div>')
                bs.append('<div class="block working">Working / 解题过程</div>')
            else:
                lang=kind.split('_')[-1]
                if not steps(q,lang):raise ValueError(f"Missing {lang} solution for {qid(q)}")
                if q.get('answer_status')=='source_discrepancy':
                    corrected=q.get('corrected_answer_'+lang)
                    if not corrected:raise ValueError(f'Missing corrected {lang} answer for {qid(q)}')
                    bs.append(block(('Corrected result: ' if lang=='en' else '核验后的结果：')+str(corrected),'answer'))
                    historical=str(q.get('source_answer',q['answer'])).zfill(3)
                    bs.append(block(('Historical answer key: ' if lang=='en' else '历史参考答案：')+historical,'source-note'))
                    if q.get('editorial_note_'+lang):bs.append(block(q['editorial_note_'+lang],'tip'))
                else:
                    answer=str(q['answer']).zfill(3)
                    bs.append(block(('Answer: ' if lang=='en' else '答案：')+answer,'answer'))
                diagram=diagram_block(q)
                if diagram:bs.append(diagram)
                bs+=steps_blocks(steps(q,lang))
                check=q.get('check_'+lang)
                if check:bs.append(block(('Check. ' if lang=='en' else '检验：')+check,'tip'))
                if q.get('source_url'):bs.append(f'<div class="block source-note"><a href="{html.escape(q["source_url"],quote=True)}">Source / 来源</a></div>')
            units.append({'id':qid(q),'section_id':s['id'],'header':f"Section {s['section_number']}  {sname(s,'en')}",'subtitle':sname(s,'zh'),'label':f"[{qid(q)}]  |  Part {q['practice_part']} ({PARTS[q['practice_part']]})",'blocks':bs})
    return units

def render_body(kind,units):
    folder=WORK/kind;folder.mkdir(parents=True,exist_ok=True)
    spec={'kind':kind,'date_range':DATE_RANGE,'units':units,'asset_root':str(ASSETS),'output':str(folder/'body.pdf'),'html':str(folder/'body.html'),'metadata':str(folder/'body-layout.json')}
    save(folder/'render-spec.json',spec)
    cmd=[os.environ.get('AIME_NODE','node'),str(ROOT/'scripts/render_print.cjs'),str(folder/'render-spec.json')]
    subprocess.run(cmd,check=True,cwd=ROOT)
    return read(folder/'body-layout.json')

def build_book(kind,questions,sections,categories,knowledge,groups,wb_locations=None):
    units=make_units(kind,questions,sections,categories,knowledge,groups,wb_locations)
    layout=render_body(kind,units);locations={}
    for p in layout['pages']:
        locations.setdefault(p['unit_id'],p['body_page'])
        if kind=='textbook':locations.setdefault(p['section_id'],p['body_page'])
    titles={'workbook':('Topic-Based Practice Workbook','专题练习册'), 'solutions_en':('Step-by-Step Solutions','英文逐题解析'), 'solutions_zh':('Step-by-Step Solutions','中文逐题解析'), 'textbook':('Companion Textbook','双语知识教材')}
    sub,zh=titles[kind];front=WORK/kind/'front.pdf'
    toc=toc_plan(categories,sections,groups,locations,kind)
    c=canvas.Canvas(str(front),pagesize=A4,pageCompression=1)
    c.setTitle(f'AIME {DATE_RANGE} {sub}')
    cover(c,sub,zh,{'questions':len(questions),'sections':len(groups)})
    ap=atlas_plan(categories,sections)
    atlas(c,categories,sections,len(questions),ap);links=draw_toc(c,toc,locations,len(ap));c.save()
    front_count=1+len(ap)+len(toc);writer=PdfWriter()
    writer.append(PdfReader(front));writer.append(PdfReader(WORK/kind/'body.pdf'))
    for link in links:
        writer.add_annotation(link['front_page'],Link(rect=link['rect'],target_page_index=front_count+locations[link['target']]-1))
    chapter_bookmarks={}
    for s in sections:
        if not groups.get(s['id']):continue
        ca=next(c for c in categories if c['id']==s['category_id'])
        target=s['id'] if kind=='textbook' else qid(groups[s['id']][0])
        page=front_count+locations[target]-1
        if ca['id'] not in chapter_bookmarks:chapter_bookmarks[ca['id']]=writer.add_outline_item(sname(ca,'en')+' / '+sname(ca,'zh'),page)
        section_bookmark=writer.add_outline_item(f"{s['section_number']} {sname(s,'en')} / {sname(s,'zh')}",page,parent=chapter_bookmarks[ca['id']])
        if kind=='textbook':
            entry=next(k for k in knowledge if k['subtype_id']==s['id'])
            for method in entry['methods']:
                mid=method['method_id']
                writer.add_outline_item(f"{mid} {method['title_en']} / {method['title_zh']}",front_count+locations[mid]-1,parent=section_bookmark)
    writer.set_page_label(0,front_count-1,style='/r',start=1)
    writer.set_page_label(front_count,len(writer.pages)-1,style='/D',start=1)
    family='solutions' if kind.startswith('solutions_') else kind
    family_root=OUT.parent/family
    family_root.mkdir(parents=True,exist_ok=True)
    output=family_root/f'AIME_{DATE_RANGE}_{kind}.pdf'
    writer.add_metadata({'/Title':f'AIME {DATE_RANGE} {sub}','/Author':'STEMHUB','/Subject':'Bilingual original explanations and reworded mathematical statements'})
    with output.open('wb') as f:writer.write(f)
    pages=[{**p,'physical_page':front_count+p['body_page']} for p in layout['pages']]
    placements=[{'question_id':qid(q),'subtype_id':q['primary']['subtype_id'],'practice_part':q['practice_part'],'body_page':locations[qid(q)],'physical_page':front_count+locations[qid(q)]} for q in questions] if kind!='textbook' else []
    manifest={'kind':kind,'output':str(output.relative_to(ROOT)),'sha256':sha(output),'front_pages':front_count,'body_pages':len(pages),'pdf_pages':len(writer.pages),'pages':pages,'placements':placements,'question_count':len(placements),'locations':locations,'overflow_check':layout['overflow_check'],'math_errors':layout['math_errors'],'visual_review':'not_yet_reviewed'}
    if kind=='textbook':
        manifest['method_locations']={}
        for p in pages:
            if p.get('method_id'):manifest['method_locations'].setdefault(p['method_id'],{'body_page':p['body_page'],'physical_page':p['physical_page'],'section_id':p['section_id']})
    save(WORK/kind/'layout_manifest.json',manifest)
    # Split sections by actual body-page ownership, with local numbering and bookmarks.
    splits=[];source=PdfReader(output)
    for s in sections:
        selected=[p for p in pages if p['section_id']==s['id']]
        if not selected:continue
        sw=PdfWriter()
        for p in selected:sw.add_page(source.pages[p['physical_page']-1])
        sw.add_outline_item(f"Section {s['section_number']} {sname(s,'en')}",0)
        split_root=family_root/kind.split('_')[-1] if kind.startswith('solutions_') else family_root
        dest=split_root/'sections'/f"{s['section_number']}_{s['id']}.pdf";dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('wb') as f:sw.write(f)
        splits.append({'subtype_id':s['id'],'output':str(dest.relative_to(ROOT)),'page_count':len(selected),'source_physical_pages':[p['physical_page'] for p in selected]})
    save(WORK/kind/'section_manifest.json',splits)
    print(json.dumps({'kind':kind,'pages':len(writer.pages),'output':str(output),'sections':len(splits)}))
    return locations

def matrix_pdf(questions,sections,categories,lang,poster=False):
    sd={s['id']:s for s in sections};cd={c['id']:c for c in categories}
    papers=sorted({q['paper_id'] for q in questions},key=lambda p:(-next(q['exam_year'] for q in questions if q['paper_id']==p),0 if next(q.get('exam_form','') for q in questions if q['paper_id']==p)=='I' else 1))
    by={(q['paper_id'],q['number']):q for q in questions};rows=max(q['number'] for q in questions)
    matrix_root=OUT.parent/'matrix';matrix_root.mkdir(parents=True,exist_ok=True)
    output=matrix_root/f'AIME_{DATE_RANGE}_matrix_{lang}{"_poster" if poster else ""}.pdf'
    cellw=130 if lang=='bilingual' else 120;cellh=54 if lang=='bilingual' else 43
    groups=[papers] if poster else [papers[i:i+7] for i in range(0,len(papers),7)]
    pw=66+cellw*max(len(g) for g in groups);ph=130+rows*cellh
    c=canvas.Canvas(str(output),pagesize=(pw,ph),pageCompression=1)
    c.setTitle(f'AIME {DATE_RANGE} Topic Matrix ({lang})')
    for page_i,page_papers in enumerate(groups):
      c.setFillColor(BLUE);c.rect(0,ph-66,pw,66,fill=1,stroke=0)
      c.setFont('Bold',22);c.setFillColor(colors.white);c.drawString(20,ph-36,f'AIME {DATE_RANGE} | Topic Matrix')
      c.setFont('ZH',11);c.drawString(20,ph-55,'一级题型与二级题型；主考点和次考点')
      c.setFont('Body',9);c.drawRightString(pw-20,ph-46,f'{page_i+1} / {len(groups)}')
      for j,p in enumerate(page_papers):
        q=next(q for q in questions if q['paper_id']==p);x=45+j*cellw
        c.setFillColor(PALE);c.rect(x,ph-94,cellw,25,fill=1,stroke=0)
        c.setFillColor(BLUE);c.setFont('Bold',9);c.drawCentredString(x+cellw/2,ph-85,f"{q['exam_year']} AIME {q.get('exam_form','')}")
      for n in range(1,rows+1):
        y=ph-96-n*cellh;c.setFillColor(BLUE);c.setFont('Bold',9);c.drawString(17,y+cellh/2,str(n))
        for j,p in enumerate(page_papers):
            q=by.get((p,n));x=45+j*cellw
            if not q:continue
            pr=q['primary'];s=sd[pr['subtype_id']];ca=cd[pr['category_id']]
            color=colors.HexColor(ca.get('color','#DFEAF1'))
            # Tint retains readable dark text even when category uses a saturated swatch.
            color=colors.Color(.78+.22*color.red,.78+.22*color.green,.78+.22*color.blue)
            c.setFillColor(color);c.setStrokeColor(colors.white);c.rect(x,y,cellw,cellh,fill=1,stroke=1)
            vals=[]
            if lang in ('en','bilingual'):vals.append(('P: '+s['id']+' '+sname(s,'en'),'Body'))
            if lang in ('zh','bilingual'):vals.append(('主: '+s['id']+' '+sname(s,'zh'),'ZH'))
            sec=q.get('secondary',[])
            for lang_ in (['en','zh'] if lang=='bilingual' else [lang]):
                if sec:vals.append((('S: ' if lang_=='en' else '次: ')+', '.join(t['subtype_id'] for t in sec),'Body' if lang_=='en' else 'ZH'))
            yy=y+cellh-5
            for v,font in vals:
                pp=Paragraph(escape(v),ParagraphStyle('matrix',fontName=font,fontSize=7,leading=8,textColor=INK,wordWrap='CJK'))
                _,hh=pp.wrap(cellw-8,cellh);pp.drawOn(c,x+4,yy-hh);yy-=hh+2
            if yy<y+1:raise ValueError(f'Matrix overflow {qid(q)}')
      c.setFont('Body',8);c.setFillColor(MUTED);c.drawString(20,15,'P = primary topic; S = supporting topic. One column is one paper. Source links and full reasons are in the HTML/Excel matrix.')
      c.showPage()
    # Secondary codes are fully expanded in this controlled dictionary appendix.
    # A long method name can remain readable here without shrinking matrix cells.
    dictionary_pages=0;top=0
    def dictionary_header():
        nonlocal dictionary_pages,top
        dictionary_pages+=1;c.setPageSize(A4)
        text(c,'Topic dictionary',M,54,21,'Bold',BLUE)
        text(c,'主次题型代码与完整名称',M,78,12,'ZH',ORANGE)
        text(c,'Secondary codes in the matrix refer to the complete names below.',M,99,8,'Body',MUTED)
        line(c,M,111,W-M,111);top=126
    last_category=None
    for s in sections:
        en=sname(s,'en');zh=sname(s,'zh')
        labels=[(en,'Body')] if lang=='en' else [(zh,'ZH')] if lang=='zh' else [(en,'Body'),(zh,'ZH')]
        height=sum(paragraph(None,escape(label),M+60,0,W-2*M-65,9,font,leading=12)+2 for label,font in labels)+8
        category_new=s['category_id']!=last_category
        if not dictionary_pages or top+height+(24 if category_new else 0)>H-45:
            if dictionary_pages:c.showPage()
            dictionary_header()
        ca=cd[s['category_id']]
        if category_new:
            label=sname(ca,'en') if lang=='en' else sname(ca,'zh') if lang=='zh' else sname(ca,'en')+' / '+sname(ca,'zh')
            text(c,label,M,top+9,10,'Bold' if lang=='en' else 'ZH-Bold',BLUE)
            top+=24;last_category=s['category_id']
        c.setFillColor(colors.HexColor(ca.get('color','#dbeafe')));c.roundRect(M,H-top-15,48,18,3,fill=1,stroke=0)
        text(c,s['id'],M+6,top+12,9,'Bold',BLUE)
        yy=top
        for label,font in labels:yy+=paragraph(c,escape(label),M+60,yy,W-2*M-65,9,font,leading=12)+2
        top+=height;line(c,M,top-4,W-M,top-4)
    if dictionary_pages:c.showPage()
    c.save()
    return {'path':str(output.relative_to(ROOT)),'sha256':sha(output),'pages':len(groups)+dictionary_pages,'matrix_pages':len(groups),'dictionary_pages':dictionary_pages,'size_pt':[pw,ph],'questions':len(questions),'visual_review':'not_yet_reviewed'}

def main():
    global DATE_RANGE
    ap=argparse.ArgumentParser();ap.add_argument('--only',choices=['all','matrix','workbook','solutions_en','solutions_zh','textbook'],default='all');args=ap.parse_args()
    OUT.mkdir(parents=True,exist_ok=True);WORK.mkdir(parents=True,exist_ok=True);register_fonts()
    questions=read(ROOT/'data/questions.json');tax=read(ROOT/'data/taxonomy.json')
    years=[q['exam_year'] for q in questions];DATE_RANGE=f'{min(years)}-{max(years)}'
    categories=sorted(tax['categories'],key=lambda c:c.get('order',0));sections=sorted(tax['subtypes'],key=lambda s:(next(i for i,c in enumerate(categories) if c['id']==s['category_id']),s.get('order',s['id'])))
    groups=defaultdict(list)
    for q in questions:groups[q['primary']['subtype_id']].append(q)
    for qs in groups.values():qs.sort(key=lambda q:(q['practice_part'],q['exam_year'],q.get('exam_form',''),q['number']))
    dictionary_sections=list(sections)
    sections=[s for s in sections if s['id'] in groups]
    for ci,ca in enumerate(categories,1):
        for si,s in enumerate([s for s in sections if s['category_id']==ca['id']],1):s.setdefault('section_number',f'{ci}.{si}')
    questions=[q for s in sections for q in groups[s['id']]]
    receipt={'source_hashes':{p:sha(ROOT/'data'/p) for p in ['questions.json','taxonomy.json']},'question_count':len(questions),'section_count':len(sections),'math_review':'source data review status retained; printing does not certify mathematical correctness','visual_review':'pending final renders'}
    if args.only in ('all','matrix'):
        receipt['matrix']=[matrix_pdf(questions,dictionary_sections,categories,l) for l in ['en','zh','bilingual']]
        receipt['matrix'].append(matrix_pdf(questions,dictionary_sections,categories,'bilingual',poster=True))
    if args.only!='matrix':
        setup_assets();knowledge=read(ROOT/'data/knowledge.json') if (ROOT/'data/knowledge.json').exists() else []
        kinds=['workbook','solutions_en','solutions_zh','textbook'] if args.only=='all' else [args.only]
        wb=None
        wb_manifest=WORK/'workbook/layout_manifest.json'
        if wb_manifest.exists():wb=read(wb_manifest)['locations']
        for kind in kinds:
            loc=build_book(kind,questions,sections,categories,knowledge,groups,wb)
            if kind=='workbook':wb=loc
    save(WORK/f'build_receipt_{args.only}.json',receipt)
    save(WORK/'build_receipt.json',receipt)

if __name__=='__main__':main()

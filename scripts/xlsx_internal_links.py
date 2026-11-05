"""Add standard native internal links missing from the artifact authoring surface.
All cell values, formulas, styles, drawings and notes remain artifact-tool authored.
"""
import json,sys,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
target=Path(sys.argv[1]);links=json.loads(Path(sys.argv[2]).read_text(encoding='utf8'))
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
ET.register_namespace('',ns)
with zipfile.ZipFile(target) as z:
    parts={n:z.read(n) for n in z.namelist()}
root=ET.fromstring(parts['xl/worksheets/sheet1.xml'])
old=root.find(f'{{{ns}}}hyperlinks')
if old is not None:root.remove(old)
container=ET.Element(f'{{{ns}}}hyperlinks')
for item in links:ET.SubElement(container,f'{{{ns}}}hyperlink',item)
# Schema order: hyperlinks follows conditional formatting/data validation and precedes print setup.
successors={'printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst'}
index=next((i for i,node in enumerate(root) if node.tag.rsplit('}',1)[-1] in successors),len(root))
root.insert(index,container)
parts['xl/worksheets/sheet1.xml']=ET.tostring(root,encoding='utf-8',xml_declaration=True)

# Native print settings complement the separate readable Matrix PDFs.
# Manual Matrix page groups keep seven exams together and repeat the ID column.
for si,name in enumerate(['Matrix','Statistics','Problems','Tags','Taxonomy','Review'],1):
    key=f'xl/worksheets/sheet{si}.xml';sh=ET.fromstring(parts[key])
    pr=sh.find(f'{{{ns}}}sheetPr')
    if pr is None:pr=ET.Element(f'{{{ns}}}sheetPr');sh.insert(0,pr)
    setuppr=pr.find(f'{{{ns}}}pageSetUpPr')
    if setuppr is None:setuppr=ET.SubElement(pr,f'{{{ns}}}pageSetUpPr')
    setuppr.set('fitToPage','0' if si==1 else '1')
    for tag,attrs in [('pageMargins',dict(left='0.3',right='0.3',top='0.4',bottom='0.4',header='0.15',footer='0.15')),('pageSetup',dict(paperSize='8',orientation='landscape',pageOrder='overThenDown',scale='50' if si==1 else '100',fitToWidth='0' if si==1 else '1',fitToHeight='0'))]:
        e=sh.find(f'{{{ns}}}{tag}')
        if e is None:
            e=ET.Element(f'{{{ns}}}{tag}')
            later={'pageMargins':{'pageSetup','headerFooter','rowBreaks','colBreaks','drawing','legacyDrawing','tableParts','extLst'},'pageSetup':{'headerFooter','rowBreaks','colBreaks','drawing','legacyDrawing','tableParts','extLst'}}[tag]
            idx=next((i for i,c in enumerate(sh) if c.tag.rsplit('}',1)[-1] in later),len(sh));sh.insert(idx,e)
        e.attrib.update(attrs)
    if si==1:
        for tag,ids,maxv in [('rowBreaks',[9,14],54),('colBreaks',list(range(8,55,7)),18)]:
            old=sh.find(f'{{{ns}}}{tag}')
            if old is not None:sh.remove(old)
            e=ET.Element(f'{{{ns}}}{tag}',count=str(len(ids)),manualBreakCount=str(len(ids)))
            for v in ids:ET.SubElement(e,f'{{{ns}}}brk',id=str(v),min='0',max=str(maxv),man='1')
            later={'rowBreaks':{'colBreaks','drawing','legacyDrawing','tableParts','extLst'},'colBreaks':{'drawing','legacyDrawing','tableParts','extLst'}}[tag]
            idx=next((i for i,c in enumerate(sh) if c.tag.rsplit('}',1)[-1] in later),len(sh));sh.insert(idx,e)
    parts[key]=ET.tostring(sh,encoding='utf-8',xml_declaration=True)
book=ET.fromstring(parts['xl/workbook.xml']);defined=book.find(f'{{{ns}}}definedNames')
if defined is None:
    defined=ET.Element(f'{{{ns}}}definedNames');idx=next((i for i,c in enumerate(book) if c.tag.rsplit('}',1)[-1] in {'calcPr','oleSize','customWorkbookViews','pivotCaches','extLst'}),len(book));book.insert(idx,defined)
for e in list(defined):
    if e.get('name') in {'_xlnm.Print_Area','_xlnm.Print_Titles'}:defined.remove(e)
for si,name in enumerate(['Matrix','Statistics','Problems','Tags','Taxonomy','Review']):
    sh=ET.fromstring(parts[f'xl/worksheets/sheet{si+1}.xml']);dimension=sh.find(f'{{{ns}}}dimension');ref=dimension.get('ref') if dimension is not None else None
    if ref:
        area=ref.replace(':',':$').replace('A1','A$1')
        # Convert ordinary A1 bounds to absolute A1 references.
        import re
        area=':'.join(re.sub(r'([A-Z]+)(\d+)',r'$\1$\2',r) for r in ref.split(':'))
        ET.SubElement(defined,f'{{{ns}}}definedName',name='_xlnm.Print_Area',localSheetId=str(si)).text=f"'{name}'!{area}"
    titles=f"'{name}'!$4:$4"+(f",'{name}'!$A:$A" if si==0 else '')
    ET.SubElement(defined,f'{{{ns}}}definedName',name='_xlnm.Print_Titles',localSheetId=str(si)).text=titles
parts['xl/workbook.xml']=ET.tostring(book,encoding='utf-8',xml_declaration=True)
temp=target.with_suffix('.tmp.xlsx')
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
    for n,data in parts.items():z.writestr(n,data)
temp.replace(target)
with zipfile.ZipFile(target) as z:
    check=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    actual=check.find(f'{{{ns}}}hyperlinks')
    assert actual is not None and len(actual)==len(links)
    for n in z.namelist():
        if n.endswith('.xml'):ET.fromstring(z.read(n))
    assert check.find(f'{{{ns}}}pageSetup').get('orientation')=='landscape'
print(f'Verified {len(links)} native internal matrix links and six-sheet print settings.')

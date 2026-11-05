"""Isolated pagination/math smoke test. Never writes fabricated public data."""
from pathlib import Path
import json
import build_print as p

ROOT=p.ROOT
p.WORK=ROOT/'tmp/print-smoke'
p.OUT=p.WORK/'pdf'
p.OUT.mkdir(parents=True,exist_ok=True)
p.register_fonts();p.setup_assets()
cats=[{'id':'AL','name_en':'Algebra','name_zh':'代数','color':'#5391A7','order':1}]
secs=[{'id':'AL01','category_id':'AL','name_en':'Polynomial identities','name_zh':'多项式恒等式','section_number':'1.1','order':1}]
q={'question_id':'SMOKE-Q01','paper_id':'SMOKE','exam_year':2026,'exam_form':'I','number':1,'practice_part':'A','primary':{'category_id':'AL','subtype_id':'AL01'},'secondary':[],
'statement_en':r'For positive real numbers $x$ and $y$, suppose $x+y=7$ and $xy=10$. Compute $x^2+y^2$.',
'statement_zh':r'正实数 $x,y$ 满足 $x+y=7$ 且 $xy=10$，求 $x^2+y^2$。',
'answer':29,'solution_en':[r'Expand the square: $(x+y)^2=x^2+2xy+y^2$.',r'Hence $x^2+y^2=7^2-2(10)=29$.',r'Check: the roots of $t^2-7t+10=0$ are $2,5$, and $2^2+5^2=29$.'],
'solution_zh':[r'展开 $(x+y)^2=x^2+2xy+y^2$。',r'因此 $x^2+y^2=7^2-2(10)=29$。',r'检验：$t^2-7t+10=0$ 的两根为 $2,5$，且 $2^2+5^2=29$。'],
'source_url':'https://example.com'}
knowledge=[{'subtype_id':'AL01','introduction_en':'Use the symmetric sums before solving for each variable.','introduction_zh':'优先利用对称式，避免逐个解出变量。','methods':[{'title_en':'Subtract the cross term','title_zh':'减去交叉项','example_en':r'If $a+b=9$ and $ab=14$, find $a^2+b^2$.','example_zh':r'若 $a+b=9,ab=14$，求 $a^2+b^2$。','steps_en':[r'Start with $a^2+b^2=(a+b)^2-2ab$.',r'Substitute to get $81-28=53$.'],'steps_zh':[r'由恒等式 $a^2+b^2=(a+b)^2-2ab$ 入手。',r'代入得 $81-28=53$。']}],'practice_ids':['SMOKE-Q01']}]
group={'AL01':[q]}
for kind in ['workbook','solutions_en','solutions_zh','textbook']:
    p.build_book(kind,[q],secs,cats,knowledge,group)
p.matrix_pdf([q],secs,cats,'bilingual')
print(json.dumps({'smoke':'passed','output':str(p.OUT),'note':'Synthetic render test only, not public contest data'}))

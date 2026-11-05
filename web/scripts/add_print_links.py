from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'src/components/QuestionCard.astro';s=p.read_text(encoding='utf8')
if "import PrintLinks" not in s:s=s.replace("import Bi from './Bi.astro';","import Bi from './Bi.astro';\nimport PrintLinks from './PrintLinks.astro';")
if '<PrintLinks resources={q.print?.workbook' not in s:s=s.replace('<div class="question-statement" data-content-language="en">','<PrintLinks resources={q.print?.workbook?{workbook:q.print.workbook}:{}} compact/>\n<div class="question-statement" data-content-language="en">')
if 'solutions_en:q.print?.solutions_en' not in s:s=s.replace('</div></details>','<PrintLinks resources={{...(q.print?.solutions_en?{solutions_en:q.print.solutions_en}:{}),...(q.print?.solutions_zh?{solutions_zh:q.print.solutions_zh}:{})}}/></div></details>')
p.write_text(s,encoding='utf8')
p=ROOT/'src/pages/sections/[section].astro';s=p.read_text(encoding='utf8')
if 'import PrintLinks' not in s:s=s.replace("import Bi from '../../components/Bi.astro';","import Bi from '../../components/Bi.astro';\nimport PrintLinks from '../../components/PrintLinks.astro';")
if '<PrintLinks resources={section.print}' not in s:s=s.replace('<a class="section-knowledge-link"','<PrintLinks resources={section.print}/><a class="section-knowledge-link"',1)
p.write_text(s,encoding='utf8')

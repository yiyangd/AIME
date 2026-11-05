"""Small authoring utility. This does not infer mathematical classifications or prose."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
TAX=json.loads((ROOT/'data/taxonomy.json').read_text(encoding='utf8'))
SUB={s['id']:s for s in TAX['subtypes']}

class Batch:
    def __init__(self,paper,author='root'):
        self.paper=paper; self.author=author; self.rows=[]
        self.sources=json.loads((ROOT/f'sources/records/{paper}.json').read_text(encoding='utf8'))
    def add(self,num,primary,secondary,en,zh,steps_en,steps_zh,notes=''):
        q=self.sources[num-1]
        def tag(code,reason_en,reason_zh):
            return dict(category_id=SUB[code]['category_id'],subtype_id=code,reason_en=reason_en,reason_zh=reason_zh)
        sec=[]
        for item in secondary:
            code,step=item if isinstance(item,tuple) else (item,min(1,len(steps_en)-1))
            sec.append(tag(code,steps_en[step],steps_zh[step]))
        self.rows.append(dict(question_id=q['question_id'],paper_id=q['paper_id'],exam_year=q['year'],exam_form=q['form'],number=num,practice_part='ABC'[(num-1)//5],primary=tag(primary,steps_en[0],steps_zh[0]),secondary=sec,statement_en=en,statement_zh=zh,answer=int(q['answer']),solution_en=steps_en,solution_zh=steps_zh,source_url=q['source_url'],method_chain=[SUB[code]['name_en'] for code in [primary]+[x['subtype_id'] for x in sec]],review=dict(author=self.author,source_checked=True,recomputed=True,notes=notes,cross_review='pending'),unresolved_issues=[]))
    def save(self):
        assert len(self.rows)==15 and {q['number'] for q in self.rows}==set(range(1,16))
        p=ROOT/f'data/batches/{self.paper}.json';p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(self.rows,ensure_ascii=False,indent=2),encoding='utf8')
        print(p)

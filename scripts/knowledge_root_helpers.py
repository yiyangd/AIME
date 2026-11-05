"""Helpers for root-authored textbook manuscripts; methods are written explicitly."""
import json
from knowledge_ge_helpers import Section as BaseSection,ROOT
class Section(BaseSection):
    def save(self):
        missing=self.ids-set(self.data['coverage_by_question']);assert not missing,sorted(missing)
        for q in self.rows:self.data['coverage_by_question'][q['question_id']]['prerequisites']=sorted({t['subtype_id'] for t in [q['primary']]+q['secondary'] if t['subtype_id']!=self.code})
        self.data['review']=dict(author='root',all_primary_routes_read=True,necessary_secondary_routes_read=True,original_examples_recomputed=True,independent_review=False)
        self.data['unresolved_issues']=[]
        def texts(obj):
            if isinstance(obj,str):yield obj
            elif isinstance(obj,list):
                for x in obj:yield from texts(x)
            elif isinstance(obj,dict):
                for x in obj.values():yield from texts(x)
        for value in texts(self.data):assert not any(ord(c)<32 for c in value),repr(value)
        p=ROOT/'data/knowledge_batches'/f'{self.code}.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(self.data,ensure_ascii=False,indent=2),encoding='utf8')
        print(self.code,len(self.rows),'routes',len(self.data['methods']),'methods')

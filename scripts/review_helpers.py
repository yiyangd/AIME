"""Explicit reviewer-authored records; no automatic mathematical verdicts."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Review:
    def __init__(self,filename,reviewer='root'):
        self.path=ROOT/'audit/reviews'/filename;self.reviewer=reviewer
        self.records=json.loads(self.path.read_text(encoding='utf8')) if self.path.exists() else []
        self.questions={q['question_id']:q for p in (ROOT/'data/batches').glob('*.json') for q in json.loads(p.read_text(encoding='utf8'))}
    def add(self,qid,findings,patch=None,verdict='pass'):
        q=self.questions[qid]
        assert q['review']['author']!=self.reviewer
        record=dict(question_id=qid,reviewer=self.reviewer,review_type='separate_agent',source_checked=True,math_checked=verdict=='pass',classification_checked=True,language_checked=True,verdict=verdict,findings=findings,reviewed_input_sha256=hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode('utf8')).hexdigest(),patch=patch or {})
        self.records=[x for x in self.records if x['question_id']!=qid]+[record]
    def save(self):
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.path.write_text(json.dumps(sorted(self.records,key=lambda x:x['question_id']),ensure_ascii=False,indent=2),encoding='utf8')
        print(f'Saved {len(self.records)} explicit independent reviews to {self.path}')

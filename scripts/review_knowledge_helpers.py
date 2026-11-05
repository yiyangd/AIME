"""Explicit textbook-review receipts, accepted only for the exact reviewed content."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def digest(s):return hashlib.sha256(json.dumps({k:v for k,v in s.items() if k!='review'},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
class KnowledgeReview:
 def __init__(self,reviewer):
  self.reviewer=reviewer;self.path=ROOT/'audit/knowledge_reviews'/f'{reviewer}.json'
  self.records=json.loads(self.path.read_text(encoding='utf8')) if self.path.exists() else []
 def accept(self,code,findings,patch=None):
  s=json.loads((ROOT/'data/knowledge_batches'/f'{code}.json').read_text(encoding='utf8'));assert s['review']['author']!=self.reviewer
  s.update(patch or {})
  self.records=[r for r in self.records if r['subtype_id']!=code]+[dict(subtype_id=code,reviewer=self.reviewer,content_sha256=digest(s),math_checked=True,language_checked=True,route_checked=True,checked_method_ids=[m['method_id'] for m in s['methods']],findings=findings,patch=patch or {})]
 def save(self):
  self.path.parent.mkdir(parents=True,exist_ok=True);self.path.write_text(json.dumps(sorted(self.records,key=lambda r:r['subtype_id']),ensure_ascii=False,indent=2),encoding='utf8');print('Saved',len(self.records),'explicit knowledge reviews')

"""Download diagram reference files for private source inspection, not publication."""
from pathlib import Path
import json, hashlib, requests, concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
qs=json.loads((ROOT/'sources/records/all_source_records.json').read_text(encoding='utf-8'))
urls=sorted(set(u for q in qs for u in q['diagram_source_urls']))
def fetch(url):
    r=requests.get(url,timeout=60);r.raise_for_status()
    rel='sources/assets/'+url.split('live.poshenloh.com/')[-1]
    path=ROOT/rel;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(r.content)
    return {'url':url,'local_path':rel,'sha256':hashlib.sha256(r.content).hexdigest(),'bytes':len(r.content)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: records=list(p.map(fetch,urls))
(ROOT/'sources/asset_manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Downloaded',len(records),'unique diagrams')

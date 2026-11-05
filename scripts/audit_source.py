"""Fetch/audit the public LIVE AIME source data. Raw source is local audit input."""
from pathlib import Path
import json, re, hashlib, datetime, concurrent.futures, argparse
import requests

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://live.poshenloh.com'

def extract(html):
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.S)
    if not match:
        raise ValueError('Missing Next.js structured data')
    return json.loads(match.group(1))

def fetch(year, form, locale):
    slug = f'{year}{form}'
    url = f'{BASE}/{"zh/" if locale == "zh" else ""}past-contests/aime/{slug}'
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    # Decode the bytes as UTF-8, not requests' guessed encoding.
    html = response.content.decode('utf-8')
    data = extract(html)
    path = ROOT / 'sources' / 'raw' / f'{slug}.{locale}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    props = data['props']['pageProps']
    return {'year':year, 'form':form, 'locale':locale, 'url':url,
            'path':path.relative_to(ROOT).as_posix(),
            'sha256':hashlib.sha256(response.content).hexdigest(),
            'structured_json_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'props_keys':list(props), 'byte_length':len(response.content)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--years', nargs='+', type=int, default=list(range(2020,2027)))
    parser.add_argument('--locales', nargs='+', default=['en','zh'])
    args = parser.parse_args()
    tasks = [(y,f,l) for y in args.years for f in ['I','II'] for l in args.locales]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(lambda t: fetch(*t), tasks))
    out = ROOT/'sources'/'fetch_manifest.json'
    out.parent.mkdir(exist_ok=True)
    if out.exists():
        prior=json.loads(out.read_text(encoding='utf-8'))
        keys={(r['year'],r['form'],r['locale']) for r in records}
        records.extend(r for r in prior if (r['year'],r['form'],r['locale']) not in keys)
    records.sort(key=lambda r:(r['year'],r['form'],r['locale']))
    out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Fetched {len(records)} pages; manifest: {out}')
    for r in records:
        d=json.loads((ROOT/r['path']).read_text(encoding='utf-8'))['props']['pageProps']
        print(r['year'],r['form'],r['locale'],[(k,len(v) if hasattr(v,'__len__') else type(v).__name__) for k,v in d.items()])

if __name__=='__main__': main()

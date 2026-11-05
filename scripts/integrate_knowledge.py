"""Validate and combine explicitly authored bilingual textbook sections."""
import argparse,hashlib,json,re
from pathlib import Path
from review_knowledge_helpers import digest
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf8'))
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf8')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--allow-partial',action='store_true');ap.add_argument('--require-reviewed',action='store_true');args=ap.parse_args()
    T=read(ROOT/'data/taxonomy.json')['subtypes'];codes={x['id'] for x in T}
    Q=read(ROOT/'data/questions.json');qmap={q['question_id']:q for q in Q};errors=[];sections=[];seen=set();methods=set();stale=[];reviews={}
    for path in sorted((ROOT/'audit/knowledge_reviews').glob('*.json')):
        for r in read(path):reviews.setdefault(r['subtype_id'],[]).append(r)
    for path in sorted((ROOT/'data/knowledge_batches').glob('*.json')):
        s=read(path);code=s.get('subtype_id');seen.add(code)
        for r in reviews.get(code,[]):
            if r['reviewer']==s.get('review',{}).get('author'):errors.append(f'{code}: textbook reviewer equals author');continue
            candidate=dict(s,**r.get('patch',{}))
            if digest(candidate)!=r.get('content_sha256'):stale.append(dict(subtype_id=code,reviewer=r['reviewer']));continue
            if all(r.get(k) is True for k in ['math_checked','language_checked','route_checked']) and set(r.get('checked_method_ids',[]))=={m['method_id'] for m in candidate.get('methods',[])}:
                s=candidate;s['review']=dict(s.get('review',{}),independent_review=True,independent_reviewer=r['reviewer'],independent_findings=r['findings'])
        if code not in codes:errors.append(f'{path.name}: unknown subtype {code}');continue
        if any(x['subtype_id']==code for x in sections):errors.append(f'{code}: duplicate section')
        expected={q['question_id'] for q in Q if code in [t['subtype_id'] for t in [q['primary']]+q['secondary']]}
        primary={q['question_id'] for q in Q if q['primary']['subtype_id']==code}
        if set(s.get('practice_ids',[]))!=primary:errors.append(f'{code}: primary practice set mismatch {sorted(set(s.get("practice_ids",[]))^primary)}')
        coverage=s.get('coverage_by_question',{})
        if set(coverage)!=expected:errors.append(f'{code}: route coverage set mismatch {sorted(set(coverage)^expected)}')
        if not s.get('methods'):errors.append(f'{code}: no methods')
        local={}
        for m in s.get('methods',[]):
            mid=m.get('method_id')
            if not mid or mid in methods or not mid.startswith(code+'-M'):errors.append(f'{code}: invalid or duplicate method ID {mid}')
            methods.add(mid);local[mid]=m
            for key in ('title','example','tip'):
                for lang in ('en','zh'):
                    if not isinstance(m.get(key+'_'+lang),str) or not m[key+'_'+lang].strip():errors.append(f'{mid}: missing {key}_{lang}')
            for key in ('steps','solution'):
                for lang in ('en','zh'):
                    v=m.get(key+'_'+lang,[])
                    if not isinstance(v,list) or not 3<=len(v)<=4 or any(not isinstance(x,str) or not x.strip() for x in v):errors.append(f'{mid}: invalid {key}_{lang}')
                if len(m.get(key+'_en',[]))!=len(m.get(key+'_zh',[])):errors.append(f'{mid}: unmatched {key} translations')
            ids=m.get('question_ids',[])
            if not ids or len(ids)!=len(set(ids)) or not set(ids)<=expected:errors.append(f'{mid}: invalid applicable-question IDs {sorted(set(ids)-expected)}')
            for qid in ids:
                if mid not in coverage.get(qid,{}).get('method_ids',[]):errors.append(f'{mid}/{qid}: missing reverse coverage link')
            for p in m.get('prerequisites',[]):
                if p not in codes or p==code:errors.append(f'{mid}: invalid prerequisite {p}')
            if len(m.get('extensions_en',[]))!=len(m.get('extensions_zh',[])):errors.append(f'{mid}: unmatched extensions')
        for qid,route in coverage.items():
            ids=route.get('method_ids',[])
            if not ids or len(ids)!=len(set(ids)):errors.append(f'{code}/{qid}: empty or duplicate method route')
            for mid in ids:
                if mid not in local or qid not in local[mid].get('question_ids',[]):errors.append(f'{code}/{qid}: invalid method route {mid}')
            for p in route.get('prerequisites',[]):
                if p not in codes or p==code:errors.append(f'{code}/{qid}: invalid supporting subtype {p}')
        for lang in ('en','zh'):
            if not s.get('introduction_'+lang):errors.append(f'{code}: missing introduction_{lang}')
        def texts(obj):
            if isinstance(obj,str):yield obj
            elif isinstance(obj,list):
                for x in obj:yield from texts(x)
            elif isinstance(obj,dict):
                for x in obj.values():yield from texts(x)
        for v in texts(s):
            if any(ord(c)<32 for c in v):errors.append(f'{code}: control character in text')
            if len(re.findall(r'(?<!\\)\$',v))%2:errors.append(f'{code}: unmatched math delimiter {v[:90]}')
        if s.get('unresolved_issues') or s.get('honest_gaps'):errors.append(f'{code}: unresolved knowledge gaps')
        if args.require_reviewed and not s.get('review',{}).get('independent_review'):errors.append(f'{code}: independent textbook review pending')
        sections.append(s)
    missing=codes-seen
    if missing and not args.allow_partial:errors.append(f'Missing sections: {sorted(missing)}')
    if errors:
        print('\n'.join(errors));raise SystemExit(f'{len(errors)} knowledge validation errors; no output written')
    order={t['id']:i for i,t in enumerate(T)};sections.sort(key=lambda s:order[s['subtype_id']])
    write(ROOT/'data/knowledge.json',sections)
    report=dict(sections=len(sections),expected_sections=len(codes),missing_sections=sorted(missing),methods=len(methods),question_route_incidences=sum(len(s['coverage_by_question']) for s in sections),primary_practice_links=sum(len(s['practice_ids']) for s in sections),independently_reviewed_sections=[s['subtype_id'] for s in sections if s.get('review',{}).get('independent_review')],stale_reviews=stale,canonical_questions_sha256=hashlib.sha256((ROOT/'data/questions.json').read_bytes()).hexdigest(),knowledge_sha256=hashlib.sha256((ROOT/'data/knowledge.json').read_bytes()).hexdigest(),note='Coverage checks validate links and bilingual structure. Mathematical correctness requires the separate author and reviewer judgments retained in each section.')
    write(ROOT/'output/qa/knowledge-coverage.json',report);print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()

"""Validate and integrate authored batches. Full builds require the complete source inventory."""
import argparse, collections, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf8'))
def write(p,d):
    out=ROOT/p;out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
def normalize(s):
    return s.replace('\\[','$$').replace('\\]','$$').replace('\\(','$').replace('\\)','$')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--allow-partial',action='store_true');ap.add_argument('--require-reviewed',action='store_true');args=ap.parse_args()
    config=read('project.config.json');taxonomy=read('data/taxonomy.json')
    subtype={x['id']:x for x in taxonomy['subtypes']}
    sources=read('sources/records/all_source_records.json');source={x['question_id']:x for x in sources}
    review_records={}
    for path in sorted((ROOT/'audit/reviews').glob('*.json')):
        records=json.loads(path.read_text(encoding='utf8'))
        if isinstance(records,dict):records=records.get('records',[records])
        for record in records:review_records.setdefault(record['question_id'],[]).append(record)
    questions=[];seen=set();errors=[]
    for path in sorted((ROOT/'data/batches').glob('*.json')):
        rows=json.loads(path.read_text(encoding='utf8'))
        for q in rows:
            qid=q['question_id']
            if qid in seen:errors.append(f'Duplicate authored ID {qid} in {path.name}');continue
            seen.add(qid)
            applied_reviews=[]
            for record in review_records.get(qid,[]):
                if record.get('reviewer')==q.get('review',{}).get('author'):errors.append(f'{qid}: cross-review must be by another agent')
                for field,value in record.get('patch',{}).items():q[field]=value
                applied_reviews.append({k:v for k,v in record.items() if k!='patch'})
            if applied_reviews:
                q.setdefault('review',{})['cross_review']=applied_reviews
                last=applied_reviews[-1]
                source_discrepancy=last.get('verdict')=='source_discrepancy_documented'
                passed=(last.get('verdict')=='pass' or source_discrepancy) and all(last.get(k) is True for k in ['source_checked','math_checked','classification_checked','language_checked']) and not q.get('unresolved_issues')
                q['review']['status']=('source_discrepancy_documented' if source_discrepancy else 'reviewed') if passed else 'needs_correction'
                if source_discrepancy and not all(q.get(k) for k in ['corrected_answer_en','corrected_answer_zh','editorial_note_en','editorial_note_zh']):errors.append(f'{qid}: incomplete documented source discrepancy')
                if args.require_reviewed and not passed:errors.append(f'{qid}: independent review not accepted')
            elif args.require_reviewed:errors.append(f'{qid}: independent review missing')
            questions.append(q)
            s=source.get(qid)
            if not s:errors.append(f'Unknown ID {qid}');continue
            for field,expected in [('paper_id',s['paper_id']),('exam_year',s['year']),('exam_form',s['form']),('number',s['number']),('practice_part','ABC'[(s['number']-1)//5])]:
                if q.get(field)!=expected:errors.append(f'{qid}: {field} {q.get(field)!r} != {expected!r}')
            if int(q['answer'])!=int(s['answer']):errors.append(f'{qid}: answer conflict')
            if not 0<=int(q['answer'])<=999:errors.append(f'{qid}: answer outside AIME range')
            used=set()
            for tag in [q['primary']]+q.get('secondary',[]):
                code=tag['subtype_id']
                if code not in subtype:errors.append(f'{qid}: unknown subtype {code}');continue
                if tag['category_id']!=subtype[code]['category_id']:errors.append(f'{qid}: inconsistent category {code}')
                if code in used:errors.append(f'{qid}: repeated tag {code}')
                used.add(code)
            for lang in ['en','zh']:
                sk='statement_'+lang;sol='solution_'+lang
                if not isinstance(q.get(sk),str) or len(q[sk])<12:errors.append(f'{qid}: missing {sk}')
                if not isinstance(q.get(sol),list) or len(q[sol])<2:errors.append(f'{qid}: missing worked {sol}')
                q[sk]=normalize(q.get(sk,''));q[sol]=[normalize(x) for x in q.get(sol,[])]
                if lang=='en' and re.search(r'[\u3400-\u9fff]',q[sk]+' '.join(q[sol])):errors.append(f'{qid}: untranslated CJK in English')
                for text in [q[sk]]+q[sol]:
                    if len(re.findall(r'(?<!\\)\$',text))%2:errors.append(f'{qid}: unmatched dollar math delimiter')
            q['source_url']=s['source_url']
            q.setdefault('unresolved_issues',[])
    missing=sorted(set(source)-seen)
    if missing and not args.allow_partial:errors.append(f'Missing {len(missing)} of {len(source)} problems; use --allow-partial for internal preview only')
    if errors:
        write('output/qa/integration_errors.json',errors)
        raise SystemExit('\n'.join(errors[:30])+f'\n{len(errors)} validation errors')
    catorder={x['id']:x['order'] for x in taxonomy['categories']}
    def order(q):
        s=subtype[q['primary']['subtype_id']]
        return catorder[s['category_id']],s['order'],q['practice_part'],q['exam_year'],0 if q['exam_form']=='I' else 1,q['number']
    questions.sort(key=order)
    sections=[];topics=[]
    for cat in sorted(taxonomy['categories'],key=lambda x:x['order']):
        catrows=[q for q in questions if q['primary']['category_id']==cat['id']]
        catsubs=[s for s in taxonomy['subtypes'] if s['category_id']==cat['id'] and any(q['primary']['subtype_id']==s['id'] for q in catrows)]
        for i,s in enumerate(sorted(catsubs,key=lambda x:x['order']),1):
            rows=[q for q in catrows if q['primary']['subtype_id']==s['id']]
            sections.append(dict(id=s['id'],category_id=cat['id'],section_number=s['section_number'],name_en=s['name_en'],name_zh=s['name_zh'],question_ids=[q['question_id'] for q in rows],part_counts=dict(collections.Counter(q['practice_part'] for q in rows))))
        if catrows:topics.append(dict(**cat,section_ids=[s['id'] for s in catsubs],question_count=len(catrows)))
    write('data/questions.json',questions);write('data/topics.json',topics);write('data/sections.json',sections)
    write('data/solutions.json',[dict(question_id=q['question_id'],answer=q['answer'],solution_en=q['solution_en'],solution_zh=q['solution_zh'],**{k:q[k] for k in ['source_answer','answer_status','corrected_answer_en','corrected_answer_zh','editorial_note_en','editorial_note_zh'] if k in q}) for q in questions])
    write('data/inventory.json',read('sources/inventory.json'))
    write('data/source_manifest.json',read('sources/fetch_manifest.json'))
    coverage=dict(scope=config['scope'],source_papers=len({s['paper_id'] for s in sources}),source_questions=len(sources),authored_questions=len(questions),missing_ids=missing,primary_counts=dict(collections.Counter(q['primary']['category_id'] for q in questions)),primary_subtypes=len(sections),topics=len(topics),cross_reviewed=sum(q.get('review',{}).get('status') in ['reviewed','source_discrepancy_documented'] for q in questions),documented_source_discrepancies=[q['question_id'] for q in questions if q.get('answer_status')=='source_discrepancy'],unresolved={q['question_id']:q['unresolved_issues'] for q in questions if q['unresolved_issues']},content_sha256=hashlib.sha256((ROOT/'data/questions.json').read_bytes()).hexdigest(),complete_coverage=not missing,mathematical_review='Independent review statuses and patches are preserved per question; structure checks do not certify mathematics. Historical source keys are labeled separately wherever a proven discrepancy is documented.')
    write('output/qa/coverage.json',coverage)
    p=read('progress.json')
    reviewed=coverage['cross_reviewed']==len(sources) and not coverage['unresolved'] and not missing
    p['source_inventory']=dict(status='completed',papers=coverage['source_papers'],questions=len(sources),empty_solutions=sum(not s['solution_source_en'] for s in sources))
    p['question_content']=dict(status='completed' if reviewed else 'drafted' if not missing else 'in_progress',completed_ids=sorted(seen),count=len(seen))
    p['mathematical_cross_review']=dict(status='completed' if reviewed else 'in_progress',accepted_count=coverage['cross_reviewed'],documented_source_discrepancies=coverage['documented_source_discrepancies'])
    if not reviewed:
        p['stage']='authoring'
        p['next']='Complete missing authored batches and independent mathematics/classification reviews.'
    elif p.get('stage')=='authoring':
        p['stage']='artifact_qa'
        p['next']='Complete final textbook, cross-format visual/link checks and deployment.'
    write('progress.json',p)
    print(json.dumps({k:coverage[k] for k in ['source_papers','source_questions','authored_questions','primary_subtypes','topics','complete_coverage']},ensure_ascii=False))
if __name__=='__main__':main()

from pathlib import Path
import json, re, hashlib
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'sources'/'records'
out.mkdir(parents=True,exist_ok=True)
inventory=[]
all_records=[]
for year in range(2000,2027):
    for form in ('I','II'):
        slug=f'{year}{form}'
        source=ROOT/'sources'/'raw'/f'{slug}.en.json'
        data=json.loads(source.read_text(encoding='utf-8'))
        questions=data['props']['pageProps']['baseQuestions']
        records=[]
        # IMPORTANT: array position is the exam number. aimeProblemNumber is a
        # difficulty calibration field (duplicates and missing numbers occur).
        for num,q in enumerate(questions,1):
            diagrams=re.findall(r'<img\s+[^>]*src=[\"\']([^\"\']+)',q['question']+'\n'+q.get('solutions',''))
            records.append({'question_id':f'AIME-{year}-{form}-Q{num:02}',
                'paper_id':f'AIME-{year}-{form}', 'year':year, 'form':form, 'number':num,
                'source_url':f'https://live.poshenloh.com/past-contests/aime/{slug}/problem/{num}',
                'paper_url':f'https://live.poshenloh.com/past-contests/aime/{slug}',
                'question_source_en':q['question'], 'solution_source_en':q.get('solutions',''),
                'answer':q.get('answer'), 'hints_source_en':q.get('hints',[]),
                'source_concepts':q.get('concepts','').split('; '),
                'source_rating':q.get('seedElo'), 'source_solve_time':q.get('solveTimeSeconds'),
                'source_numbering_note':'Actual exam number is baseQuestions array position + 1; aimeProblemNumber is NOT exam number',
                'diagram_source_urls':[('https://live.poshenloh.com/images/past-contests'+u if u.startswith('/aime/') else ('https://live.poshenloh.com'+u if u.startswith('/') else u)) for u in diagrams],
                'status':'source_extracted_not_mathematically_reviewed'})
        assert sorted(q['number'] for q in records)==list(range(1,16))
        (out/f'{slug}.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
        text='\n\n'.join(f"## {q['question_id']}\n\nQuestion:\n{q['question_source_en']}\n\nAnswer: {q['answer']}\n\nConcepts: {'; '.join(q['source_concepts'])}\n\nSolution:\n{q['solution_source_en']}" for q in records)
        (out/f'{slug}.md').write_text(text,encoding='utf-8')
        all_records.extend(records)
        inventory.append({'paper_id':f'AIME-{year}-{form}','exam_year':year,'administration':form,
            'exam_form':None,'paper_url':records[0]['paper_url'],'expected_numbers':list(range(1,16)),
            'actual_numbers':[q['number'] for q in records], 'question_count':len(records),
            'diagram_occurrences':sum(len(q['diagram_source_urls']) for q in records),
            'empty_solution_count':sum(not q['solution_source_en'] for q in records),
            'source_json':source.relative_to(ROOT).as_posix()})
(ROOT/'sources'/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'all_source_records.json').write_text(json.dumps(all_records,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'concept_answer_index.tsv').write_text('question_id\tanswer\tconcepts\tdiagram_count\n'+'\n'.join(f"{q['question_id']}\t{q['answer']}\t{'; '.join(q['source_concepts'])}\t{len(q['diagram_source_urls'])}" for q in all_records),encoding='utf-8')
print('Extracted',len(all_records),'records from',len(inventory),'papers')
print('Diagram occurrences',sum(p['diagram_occurrences'] for p in inventory))
print('Empty solutions',sum(p['empty_solution_count'] for p in inventory))
print('Source fields:',list(all_records[0]))

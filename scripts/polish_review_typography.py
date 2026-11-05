"""Apply only the six English typography fields approved after visual QA."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'audit/reviews/root_2015_2022.json'
records=json.loads(path.read_text(encoding='utf-8'))
by_id={r['question_id']:r for r in records}
patch=by_id['AIME-2016-I-Q09']['patch']
patch['editorial_note_en']=patch['editorial_note_en'].replace('is744','is 744')
patch['solution_en']=[x.replace('Thus744','Thus 744').replace('value744','value 744') for x in patch['solution_en']]
patch=by_id['AIME-2022-I-Q14']['patch']
patch['solution_en'][0]=r'To prove the midpoint-cleaver lemma, put $C$ at the origin and use unit vectors $u$ along $CA$ and $v$ along $CB$. Write $a=CB,b=CA,c=AB$ and $M=(bu+av)/2$. If $a\ge b$, let $X=M-b(u+v)/2=((a-b)/2)v$, a point on $CB$. Then $MX$ is parallel to $u+v$, the internal bisector direction at $C$. The boundary route $M-A-C-X$ has length $c/2+b+(a-b)/2=(a+b+c)/2$; the other route $M-B-X$ has the same length $c/2+a-(a-b)/2$. Their common cut segment adds equally to both polygon perimeters. If $b>a$, swap the roles and choose $X=((b-a)/2)u$. Thus the midpoint perimeter bisector is parallel to the opposite internal angle bisector.'
patch['solution_en'][1]=r'Apply the lemma at the midpoints of $AB$ and $AC$: the two lines are parallel to the internal bisectors at $C$ and $B$. Their acute angle is $90^\circ-A/2$, so the given $30^\circ$ forces $A=120^\circ$.'
path.write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Polished only approved2016 I Q9 and2022 I Q14 English typography; mathematical statements unchanged.')

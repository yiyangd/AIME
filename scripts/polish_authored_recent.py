"""Small wording corrections shared by author sources and generated batches."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
replacements={
 '2005I':[(r'Let $M$ be the midpoint of $AB$, and the incircle cut $CM$ at one-third and two-thirds positions.',r'Let $M$ be the midpoint of $AB$, let $R$ be the incircle contact point on $AC$, and let the incircle cut $CM$ at one-third and two-thirds positions.'),(r'$AC=AT+CT_{AC}=AT+MT=AM=10$',r'$AC=AR+CR=AT+MT=AM=10$')],
 '2009II':[(r'正数 $a,b,c$ 满足 $a^{\log_3 7}=27,b^{\log_7 11}=49,c^{\log_{11}25}=\sqrt{11}$，求对应对数指数平方的三个幂之和。',r'正数 $a,b,c$ 满足 $a^{\log_3 7}=27,b^{\log_7 11}=49,c^{\log_{11}25}=\sqrt{11}$，求 $a^{(\log_3 7)^2}+b^{(\log_7 11)^2}+c^{(\log_{11}25)^2}$。')],
 '2019I':[(r'十五分之二（即 $15/2$）',r'$15/2$')],
 '2024I':[(r'(69+96\sqrt6)/46',r'(-21+96\sqrt6)/23'),(r'(equivalent to $\sqrt6<253/96$)',r'(use $\sqrt6<5/2$, giving $s<219/23<39/4$)')]
}
def change(obj,pairs):
 if isinstance(obj,str):
  for a,b in pairs:obj=obj.replace(a,b)
  return obj
 if isinstance(obj,list):return [change(v,pairs) for v in obj]
 if isinstance(obj,dict):return {k:change(v,pairs) for k,v in obj.items()}
 return obj
for paper,pairs in replacements.items():
 p=ROOT/f'data/batches/{paper}.json';data=json.loads(p.read_text(encoding='utf8'));p.write_text(json.dumps(change(data,pairs),ensure_ascii=False,indent=2),encoding='utf8')
 p=ROOT/f'scripts/author_{paper}.py';s=p.read_text(encoding='utf8');p.write_text(change(s,pairs),encoding='utf8')
print('Applied wording corrections to author scripts and batches.')

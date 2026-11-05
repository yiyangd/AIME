"""Independent finite checks for recent-paper authoring arithmetic and counts."""
from itertools import product,combinations,permutations
from collections import Counter,defaultdict
from pathlib import Path
import json,math
results={}
results['2024I-Q13']=[x for x in range(289) if (x**4+1)%289==0]
assert results['2024I-Q13']==[110,134,155,179]
results['2024I-Q11']=sum(any(not(set(B)&{(v+k)%8 for v in B}) for k in range(8)) for n in range(9) for B in combinations(range(8),n))
assert results['2024I-Q11']==115
results['2025I-Q03']=sum(1 for a in product(range(3),repeat=9) if (c:=Counter(a))[0]>c[1]>c[2]>0)
assert results['2025I-Q03']==2016
results['2025I-Q05']=sum(1 for ds in permutations('12345678') if int(''.join(ds))%22==0)
assert results['2025I-Q05']==2304
results['2025I-Q15']=sum(ca*cb*cubes[(-a-b)%2187] for cubes in [Counter(pow(x,3,2187) for x in range(1,730))] for a,ca in cubes.items() for b,cb in cubes.items())
assert results['2025I-Q15']==885735
results['2025II-Q10']=sum(all(not({i,i+1,i+2}<=set(S)) for i in range(14)) for S in combinations(range(16),8))
assert results['2025II-Q10']==2907
results['2026I-Q07']=sum(all(p[p[p[p[p[p[i]]]]]]==i for i in range(6)) for p in permutations(range(6)))
assert results['2026I-Q07']==396
success=0;good=0
for f in product(range(6),repeat=6):
 visible={i+1 for i in range(6) if f[i] not in f[i+1:]}
 if {2,4,6}<=visible:
  success+=1;good+=len(set(f))==5
results['2026I-Q09']={'conditioned':success,'favorable':good}
assert(success,good)==(14400,6480)
D=defaultdict(int);D[0,0]=1
for s in range(12):
 for (ss,v),count in list(D.items()):
  if ss!=s:continue
  for t in range(1,13-s):D[s+t,v-t if v%2 and t%2==0 else v+t]+=count
results['2026II-Q14']=D[12,0];assert D[12,0]==157
counts=Counter()
for a in product(range(3),repeat=7):
 if sum(a)%3==0 and sum(a[i]*a[(i+1)%7]*a[(i+3)%7] for i in range(7))%3==0:counts[a.count(0)]+=1
results['2026II-Q15']=dict(sorted(counts.items()));assert sum(counts.values())==393
out=Path(__file__).resolve().parents[1]/'audit/recent-discrete-checks.json';out.write_text(json.dumps(results,indent=2),encoding='utf8');print(json.dumps(results,indent=2))

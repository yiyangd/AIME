"""Independent finite enumerations supporting selected authored mathematical routes."""
from pathlib import Path
from itertools import permutations, combinations
from collections import deque,Counter
from math import gcd,comb,isqrt
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(q,got,expected,method):
    assert got==expected,(q,got,expected)
    checks.append({'question_id':q,'computed':str(got),'expected':str(expected),'method':method,'passed':True})
P=list(permutations(range(1,7)))
check('AIME-2020-I-Q05',sum(any(all(p[j]<p[j+1] for j in range(4)) or all(p[j]>p[j+1] for j in range(4)) for p in [t[:i]+t[i+1:] for i in range(6)]) for t in P),52,'Enumerate all 720 permutations and six deletions')
check('AIME-2020-I-Q11',sum(a==-6 or c==-20-6*a-2*b for a in range(-10,11) for b in range(-10,11) for c in range(-10,11)),510,'Enumerate all 9261 coefficient triples using necessary and sufficient root cases')
check('AIME-2020-II-Q09',sum(all(abs(p[i+1]-p[i])!=1 for i in range(5)) for p in P),90,'Direct permutation forbidden-adjacency check')
check('AIME-2020-II-Q10',sum(n for n in range(1,333) if (n*(n+1)//2)**2%(n+5)==17),239,'Direct remainder check through the proved divisor bound')
check('AIME-2020-II-Q12',sum(m-1<abs(1800-(m-1)*n) for m in range(3,11,2) for n in range(201,2001,2) if (m-1)*n<2000<=m*n),248,'Enumerate actual odd-grid and slope constraints')
check('AIME-2021-I-Q03',len({2**a-2**b for a in range(1,20) for b in range(a) if 0<2**a-2**b<1000}),50,'Direct distinct difference set')
check('AIME-2021-I-Q04',sum(a<b<66-a-b for a in range(1,66) for b in range(1,66) if 66-a-b>0),331,'Direct positive increasing triples')
special=[]
for a in range(3,1000):
    if 3*a*a%(a-2)==0:
        d2=3*a*a//(a-2);d=isqrt(d2)
        if d*d==d2:special.append(a+d)
check('AIME-2021-I-Q05',sum(special),31,'Exhaustive middle-term scan beyond all divisor candidates')
check('AIME-2021-I-Q07',sum((n-m)%(4*gcd(m,n))==0 for n in range(2,31) for m in range(1,n)),63,'Direct gcd feasibility count')
m,n=2020,2021; good=[]
for j in range(1,101):
    if n-m==1:good.append(j)
    m,n=m+18,n+19;d=gcd(m,n);m//=d;n//=d
check('AIME-2021-I-Q10',good,[1,2,8,18,30],'Exact reduced-fraction recurrence')
check('AIME-2021-II-Q03',sum(sum(p[i]*p[(i+1)%5]*p[(i+2)%5] for i in range(5))%3==0 for p in permutations(range(1,6))),80,'Enumerate all 120 cyclic product sums')
check('AIME-2021-II-Q06',sum(a.bit_count()*b.bit_count()==(a&b).bit_count()*(a|b).bit_count() for a in range(32) for b in range(32)),454,'Enumerate all 1024 subset pairs')
paths={(0,-1):1}
for step in range(8):
    nxt=Counter()
    for (v,prev),cnt in paths.items():
        for bit in (1,2,4):
            w=v^bit
            if w!=prev:nxt[w,v]+=cnt
    paths=nxt
check('AIME-2021-II-Q08',Fraction(sum(c for (v,p),c in paths.items() if v&4),sum(paths.values())),Fraction(17,32),'Enumerate all nonbacktracking cube paths as vertex-edge states')
check('AIME-2021-II-Q09',sum(gcd(2**m+1,2**n-1)>1 for m in range(1,31) for n in range(1,31)),295,'Direct 900 gcd calculations')
runs=[set(range(a,a+4)) for a in range(10,97) if any(x%6==0 and y%7==0 and x!=y for x in range(a,a+4) for y in range(a,a+4))]
freq=Counter(x for s in runs for x in s)
surv=[s for s in runs if all(freq[x]>1 for x in s)]
check('AIME-2021-II-Q11',sum(max(s) for s in surv),258,'Enumerate publicly possible sets and eliminate unique private numbers')
assert all(sum(x in s for s in surv)==1 for s in surv for x in s)
check('AIME-2021-II-Q13',next(n for n in range(1,1001) if (pow(2,n,1000)+pow(5,n,1000)-n)%1000==0),797,'Direct modular-power scan of all smaller exponents')
def funcs(n):
    k=isqrt(n)
    if k*k<n:k+=1
    j=k+(k%2!=n%2)
    return k+k*k-n,j+j*j-n
check('AIME-2021-II-Q15',next(n for n in range(1,300) if (lambda f,g:7*f==4*g)(*funcs(n))),258,'Direct explicit recurrence endpoint scan')
q=deque(range(1,2001));removed=[]
while q:
    removed.append(q.popleft())
    if q:q.rotate(-1)
check('AIME-2000-I-Q15',removed[-2]-1,927,'Independent deque simulation of original positions')
check('AIME-2000-II-Q02',sum((4000000//d+d)%2==0 for d in range(1,4000001) if 4000000%d==0)*2,98,'Direct factor pairs of x-y and x+y with parity')
check('AIME-2000-II-Q05',comb(8,5)*120*comb(8,3),376320,'Exact choose-order-distribute product')
out=ROOT/'output/qa';out.mkdir(parents=True,exist_ok=True)
(out/'authored-math-enumerations.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print('Passed',len(checks),'independent finite mathematical checks')

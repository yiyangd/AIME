"""Independent finite certificates used during the root's cross-review."""
import itertools,json,math
from pathlib import Path
from fractions import Fraction
R={}
def check(k,actual,expected):
    assert actual==expected,(k,actual,expected)
    R[k]=actual
check('2010II08-complementary-sets',sum(1 for a in range(1,4095) if not(a>>(a.bit_count()-1)&1) and not(((4095^a)>>(12-a.bit_count()-1))&1)),772)
lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
check('2010II11-all-weight-five-grids',sum(sum(len({(m>>i)&1 for i in L})==1 for L in lines)<=1 for m in range(512) if m.bit_count()==5),68)
triples=[]
for b in range(26):
    d=8044-3*b*b;s=math.isqrt(d)
    if s*s==d and (s-b)%2==0:triples.append([(s-b)//2,b,-(s+b)//2])
check('2011I15-integer-roots',triples,[[39,10,-49]])
check('2011II06-four-subsets',sum(a+d>b+c for a,b,c,d in itertools.combinations(range(1,11),4)),80)
valid=0
for A in itertools.combinations(range(9),3):
    remain=set(range(9))-set(A)
    for B in itertools.combinations(remain,3):
        labels=[2]*9
        for i in A:labels[i]=0
        for i in B:labels[i]=1
        valid+=all(labels[(i-1)%9]!=labels[i] or labels[(i+1)%9]!=labels[i] for i in range(9))
check('2011II12-valid-country-patterns',valid,1230)
check('2012I01-reversible-multiples-four',sum((100*a+10*b+c)%4==0 and (100*c+10*b+a)%4==0 for a in range(1,10) for b in range(10) for c in range(1,10)),40)
patterns=set(itertools.permutations((0,0,0,1,1,1,2,2,2)))
check('2012I03-exactly-one-correct-meal',sum(sum(x==i//3 for i,x in enumerate(p))==1 for p in patterns),216)
B={x for x in range(8192) if x.bit_count()==8}
check('2012I05-weight-preserving-increment',sum(x+1 in B for x in B),330)
roots=[x for x in range(1,3000) if x*x%1000==256]
check('2012I10-tenth-positive-root',roots[9],2484)
check('2012I11-invariant-diamond-points',sum((x+y)%3==0 and (x-y)%5==0 for x in range(-100,101) for y in range(-100+abs(x),101-abs(x))),1373)
check('2012I15-possible-moduli',sum(math.gcd(n,6)==1 for n in range(2,1000)),332)
check('2014II09-circular-chair-subsets',sum(any(all(m>>((i+j)%10)&1 for j in range(3)) for i in range(10)) for m in range(1024)),581)
hexagon=[(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]
vertices=[(x,y,z) for z in (0,2) for x,y in hexagon]
def ds(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2+4*(a[2]-b[2])**2
check('2018I07-isosceles-prism-triples',sum(len({ds(a,b),ds(a,c),ds(b,c)})<3 for a,b,c in itertools.combinations(vertices,3)),52)
check('2018I09-fixed-sum-four-subsets',sum(any(a+b==16 for a,b in itertools.combinations(S,2)) and any(a+b==24 for a,b in itertools.combinations(S,2)) for S in itertools.combinations(range(1,21),4)),210)
state={(0,0):1}
for _ in range(15):
    ns={}
    for (ring,pos),v in state.items():
        for k in ((ring,(pos+(1 if ring==0 else -1))%5),(1-ring,pos)):
            ns[k]=ns.get(k,0)+v
    state=ns
check('2018I10-directed-wheel-state-DP',state[(0,0)],3004)
check('2018II10-all-functions-five',sum(all(f[f[x]]==f[f[f[x]]] for x in range(5)) for f in itertools.product(range(5),repeat=5)),756)
check('2018II11-indecomposable-permutations',sum(all(max(p[:k])>k for k in range(1,6)) for p in itertools.permutations(range(1,7))),461)
valid=0
for steps in itertools.product((-3,-2,-1,1,2,3),repeat=6):
    if sum(steps)!=12:continue
    f=[0]
    for x in steps:f.append(f[-1]+x)
    valid+=all(j-i<=abs(f[j]-f[i])<=3*(j-i) for i in range(7) for j in range(i+1,7))
check('2018II15-all-increment-words',valid,185)
ab=0
for a,b in itertools.product(range(-20,21),repeat=2):
    d=(a+2)**2-4*(2*a+b+4)
    roots=set()
    if d>=0 and math.isqrt(d)**2==d:
        for sgn in (-1,1):
            num=-a-2+sgn*math.isqrt(d)
            if num%2==0:roots.add(num//2)
    roots.discard(2)
    ab+=len(roots)==1
check('2023I09-all-coefficient-pairs',ab*41,738)
check('2023I11-all-subsets',sum(sum(bool(m>>i&1 and m>>(i+1)&1) for i in range(9))==1 for m in range(1024)),235)
weak=[];admissible=[]
for b in range(1,22):
    for a in range(b+1,32):
        p=a*a+b*b;q=p-4*a*b
        if q*q<p<1000:
            weak.append(p)
            if all(p%d for d in range(2,math.isqrt(p)+1)) and (a+b)*abs(q)<p:admissible.append(p)
check('2023I15-prime-norm-candidates',sorted(admissible),[17,53,241,349])
check('2023I15-weaker-norm-candidates',sorted(weak),[10,17,53,68,130,153,212,241,272,349,386,520,565,725,778,905,964])
clock=0
for word in itertools.product((0,1),repeat=12):
    a=b=0;seen=set()
    for t in range(144):
        seen.add((a,b))
        if word[t%12]:a=(a+1)%12
        else:b=(b+1)%12
    clock+=len(seen)==144 and (a,b)==(0,0)
check('2023I14-all-periodic-clock-rules',clock,1608)
check('2023II07-all-two-colorings',sum(sum((m>>i&1)==(m>>(i+6)&1)==1 for i in range(6))<=1 and sum((m>>i&1)==(m>>(i+6)&1)==0 for i in range(6))<=1 for m in range(4096)),928)
out=Path(__file__).resolve().parents[1]/'output/qa/root-review-enumerations.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(R,indent=2),encoding='utf8')
print(f'{len(R)} independently enumerated review certificates passed')

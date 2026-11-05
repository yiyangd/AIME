"""Independent finite checks for selected 2017 problems reviewed by source_audit."""
import itertools,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(q,actual,expected,method):
 assert actual==expected,(q,actual,expected)
 checks.append({'question_id':'AIME-2017-'+q,'actual':actual,'expected':expected,'method':method,'passed':True})
pts=[(F(x),F(0)) for x in range(5)]+[(F(4)*(5-k)/5,F(6)*k/5) for k in range(1,5)]+[(F(0),F(y)) for y in range(1,7)]
check('I-Q01',sum((b[0]-a[0])*(c[1]-a[1])!=(b[1]-a[1])*(c[0]-a[0]) for a,b,c in itertools.combinations(pts,3)),390,'Exact rational determinants on an equivalent 15-point triangle boundary')
check('I-Q03',sum((n*(n+1)//2)%10 for n in range(1,2018))%1000,69,'Direct sum of every triangular-number last digit')
digits=[]
for a,b,c,d in itertools.product(range(1,8),repeat=4):
 if 8*a+b+F(8*c+d,64)==13*b+F(12*b+a,144):digits.append((a,b,c,d))
check('I-Q05',digits,[(3,2,1,4)],'Exhaust every nonzero base-eight digit quadruple with rational arithmetic')
check('I-Q07',sum(math.comb(6,a)*math.comb(6,b)*math.comb(6,a+b) for a in range(7) for b in range(7-a))%1000,564,'Direct binomial-coefficient sum')
a=10
hits=[]
for n in range(11,100):
 a=(100*a+n)%99
 if a==0:hits.append(n)
check('I-Q09',min(hits),45,'Iterate the concatenation recurrence modulo 99')
count=0
for p in itertools.permutations(range(1,10)):
 med=[sorted(p[3*i:3*i+3])[1] for i in range(3)]
 count+=sorted(med)[1]==5
check('I-Q11',count,207360,'Enumerate all 9! ordered grids and compute both levels of medians')
valid=0
for mask in range(1<<10):
 s={i+1 for i in range(10) if mask>>i&1}
 valid+=not any(a*b in s for a in s for b in s)
check('I-Q12',valid,252,'Test all 1024 subsets including repeated factor choices')
check('I-Q14',pow(2,192,1000),896,'Exact modular exponentiation after the analytic exponent reduction')
check('II-Q01',sum(not(s<=set(range(1,6)) or s<=set(range(4,9))) for s in ({i+1 for i in range(8) if m>>i&1} for m in range(256))),196,'Test every subset against the two forbidden containments')
def nonzero_ternary(n):
 while n:
  if n%3==0:return False
  n//=3
 return True
check('II-Q04',sum(nonzero_ternary(n) for n in range(1,2018)),222,'Convert each integer by repeated division by three')
check('II-Q06',sum(n for n in range(1,1000) if math.isqrt(n*n+85*n+2017)**2==n*n+85*n+2017),195,'Direct square test through 999, supplemented by the complete factor-pair proof')
check('II-Q08',sum(sum(F(n**j,math.factorial(j)) for j in range(7)).denominator==1 for n in range(1,2017)),134,'Sum each rational truncated exponential without modular simplification')
edges=list(itertools.combinations(range(5),2));strong=0
for mask in range(1<<10):
 adjacency=[set() for _ in range(5)]
 for k,(i,j) in enumerate(edges):
  if mask>>k&1:adjacency[i].add(j)
  else:adjacency[j].add(i)
 ok=True
 for start in range(5):
  seen={start};stack=[start]
  while stack:
   for nxt in adjacency[stack.pop()]-seen:seen.add(nxt);stack.append(nxt)
  if len(seen)!=5:ok=False;break
 strong+=ok
check('II-Q11',strong,544,'Enumerate every tournament and perform directed reachability from every vertex')
def f(n):return n*((n-1)//2)-(2*n//3 if n%3==0 else 0)
check('II-Q13',[n for n in range(3,1000) if f(n+1)-f(n)==78],[36,52,157],'Scan the exact closed counting formula across every congruence class')
def tri_count(n):
 total=0
 for a,b,c in itertools.combinations(range(n),3):
  dist=[min(b-a,n-(b-a)),min(c-b,n-(c-b)),min(c-a,n-(c-a))]
  total+=len(set(dist))<3
 return total
for n in (36,37,52,53,157,158):check('II-Q13',tri_count(n),f(n),'Enumerate all vertex triples and compare cyclic chord-length indices for n='+str(n))
directions=[v for v in itertools.product((-1,0,1),repeat=3) if v!=(0,0,0) and next(x for x in v if x)!=-1]
linecount=0
for v in directions:
 for p in itertools.product(range(1,11),repeat=3):
  prev=tuple(p[i]-v[i] for i in range(3))
  if all(1<=x<=10 for x in prev):continue
  length=0
  while all(1<=p[i]+length*v[i]<=10 for i in range(3)):length+=1
  linecount+=length==8
check('II-Q14',linecount,168,'Enumerate all primitive allowed directions and canonical first grid points')
target=ROOT/'output/qa/review-2017-enumerations.json';target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps({'checks':checks,'passed':len(checks)},indent=2),encoding='utf-8')
print('Passed',len(checks),'independent finite checks')

"""Author-side exact/finite checks of original teaching examples (not independent review)."""
import itertools,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];out=[]
def check(code,value,expected,method):
 assert value==expected,(code,value,expected)
 out.append({'method_id':code,'actual':str(value),'expected':str(expected),'check':method,'passed':True})
def tau(n):return sum(n%d==0 for d in range(1,n+1))
def square(n):return math.isqrt(n)**2==n
def cube(n):return any(k**3==n for k in range(1,1+math.isqrt(n)))
check('NT01-M01',next(u for u in range(1,100) if square(u) and cube(72*u)),81,'Independent bounded search; valuation proof supplies global minimum')
divs=[d for d in range(1,361) if 360%d==0 and math.gcd(d,360//d)==1]
check('NT01-M04',(len(divs),sum(divs)),(8,540),'Enumerate unitary divisors directly')
check('NT02-M01',[n for n in range(1,200) if (n*n+2*n+8)%(n+3)==0],[8],'Direct polynomial remainder test; proof supplies exhaustive bound')
check('NT02-M03',sum(24%x==0 and (24-x)%x==0 for x in range(1,24)),7,'Enumerate all possible positive first coordinates')
check('NT02-M07',max(n for n in range(1,16) if (math.factorial(10)+math.factorial(9))%math.factorial(n)==0),9,'Test exact factorial divisibility through the proved upper bound')
check('NT03-M01',sum((6*x-9)%15==0 for x in range(1,81)),16,'Direct residue test')
check('NT03-M03',[x for x in range(40) if (x*x-x)%40==0],[0,1,16,25],'Exhaust all residues independently of CRT')
check('NT03-M06',sum(sum(i+1 for i in range(4) if mask>>i&1)%3==0 for mask in range(16)),6,'Enumerate every subset')
representable={4*a+7*b for a in range(31) for b in range(18)}
check('NT03-M08',max(n for n in range(1,101) if n not in representable),17,'Direct bounded stamp reachability; residue proof handles all larger integers')
check('NT04-M03',pow(6,20,40),16,'Direct modular exponentiation')
check('NT04-M04',next(n for n in range(1,26) if pow(2,n,25)==1),20,'Exhaust possible exponents')
check('NT04-M05',[n for n in range(20) if n%10==pow(3,n,10)],[7,13],'Exhaust complete combined period')
check('NT04-M06',next(n for n in range(1,41) if all(sum(pow(a,k,5) for k in range(1,n+1))%5==0 for a in range(5))),20,'Test every residue for each candidate universal exponent')
check('NT05-M01',[(x,y) for x in range(1,10) for y in range(1,17) if 7*x+4*y==65],[(3,11),(7,4)],'Direct finite positive integer enumeration')
check('NT05-M02',[(u,v) for u in range(1,25) for v in range(u) if u*u-v*v==45],[(7,2),(9,6),(23,22)],'Enumerate all candidate integer coordinates within factor bound')
check('NT05-M03',[(x,y) for x in range(1,43) for y in range(x,43) if F(1,x)+F(1,y)==F(1,6)],[(7,42),(8,24),(9,18),(10,15),(12,12)],'Exact rational Egyptian-fraction enumeration')
check('NT05-M05',[(a,b,c) for a in range(1,4) for b in range(a,4) for c in range(b,4) if a*a+b*b+c*c==14],[(1,2,3)],'Enumerate ordered square triples')
check('NT05-M06',[(x,y) for x in range(7) for y in range(4) if 4*x+7*y==25],[(1,3)],'Exhaust the bounded rectangle')
check('NT05-M08',next(n for n in range(1,20) if any(F(1,3)<F(m,n)<F(2,5) for m in range(1,n))),8,'Exhaust smaller denominators')
check('NT05-M10',sorted({x+y+z for x in range(13) for y in range(5) for z in range(3) if x+3*y+5*z==12}),[4,6,8,10,12],'Enumerate all original nonnegative solutions')
pals=[n for n in range(100,1000) if str(n)==str(n)[::-1] and n%3==0]
check('NT06-M03',(len(pals),F(sum(pals),len(pals))),(30,F(5601,10)),'Direct decimal palindrome scan and exact average')
check('NT06-M05',[n for n in range(64) if n.bit_count()==2][4],10,'Enumerate binary values in numerical order')
def digitsum(n,b):
 s=0
 while n:s+=n%b;n//=b
 return s
check('NT06-M06',next(n for n in range(1,200) if digitsum(n,5)==11),99,'Brute-force digit expansion independent of greedy proof')
check('NT06-M07',sum('11' not in format(n,'04b') for n in range(16)),8,'Enumerate all four-bit strings')
check('NT06-M10',sum(digitsum(n,10) for n in range(1000)),13500,'Direct sum of every decimal digit')
check('NT07-M03',sorted({F(k,12).numerator for k in range(1,13)}),[1,2,3,5,7,11],'Reduce every fraction explicitly')
check('NT07-M05',(F(1,2)+F(3,8)+F(5,32)).denominator,32,'Exact rational addition')
sqdiv=[d for d in range(1,145) if 144%d==0 and square(d)]
check('NT08-M01',(len(sqdiv),sum(sqdiv)),(6,210),'Enumerate actual square divisors')
check('NT08-M02',next(n for n in range(1,129) if tau(n)==8),24,'Exhaust all smaller integers')
cum=0;odd=0
for n in range(1,21):cum+=tau(n);odd+=cum%2
check('NT08-M05',odd,10,'Compute each divisor count instead of using square-block parity')
check('NT08-M06',sum(18%n==0 or 24%n==0 for n in range(1,25)),10,'Enumerate divisor-set union')
check('AL01-M01',F(3,10)*F(15,2)+F(7,10)*F(9,2),F(45,100)*12,'Verify exact mixture conservation')
check('AL01-M04',1**2+3**2+6**2,46,'Recover coordinates and calculate target')
check('AL01-M08',(2*2**2+3*3**2,2*2*3,2**2*3**2),(35,12,36),'Explicit real-radical witness verifies constant and cross coefficients')
check('AL01-M08',[(a,b) for a in range(1,6) for b in range(1,5) if 2*a*a+3*b*b==35 and 2*a*b==12],[(2,3)],'Exhaust the positive-integer coefficient solutions within the radical magnitude bounds; rational coefficient premise is essential')
check('AL02-M06',len({(-(r+12//r),12) for r in range(1,13) if 12%r==0}),3,'Count distinct coefficient pairs, not ordered roots')
coeff=[1,-3,4,-4,3,-1]
check('AL02-M09',sum(abs(c) for c in coeff),16,'Direct expanded coefficient absolute sum')
check('AL03-M01',(2-1j)+2*(2+1j),6+1j,'Substitute the complex solution')
check('AL03-M02',-(2+1j)*(2-1j)*(-3),15+0j,'Direct conjugate root product')
check('AL03-M08',(3+4j)*F(1,5)*(3-4j),5+0j,'Direct maximizing complex witness')
N=10
check('AL05-M03',sum(F(1,k*(k+1)*(k+2)) for k in range(1,N+1)),F(1,4)-F(1,2*(N+1)*(N+2)),'Sum rational terms directly')
u=[F(1),F(2)]
for n in range(1,11):u.append((u[n]*u[n-1]+2)/u[n])
check('AL05-M07',u[10]*u[11],F(22),'Iterate the original nonlinear recurrence exactly')
sample=list(itertools.combinations(range(7),3))
check('PS01-M01',F(sum(sum(i<4 for i in s)==2 for s in sample),len(sample)),F(18,35),'Enumerate all labeled three-subsets')
sets=[{i for i in range(4) if m>>i&1} for m in range(16)]
check('PS01-M03',F(sum(len(a&b)==1 for a in sets for b in sets),256),F(27,64),'Enumerate all independent subset pairs')
check('PS01-M04',F(sum((a-b)%2==0 and a!=b for a in range(1,7) for b in range(1,7)),36),F(1,3),'Enumerate all dice pairs')
terminal=[]
for word in itertools.product('HT',repeat=3):
 stop=word.index('H')+1 if 'H' in word else 3
 t=word[:stop];terminal.append(t.count('T')>t.count('H'))
check('PS01-M06',F(sum(terminal),8),F(1,4),'Use eight equal-probability full toss strings and apply the stopping rule')
check('PS01-M07',F(sum(sum(i==p[i] for i in range(4))==1 for p in itertools.permutations(range(4))),24),F(1,3),'Enumerate all four-label permutations')
latent=[]
for model in ('fair','always'):
 for tosses in itertools.product((0,1),repeat=3):
  actual=tosses if model=='fair' else (1,1,1)
  if actual[0]:latent.append(actual)
check('PS02-M02',(F(sum(t[1] for t in latent),len(latent)),F(sum(t[1] and t[2] for t in latent),len(latent))),(F(5,6),F(3,4)),'Enumerate a uniform latent-model and three-bit experiment')
import sympy as s
h=s.symbols('h0:4');eq=[]
for state in range(2):
 for parity in range(2):
  idx=2*state+parity;newparity=1-parity
  onH=F(newparity) if state==1 else h[2+newparity]
  onT=h[newparity]
  eq.append(s.Eq(h[idx],(onH+onT)/2))
check('PS02-M06',s.solve(eq,h)[h[0]],s.Rational(2,5),'Independent four-state ordinary hitting-probability system rather than signed moments')
def area(pts):return abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))))/2
check('PS03-M02',area([(F(1,2),0),(2,0),(F(1,2),F(3,2))])/6,F(3,16),'Exact shoelace area')
check('PS03-M03',F(1,2)-area([(F(3,4),F(1,4)),(1,0),(1,F(1,2))]),F(7,16),'Exact shoelace subtraction for joint sum-and-difference event')
pairs=list(itertools.combinations(range(4),2));types={'cross':0,'avoid':0,'half':0}
for a,b in itertools.product(pairs,repeat=2):
 if set(a)&set(b):types['half']+=1
 elif a==(0,2) or b==(0,2):types['cross']+=1
 else:types['avoid']+=1
check('PS03-M04',types,{'cross':2,'avoid':4,'half':30},'Enumerate all 36 ordered quadrant-pair choices')
target=ROOT/'output/qa/knowledge-source-example-checks.json'
target.write_text(json.dumps({'kind':'author-side exact and finite checks; not independent review','passed':len(out),'checks':out},indent=2),encoding='utf-8')
print('Passed',len(out),'author-side original-example checks')

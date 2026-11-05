"""Independent finite/example arithmetic checks supplementing the proof-review receipts."""
from fractions import Fraction as F
from itertools import product,combinations,permutations
from math import comb,factorial,gcd,lcm,isqrt
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(mid,value,expected):
 assert value==expected,(mid,value,expected)
 checks.append(dict(method_id=mid,result=str(value),expected=str(expected),passed=True))
def divisors(n):return [d for d in range(1,n+1) if n%d==0]
def power(n,k):
 lo,hi=0,n+1
 while hi-lo>1:
  m=(lo+hi)//2
  if m**k<=n:lo=m
  else:hi=m
 return lo**k==n
def valuation(n,p):
 e=0
 while n%p==0:e+=1;n//=p
 return e
def subsets(xs):
 return [c for k in range(len(xs)+1) for c in combinations(xs,k)]
def area(poly):
 return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))/2

check('NT01-M01',min(u for u in range(1,1000) if power(u,2) and power(72*u,3)),81)
check('NT01-M02',factorial(9)//(factorial(3)**4),280)
unitary=[d for d in divisors(360) if gcd(d,360//d)==1]
check('NT01-M04',(len(unitary),sum(unitary)),(8,540))
primes=[p for p in range(7,100) if all(p%d for d in range(2,isqrt(p)+1))]
check('NT01-M05',min(a*b*c for a,b,c in product(primes,repeat=3) if not a==b==c),539)
check('NT01-M06',len([n for n in range(1,17) if valuation(n,2)>=2]),4)
check('NT01-M07',[(x,y) for x in range(1,257) for y in range(1,257) if x*gcd(x,y)==256 and y==4*gcd(x,y)],[(16,64)])
check('NT01-M08',next(k for k in range(1,82) if pow(10,k,81)==1),9)
check('NT01-M01-growth',sum(a for n in range(12) for m in range(12) if ((a:=2**n*3**m)<6*n or a<6*m)),42)

check('NT02-M01',[n for n in range(1,500) if (n*n+2*n+8)%(n+3)==0],[8])
check('NT02-M02',next(11*t for t in range(1,100) if 4*(4*t+5)==3*7*t),44)
check('NT02-M03',sum(1 for x in range(1,24) if (24-x)%x==0),7)
seen=set();cycles=[]
for i in range(30):
 if i in seen:continue
 cycle=[];j=i
 while j not in seen:cycle.append(j);seen.add(j);j=(j+8)%30
 cycles.append(len(cycle))
check('NT02-M04',cycles,[15,15])
for a,b in [(1,2),(2,5),(5,7),(7,11)]:
 g=gcd(a+2,b+3);d=b-a;inv=3*a-2*b
 assert gcd(inv,d+1)==g and F((b+3)-(a+2),g)==F(d+1,g)
check('NT02-M05',True,True)
check('NT02-M06',sum(lcm(*s)==12 for s in subsets(divisors(12)) if s),44)
check('NT02-M07',max(n for n in range(1,12) if (factorial(10)+factorial(9))%factorial(n)==0),9)

check('NT03-M01',sum((6*x-9)%15==0 for x in range(1,81)),16)
check('NT03-M02',[n%2 for n in range(1,100) if (n*(n+1)//2)%(n+2)==1],[1]*50)
check('NT03-M03',[x for x in range(40) if (x*x-x)%40==0],[0,1,16,25])
check('NT03-M04',7 in {(a*a+b*b+c*c)%8 for a,b,c in product(range(8),repeat=3)},False)
check('NT03-M05',sum(n*n//3 for n in range(1,13)),214)
check('NT03-M06',sum(sum(s)%3==0 for s in subsets([1,2,3,4])),6)
check('NT03-M07',[x for x in range(49) if x%7==2 and (x*x-4)%49==0],[2])
represented={4*a+7*b for a,b in product(range(50),repeat=2)}
check('NT03-M08',max(n for n in range(1,100) if n not in represented),17)
win=[False]
for n in range(1,100):win.append(any(not win[n-k] for k in (1,2) if n>=k))
check('NT03-M09',[n for n in range(100) if not win[n]],list(range(0,100,3)))

check('NT04-M01',(next(d for d in range(1,13) if pow(3,d,13)==1),(pow(3,100,13)+1)%13),(3,4))
fib=[0,1]
for n in range(99):fib.append((fib[-1]+fib[-2])%2)
check('NT04-M02',fib[100],1)
check('NT04-M03',pow(6,20,40),16)
check('NT04-M04',next(d for d in range(1,26) if pow(2,d,25)==1),20)
check('NT04-M05',[n for n in range(20) if n%10==pow(3,n,10)],[7,13])
check('NT04-M06',next(N for N in range(1,41) if all(sum(pow(a,j,5) for j in range(1,N+1))%5==0 for a in range(5))),20)
for k in range(1,5):
 image={pow(a,3,3**(k+1)) for a in range(3**k) if a%3}
 assert image=={a for a in range(3**(k+1)) if a%9 in (1,8)}
check('NT04-M04-cube-classes',True,True)

check('NT05-M01',[(x,y) for x,y in product(range(1,20),repeat=2) if 7*x+4*y==65],[(3,11),(7,4)])
check('NT05-M02',[(u,v) for u in range(24) for v in range(u) if u*u-v*v==45],[(7,2),(9,6),(23,22)])
check('NT05-M03',[(x,y) for x in range(1,50) for y in range(x,50) if F(1,x)+F(1,y)==F(1,6)],[(7,42),(8,24),(9,18),(10,15),(12,12)])
check('NT05-M04',[(a*a,b*b) for a in range(1,7) for b in range(a,7) if a+b==7],[(1,36),(4,25),(9,16)])
check('NT05-M05',[(a,b,c) for a in range(1,5) for b in range(a,5) for c in range(b,5) if a*a+b*b+c*c==14],[(1,2,3)])
check('NT05-M06',[(x,y) for x,y in product(range(7),range(4)) if 4*x+7*y==25],[(1,3)])
check('NT05-M07',max(n for n in range(1,100) if (isqrt(n)+1)**2>2*n)+1,5)
check('NT05-M08',min(n for n in range(1,30) for m in range(1,n) if F(1,3)<F(m,n)<F(2,5)),8)
check('NT05-M10',sorted({x+y+z for x,y,z in product(range(13),repeat=3) if x+3*y+5*z==12}),[4,6,8,10,12])

check('NT06-M01',[(b,d) for b in range(3,100) for d in range(b) if b*b+d*b+2==2*b*b],[])
check('NT06-M02',([q for q in range(7) if (100*q+37)%7==0],(100*6+12)%7),([6],3))
pal=[n for n in range(100,1000) if str(n)==str(n)[::-1] and n%3==0]
check('NT06-M03',(len(pal),F(sum(pal),len(pal))),(30,F(5601,10)))
for bits in range(2,9):
 valid=[n for n in range(2**bits) if n.bit_count()==(n+1).bit_count()]
 assert valid==[n for n in range(2**bits) if n%4==1]
check('NT06-M04',True,True)
check('NT06-M04-boundary',((1).bit_count(),(2).bit_count()),(1,1))
check('NT06-M05',[n for n in range(64) if n.bit_count()==2][4],10)
check('NT06-M06',min(25*a+5*b+c for a in range(1,5) for b,c in product(range(5),repeat=2) if a+b+c==11),99)
check('NT06-M07',sum('11' not in ''.join(x) for x in product('01',repeat=4)),8)
check('NT06-M08',next(ds for ds in product((-1,0,1),repeat=3) if sum(d*3**i for i,d in enumerate(ds))==8),(-1,0,1))
check('NT06-M09',sum(a+b==9 and a!=b for a in range(1,10) for b in range(10)),9)
check('NT06-M10',sum(sum(map(int,str(n))) for n in range(1000)),13500)
check('NT06-M04-zero-cases',sum('0' not in str(a) and '0' not in str(1000-a) for a in range(1,1000)),738)

check('NT07-M01',F(12+21+3,99),F(4,11))
check('NT07-M02',[b for b in range(1,100) if gcd(18,b)==6],[6*t for t in range(1,17) if t%3])
check('NT07-M03',sorted({F(k,12).numerator for k in range(1,13)}),[1,2,3,5,7,11])
check('NT07-M04',[(m,n) for n in range(1,11) for m in range(n+1) if F(501,1000)<=F(m,n)<F(510,1000)],[])
check('NT07-M05',F(1,2)+F(3,8)+F(5,32),F(33,32))

sd=[d for d in divisors(144) if power(d,2)]
check('NT08-M01',(len(sd),sum(sd)),(6,210))
check('NT08-M02',next(n for n in range(1,200) if len(divisors(n))==8),24)
check('NT08-M03',all((4*a+1)*(4*b+1)%4==1 for a,b in product(range(10),repeat=2)),True)
check('NT08-M04',F(sum(gcd(n,30)==1 for n in range(30)),15),F(8,15))
check('NT08-M05',sum(sum(len(divisors(j)) for j in range(1,n+1))%2 for n in range(1,21)),10)
check('NT08-M06',len(set(divisors(18))|set(divisors(24))),10)
check('NT08-M07',(len(divisors(6)),F(1,100)/(1-F(1,100))**2),(4,F(100,9801)))

check('AL01-M01',F(3,10)*F(15,2)+F(7,10)*F(9,2),F(45,100)*12)
check('AL01-M02',2+F(2,3)/F(1,12),10)
check('AL01-M03',(3-1)**2+(4-0)**2,20)
check('AL01-M04',1**2+3**2+6**2,46)
check('AL01-M05',(5*5-2*3)**2-2*3**2,343)
check('AL01-M06',[(x,y,z) for x,y,z in product(range(-3,4),repeat=3) if x+y+z==0 and x*y+z==y*z+x==z*x+y],[(-2,1,1),(0,0,0),(1,-2,1),(1,1,-2)])
check('AL01-M07',(F(5,2)-F(3,2))**2,1)
check('AL01-M08',(2*2**2+3*3**2,2*2*3,2**2*3**2),(35,12,36))
check('AL01-M10',2*F(0,1)/(0**2-1),0)
check('AL02-M01',2*(2**2+6)-(-3)*2+3*(-1),23)
check('AL02-M02',(3*1+4,2**2-2-1),(7,1))
check('AL02-M03',[sum(([1,1,1][i]*[1,1,1][j] for i in range(3) for j in range(3) if i+j==k)) for k in range(5)],[1,2,3,2,1])
check('AL02-M06',[(a,b) for a in range(13) for b in range(a,13) if a*b==12],[(1,12),(2,6),(3,4)])
check('AL02-M09',[sum(comb(3,j)*(-1)**j for j in range(4) if j==k or j+2==k) for k in range(6)],[1,-3,4,-4,3,-1])
check('AL03-M01',complex(2,-1)+2*complex(2,1),complex(6,1))
check('AL03-M02',-complex(2,1)*complex(2,-1)*(-3),15)
c=complex(F(1,2),F(1,2));check('AL03-M04',1j*c+1,c)
check('AL03-M08',(3*F(3,5)-4*F(-4,5),F(3,5)**2+F(-4,5)**2),(5,1))
z=2;orb=[]
for _ in range(4):orb.append(z);z=F(1,1-z)
check('AL03-M09',orb,[2,-1,F(1,2),2])
check('AL04-M02',(8*4,F(8,4)),(32,2))
check('AL04-M05',F(4,3)-1+F(8,3)-2,1)
check('AL04-M06',8,2**3)
check('AL05-M01',(3+8==1+10==5+6),True)
check('AL05-M02',F(3,4)/(1-F(1,64)),F(16,21))
for N in range(1,30):assert sum((F(1,k*(k+1)*(k+2)) for k in range(1,N+1)),F())==F(1,4)-F(1,2*(N+1)*(N+2))
check('AL05-M03',True,True)
check('AL05-M04',F(1,3)/(1-F(1,3))**2,F(3,4))
u=[0]
for _ in range(12):u.append(3*u[-1]+2)
check('AL05-M05',u,[3**n-1 for n in range(13)])
u=[2,5]
for _ in range(12):u.append(2*u[-1]-u[-2]+4)
check('AL05-M06',u,[2*n*n+n+2 for n in range(14)])
u=[F(1),F(2)]
for _ in range(10):u.append((u[-1]*u[-2]+2)/u[-1])
check('AL05-M07',u[10]*u[11],22)
u=[3,3]
for _ in range(7):u.append(u[-1]*(u[-2]-1))
check('AL05-M08',min(u),3)
t=[F(2)+j*F(3) for j in range(10)]
b=[v for i in range(9) for v in (t[i]**2,t[i]*t[i+1])]+[t[9]**2]
check('AL05-M09',all(b[j+1]**2==b[j]*b[j+2] if j%2==0 else b[j]+b[j+2]==2*b[j+1] for j in range(len(b)-2)),True)
check('AL05-M10',[F(2),F(3),F(1,2),F(1,3)],[F(2),F(3),1/F(2),1/F(3)])
check('AL05-M11',sum({x for x in range(-5,10) if abs(x-2) in (-1,1,3)}),8)
trib=[-1,1,1,1]
for _ in range(30):trib.append(sum(trib[-3:]))
check('AL05-M05-tribonacci',all(2*sum(trib[1:N+1])==trib[N+2]+trib[N]-trib[2]-trib[0] for N in range(1,29)),True)
for r in range(1,4):
 u=list(range(1,2*r+1))
 for n in range(2*r,100):u.append(sum((-1)**(j+1)*u[n-j] for j in range(1,2*r+1)))
 assert all(u[n]==-u[n-2*r-1] for n in range(2*r+1,100))
check('AL05-M05-antiperiod',True,True)

check('PS01-M01',F(comb(4,2)*comb(3,1),comb(7,3)),F(18,35))
check('PS01-M02',F(4,comb(4,2)),F(2,3))
ss=subsets(range(4))
check('PS01-M03',F(sum(len(set(a)&set(b))==1 for a,b in product(ss,repeat=2)),len(ss)**2),F(27,64))
check('PS01-M04',F(sum(a%2==b%2 and a!=b for a,b in product(range(1,7),repeat=2)),36),F(1,3))
check('PS01-M05',F(sum(c[1]==c[3] for c in product(range(2),repeat=4)),16),F(1,2))
check('PS01-M06',sum((F(1,2**len(w)) for w in ['H','TH','TTH','TTT'] if w.count('T')>w.count('H')),F()),F(1,4))
check('PS01-M07',F(sum(sum(i==v for i,v in enumerate(p))==1 for p in permutations(range(4))),factorial(4)),F(1,3))
check('PS02-M01',F(sum(a%2 and b%2 for a,b in product(range(1,7),repeat=2)),sum((a+b)%2==0 for a,b in product(range(1,7),repeat=2))),F(1,2))
check('PS02-M02',(F(1,3)*F(1,2)+F(2,3),F(1,3)*F(1,4)+F(2,3)),(F(5,6),F(3,4)))
check('PS02-M03',(F(1,4)*F(1,2)+F(3,4)*F(1,3),F(1,8)/F(3,8)),(F(3,8),F(1,3)))
check('PS02-M04',F(1,2)*F(2,3)+F(1,2)*F(1,3),F(1,2))
check('PS02-M05',F(1,2)*F(1,3),F(1,6))
u0,u1=F(1,5),F(-3,5)
check('PS02-M06',(u0==-(u0+u1)/2 and u1==-(u0+1)/2,(1-u0)/2),(True,F(2,5)))
check('PS03-M01',(F(1,2)-F(1,6))/F(1,2),F(2,3))
check('PS03-M02',area([(F(1,2),F(0)),(F(2),F(0)),(F(1,2),F(3,2))])/6,F(3,16))
check('PS03-M03',F(1,2)-area([(F(3,4),F(1,4)),(F(1),F(0)),(F(1),F(1,2))]),F(7,16))
check('PS03-M04',2*F(1,3)*F(2,3),F(4,9))
check('PS03-M05',2*F(1,4)*F(3,4),F(3,8))
arc_pairs=list(combinations(range(4),2));cross=F()
for a,b in product(arc_pairs,repeat=2):
 groups=[[name for name,arc in [('A0',a[0]),('A1',a[1]),('B0',b[0]),('B1',b[1])] if arc==i] for i in range(4)]
 orders=list(product(*[list(permutations(g)) for g in groups]));good=0
 for order in orders:
  word=''.join(v[0] for g in order for v in g)
  good+=word in ('ABAB','BABA')
 cross+=F(good,len(orders))
check('PS03-M04-four-arcs',cross/36,F(17,36))

# GE10 was assigned later to accelerate the final independent-review freeze.
check('GE10-M01',(130*F(4,13),130*F(9,13),F(2,3)**3),(40,90,F(8,27)))
check('GE10-M02',1+6*F(1,6),2)
for s,x,y,z in [(2,1,3,4),(7,-2,5,11),(3,0,0,0)]:
 pb=(x-s)**2+y*y+z*z;pc=x*x+(y-s)**2+z*z;pd=x*x+y*y+(z-s)**2;pg=(x-s)**2+(y-s)**2+(z-s)**2
 assert pb+pc+pd-pg==2*(x*x+y*y+z*z)
check('GE10-M03',True,True)
vertices=list(product(range(2),repeat=3));eq=0;types={}
for tri in combinations(vertices,3):
 ds=tuple(sorted(sum((a-b)**2 for a,b in zip(p,q)) for p,q in combinations(tri,2)))
 types[ds]=types.get(ds,0)+1;eq+=len(set(ds))==1
check('GE10-M04',(eq,F(eq,comb(8,3)),types),(8,F(1,7),{(1,1,2):24,(1,2,3):24,(2,2,2):8}))
check('GE10-M05',(2*(2*2+2*3+2*3),2+2+3+F(4,3)),(32,F(25,3)))
check('GE10-M06',((3+F(7,5))+(3-F(7,5)))/2,3)
check('GE10-M07',(2*3*4,comb(3,2),comb(4,2)-1,comb(5,2)-2),(24,3,5,8))
check('GE10-M08',min(((4+8*k)**2+9,k) for k in range(-10,11))[0],25)
check('GE10-M08-two-paths',sum((4+8*k)**2+9==25 for k in range(-10,11)),2)
check('GE10-M09',F(6*8,2)*12/3,96)
u=(1,0,1);v=(0,1,1);crossv=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
check('GE10-M10',sum(c*c for c in crossv),3)
check('GE10-M11',3**2-1**2,8)
check('GE10-M12',F(3**2*(3+3),3),18)
check('GE10-M13',F(3**3,6)-3*F(1,6),4)
check('GE10-M14',4**2*3,48)
check('GE10-M15',1-3*F(1,2)**2+2*F(1,2)**3,F(1,2))
check('GE10-M16',F(2+3-6,2),F(-1,2))
for p,q,r in [(1,2,3),(2,5,7)]:
 vv=[(p,q,r),(p,-q,-r),(-p,q,-r),(-p,-q,r)]
 ds=[sum((x-y)**2 for x,y in zip(vv[a],vv[b])) for a,b in [(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]]
 assert ds[0]==ds[1] and ds[2]==ds[3] and ds[4]==ds[5]
check('GE10-M16-midpoint-box',True,True)

out=ROOT/'output/qa/knowledge-template-example-checks.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(dict(passed=True,checks=checks,note='Independent finite arithmetic and example checks. General theorem hypotheses and bilingual derivations were separately inspected in exact-content review receipts.'),ensure_ascii=False,indent=2),encoding='utf8')
print('Passed',len(checks),'independent example and lemma checks')

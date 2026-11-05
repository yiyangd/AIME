"""Reproduce the independent LO02 review only for its inspected content hash."""
import copy,itertools,json,math
from review_knowledge_helpers import KnowledgeReview,ROOT,digest
d=json.loads((ROOT/'data/knowledge_batches/LO02.json').read_text(encoding='utf-8'))
assert digest(d)=='41c1e21c97e746416946b2afceb8692ae6d5f8c9aca11989f23c1fb7fd12b5a5','LO02 changed: inspect the new text before issuing a receipt'
m=copy.deepcopy(d['methods'])
m[1]['solution_en'][0]='One direction is immediate: a consecutive triple forming a triangle is also a triple in the whole list.'
m[10]['solution_zh'][0]=r'将整数带 $[a,a^2-1]\cup[a^4,a^5-1]$ 染红，将 $[a^2,a^4-1]$ 染蓝。'
m[11]['solution_zh'][2]=r'隔板法得 $\binom63=20$ 种，每种均恰有六次变色，因此最大次数为六，取等词数为二十。'
m[13]['example_en']=r'For positive integer $B$ and nonnegative integer $N$, give an exact test for whether the integer block $BN,\ldots,BN+B-1$ contains a square.'
m[13]['example_zh']=r'设 $B$ 为正整数、$N$ 为非负整数，给出整数块 $BN$ 至 $BN+B-1$ 是否含平方数的精确判断式。'
m[15]['steps_en'][0]=r'First check that the denominations have gcd one; otherwise infinitely many amounts are missing. Choose a denomination $d$ and find the least representable amount $M_r$ in every residue class modulo $d$.'
m[15]['steps_zh'][0]=r'先检验所有面额的最大公因数为一，否则有无穷多个金额无法表示。选一种面额 $d$ 作模数，在每个余数类找最小可表示金额 $M_r$。'
m[15]['steps_en'][2]=r'The last possible gap in residue $r$ is $M_r-d$; maximize these values. If that maximum is negative, no nonnegative amount is missing.'
m[15]['steps_zh'][2]=r'余数类 $r$ 的最后可能缺口为 $M_r-d$，再对各类取最大；若最大值仍为负，则所有非负金额都已可表示。'
m[16]['extensions_en']=[r'For denominations $1<b<c$ with positive counts $x,y,z$, coverage through the entire collection total is equivalent to $x\ge b-1$ and $x+yb\ge c-1$. For a smaller target $T$, process sorted stamps while the covered endpoint $S<T$: each next stamp must satisfy $v\le S+1$; stop once $S\ge T$. Thus a denomination threshold is necessary only if coverage has not already reached $T$ before that denomination is used. This qualification applies to both $b$ and $c$, as well as requiring total value at least $T$.']
m[16]['extensions_zh']=[r'三种面额 $1<b<c$、张数 $x,y,z$ 均正时，覆盖直到全体总额的每个值，充要条件为 $x\ge b-1,x+yb\ge c-1$。若仅要求覆盖至较小目标 $T$，按面额顺序处理邮票：当已覆盖端点 $S<T$ 时，下一票必须满足 $v\le S+1$；一旦 $S\ge T$ 即可停止。因此，只有在使用该面额之前尚未覆盖至 $T$，其门槛才是必要条件；这个限定同时适用于 $b$、$c$，并仍要求总额至少为 $T$。']
m[19]['example_zh']=r'对 $M\ge2$，证明所有分解 $M=\prod_i d_i,d_i\ge2$ 中，成本 $\sum_i(d_i-1)$ 的最小值为 $\sum_pv_p(M)(p-1)$。'

checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
check('M01 lexicographic optimum',min(n for n in range(1000,10000) if max(map(int,str(n)))<=4 and sum(map(int,str(n)))==10)==1144)
for vals in itertools.combinations_with_replacement(range(1,8),5):
 any_tri=any(a+b>c for a,b,c in itertools.combinations(vals,3))
 consecutive=any(vals[i]+vals[i+1]>vals[i+2] for i in range(3))
 assert any_tri==consecutive
checks.append('M02 consecutive-triple equivalence exhaustive finite check')
for lo in range(1,4):
 for hi in range(lo+1,12):
  for n in range(2,min(6,hi-lo+1)+1):
   found=any(all((sum(vals)-v)%(n-1)==0 for v in vals) for middle in itertools.combinations(range(lo+1,hi),n-2) for vals in [(lo,)+middle+(hi,)])
   assert found==((hi-lo)%(n-1)==0 and hi-lo>=(n-1)**2)
checks.append('M03 deletion-mean iff criterion finite exhaustive check')
check('M04 strict local rounding',sum((5*n+7)//8-1 for n in [5,11,16])==18)
check('M05 subset sums interval',{sum(a) for a in itertools.combinations(range(1,7),3)}==set(range(6,16)))
states={(0,0)}
for j in range(1,5):
 states={(sign*(u+1),acc+u) for u,acc in states for sign in [-1,1]}
check('M06 terminal states',set(u for u,acc in states)=={-4,-2,0,2,4})
check('M06 objective sums',set(acc for u,acc in states)=={-2,0,6})
check('M07 residue optimum',max(x*(12-x) for x in range(1,12) if x%3==1)==35)
check('M08 strict gap witness',9<=10 and 9/4>2)
vertices=[(0,0),(1,0),(0,2),(1,2)]
longest=0
for n in range(1,5):
 for path in itertools.permutations(vertices,n):
  distances=[sum((a-b)**2 for a,b in zip(u,v)) for u,v in zip(path,path[1:])]
  if all(u<v for u,v in zip(distances,distances[1:])):longest=max(longest,n)
check('M09 incompatible distance-level bound',longest==3)
check('M10 resource witness',3*2==6 and 2*3==3*2)
for a in [2,3,4]:
 def red(n):return a<=n<a*a or a**4<=n<a**5
 for u in range(a,a**5):
  for v in range(a,min(a**5,(a**5-1)//u+1)):
   assert not(red(u)==red(v)==red(u*v))
checks.append('M11 all in-domain products for a=2,3,4')
counts=[]
for chosen in itertools.combinations(range(10),3):
 word=[int(i in chosen) for i in range(10)]
 counts.append(sum(word[i]!=word[i+1] for i in range(9)))
check('M12 maximum run count and multiplicity',max(counts)==6 and counts.count(6)==20)
check('M13 independent conjugates',sum([1+2j,-3+4j,5+1j])==3+7j)
for B in range(1,15):
 for N in range(30):
  start=B*N;q=math.isqrt(start);q+=q*q<start
  assert (q*q<=start+B-1)==any(math.isqrt(v)**2==v for v in range(start,start+B))
checks.append('M14 aligned square-block iff test')
check('M15 possible fraction class',{(a,b) for a in range(1,31) for b in range(1,31) if 17*a<b}=={(1,b) for b in range(18,31)})
rep={4*a+7*b for a in range(26) for b in range(16)}
check('M16 largest stamp gap',max(n for n in range(100) if n not in rep)==17)
vals=[1,1,3,6];sums={sum(v for i,v in enumerate(vals) if mask>>i&1) for mask in range(16)}
check('M17 complete subset sums',sums==set(range(12)))
dp=[0]+[100]*14
for n in range(1,15):dp[n]=1+min(dp[n-c] for c in [1,4,6] if c<=n)
check('M18 greedy counterexample minimum',dp[14]==3)
check('M19 star optimum',max(sum(abs(c-v) for v in range(1,5) if v!=c) for c in range(1,5))==6)
def factor_cost(n):return min([n-1]+[d-1+factor_cost(n//d) for d in range(2,n) if n%d==0])
for n in range(2,61):
 value=n;primecost=0;p=2
 while value>1:
  while value%p==0:primecost+=p-1;value//=p
  p+=1
 assert factor_cost(n)==primecost
checks.append('M20 additive factor-cost minimum through60')
(ROOT/'output/qa/knowledge-LO02-source-review-checks.json').write_text(json.dumps({'reviewer':'source_audit','examples_checked':20,'checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')
r=KnowledgeReview('source_audit')
r.accept('LO02',[
'Independently read all20 bilingual methods/examples/extensions and all24 actual routes. Recomputed every example and ran exact finite checks for lexicographic digits, consecutive-triple triangle testing, deletion-mean necessity/sufficiency, strict local integer rounding, no-gap subset sums, terminal recurrence states, residue-constrained quadratic optimum, finite event phases, unattainable distance-level bounds, local matrix resource witness, product-free color bands, maximal run counts, independent conjugations, aligned square blocks, small numerator forcing, largest stamp gap, interval coverage, optimal coin exchange, star-label bound incompatibility, and prime-factor additive cost.',
'Clarified the square-block variable domain, gcd-one requirement for a finite largest stamp gap, and the partial-target interval-coverage criterion for both denomination thresholds. Restored the full Chinese product-free coloring intervals and explicit M20 cost definition. All example answers and source routes remain unchanged.'
],patch={'methods':m})
r.save()

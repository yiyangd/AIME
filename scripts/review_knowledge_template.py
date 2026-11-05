"""Independent mathematical and bilingual review overlays; source author files stay intact."""
import copy,json
from pathlib import Path
from review_knowledge_helpers import KnowledgeReview
ROOT=Path(__file__).resolve().parents[1]
review=KnowledgeReview('template_audit')

def accept(code,findings,mutate=None):
 s=json.loads((ROOT/'data/knowledge_batches'/f'{code}.json').read_text(encoding='utf8'))
 methods=copy.deepcopy(s['methods'])
 # Raw-string apostrophe escaping is visible prose, not LaTeX.
 def clean(v):
  if isinstance(v,str):return v.replace("\\'", "'")
  if isinstance(v,list):return [clean(x) for x in v]
  if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
  return v
 methods=clean(methods)
 if mutate:mutate(methods)
 patch={'methods':methods} if methods!=s['methods'] else None
 review.accept(code,findings,patch=patch)
 review.save()

def nt01(m):
 m[2]['steps_zh'][2]='有理数平方根问题先约分，既约分数的分子与分母必须各为平方数。'
 m[0]['extensions_en']=[r'If an exponent itself occurs inside the integer, a finite check needs a growth proof. For $c\ge2$ and $n\ge1$, the ratio of $c^{n+1}/(n+1)$ to $c^n/n$ is $cn/(n+1)\ge1$. Thus once $c^n\ge Kn$ holds, it persists at all later indices. In a product of independent prime powers, bound the other factors below before applying this comparison to each exponent.']
 m[0]['extensions_zh']=[r'若指数本身也出现在整数表达式中，有限检验必须有增长证明。对 $c\ge2,n\ge1$，$c^{n+1}/(n+1)$ 与 $c^n/n$ 的比为 $cn/(n+1)\ge1$，所以 $c^n\ge Kn$ 一旦成立，此后各下标均成立。多个独立质数幂相乘时，先给其余因子建立下界，再逐指数使用此比较。']
accept('NT01',[
 'Recomputed all eight examples: u=81; 9!/((3!)^3 3!)=280 has v3=0; irrationality excludes every positive rational r; unitary divisor count/sum 8 and 540; prime-product minimum539; four distinct multiples with v2>=2 below17; unique pair(16,64); lifting minimumk=9.',
 'Checked prime-exponent allocation, Legendre layers, rational-square parity, valuation uniqueness, gcd min/max equations, odd-prime LTE hypotheses, multiplicative cost splitting, and binary-carry invariant against their mapped routes. Cubing-unit injectivity uses v3(a^3-b^3)=v3(a-b)+1; it is not inferred from a nonsingular derivative.',
 'Corrected a Chinese numerator/denominator typo and supplied the exponential-versus-linear induction bound needed by2002II5; all original example existence and attainment checks remain valid.'
],nt01)

accept('NT02',[
 'Recomputed all seven examples independently: n=8; class size44; seven ordered divisibility pairs; two 15-cycles; exact reduced update g=gcd(I,d+1); 44 subsets with LCM12; maximal factorial index9.',
 'Verified Euclidean remainder equivalences, primitive-lattice cell formula m+n-gcd(m,n), Bezout period reduction, reduced-state gcd invariant, reversible divisibility-chain decomposition and factorial search bounds. Actual routes retain digit, orbit and public-announcement prerequisites.',
 'Removed literal backslashes before apostrophes in English prose.'
])

def nt03(m):
 m[6]['tip_en']='Unique lifting from modulo $p$ to modulo $p^2$ requires a nonzero derivative modulo $p$. If the derivative vanishes, the linear condition gives either no lift or all $p$ lifts in that initial root class.'
 m[6]['tip_zh']='从模 $p$ 到模 $p^2$ 的唯一提升要求导数模 $p$ 非零。若导数为零，线性条件会给出无提升，或该初始根类中的全部 $p$ 个提升。'
 m[7]['steps_en'][0]='Fix a denomination $m$ and find the least representable amount $M_r$ in every residue class modulo $m$. If a class has no representable amount, infinitely many positive amounts are missing.'
 m[7]['steps_zh'][0]='固定面额 $m$，求模 $m$ 每个剩余类中的最小可表示金额 $M_r$；若某类根本不可表示，则有无穷多个正整数金额无法表示。'
accept('NT03',[
 'Recomputed all nine examples:16 linear-congruence representatives; precisely odd n in the triangular-number remainder condition; idempotents0,1,16,25 modulo40; square residues exclude7 modulo8; floor sum214; six zero-sum subsets; unique root lift2 modulo49; Frobenius gap17; losing piles exactly multiples of3.',
 'Verified CRT prime-power allocations, denominator nonunit warning, residue-polynomial coefficient interpretation, Frobenius quotient identity, Fano line incidence, power-splitting sufficiency, and finite residue-representative counts across mapped routes.',
 'Sharpened the singular first-lift statement: derivative zero gives zero or p lifts, rather than an unsupported unique-lift alternative. Added the missing-residue case to the least-representable-amount procedure.'
],nt03)

accept('NT04',[
 'Recomputed all six examples:ord13(3)=3 and 3^100+1=4 mod13; Fibonacci parity value1;6^20=16 mod40;ord25(2)=20; exponent fixed points7,13 modulo20; universal geometric-sum minimum20.',
 'Verified full-state recurrence periodicity, nonunit local prefixes, prime-square order lifting, odd-prime LTE, and cubing bijection from units mod3^k to cube classes mod3^(k+1). Image size2*3^(k-1) and the plus/minus1 mod9 characterization agree.',
 'Checked least-exponent necessity using actual residues and both nonzero geometric denominator and a=1 cases; no patch needed.'
])

accept('NT05',[
 'Recomputed all ten examples, including complete signed/domain restrictions:linear pairs(3,11),(7,4);difference-square pairs(23,22),(9,6),(7,2); five reciprocal pairs; three radical pairs; sole square-sum triple(1,2,3); unique lattice point(1,3); last square-gap failure4; least denominator8 attained by3/8; infinite integer descent zero; five distinct projected values.',
 'Inspected fixed-product reversibility, positivity of reciprocal shifts, parity-compatible factor pairs, rational-square-root integrality, exhaustive search bounds, attaining constructions, power-block endpoint comparison, and union rather than sum of projected intervals. Each method matches its mapped algebraic or geometric integer route.',
 'No mathematical or bilingual correction required.'
])

def nt06(m):
 m[3]['example_en']='For binary integers of a fixed length of at least two bits, characterize when adding one leaves the number of ones unchanged.'
 m[3]['example_zh']='对位数固定且至少有两位的二进制整数，刻画何时加一后数字一的数目保持不变。'
 m[3]['solution_en'][2]='Thus the numeral must end in $01$ and become one ending in $10$. An all-one string of length at least two has change $1-t<0$, so its overflow cannot qualify.'
 m[3]['solution_zh'][2]='故原数须以 $01$ 结尾，更新后以 $10$ 结尾。至少两位的全一串满足 $1-t<0$，所以溢出不能合格。'
 m[3]['extensions_en']=[r'For $a+b=10^k$, first separate the case of zero units digits. Otherwise the units sum to ten and every higher pair of padded digits sums to nine. A zero in one higher position therefore forces nine in the complementary position, which helps make forbidden-zero cases disjoint. Leading padding zeroes are not digits of the original positive numeral.',r'For coefficients $0\le a_i<b^2$, split $a_i=bb_i+c_i$ into legal base-$b$ digits. Then $\sum a_ib^i=bB+C$, with $B=\sum b_ib^i$ and $C=\sum c_ib^i$. Bound both $B,C$ in their $k$-digit ranges before counting; conversely their padded digit expansions uniquely recover every coefficient. This supplies a reversible digit-stream encoding rather than only a carry count.']
 m[3]['extensions_zh']=[r'对 $a+b=10^k$，先分出个位均为零的情形；否则个位之和为十，此后每对补齐位数的高位数字之和为九。某个高位为零便迫使互补位置为九，可据此证明某些禁零情形互斥。首部补齐的零不属于原正整数的数位。',r'若系数满足 $0\le a_i<b^2$，将其拆为合法 $b$ 进制数字 $a_i=bb_i+c_i$，则 $\sum a_ib^i=bB+C$，其中 $B=\sum b_ib^i,C=\sum c_ib^i$。计数前先给 $B,C$ 都施加 $k$ 位范围界；反过来，二者补齐后的数位展开能唯一恢复每个系数。这提供可逆的数位流编码，而非仅仅统计进位。']
accept('NT06',[
 'Recomputed all ten examples:invalid base-digit pair;prefix residue6 and changed suffix residue3;30 three-digit palindromes of mean560.1; popcount change1-t; fifth weight-two six-bit word001010;minimum344_5=99;eight four-bit no-adjacency strings;balanced ternary8=9-1;nine distinct-digit sum9 numerals;total digit sum13500.',
 'Verified digit validity in every base, suffix versus numeral leading zeros, carry accounting, bounded prefix unranking, greedy digit-mass minimization, transition-state recurrence, factorial telescoping legal blocks and binary-carry uniqueness against mapped routes.',
 'Fixed the one-bit exception in the popcount example by stating length at least two; binary1+1=10 otherwise has unchanged weight despite overflow. Added complement-digit disjoint cases and bounded digit-stream encoding for2006II7 and2010I10.'
],nt06)

def nt07(m):
 m[2]['steps_en'][0]=r'For fractions $k/N$ with $1\le k\le N$, every reduced denominator is a divisor $D$ of $N$.'
 m[2]['steps_zh'][0]=r'对 $1\le k\le N$ 的分数 $k/N$，每个最简分母都是 $N$ 的约数 $D$。'
accept('NT07',[
 'Recomputed all five examples:repeating-block sum4/11;denominators b=6t with3 not dividing t;distinct reduced numerators{1,2,3,5,7,11};denominator<=10 interval impossibility;valuation denominator2^5.',
 'Checked gcd cancellation independent of the reduced numerator, bounded reduced-numerator realization by divisor denominators, decimal shifts preserving denominator divisibility, and unique minimum valuation preventing cancellation.',
 'Made the k/N interval1<=k<=N explicit in the general numerator procedure; without it the asserted m<=D bound is false.'
],nt07)

def nt08(m):
 for lang in ('en','zh'):
  old=m[1]['extensions_'+lang][0]
  m[1]['extensions_'+lang][0]=old.replace('$p^3$ or $pq$', '$p^3$ or $pq$ with distinct primes $p,q$').replace('$p^3$ 或 $pq$', '$p^3$ 或不同质数 $p,q$ 的乘积 $pq$')
accept('NT08',[
 'Recomputed all seven examples:six square divisors summing210;least eight-divisor integer24;fourth-power divisor counts exactly1 mod4;conditional unit probability8/15;ten odd cumulative-divisor counts through20;divisor union10;Lambert coefficient4 and bound100/9801.',
 'Verified multiplicative exponent-count inversion including single-prime patterns, exchange proof assigning larger exponents to smaller primes, kth-power count sufficiency, fixed-point-free totient pairing restrictions, square-block parity, divisor-set intersections and nonnegative series regrouping with carry-aware tail bounds.',
 'Made the distinct-prime requirement explicit in the tau=4 pattern pq; all mapped routes remain covered.'
],nt08)

accept('AL01',[
 'Read the latest author revision and recomputed all ten examples:mixture7.5/4.5;work time10;water speed2sqrt5;shared-total square sum46;symmetric fourth-power sum343;triple family(0,0,0) and permutations(1,1,-2);radical root9/4;integer radical coefficients(2,3) giving36;log-domain k>0;centered roots0,+/-sqrt3.',
 'Checked conservation units, stage endpoints, vector relative velocity, shared boundary lengths, symmetric-real reconstruction, every factored branch, unsquared sign restoration, rational radical independence and discarded zero/pole branches. Confirmed the latest positive-integer domain in M08 and removal of GE02 prerequisite from2000I4.',
 'No further correction needed.'
])

accept('AL02',[
 'Recomputed all nine original examples:power sum23;root-remainder results7 and1;unique square-root polynomial1+x+x^2;disjoint quadratic root sets with equal sums;interpolation value100;three integer-root quadratics;all Q=x^2+c(x-2)^2,c>=0;unit-root moduli;absolute coefficient sum16.',
 'Verified repeated-root copy counts, Heron-type radical identity4e2-e1^2, signed root-product interchange, polynomial root-count rigidity, monic rational-factor integrality, double-root minima, compact positive-root perturbation criterion, finite root orbits and coefficient-sign proof before evaluation.',
 'Removed literal apostrophe escapes in Gauss lemma prose; no mathematical correction needed.'
])

def al03(m):
 m[1]['steps_en'][2]='Use Vieta to connect that factor with the remaining roots. For an integer polynomial, trace and norm of this pair are integral only when the pair is known to form a monic rational quadratic factor; Gauss\'s lemma then applies.'
 m[1]['steps_zh'][2]='用韦达将该因子与其余根联系。整系数多项式中，只有已知该根对构成首一有理二次因子时，才能由高斯引理要求其迹与范数为整数。'
 m[1]['extensions_en']=[r'Integer coefficients alone do not force each conjugate pair to have integral trace or norm: in $x^3-2$, the nonreal pair has irrational sum $-\sqrt[3]2$. Apply coefficient integrality only after establishing a rational factor, or use the full polynomial coefficient equations.']
 m[1]['extensions_zh']=[r'整系数并不自动使每个共轭根对的迹与范数为整数。例如 $x^3-2$ 的非实根对之和为无理数 $-\sqrt[3]2$。须先确定因子系数为有理数，才能使用因子整系数性；否则应使用整个多项式的系数方程。']
 m[3]['steps_en'][1]=r'For finite motion with $q\ne1$, use $\sum_{j=0}^{n-1}q^j=(1-q^n)/(1-q)$; if $q=1$, the sum is $n$. For a limit verify $|q|<1$ first.'
 m[3]['steps_zh'][1]=r'有限运动中，$q\ne1$ 时用 $\sum_{j=0}^{n-1}q^j=(1-q^n)/(1-q)$；$q=1$ 时和为 $n$。极限问题先验证 $|q|<1$。'
accept('AL03',[
 'Recomputed all nine examples:z=2-i;cubic constant15;four unit complex solutions;rotation center(1+i)/2 and exact nonfixed period4;fifth-root product5;unit circle minus -1 including1;open inversion disk;real-part maximum5 attained at(3-4i)/5;three-cycle2,-1,1/2.',
 'Inspected Gaussian-integer norms and triangle bounds, conjugate multiplicities, polar angle congruences, affine centers, nested-disk uniqueness, signed unit-root products, cross-ratio exclusions, inverse half-plane strictness, norm equality direction, and pole-safe fractional-map iterations.',
 'Corrected an overgeneralization: conjugate-pair trace/norm of an integer polynomial need not be integers. Added the x^3-2 counterexample and restricted Gauss lemma to an established monic rational quadratic factor. Also restored the q=1 branch of the finite geometric sum.'
],al03)

def al04(m):
 m[2]['steps_en'][0]=r'If the exponents share a nonconstant linear expression, put $t=b^{cx}$ with $b>0,b\ne1,c\ne0$. For unrestricted real $x$ its exact range is $t>0$; intersect this with any original restrictions on $x$.'
 m[2]['steps_zh'][0]=r'若指数共享非恒定线性表达式，可令 $t=b^{cx}$，其中 $b>0,b\ne1,c\ne0$。当 $x$ 遍历实数时其准确值域为 $t>0$；若原 $x$ 有限制，还须取相应交集。'
accept('AL04',[
 'Recomputed all seven examples:log product4;positive variables(8,4);exponential quadratic has0/1/2 real solutions for a<2/a=2/a>2;unique nested-log base2;floor-event length probability1/3;telescoping log product3;inverse-sine log domain[1/2,2].',
 'Verified change-of-base domains, shared logarithmic coordinates, positive substitution range, variable-base monotonicity, exact half-open power thresholds, product cancellation endpoints and inequality reversal for bases below1 against all mapped routes.',
 'Made the nonconstant exponential-substitution hypotheses and original range intersection explicit; no example correction required.'
],al04)

def al05(m):
 m[4]['extensions_en'] += [r'A higher-order recurrence need not be solved by a quadratic characteristic equation. Combine adjacent recurrences first: if $u_n=\sum_{j=1}^{2r}(-1)^{j+1}u_{n-j}$, substituting the previous recurrence cancels all middle terms and gives $u_n=-u_{n-2r-1}$ once both formulas apply. Thus a period dividing $4r+2$ follows, with the initial transition checked separately.',r'For tribonacci terms $u_{n+3}=u_{n+2}+u_{n+1}+u_n$, let $T_n=u_{n+2}+u_n$. Direct subtraction gives $T_n-T_{n-1}=2u_n$. Hence $2\sum_{j=1}^N u_j=u_{N+2}+u_N-u_2-u_0$, where $u_0$ can be recovered from the first recurrence if necessary. This is a partial-sum identity, not a second-order closed-form claim.']
 m[4]['extensions_zh'] += [r'高阶递推未必需要解二次特征方程。先合并相邻递推：若 $u_n=\sum_{j=1}^{2r}(-1)^{j+1}u_{n-j}$，代入前一递推后，中间项全部消去，在两式都适用时得 $u_n=-u_{n-2r-1}$。所以周期整除 $4r+2$，另须检查初始过渡。',r'对 tribonacci 递推 $u_{n+3}=u_{n+2}+u_{n+1}+u_n$，令 $T_n=u_{n+2}+u_n$，直接相减得 $T_n-T_{n-1}=2u_n$。故 $2\sum_{j=1}^N u_j=u_{N+2}+u_N-u_2-u_0$；必要时可由首个递推恢复 $u_0$。这是部分和恒等式，并不声称数列满足二阶通项公式。']
accept('AL05',[
 'Recomputed all eleven examples:arithmetic-pair total40;annulus fraction16/21;telescoping sum1/4-1/[2(N+1)(N+2)];weighted geometric sum3/4;affine recurrence3^n-1;second difference2n^2+n+2;adjacent product22;invariant terms>=3;alternating square/product triples;least rational period4;preimage sum8.',
 'Checked all eleven route families and full extensions:nonconsecutive AP placements;adjacent-sum triangular formula;dimension-scaled geometric increments and three-stage tetrahedron nonoverlap limit;Pascal/trigonometric telescoping;absolute-value square difference;positive-series regrouping;tridiagonal determinant recurrence;sharp nontriangle Fibonacci envelope;nonlinear transformed recurrence positivity;alternating progression induction;Lyness five-step ordered-state return;invalid preimage filtering.',
 'Removed literal apostrophe escapes. Added explicit higher-order cancellation/anti-period and tribonacci partial-sum lemmas for2001II3 and2006II11, whose actual routes need more than a second-order characteristic formula. Endpoints, denominator and repeated characteristic-root exceptions remain explicit.'
],al05)

accept('PS01',[
 'Recomputed all seven examples by labeled outcome counts:18/35 hypergeometric;2/3 edge pair;27/64 intersection-size event;1/3 distinct same-parity dice;1/2 diagonal reflection;1/4 stopped-path event;1/3 exactly-one-fixed-point permutation.',
 'Inspected uniform sample definitions, ordered/unordered consistency, semicircle unique anchors, residue/parity multiplicity weights, inclusion-exclusion intersections, fixed-symmetry orbit sizes, unequal stopped-path lengths and matching versus permutation models against their full route lists.',
 'Read latest color-word tip revision; removed the remaining literal apostrophe escape in stopped-path prose. No mathematical correction needed.'
])

accept('PS02',[
 'Recomputed all six examples:conditional same-parity probability1/2;hidden-coin posterior(1/3,2/3) with future head5/6 and joint3/4;total success3/8 and posterior1/3;PGF coefficient1/2;without-replacement joint1/6;HH stopping-time odd probability2/5 with almost-sure absorption.',
 'Verified conditioning renormalization, uniqueness before matching-plus-extra-edge enumeration, sticker forbidden equalities, lineup ordered block compositions, Bayes mixture dependence, first-stage partition weights, independent convolution and transformed-walk assumptions, exchangeable full deals and signed minimal-memory first-step equations.',
 'All original examples and full extensions are mathematically valid in the stated domains; no patch needed.'
])

accept('PS03',[
 'Recomputed all five examples in original sampling coordinates:angle probability2/3;clipped polygon area9/8 and probability3/16;parameter-square complement7/16;crossing probability4/9;unequal-region probability3/8.',
 'Verified nonuniform transformed sine warning, floor interval endpoints, center feasibility erosion, distance half-plane reduction, slope sign cases, independent parameter square, cyclic endpoint alternation and conditioned arc ordering. Independently counted the four-arc extension:2 forced crossings,4 forced noncrossings,30 half-probability cases among36, giving17/36.',
 'Checked geometric piece weights and conditional coordinate independence against every mapped route. No correction required.'
])

def ge10(m):
 m[0].update(
  example_en='Two similar closed boxes have corresponding edge lengths in ratio $2:3$. Their total surface area is $130$. Find each surface area and the ratio of their volumes.',
  example_zh='两个相似的封闭长方体，对应棱长比为 $2:3$，表面积之和为 $130$。求各自表面积及体积比。',
  solution_en=[r'Area scales as the square of the linear ratio, so write the two surface areas as $4c$ and $9c$.',r'The total gives $13c=130$, hence the areas are $40$ and $90$.',r'Volume scales as the cube, so the volume ratio is $8:27$. Similar boxes realizing these areas exist by uniformly scaling any fixed box.'],
  solution_zh=[r'面积按线性比的平方缩放，故把两表面积写成 $4c,9c$。',r'总和给出 $13c=130$，所以表面积分别为 $40,90$。',r'体积按线性比的立方缩放，故体积比为 $8:27$。将任一固定长方体整体缩放，即可实现这些表面积。'])
 m[1].update(
  example_en='Attach one outward square pyramid of height $1/2$ to each face of a unit cube, using that entire face as its base. Find the new volume and justify adding the six pyramid volumes.',
  example_zh='在单位立方体每个面外侧，各接一个以整面为底、高为 $1/2$ 的正四棱锥。求新体积，并说明为何可将六个棱锥的体积相加。',
  solution_en=[r'Each pyramid has base area one and volume $1\cdot(1/2)/3=1/6$.',r'The pyramid on $x=1$ lies in $x\ge1$, with its other coordinates in $[0,1]$; the corresponding statement holds at every face. Distinct outward pyramids therefore have disjoint interiors and meet the cube only on its boundary.',r'The total is $1+6(1/6)=2$. The geometric separation, rather than the number of faces alone, justifies the sum.'],
  solution_zh=[r'每个棱锥底面积为一，体积为 $1\cdot(1/2)/3=1/6$。',r'$x=1$ 面上的棱锥满足 $x\ge1$，另两坐标均在 $[0,1]$ 内；其余面同理。不同外接棱锥的内部互不相交，且只在边界接触原立方体。',r'总体积为 $1+6(1/6)=2$。能相加的依据是几何隔离，而非仅仅知道面数。'])
 m[3].update(
  example_en='How many equilateral triangles have all three vertices among the vertices of a cube? What fraction of the cube-vertex triples do they form?',
  example_zh='立方体顶点中有多少组三点能构成等边三角形？它们占全部顶点三元组的比例是多少？',
  solution_en=[r'Normalize vertices to $\{0,1\}^3$. A pairwise equal-distance triple cannot use cube edges or space diagonals, so all its squared side lengths must be two.',r'Partition the eight vertices by the parity of their coordinate sum. Each class contains four vertices; any two distinct members differ in exactly two coordinates.',r'Each parity class therefore forms a regular tetrahedron, contributing $\binom43=4$ equilateral triangles. There are eight altogether.',r'There are $\binom83=56$ vertex triples, so their fraction is $8/56=1/7$.'],
  solution_zh=[r'将顶点归一为 $\{0,1\}^3$。两两等距三点不能以棱或体对角线相连，所以各边平方只能为二。',r'按坐标和的奇偶把八顶点分为两类，每类四点；同类不同点恰有两个坐标不同。',r'所以每类形成正四面体，贡献 $\binom43=4$ 个等边三角形，共八个。',r'全部顶点三元组有 $\binom83=56$ 个，所占比例为 $8/56=1/7$。'])
 m[4].update(
  example_en='A solid box has side lengths $a,b,c>0$. A coating consists of all exterior points at distance at most $r>0$ from the box. Derive the coating volume as a polynomial in $r$.',
  example_zh='实心长方体三边为 $a,b,c>0$。涂层由长方体外部距其不超过 $r>0$ 的点组成。把涂层体积写成关于 $r$ 的多项式。',
  solution_en=[r'The six face slabs have total volume $2(ab+ac+bc)r$; the original box is excluded from the coating.',r'The four edges parallel to a side of length $a$ contribute four quarter-cylinders, totaling $\pi ar^2$. The three directions together give $\pi(a+b+c)r^2$.',r'The eight corner octants combine into one sphere of volume $4\pi r^3/3$.',r'The coating volume is $2(ab+ac+bc)r+\pi(a+b+c)r^2+4\pi r^3/3$. Assigning each exterior point to its nearest box face, edge or vertex proves coverage and disjoint interiors.'],
  solution_zh=[r'六个面上的薄层总体积为 $2(ab+ac+bc)r$；原长方体不属于涂层。',r'平行于长度 $a$ 的四条棱各贡献四分之一圆柱，共为 $\pi ar^2$；三个方向合计 $\pi(a+b+c)r^2$。',r'八个角部八分之一球合成一个球，体积为 $4\pi r^3/3$。',r'涂层体积为 $2(ab+ac+bc)r+\pi(a+b+c)r^2+4\pi r^3/3$。按外部点的最近面、棱或顶点分类，可证明完整覆盖及内部互不相交。'],
  tip_en='Adding twice the radius to every box dimension replaces curved edge and corner pieces by rectangular ones and gives the wrong volume.')
 m[7].update(
  example_en='A cylinder has circumference $8$ and height $3$. Find the shortest path on its lateral surface from a point on its bottom rim to the diametrically opposite point on its top rim. How many shortest paths are there?',
  example_zh='圆柱周长为 $8$、高为 $3$。从下底圆周一点沿侧面到上底圆周上与其对径的位置，求最短距离及最短路径条数。',
  solution_en=[r'Unroll the lateral surface into its periodic strip. Put the start at $(0,0)$; the endpoint lifts are $(4+8k,3)$ for integers $k$.',r'A straight lifted path has squared length $(4+8k)^2+9$. The least absolute horizontal displacement is four, attained exactly at $k=0,-1$.',r'The minimum distance is therefore $5$. Both straight segments stay between the two rim lines, giving two shortest paths, one around each side of the cylinder.'],
  solution_zh=[r'把侧面展开为周期条带。起点取 $(0,0)$，终点各提升为 $(4+8k,3)$，其中 $k$ 为整数。',r'直线提升的长度平方为 $(4+8k)^2+9$。最小水平位移绝对值为四，且仅在 $k=0,-1$ 达到。',r'所以最短距离为 $5$；两条直线均在上下底边之间，投回圆柱后得到分别绕两侧的两条最短路径。'])
 m[8].update(
  example_en='A tetrahedron has a right-triangle base with legs $6,8$. Each edge from its apex to a base vertex has length $13$. Find its volume.',
  example_zh='四面体底面为两直角边长 $6,8$ 的直角三角形，顶点到三个底面顶点的距离均为 $13$。求体积。',
  solution_en=[r'The base hypotenuse is ten, so its circumcenter is the hypotenuse midpoint and its circumradius is five. Its area is $6\cdot8/2=24$.',r'Equal apex distances put its perpendicular projection at that circumcenter. The vertical height is $\sqrt{13^2-5^2}=12$.',r'Thus the volume is $24\cdot12/3=96$. Placing the apex twelve units above the circumcenter realizes all three required lateral lengths.'],
  solution_zh=[r'底面斜边为十，外心为斜边中点，外接圆半径为五，面积为 $6\cdot8/2=24$。',r'顶点到三底面点等距，故其垂足在外心；垂直高为 $\sqrt{13^2-5^2}=12$。',r'体积为 $24\cdot12/3=96$。将顶点放在外心正上方十二处，确能实现三条长为十三的侧棱。'])
 m[12]['extensions_en'][0]=m[12]['extensions_en'][0].replace('that the submerged depth is below the container bottom','that the submerged depth is less than the container depth')
 m[15].update(
  example_en='Could a tetrahedron have its three opposite-edge pairs of lengths $\sqrt2,\sqrt3,\sqrt6$? Each proposed face is a valid triangle; determine whether the spatial solid exists.',
  example_zh='四面体三组对棱长度能否分别为 $\sqrt2,\sqrt3,\sqrt6$？虽然每个拟定面都满足三角不等式，请判断空间立体是否存在。',
  solution_en=[r'The strongest face inequality is $\sqrt2+\sqrt3>\sqrt6$, so planar face validity alone gives no obstruction.',r'For an opposite-edge-equal tetrahedron, box dimensions would satisfy $a^2+b^2=2,a^2+c^2=3,b^2+c^2=6$.',r'The first two equations minus the third give $2a^2=-1$, impossible for a real box dimension. Thus the tetrahedron does not exist, despite the valid individual faces.'],
  solution_zh=[r'最强的面三角不等式为 $\sqrt2+\sqrt3>\sqrt6$，所以单独检查各面无法排除。',r'若对棱相等四面体存在，长方体边长应满足 $a^2+b^2=2,a^2+c^2=3,b^2+c^2=6$。',r'前两式相加再减第三式得 $2a^2=-1$，不可能对应实数边长。因此各面虽合法，空间四面体仍不存在。'])
 m[15]['extensions_en'] += [r'The box representation is a theorem, not an extra assumption. Put the tetrahedron centroid at zero and let $u,v,w$ be the midpoints of the three edges from one vertex. The four vertex vectors are $u+v+w,u-v-w,-u+v-w,-u-v+w$. Equality of each opposite-edge pair gives $|v+w|=|v-w|$ and its cyclic counterparts, so $u,v,w$ are pairwise perpendicular. Their doubled lengths are the box dimensions; nondegeneracy requires all three to be positive.']
 m[15]['extensions_zh'] += [r'长方体表示是定理而非额外假设。把四面体重心放在原点，令 $u,v,w$ 为同一顶点引出的三条棱的中点向量，则四顶点向量为 $u+v+w,u-v-w,-u+v-w,-u-v+w$。每组对棱相等给出 $|v+w|=|v-w|$ 及循环同式，所以 $u,v,w$ 两两垂直。其长度的两倍即长方体三边，非退化要求三者均正。']
accept('GE10',[
 'Read all16 methods, bilingual examples, full extensions and all33 actual canonical question routes. Recomputed similarity complements and face-centroid scale; additive attachment volumes; squared-distance cancellation;cube triangle types;nearest-feature offset volume;affine-height averaging;inward-face counts;curved-surface lifts;perpendicular pyramid heights;section area factors;rigid-fold height;double-cone volumes;clipped simplex inclusions;dihedral section;Gram determinant;disphenoid box and Heron identities.',
 'Replaced direct source-scaled worked examples with original teaching problems:similar closed-box areas/volumes;cube-face pyramid attachments with separation proof;cube equilateral-triple fraction;symbolic external coating polynomial;two cylinder geodesics;right-triangle-base tetrahedron;valid planar faces but impossible disphenoid. Independently checked values40/90 and8:27,2,8/56,coating polynomial,5 and two paths,96,and a negative squared box dimension.',
 'Added a proof that equal opposite edges force the orthogonal midpoint-vector box representation, making the feasibility test necessary as well as sufficient. Fixed the English container-depth condition and the twice-radius offset wording. All other examples are valid:PA5,affine volume12pi,hidden count24,section sqrt3,fold2sqrt2,rotation18pi,clipped volume4,dihedral4sqrt3,Gram volume1/sqrt2.'
],ge10)

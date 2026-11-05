"""Progressive, explicitly completed textbook reviews by the print reviewer."""
from review_knowledge_helpers import KnowledgeReview
import json
from pathlib import Path

r = KnowledgeReview('print_builder')
r.accept('CO01', [
    'Read all eight bilingual method procedures, examples, solutions, tips and extensions; recomputed the original example counts 480,20,20,72,1120,24,12,16.',
    'Checked the mapped question routes, including the rank-pattern, card-grid unique-removal, constrained insertion/deletion, and median-of-medians arguments; the procedures and special-lemma extensions cover their actual counting structure.',
    'Checked the ordered/unordered distinctions, repeated-object divisors, circular stabilizers, and reversible-construction multiplicities. English and Chinese conditions and worked steps agree.'
])
r.accept('CO02', [
    'Read all seven bilingual methods and recomputed every original example: 90,640,452,(56 and 21),1 modulo 5,rank 15,and the star-or-triangle argument.',
    'Checked all mapped routes, including equal-cardinality intersection sums, binary prefixes, function fibers, iterated fractional-part inverse intervals, prime-binomial reduction, and pairwise-intersecting edge families.',
    'Verified strict endpoint handling, symmetry factors and binomial-convolution explanations; the bilingual procedures, examples and extensions give equivalent mathematical conditions.'
])
co03 = json.loads((Path(__file__).resolve().parents[1]/'data/knowledge_batches/CO03.json').read_text(encoding='utf8'))
co03['methods'][1]['extensions_en'][0] = co03['methods'][1]['extensions_en'][0].replace('For $L\\le ax+by\\le U$', 'For $b>0$ and $L\\le ax+by\\le U$')
co03['methods'][1]['extensions_zh'][0] = co03['methods'][1]['extensions_zh'][0].replace('对固定 $x$，若 $L', '对固定 $x$，若 $b>0$ 且 $L')
r.accept('CO03', [
    'Read all six bilingual procedures, examples, worked solutions and extensions. Recomputed the counts 30,6,30,(60 and 15),expected range 5,and all six interval distances in the increment example.',
    'Checked all mapped routes, including divisor-exponent distributions, bounded generating-function coefficients, run compositions, order-statistic gap exchangeability, and the sufficiency of the unique negative increment rule.',
    'Made the positive-divisor hypothesis b>0 explicit in the clipped integer interval lemma in both languages; its displayed ceil/floor bounds require that sign. All other mathematical and bilingual checks pass.'
], patch={'methods':co03['methods']})
r.accept('CO04', [
    'Read all six bilingual methods and their special extensions; recomputed 19 exactly-one multiples,14 directed-block permutations,subset-square total 240,nonuniform witness total 30 versus 19 objects,the three-column capacity construction,and the sharp three zero-overlap rotations.',
    'Checked all mapped inclusion-exclusion and incidence routes, including overlapping 2x2 board blocks, circular long runs, arithmetic-progression witnesses, tournament source/sink structure, primitive grid-line representatives, and equilateral-apex correction.',
    'The cyclic overlap identity counts ordered differences correctly, and complement exchange requires even rotation cycles. Capacity examples include an attaining configuration. English and Chinese formulas and boundary conditions agree.'
])
co05 = json.loads((Path(__file__).resolve().parents[1]/'data/knowledge_batches/CO05.json').read_text(encoding='utf8'))
co05['methods'][7]['extensions_zh'][0] = co05['methods'][7]['extensions_zh'][0].replace('十乘十五环题', '$10\\times10$ 棋盘的五环题')
r.accept('CO05', [
    'Read all eight bilingual methods and extensions; independently verified the suffix-state vectors and count 21,the mixed-step path count 16,binary-path shape count 16,indecomposable convolution 177,first-hit set {5,6,8},divisor-chain count 8,coin expectation 6,and three domino tilings.',
    'Checked the mapped route recurrences and state sufficiency, including Hamilton closure, nonbacktracking edge memory, cycle-color identification, absorbing frog states, prefix success constraints, unique-negative increments, and divisor-chain normalization.',
    'The 2026 I Q15 exact-cover recurrence and candidate/certificate implementation were separately inspected and rerun during problem review; the stated 2025 candidates and 83 covers agree. Clarified the Chinese phrase as a 10 by 10 board with five loops to avoid merging the numbers.'
], patch={'methods':co05['methods']})
co06 = json.loads((Path(__file__).resolve().parents[1]/'data/knowledge_batches/CO06.json').read_text(encoding='utf8'))
co06['methods'][2]['steps_en'][2] = 'In a disk partitioned by full chords, a new chord with no overlapping old edge and $r$ distinct interior crossings adds $r+1$ regions. Coincident crossings count as one point; free-ended segments need a separate Euler calculation.'
co06['methods'][2]['steps_zh'][2] = '圆盘已由完整弦分割时，新增弦若不与旧边重合，且有 $r$ 个不同内部交点，就新增 $r+1$ 个区域。重合交点只计一个点；端点自由的线段须另用欧拉公式计算。'
co06['methods'][5]['steps_en'][0] = 'Identify a quantity that changes monotonically along the path, such as height.'
co06['methods'][5]['steps_zh'][0] = '找出沿路径单调变化的量，例如高度。'
r.accept('CO06', [
    'Read all fourteen bilingual methods, original examples, worked solutions, tips and extensions. Recomputed the explicit example results: bipartite obstruction,8 triangles,6 disk regions,8 crossed cells,4 matchings,15 layered paths,(10,20,10) equilibrium,6 tournament extensions,circular separation impossibility,offset 4/5,nine torus states,Fano sums 1 and -1,10 shared-edge colorings,and maximum path variation 7.',
    'Checked the mapped graph and incidence routes, the Hamiltonian diagonal-rule/gcd proof, finite Fano/K4 incidence lemmas, strict circular separation, chord segment containment, graph-equilibrium maximum principle, and attainment of the weighted-degree bound.',
    'Added the necessary boundary-endpoint/transverse-intersection hypothesis to the r+1 planar-region increment in both languages; a free-ended segment would not satisfy that increment. Rephrased layer monotonicity to cover either height direction. The remaining bilingual statements and special-lemma extensions pass.'
], patch={'methods':co06['methods']})
r.accept('CO07', [
    'Read all eight bilingual procedures, original examples, full worked steps, tips and extensions. Recomputed no shuffle fixed points,56 unequal-gap schedules,136 unordered subset-pair designs,4 half-turn colorings,8 lamp histories,5 digit-stream solutions,6 maximal-board tokens,and 15 independent-chain target sets.',
    'Checked every mapped route and inverse construction, including the unique orientation of three-color strips, two-ring displacement cancellation, maximal row/column support reconstruction, and singleton/two-block collision-chain decomposition.',
    'Verified that the prime-factor cost minimization follows from splitting a composite factor and that separated chains attain the cost. Fixed points, nonfree symmetry actions, endpoint bounds, and target-set independence are treated explicitly and consistently in both languages.'
])
al06 = json.loads((Path(__file__).resolve().parents[1]/'data/knowledge_batches/AL06.json').read_text(encoding='utf8'))
al06['methods'][0]['extensions_en'][0] = al06['methods'][0]['extensions_en'][0].replace('For positive $k$', 'For $A>0,n>0$ and positive $k$')
al06['methods'][0]['extensions_zh'][0] = al06['methods'][0]['extensions_zh'][0].replace('正 $k$ 时', '在 $A>0,n>0,k>0$ 时')
al06['methods'][0]['extensions_en'][1] = al06['methods'][0]['extensions_en'][1].replace('For $f(x)=x\\{x\\}$ on', 'For an integer $j\\ge0$, $f(x)=x\\{x\\}$ on')
al06['methods'][0]['extensions_zh'][1] = al06['methods'][0]['extensions_zh'][1].replace('在 $[j,j+1)$ 上', '对整数 $j\\ge0$，在 $[j,j+1)$ 上')
al06['methods'][1]['extensions_en'][0] = r'For positive integers $n,k$, the nearest integer to $\sqrt n$ is $k$ precisely when $(k-1/2)^2<n<(k+1/2)^2$. This becomes $k^2-k+1\le n\le k^2+k$, with $2k$ inputs. No square-root tie occurs because the squared half-integer endpoints are not integers. The case $n=0$ gives rounded value zero separately.'
al06['methods'][1]['extensions_zh'][0] = r'对正整数 $n,k$，$\sqrt n$ 最近整数为 $k$ 恰要求 $(k-1/2)^2<n<(k+1/2)^2$，即 $k^2-k+1\le n\le k^2+k$，共有 $2k$ 个输入。半整数端点的平方非整数，因此无取舍平局；$n=0$ 时另有取整值零。'
al06['methods'][3]['extensions_en'][0] = al06['methods'][3]['extensions_en'][0].replace('If changing a parameter by one changes the smooth sum by more than', 'If each unit increase of an integer parameter changes the smooth sum in the same direction by more than')
al06['methods'][3]['extensions_zh'][0] = al06['methods'][3]['extensions_zh'][0].replace('若参数改变一使未取整和的变化超过', '若整数参数每增加一都使未取整和向同一方向变化，且变化量超过')
al06['methods'][7]['extensions_en'][0] = al06['methods'][7]['extensions_en'][0].replace('suppose all values through $S$ are obtainable', 'suppose the already processed stamps have total value $S$ and their subcollections attain every value from zero through $S$')
al06['methods'][7]['extensions_zh'][0] = al06['methods'][7]['extensions_zh'][0].replace('若已有组合能覆盖零至 $S$', '若已处理邮票的总面值为 $S$，且其子组合能覆盖零至 $S$')
al06['methods'][8]['extensions_en'][1] = r'For the coupled trigonometric-fold example, define $h(u)=4\bigl||u-1/2|-1/4\bigr|$ on $[0,1]$ and solve $y=F(x)=h(|\sin2\pi x|)$, $x=G(y)=h(|\cos3\pi y|)$. The knot values of $h$ at $0,1/4,1/2,3/4,1$ are $1,0,1,0,1$, giving sixteen full-height branches of $F$ and twenty-four full-width branches of $G$; their only boundary solution is $(1,1)$. The derivative magnitude is $D=96\pi^2|\cos2\pi x\sin3\pi y|$. If $|\cos2\pi x|\le1/20$, the equations imply $y\ge.99$ and $x\ge1-18\pi^2(.01)^2>.982$, contradicting that cosine bound. If $D\le1$, one factor is at most $1/20$, so the sine factor must be small. The equations then force $a=1-x\le.01$, $b=1-y<.01$ and exactly $b=4\sin2\pi a$, $a=4(1-\cos3\pi b)$.'
al06['methods'][8]['extensions_zh'][1] = r'联立三角折叠例中，先定义 $h(u)=4\bigl||u-1/2|-1/4\bigr|$（$0\le u\le1$），求解 $y=F(x)=h(|\sin2\pi x|)$、$x=G(y)=h(|\cos3\pi y|)$。$h$ 在 $0,1/4,1/2,3/4,1$ 的节点值为 $1,0,1,0,1$，故 $F$ 有十六个满高度分支、$G$ 有二十四个满宽度分支，唯一边界解为 $(1,1)$。导数绝对乘积为 $D=96\pi^2|\cos2\pi x\sin3\pi y|$。若余弦因子至多二十分之一，方程迫使 $y\ge.99$ 与 $x\ge1-18\pi^2(.01)^2>.982$，与该余弦界矛盾。若 $D\le1$，至少一因子不超过二十分之一，所以只能正弦因子小。方程进而迫使 $a=1-x\le.01,b=1-y<.01$，并精确满足 $b=4\sin2\pi a,a=4(1-\cos3\pi b)$。'
r.accept('AL06', [
    'Read all nine bilingual methods, examples, solutions and extensions. Recomputed the negative floor solutions {-5,-4},seven rounding successes,logarithmic-band probability 3/13,floor sum 43,absolute-value roots and flat interval,area 2 and enclosing radius sqrt(2),three wave intersections,five finite-window events,and cubic-fold boundary/interior roots.',
    'Checked all mapped routes, including reciprocal floor intervals, square-root threshold blocks, exact residue sums, nested absolute-value preimages, ordered positive/negative mass bounds, closure-forced disks, tent-piece filtering, finite traffic windows,and stamp no-gap minimality.',
    'Made necessary positivity and domain conditions explicit in reciprocal-floor and fractional-part branches; separated n=0 from positive square-root rounding. Specified monotone smooth-sum changes and that S is the total value of processed stamps in the no-gap lemma.',
    'Independently checked the 2024 I Q12 derivative-product and strict-convexity certificate. Added definitions of h,F,G and their knot/branch data so the extension is self-contained before using its equations. Bilingual conditions and proofs agree.'
], patch={'methods':al06['methods']})
r.save()

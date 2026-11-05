"""Independent geometry textbook receipts for the exact author versions inspected."""
import copy,json
import sympy as s
from review_knowledge_helpers import KnowledgeReview,ROOT,digest

expected={
 'GE01':'81c637698481947bcd93426a0c2ac03bfd67d426c79aea568bbb3ce6b593e7c8',
 'GE02':'236a377512592dc0def2475793a0a0a42f02ab0b8d377a3b4ca0be2f939506c9',
 'GE03':'95c2f3d3e74cb2bdf99e438b0cd74662c842b54820c06f8040c1c1a378c52f6f',
 'GE04':'fcd7503c20e3cd047929dfe84857d3d270b8e5fd35b03d9c368de2646cbc618e',
 'GE05':'7312e6359171932e182d3fccc4c80d7fe0aa09ac612b4ae148264a8c15a85c18'}
chapters={c:json.loads((ROOT/'data/knowledge_batches'/f'{c}.json').read_text(encoding='utf-8')) for c in expected}
for c,d in chapters.items():
 assert digest(d)==expected[c],f'{c} changed: inspect before issuing a new receipt'

# Preserve original method content except for the explicit reviewed overlays below.
g1=copy.deepcopy(chapters['GE01']['methods']);m=g1[2]
m['example_en']=r'In triangle $ABC$, choose $D\in AB,E\in AC$ with $AD/AB=AE/AC=2/5$. Reflect $D,E$ in point $A$ to $D\prime,E\prime$. Find the signed homothety scale from $ABC$ to $AD\prime E\prime$ and their area ratio.'
m['example_zh']=r'三角形中，$D\in AB,E\in AC$ 满足 $AD/AB=AE/AC=2/5$。将 $D,E$ 关于点 $A$ 作中心反射得 $D\prime,E\prime$。求从 $ABC$ 到 $AD\prime E\prime$ 的有向位似比及面积比。'
m['solution_en']=[r'The equal fractions and shared angle give $ADE\sim ABC$, with $DE\parallel BC$ and scale $2/5$.',r'With $A$ as vector origin, $D\prime=-2B/5$ and $E\prime=-2C/5$. Thus the signed homothety scale is $-2/5$: both images lie on the opposite rays.',r'Ordinary area uses the square, so $[AD\prime E\prime]/[ABC]=4/25$. The negative length scale does not make area negative.']
m['solution_zh']=[r'两边比例相等且夹角共用，得 $ADE\sim ABC$，且 $DE\parallel BC$，线性比例为 $2/5$。',r'以 $A$ 为向量原点，则 $D\prime=-2B/5,E\prime=-2C/5$，有向位似比为 $-2/5$，两个像点均在反向射线上。',r'普通面积取比例平方，故 $[AD\prime E\prime]/[ABC]=4/25$；负线性比例不会产生负的普通面积。']
m['extensions_en'].append(r'If three parallel corner cuts leave a six-equal-sided hexagon inside a triangle of sides $a,b,c$, its common side $s$ satisfies $1=s(1/a+1/b+1/c)$. On the side of length $a$, the two removed lengths are $as/b$ and $as/c$, leaving the middle length $s$; divide their sum by $a$.')
m['extensions_zh'].append(r'若三条平行截角线在边长为 $a,b,c$ 的三角形内留下六边等长的六边形，其公共边长 $s$ 满足 $1=s(1/a+1/b+1/c)$。沿长为 $a$ 的边，两端切去段为 $as/b,as/c$，中央保留 $s$；将三段之和除以 $a$ 即得。')

g2=copy.deepcopy(chapters['GE02']['methods']);m=g2[1]
m['example_en']='A triangle has area 72. Two parallel chords lie at one half and one third of its altitude measured from the apex. Find the area of the band between them.'
m['example_zh']='一个三角形面积为72。两条平行截线从顶点量起的高度，分别是原高的一半与三分之一。求两截线之间条带的面积。'
m['solution_en']=[r'The two apex triangles have linear scales $1/2$ and $1/3$, since all three bases are parallel.',r'Their areas are $72(1/2)^2=18$ and $72(1/3)^2=8$.',r'The smaller apex triangle is contained in the larger, so the band area is $18-8=10$, or $5/36$ of the original area.']
m['solution_zh']=[r'三底平行，所以两个顶端小三角形的线性比例分别为 $1/2,1/3$。',r'两面积分别为 $72(1/2)^2=18$ 与 $72(1/3)^2=8$。',r'较小顶端三角形包含在较大者内，故条带面积为 $18-8=10$，即原面积的 $5/36$。']
m['extensions_en']=[r'For a trapezoid of parallel bases $0<a<b$, extend its legs to an apex. A parallel chord $x$ bisects the trapezoid area exactly when $x^2-a^2=b^2-x^2$, hence $x=\sqrt{(a^2+b^2)/2}$. The positive root lies between the two bases.']
m['extensions_zh']=[r'两底满足 $0<a<b$ 的梯形，延长两腰至公共顶点。平行截段 $x$ 平分面积，等价于 $x^2-a^2=b^2-x^2$，所以 $x=\sqrt{(a^2+b^2)/2}$，正根介于两底之间。']
g2[7]['steps_en'][0]=r'For convex $ABCD$, orient the full diagonals as $u=\overrightarrow{AC}$ and $v=\overrightarrow{BD}$; then $K=|u\times v|/2$.'
g2[7]['steps_zh'][0]=r'对凸四边形 $ABCD$，将整条对角线定向为 $u=\overrightarrow{AC},v=\overrightarrow{BD}$，则 $K=|u\times v|/2$。'
coverage2=copy.deepcopy(chapters['GE02']['coverage_by_question'])
coverage2['AIME-2006-I-Q08']['prerequisites'].remove('LO02')

g4=copy.deepcopy(chapters['GE04']['methods']);m=g4[6]
m['steps_en']=[r'Let the incircle touch $AB,AC,BC$ at $Z,W,X$. Let $Y$ be the first circle intersection on ray $AX$, and let its tangent cut side segments $AB,AC$ at $P,Q$. Set $\ell=AZ=AW,p=AP,q=AQ$.',r'Equal tangents give $PY=\ell-p$ and $BX=AB-\ell$. The common angle at $A$ and supplementary tangent–chord angles give the sine-rule ratio $PY/p=BX/AB$.',r'Rearrange to $\ell/p+\ell/AB=2$. Repeating on the other side gives $\ell/q+\ell/AC=2$.',r'Check the near-intersection order and positive cut segments. An arbitrary tangent to the near incircle arc does not satisfy these reciprocal laws without $A,Y,X$ collinear.']
m['steps_zh']=[r'设内切圆切 $AB,AC,BC$ 于 $Z,W,X$。令 $Y$ 为射线 $AX$ 先遇到的圆交点，$Y$ 处切线交边线段 $AB,AC$ 于 $P,Q$；记 $\ell=AZ=AW,p=AP,q=AQ$。',r'等切线给出 $PY=\ell-p,BX=AB-\ell$。由共同的 $A$ 角及互补的弦切角，正弦定理得 $PY/p=BX/AB$。',r'整理得 $\ell/p+\ell/AB=2$，另一边同理得 $\ell/q+\ell/AC=2$。',r'检查近交点次序及各截段为正。若缺少 $A,Y,X$ 共线条件，任意近弧切线并不满足这些倒数关系。']
m['example_en']=r'The incircle of $ABC$ touches $BC$ at $X$. Let $Y$ be the first intersection of ray $AX$ with the incircle, and let the tangent at $Y$ meet $AB,AC$ at $P,Q$ inside the sides. Prove $AP=AQ$ if and only if $AB=AC$.'
m['example_zh']=r'三角形内切圆切 $BC$ 于 $X$。射线 $AX$ 先交圆于 $Y$，$Y$ 处切线交边内于 $P\in AB,Q\in AC$。证明 $AP=AQ$ 当且仅当 $AB=AC$。'
m['solution_en']=[r'Write $p=AP,q=AQ$ and let $\ell$ be the common vertex tangent length. The tangent–chord and sine-rule calculation gives $1/p+1/AB=2/\ell$.',r'The same argument on the $AC$ side gives $1/q+1/AC=2/\ell$. Subtracting yields $1/p-1/q=1/AC-1/AB$.',r'All four lengths are positive. Thus the left side vanishes exactly when $p=q$, and the right side exactly when $AB=AC$, proving both directions.']
m['solution_zh']=[r'记 $p=AP,q=AQ$，公共顶点切线长为 $\ell$。由弦切角与正弦定理得到 $1/p+1/AB=2/\ell$。',r'在 $AC$ 一侧同理得到 $1/q+1/AC=2/\ell$。相减得 $1/p-1/q=1/AC-1/AB$。',r'四个长度均为正，所以左边为零等价于 $p=q$，右边为零等价于 $AB=AC$，两方向均得证。']
g4[3]['steps_en'][0]=r'For circles with distinct centers, subtract their equations to cancel $x^2+y^2$; the equal-power locus is the resulting radical-axis line, containing any common chord.'
g4[3]['steps_zh'][0]=r'对圆心不同的两圆，相减方程消去 $x^2+y^2$；等点幂轨迹是所得根轴直线，若有公共弦则包含它。'
g4[9]['steps_en'][1]='Distinct circles intersect in at most two points; coincident boundary circles give no proper strictly separated subset. Thus a disk selects one consecutive run of vertices on a circle, unless empty or full.'
g4[9]['steps_zh'][1]='不同圆至多交于两点；边界圆重合时不能严格分离非空真子集。因此圆盘在圆周顶点中选出的子集应为连续一段，或空集、全集。'
g4[10]['steps_en'][0]=r'Assume the orthocenter $H$ and $B,C$ are distinct. With the circumcenter at the vector origin, use $h=a+b+c$.'
g4[10]['steps_zh'][0]=r'先假设垂心 $H$ 与 $B,C$ 互不重合。以外心为向量原点，使用 $h=a+b+c$。'
g4[7]['question_ids'].remove('AIME-2019-II-Q15')
coverage4=copy.deepcopy(chapters['GE04']['coverage_by_question'])
coverage4['AIME-2019-II-Q15']['method_ids'].remove('GE04-M08')

g5=copy.deepcopy(chapters['GE05']['methods'])
g5[6]['extensions_zh'][0]=g5[6]['extensions_zh'][0].replace('三个等角圆','三个等半径顶角圆')

# Supplemental exact checks; all52 examples were also inspected and recomputed.
checks=[]
def check(name,condition):
 assert bool(condition),name
 checks.append(name)
x=s.symbols('x',positive=True)
check('GE01 signed-area scale',s.Rational(-2,5)**2==s.Rational(4,25))
check('GE01 altitude series',s.Rational(12,5)/(1-s.Rational(3,5))==6)
check('GE02 nested band',72*(s.Rational(1,4)-s.Rational(1,9))==10)
points=[(0,0),(4,0),(4,1),(1,1),(1,3),(0,3)]
check('GE02 concave shoelace',sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(points,points[1:]+points[:1]))==12)
check('GE02 segment',s.simplify(4*s.pi/3-2*s.sin(2*s.pi/3)-(4*s.pi/3-s.sqrt(3)))==0)
check('GE02 sine-area branches',set([34-30*s.Rational(3,5),34+30*s.Rational(3,5)])=={16,52})
check('GE02 spatial patch',s.Matrix([3,0,6]).cross(s.Matrix([0,2,0])).norm()==6*s.sqrt(5))
check('GE03 Heron',16*12*3*1==24**2)
check('GE03 circumradius',s.Rational(4*13*15,4*24)==s.Rational(65,8))
check('GE03 shared cosine',(6/s.Integer(10))==s.Rational(3,5))
check('GE03 tangent lengths',s.sqrt(4**2-2**2)==2*s.sqrt(3))
check('GE03 constrained sum',(s.Rational(1,2)+s.sqrt(3)/2)==(1+s.sqrt(3))/2)
check('GE03 rolling angle',s.Rational(4,3)*s.pi/2==2*s.pi/3)
check('GE04 tangent power',4*9==3*12==6**2)
check('GE04 two chord points',4**2+3**2==25 and (4-4)**2+3**2==9)
check('GE04 separation maximum',s.simplify(x/((1+x)*(1+2*x))).subs(x,1/s.sqrt(2)).simplify()==3-2*s.sqrt(2))
check('GE04 cyclic circumradius',16*12**2*s.Rational(25,4)==24*25*24)
check('GE04 chord probability',1-3*s.Rational(1,3)**2==s.Rational(2,3))
check('GE04 arc height',s.simplify(s.sqrt(s.Rational(4,3))/2-1/s.sqrt(3))==0)
check('GE05 internal bisector',6*9-4*6==30)
check('GE05 incenter parallel',6*(1-s.Rational(6,18))==4)
check('GE05 tangent pieces',(15-12)+(15-5)==13)
check('GE05 Euler example feasible',s.Matrix([6,0])-s.Matrix([2,2])==s.Matrix([4,-2]) and s.Matrix([4,-2]).dot(s.Matrix([-1,-2]))==0)
check('GE05 Euler distance',s.Matrix([4,-2]).norm()==2*s.sqrt(5))
check('GE05 arc-midpoint data',s.Rational(9,2)-3==s.Rational(3,2))
check('GE05 perimeter routes',5+1==7-1)
(ROOT/'output/qa/knowledge-geometry-source-review-checks.json').write_text(json.dumps({'reviewer':'source_audit','sections':list(expected),'all_examples_individually_recomputed':52,'supplemental_exact_checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')

r=KnowledgeReview('source_audit')
r.accept('GE01',[
'Read all7 methods/extensions and44 canonical question routes, reusing previously inspected records and reading newly encountered statements/solutions in full. Recomputed the examples: chord5, ordered-similarity sides6/8 and area4/9, signed homothety-2/5 and area4/25, isosceles angles30/30/120 and base ratio sqrt3, perpendicular median proof, constrained placement scale5/4, and altitude series6. All formulas and equality constructions hold.',
'Replaced the hexagon example, which was a numbers-only variant of2024 II Q5, with an original negative-homothety task. Preserved the needed reciprocal-side hexagon theorem as an explicitly derived bilingual extension.'
],patch={'methods':g1})
r.accept('GE02',[
'Read all11 methods/extensions and78 actual primary/secondary routes. Recomputed all examples, including cyclic-thirds area1/3, new nested band10, concave area6, segment4pi/3-sqrt3, attainable rhombus areas1/2/3, side lengths4 and2sqrt13, side distance3, quadrilateral area12 and dot magnitude24sqrt3, spatial area6sqrt5, attainable concentric-circle area3, and central-symmetry half-area pi. Verified the six-disk union wedge formula and normal-projection identities.',
'Specified the directions u=AC and v=BD in the signed side-square identity. Replaced a source-shaped trapezoid subproblem with a distinct nested-band example while retaining the exact equal-area trapezoid theorem in the extension.'
],patch={'methods':g2,'coverage_by_question':coverage2})
r.accept('GE03',[
'Read all10 methods/extensions and89 exact question routes. All ten examples recompute correctly: altitude12 and area60, shared cosine3/5, Heron area24/radius3/2/circumradius65/8, cevian ratio2, center distance4 and tangent2sqrt3, both included-angle radicals, constrained leg sum(1+sqrt3)/2, equal-side-chain angle45, Fermat sum2sqrt3, and no-slip spin120degrees. Checked acute/obtuse branches, altitude-foot feasibility, rotation bound and angular no-slip distinction in both languages.'
])
r.accept('GE04',[
'Read all12 complete methods/extensions and50 exact primary/secondary routes. Recomputed every example and verified cyclic order, tangent power, radical-axis subtraction, real cross ratio, chord-ratio optimization, cyclic quadrilateral radius formula, semicircle counting, orthocenter reflection, and fixed-angle arc height. The special near-incircle reciprocal identity was independently derived from its actual tangent-chord construction.',
'Corrected GE04-M07 by stating the essential A,Y,X collinearity with X the opposite-side contact, and replaced its source-shaped numeric task by an iff theorem. Clarified nonconcentric-circle and distinct-orthocenter-point assumptions, handled coincident circles in the circular-subset argument, and removed the unnecessary M08 link to2019 II Q15 with author agreement; its necessary M02 power route remains.'
],patch={'methods':g4,'coverage_by_question':coverage4})
r.accept('GE05',[
'Read all12 methods/extensions and43 actual primary/secondary routes. Independently recomputed all12 examples: bisector sqrt30, mass ratio5, reflection distance4, incenter chord4, tangent pieces3/10, circumradius65/8, incenter distance4 and angle120, Euler distance2sqrt5 (realized by a6-8-10 triangle), arc-midpoint distance9/2, centroid(2,2) versus circumcenter(3,3), isogonal product4, and midpoint perimeter-bisector vector(5/2)(u+v). Checked Stewart orientation, exradius identities, arc-midpoint angle proof and exact perimeter routes. Corrected one Chinese phrase from equal-angle circles to equal-radius corner circles.'
],patch={'methods':g5})
r.save()

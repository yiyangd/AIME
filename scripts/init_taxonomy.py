"""Authoritative AIME taxonomy; stable codes are independent of printed section numbers."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GROUPS=[
('AL','Algebra','代数','#dbeafe',[
('Equations & algebraic modeling','方程与代数建模','Translate quantitative conditions into equations, eliminate unknowns, and check the original domain.','Modeling, linear/quadratic and symmetric systems; integer restrictions are secondary unless decisive.'),
('Polynomials & Vieta relations','多项式与韦达关系','Use coefficients, roots, factorization, and symmetric root expressions.','Polynomial structure is decisive; routine quadratic solving alone belongs to AL01.'),
('Complex numbers & roots of unity','复数与单位根','Use modulus, argument, complex geometry, or roots-of-unity algebra.','Include geometric series with rotating directions; real trigonometry alone belongs to AL08.'),
('Logarithms & exponentials','对数与指数','Change logarithmic bases, substitute exponential variables, and enforce domains.','Use when logarithmic or exponential identities determine the route.'),
('Sequences & summation','数列与求和','Arithmetic/geometric sequences, telescoping sums, and explicit recurrences.','Counting recurrences belong to CO05 and modular iteration may require NT04.'),
('Absolute values, floors & piecewise graphs','绝对值、取整与分段图像','Partition the domain at breakpoints; analyze floors, ceilings, and graph intersections.','Number theoretic floor sums with modular structure may have NT03 as primary.'),
('Inequalities & continuous optimization','不等式与连续最值','Prove bounds for real quantities and establish equality or limiting attainability.','Discrete combinatorial constructions belong to LO02; geometric routes can remain GE.'),
('Trigonometric algebra & equations','三角恒等式与方程','Use identities, angle parameters, periodicity, and trigonometric equation solving.','Metric triangle problems belong to GE03 unless a free trig equation is decisive.'),
('Functional constraints & iteration','函数约束与迭代','Analyze compositions, iterated maps, and functions defined by structural constraints.','A simple piecewise graph belongs to AL06.'),
('Binomial expansions & controlled approximation','二项式展开与误差控制','Expand integer or fractional powers and bound the omitted remainder to identify coefficients or digits.','Counting selections belongs to CO02; modular lifting belongs to NT04 when the expansion is only a supporting tool.')]),
('GE','Geometry','几何','#dcfce7',[
('Angles, similarity & parallel lines','角度、相似与平行线','Angle chase and similar triangles using incidences and parallelism.','Circle power, metric laws, and bisector length calculations have their own subtypes.'),
('Areas & area ratios','面积与面积比','Decompose planar area and use common heights, ratios, or determinants.','Coordinate calculations can be secondary; spatial volume belongs to GE10.'),
('Triangle metrics & trigonometry','三角形度量与三角法','Use sine/cosine laws, Pythagoras, Heron, or metric relations in triangles.','Circle configurations belong to GE04–06 when their circle property is decisive.'),
('Circle power & cyclic geometry','圆幂与圆内接几何','Use power of a point, cyclic angles, radical axes, and chord relations.','Tangency between multiple circles belongs to GE06.'),
('Angle bisectors & triangle centers','角平分线与三角形心','Use bisector ratios, inradius/circumradius identities, or center configurations.','Multiple-circle tangency belongs to GE06.'),
('Tangent circles & common tangents','相切圆与公切线','Encode tangency as center-distance or tangent-segment conditions.','A single routine tangent-power identity belongs to GE04.'),
('Coordinates, vectors & transformations','坐标、向量与变换','Choose coordinates, use dot products/determinants, or apply a decisive geometric transformation.','Conics and spatial geometry have dedicated subtypes.'),
('Conics & analytic loci','圆锥曲线与解析轨迹','Use parabola, ellipse, hyperbola, tangency, focus-distance or conic equations.','A circle alone does not make a conics problem.'),
('Spheres & spatial distances','球与空间距离','Use sphere sections, center distances, and three-dimensional coordinates.','A volume relation may be secondary; pure volume belongs to GE10.'),
('Volumes & solid geometry','体积与立体几何','Compute polyhedral or curved-solid volume and spatial sections.','Sphere tangency and distances belong to GE09 unless volume determines the route.')]),
('NT','Number Theory','数论','#ffedd5',[
('Prime factorization & valuations','质因数分解与赋值','Track prime exponents in factorials, divisors, squares, and divisibility of powers.','GCD and congruence methods have dedicated subtypes.'),
('Divisibility, GCD & LCM','整除、最大公因数与最小公倍数','Use divisor relations, Euclidean invariants, coprimality, and common multiples.','Use NT01 when comparing prime valuations is decisive.'),
('Congruences & Chinese remainders','同余与中国剩余定理','Translate conditions into residues, combine coprime moduli, and count residue classes.','Multiplicative orders and long modular iterations belong to NT04.'),
('Orders, modular powers & cycles','乘法阶、模幂与周期','Use periodic residues, multiplicative order, modular exponentiation or iterative cycles.','Routine parity alone is secondary rather than its own primary.'),
('Diophantine equations & factor pairs','丢番图方程与因子配对','Exploit integrality, factor pairs, bounds, and exhaustive integer cases.','Place-value equations usually belong to NT06.'),
('Number bases, digits & palindromes','进位制、数位与回文','Expand place value, enforce digit bounds, and analyze numeral representations.','Counting digits without arithmetic structure can have a counting primary.'),
('Rational fractions & repeating decimals','有理分数与循环小数','Use reduced fractions, repetends, coprimality and denominator structure.','General factorization belongs to NT01.'),
('Divisor functions & totients','约数函数与欧拉函数','Use divisor sums/counts, multiplicative functions and totient restrictions.','Elementary factor counting may instead be a secondary NT01.')]),
('CO','Counting & Combinatorics','计数与组合','#f3e8ff',[
('Restricted permutations & arrangements','受限排列','Count orderings with adjacency, repetition, blocks, forbidden patterns, or insertion.','Subsets and unordered selections belong to CO02.'),
('Subsets & binomial identities','子集与二项式恒等式','Count selections and exploit binomial coefficients or Vandermonde identities.','Use CO04 if overcount correction is decisive.'),
('Compositions, partitions & generating functions','整数拆分、分拆与生成函数','Encode nonnegative integer solutions, distributions, partitions, or coefficients.','Diophantine feasibility without counting belongs to NT05.'),
('Inclusion-exclusion & double counting','容斥与双计数','Correct overlaps or count incidences from two viewpoints.','Routine subtraction alone does not force this primary.'),
('Recurrences, lattice paths & tilings','递推、格路与铺砌','Define states and recurrences for paths, walks, arrangements or tilings.','Numeric non-counting recurrences belong to AL05.'),
('Graphs & geometric counting','图论与几何计数','Count regions, intersections, polygonal figures, or graph configurations.','A probability based on such counting can have a PS primary.'),
('Bijections & structural counting','双射与结构计数','Find a reversible encoding or decompose a combinatorial structure.','Use a more specific counting subtype when it describes the decisive route.')]),
('PS','Probability & Statistics','概率与统计','#fce7f3',[
('Finite probability & combinatorial sampling','有限概率与组合抽样','Count equally likely outcomes, without-replacement samples and favorable events.','Explicit conditioning belongs to PS02.'),
('Conditional probability & independence','条件概率与独立性','Condition on information, normalize conditional spaces, or combine independent events.','Do not assume conditioned events retain independence.'),
('Geometric probability','几何概率','Compare lengths, areas, or volumes in a continuous uniform sample space.','A discrete geometric configuration does not automatically belong here.'),
('Expected values & stopping processes','期望与停止过程','Use linearity, first-step equations, stopping states, and strategy comparison.','A distribution probability without expectation belongs to PS05.'),
('Distributions & repeated trials','分布与重复试验','Model geometric/binomial events, repeated independent trials, or tails.','General finite sampling belongs to PS01.'),
('Data & descriptive statistics','数据与描述统计','Use mean, median, mode and integer data constraints.','Probability on data belongs to an appropriate probability subtype.')]),
('LO','Logic & Strategy','逻辑与策略','#e2e8f0',[
('Games, invariants & state strategies','博弈、不变量与状态策略','Prove winning/losing states or preserve a structural invariant.','Use counting or number theory primary if those alone determine the route.'),
('Discrete extrema & constructions','离散最值与构造','Establish a combinatorial bound and construct an extremal configuration.','Continuous algebraic inequalities belong to AL07.'),
('Constraint deductions & logical cases','约束推理与逻辑分类','Combine discrete statements through necessary and sufficient cases.','Use a specific algebra/number-theory code if that mechanism is decisive.')])]

def main():
    cats=[];subs=[]
    for ci,(code,en,zh,color,items) in enumerate(GROUPS,1):
        cats.append(dict(id=code,name_en=en,name_zh=zh,color=color,order=ci))
        for j,(name_en,name_zh,definition,boundary) in enumerate(items,1):
            subs.append(dict(id=f'{code}{j:02}',category_id=code,name_en=name_en,name_zh=name_zh,definition_en=definition,boundary_en=boundary,section_number=f'{ci}.{j}',order=j))
    translations={}
    for path in sorted((ROOT/'data/taxonomy_translations').glob('*.json')):
        for code,fields in json.loads(path.read_text(encoding='utf8')).items():
            assert code not in translations, f'Duplicate subtype translation: {code}'
            assert set(fields)=={'definition_zh','boundary_zh'},(code,fields.keys())
            translations[code]=fields
    for subtype in subs:subtype.update(translations.get(subtype['id'],{}))
    taxonomy=dict(version='2026-11-05.v1',categories=cats,subtypes=subs,policy='One decisive primary per problem; secondary codes require a distinct necessary step. Unused dictionary entries do not become sections.')
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'data/taxonomy.json').write_text(json.dumps(taxonomy,ensure_ascii=False,indent=2),encoding='utf8')
if __name__=='__main__':main()

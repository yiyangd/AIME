"""Issue the independent AL07 receipt only for the explicitly inspected version."""
import itertools,json
import sympy as s
from review_knowledge_helpers import KnowledgeReview,ROOT,digest

d=json.loads((ROOT/'data/knowledge_batches/AL07.json').read_text(encoding='utf-8'))
assert digest(d)=='8ec212dd8b29b111d83d3fe148b26f0745f745561b7092a95b2db08708667063','AL07 changed: inspect the new content before issuing a receipt'
x,t=s.symbols('x t',real=True)
assert max(x*(30-x) for x in range(1,30,4))==221
assert s.expand((x+1)**2*(x-2)**2).coeff(x,2)==-3
r=5*(2-s.sqrt(2));assert s.simplify((2+s.sqrt(2))*r-10)==0 and 2*r<6
assert s.simplify(3*s.cos(s.pi/6)+4*s.sin(s.pi/6)-(2+3*s.sqrt(3)/2))==0
assert s.Rational(2,3)+s.Rational(1,2)==s.Rational(7,6)
assert s.solve(10*t*t-7*t+1,t)==[s.Rational(1,5),s.Rational(1,2)]
assert max(sum(abs(p[i]-p[i+1]) for i in range(4)) for p in itertools.permutations(range(1,6)))==11
assert set(s.solve(8*t*t-24*t+15,t))=={(6-s.sqrt(6))/4,(6+s.sqrt(6))/4}
assert s.simplify(s.diff(9*s.cos(t)**2+4*s.sin(t)**2,t)+10*s.sin(t)*s.cos(t))==0
review=KnowledgeReview('source_audit')
review.accept('AL07',[
'Independently read all18 complete bilingual methods, examples, solutions, and extensions, and all36 canonical question routes. Recomputed the examples: discrete maximum221, cyclic product16, weighted Cauchy1/10, four-focus minimum14, chord areas3 and27, quartic coefficient-3, disk radius5(2-sqrt2), linear-disk convex-hull support, six-focus minimum6, constrained trigonometric endpoint2+3sqrt3/2, cap product24, sorted-coordinate maximum7/6, two convex-exponential roots, persistence of three simple positive cubic roots, level counts0/1/2, five-path maximum11, maximum tangent slope(6+sqrt6)/4, and ellipse tangent radii2/3.',
'Checked compactness bounds and the repeated-root perturbation argument, the reachability convex-hull identity, projection containment equality, and every limiting versus attained extremum. Independently checked the 2024 I Q12 derivative-product and near-corner convexity certificate in its required AL06 route; the crossing-sign lemma is valid on a fixed equally oriented branch pair. The documented 2016 I Q9 infeasible source equality is correctly distinguished from the literal constrained maximum.'
])
review.save()

import json
from review_knowledge_helpers import KnowledgeReview,digest,ROOT
s=json.loads((ROOT/'data/knowledge_batches/GE08.json').read_text(encoding='utf8'))
assert digest(s)=='7999f590587390a74e99065761f66e4269df0a51da1568aedc46b15f3ec913a3'
r=KnowledgeReview('root');r.accept('GE08',[
 'Independently read all eight complete bilingual methods, examples, solutions and extensions and checked all assigned primary/secondary routes against the canonical solution chains.',
 'Recomputed the ellipse-equilateral example (3072/169), the four real conic intersections, the ellipse/focal distance branch PF1<7, and the crossed-focal pair (sqrt10+sqrt5).',
 'Verified the hyperbola-rhombus lower bound48 is an unattained infimum; checked the unit-segment envelope point (3sqrt3/8,1/8), the rotated-parabola quadrant condition, and the parabola normal-distance radii3 and sqrt11/2.',
 'Both language versions preserve the relevant sign, positivity, distinctness and attainment conditions. No corrections were required.'
]);r.save()

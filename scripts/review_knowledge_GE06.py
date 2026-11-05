import copy,json
from review_knowledge_helpers import KnowledgeReview,digest,ROOT
s=json.loads((ROOT/'data/knowledge_batches/GE06.json').read_text(encoding='utf8'))
assert digest(s)=='e04436a11ab43b7483742424924231fc64c26cfb3fa40a0627011b13d4c77259'
m=copy.deepcopy(s['methods'])
m[2]['steps_en'][0]='For unequal radii, common external tangents meet at the external similarity center, dividing center distances in the radius ratio. Equal-radius external tangents are parallel and have no finite similarity center.'
m[2]['steps_zh'][0]='半径不等时，两条公外切线交于外位似中心，到两圆心距离比等于半径比；半径相等时公外切线平行，不存在有限外位似中心。'
m[6]['steps_en'][1]='For corner circles inside the triangle with $0<x<r$, the three centers are images of the vertices under scale $(r-x)/r$ about the incenter, where $r$ is the triangle inradius.'
m[6]['steps_zh'][1]='若三个角圆均在三角形内且 $0<x<r$，圆心是三顶点以内心为中心、比例 $(r-x)/r$ 的位似像，其中 $r$ 为原内切圆半径。'
m[6]['example_en']='In an equilateral triangle of inradius one, three equal circles inside the triangle are each tangent to the two sides at a different vertex. A fourth circle of the same radius lies inside and is externally tangent to all three. Find the common radius.'
m[6]['example_zh']='内切圆半径为一的等边三角形内，有三个等圆分别与三个顶点的两邻边相切。第四个同半径圆也在三角形内，并与前三圆均外切，求公共半径。'
m[7]['steps_en'][1]=r'For fixed-circle radius $R$, moving radius $r$, ground-frame spin $\phi$, and center sweep $\theta$, no slip gives $r\,d\phi=(R+r)\,d\theta$.'
m[7]['steps_zh'][1]=r'固定圆半径为 $R$、动圆半径为 $r$、对地自转角为 $\phi$、圆心公转角为 $\theta$ 时，无滑动给出 $r\,d\phi=(R+r)\,d\theta$。'
r=KnowledgeReview('root');r.accept('GE06',[
 'Read all ten bilingual procedures/examples/solutions/extensions and matched all25 listed routes to their canonical method chains, reading full solutions for the tangent-ray and power cases. Every worked numerical example recomputed independently.',
 'Corrected the external-similarity-center statement for equal radii; made the contained corner-circle setup and positive homothety scale explicit.',
 'Corrected a substantive radius-symbol error in the general rolling formula: the moving radius r, not fixed R, multiplies the ground-frame spin. The original example already used moving radius2 and correctly gave135 degrees.',
 'Checked center-distance example(r4 at-1), hexagonal ring radius3, similarity distance5/3, triangle inradius sqrt7, ellipse a4/b²12, power-gradient distance4, corner radius1/2, torus contact radius5/2, and incidence slope4/3.'
],{'methods':m});r.save()

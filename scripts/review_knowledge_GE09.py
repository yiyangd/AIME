import copy,json
from review_knowledge_helpers import KnowledgeReview,digest,ROOT
s=json.loads((ROOT/'data/knowledge_batches/GE09.json').read_text(encoding='utf8'))
assert digest(s)=='80256d49bfc8569f02558ae77321adb2b7a0255d270b5eb16385c9c884075fef'
m=copy.deepcopy(s['methods'])
m[2]['extensions_en'][0]=r'For a solid cone described by $\alpha u+\beta\rho\le\gamma$, where $u$ is the axial coordinate, $\rho$ the radial coordinate and $\beta>0$, every lateral supporting plane stays at least a ball radius away precisely when $\sqrt{\alpha^2+\beta^2}\,r\le\gamma-\alpha u-\beta\rho$ at its center. Two perpendicular cones give coupled absolute-value bounds; add them and check the base-plane distances too.'
m[2]['extensions_zh'][0]=r'若实心圆锥由 $\alpha u+\beta\rho\le\gamma$ 描述，其中 $u$ 为轴向坐标、$\rho$ 为径向坐标且 $\beta>0$，则各侧面支撑平面到球心距离均不小于球半径，等价于球心满足 $\sqrt{\alpha^2+\beta^2}\,r\le\gamma-\alpha u-\beta\rho$。两个垂直圆锥给出含绝对值的耦合界，可相加求界，但仍需检验底面距离。'
m[5]['extensions_en'][0]=r'For unequal radii $R,r$ in the same sector, the transverse center separation is $|R-r|/\sin\theta$. If a small sphere touches two equal spheres whose centers differ only along the intersection line, it lies halfway between them along that line.'
m[5]['extensions_zh'][0]=r'同一角域内半径为 $R,r$ 的球心横向间距为 $|R-r|/\sin\theta$。若小球同时与两个仅沿交线分离的等球相切，则小球在交线方向上位于两者正中。'
m[5]['extensions_en'][1]='A sphere through three noncollinear triangle vertices has its center on their perpendicular circumcenter axis. Two distinct sphere points on that axis are diameter endpoints. A triangle vertex then supplies a right triangle and, when its projection lies between the endpoints, the altitude-product relation.'
m[5]['extensions_zh'][1]='经过三角形三个不共线顶点的球，其球心在外心垂轴上。该轴上两个不同球面点必为直径端点。再用一个三角形顶点构造直角三角形；若其投影位于两端点之间，还可使用高线乘积关系。'
m[7]['steps_en'][0]='In the coaxial configuration, the sphere center lies on the torus rotation axis. A plane through that axis cuts the torus into its generating circles; analyze either one.'
m[7]['steps_zh'][0]='在同轴构型中，球心位于圆环旋转轴上。经过该轴的平面将圆环面截成母圆，分析其中一个即可。'
m[7]['steps_en'][1]='For sphere radius $R$ and tube radius $r$, use center distance $R-r$ for internal tangency (requiring $R>r$), or $R+r$ for external tangency.'
m[7]['steps_zh'][1]='球半径为 $R$、管半径为 $r$ 时，内切圆心距为 $R-r$（要求 $R>r$），外切为 $R+r$。'
r=KnowledgeReview('root');r.accept('GE09',[
 'Read all nine complete bilingual methods and all16 linked canonical problem statements and worked solutions; checked applicability to the actual primary/secondary method chains.',
 'Independently recomputed all nine teaching examples: sphere sections2sqrt6; hemisphere fraction1/5; tetrahedron inradius3-sqrt3; pyramid circumradius17/6; lowest cube vertex2-sqrt3; tangent spheres separation4; prism count4; torus contact15/4; affine radius5/2 with a verified distinct unit-normal tangent plane.',
 'Made the solid-cone supporting halfspaces and beta>0 explicit, used an absolute value for unequal sphere radii, and stated the common sphere/circumcenter-axis premise for the diameter extension.',
 'Added the coaxial premise and R>r internal-tangency domain to the torus method. Verified signed-height choices, filled-triangle foot inclusion, box compactness/attainment and the second-plane normalization in the linked routes.'
],{'methods':m});r.save()

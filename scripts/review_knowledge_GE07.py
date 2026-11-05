import copy,json
from review_knowledge_helpers import KnowledgeReview,digest,ROOT
s=json.loads((ROOT/'data/knowledge_batches/GE07.json').read_text(encoding='utf8'))
assert digest(s)=='e1dc30dcd573b02825172e38b0c806eb57b887842c42722844c1cb44aa1f4367'
m=copy.deepcopy(s['methods']); c=copy.deepcopy(s['coverage_by_question'])
m[2]['extensions_en'][1]=r'For vectors $v_i$ of equal positive length $R$ and sum zero, $|v_i-x|\ge R-v_i\cdot x/R$ sums to $\sum|v_i-x|\ge nR$, attained at $x=0$.'
m[2]['extensions_zh'][1]=r'若 $v_i$ 均长 $R>0$ 且向量和为零，则 $|v_i-x|\ge R-v_i\cdot x/R$ 相加得到 $\sum|v_i-x|\ge nR$，在 $x=0$ 取等。'
m[8]['extensions_en'][0]=r'A line with primitive direction $v$ has successive lattice points separated by $v$. In the grid box $\{0,\ldots,N-1\}^d$, where $N$ is a positive integer, containing $k$ grid points requires $(k-1)|v_i|\le N-1$ for every component. Normalize one endpoint to avoid counting a line repeatedly.'
m[8]['extensions_zh'][0]=r'本原方向为 $v$ 的直线，相继格点间差为 $v$。在格点盒 $\{0,\ldots,N-1\}^d$ 中（$N$ 为正整数），若直线含 $k$ 个格点，则各分量满足 $(k-1)|v_i|\le N-1$；规范一个端点可避免重复计线。'
m[14]['steps_en'][0]=r'Choose linearly independent unit side directions $u,v$ and record $u\cdot v=c$, with $|c|<1$.'
m[14]['steps_zh'][0]=r'取线性无关的单位边方向 $u,v$，记录 $u\cdot v=c$，其中 $|c|<1$。'
qid='AIME-2002-II-Q02'
m[1]['question_ids'].remove(qid);m[2]['question_ids']=sorted(m[2]['question_ids']+[qid])
c[qid]['method_ids']=[('GE07-M03' if x=='GE07-M02' else x) for x in c[qid]['method_ids']]
for qid in ['AIME-2018-II-Q04','AIME-2014-I-Q13','AIME-2026-II-Q03','AIME-2017-II-Q10']:
 m[6]['question_ids'].remove(qid);c[qid]['method_ids'].remove('GE07-M07');assert c[qid]['method_ids']
r=KnowledgeReview('root');r.accept('GE07',[
 'Read all fifteen complete bilingual methods, original examples, solutions and extensions; checked every linked canonical question route. Independently recomputed all fifteen worked examples, including the square partition, reflection path, river drift, oblique metric and inversion disk.',
 'Made the lattice-box convention explicit as N integer coordinate values per axis, required a nondegenerate oblique basis, and added R>0 to the vector support inequality.',
 'Moved 2002II2 from equal-distance centers to squared metric distances: the actual proof compares cube edge/face/body diagonal lengths. Pruned four half-plane clipping links whose actual route instead uses line intersections or unsigned area; each retains a relevant coordinate method.',
 'Verified the cleaver extension by equal perimeter routes, distinguished unsigned self-crossing area from shoelace algebraic area, and checked the nonattained/side-branch conditions in the linked methods.'
],{'methods':m,'coverage_by_question':c});r.save()

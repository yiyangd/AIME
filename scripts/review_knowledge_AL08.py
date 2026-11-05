"""Reproduce the AL08 receipt only for the actually reviewed author version."""
import json
from review_knowledge_helpers import KnowledgeReview,ROOT,digest
d=json.loads((ROOT/'data/knowledge_batches/AL08.json').read_text(encoding='utf-8'))
assert digest(d)=='098e0922543c5e6637e70514503c8343d4934f902135add70d2176e98a380513','AL08 changed; read and review the new content before issuing a receipt'
m=d['methods']
m[1]['steps_en'][0]=r'Use both exact families: $\sin u=\sin v$ gives $u-v=2k\pi$ or $u+v=(2k+1)\pi$; $\cos u=\cos v$ gives $u=\pm v+2k\pi$.'
m[1]['steps_zh'][0]=r'列全准确分支：$\sin u=\sin v$ 时，$u-v=2k\pi$ 或 $u+v=(2k+1)\pi$；$\cos u=\cos v$ 时，$u=\pm v+2k\pi$。'
m[10]['solution_en'][1]=m[10]['solution_en'][1].replace(r'For general $r<1$',r'For general $|r|<1$')
m[10]['solution_zh'][1]=r'在公比满足 $|r|<1$ 时，将闭式有理化，一般虚部为 $r\sin t/(1-2r\cos t+r^2)$。'
r=KnowledgeReview('source_audit')
r.accept('AL08',[
'Recomputed all12 original examples and checked all39 canonical primary/secondary routes, reading the previously unseen20 trigonometric/geometric statements and derivations in full. Results agree:4sqrt21/25,6 finite-angle roots,3 factor branches,arctan sum3pi/4,power sum17/81,telescoping sine formula,positive sine product sqrt5/4,triple-angle identity,pentagon cosine values,complementary-radical line x+y=1,series3sqrt3/14,and compatible maximum9/8.',
'Checked both special triangle identities algebraically and the gcd criterion for simultaneous sine maxima. Clarified the first branch rule to distinguish sine from cosine, and corrected the general geometric-series condition from r<1 to |r|<1; the original numerical example was already correct.'
],patch={'methods':m})
r.save()

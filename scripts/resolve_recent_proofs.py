"""Resolve two source-proof gaps with independent arguments/certificates."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/batches/2024I.json';rows=json.loads(p.read_text(encoding='utf8'));q=rows[11]
q['solution_en']=[
r'Every solution lies in $[0,1]^2$. Put $h(u)=4||u-1/2|-1/4|$ on $[0,1]$. Its values at $0,1/4,1/2,3/4,1$ are $1,0,1,0,1$. Thus $y=F(x)=h(|\sin2\pi x|)$ has sixteen monotone full-height branches, while $x=G(y)=h(|\cos3\pi y|)$ has twenty-four full-width branches. The only boundary solution is $(1,1)$.',
r'To justify branch-intersection uniqueness, we prove $|F\prime(x)G\prime(y)|=96\pi^2|\cos2\pi x\sin3\pi y|>1$ at every interior solution. Such solutions avoid all branch endpoints. If $|\cos2\pi x|\le1/20$, then $|\sin2\pi x|\ge399/400$, hence $y\ge.99$. It follows that $x\ge1-18\pi^2(.01)^2>.982$, forcing $|\cos2\pi x|>.99$, a contradiction.',
r'If the derivative product were at most one, at least one factor $|\cos2\pi x|,|\sin3\pi y|$ would be at most $1/20$, since $96\pi^2/400>1$. The previous argument excludes the first, so $|\sin3\pi y|\le1/20$ and $x\ge.99$. Set $a=1-x$, $b=1-y$. Then $0<a\le.01$ and $b=4\sin2\pi a\le.08\pi<.252$. The sine bound now forces $0<b<.01$ (the only nearby zero of $\sin3\pi y$ is at $y=1$). The exact equations are $b=4\sin2\pi a$ and $a=4(1-\cos3\pi b)$.',
r'Define $H(b)=4(1-\cos3\pi b)-\arcsin(b/4)/(2\pi)$. On $[0,.01]$, $H\prime\prime(b)=36\pi^2\cos3\pi b-b/[128\pi(1-b^2/16)^{3/2}]>0$. We have $H(0)=H(b)=0$ for the noncorner solution, so strict convexity gives $H\prime(b)>0$. This says $12\pi\sin3\pi b>1/(8\pi\cos2\pi a)$, precisely that the derivative product exceeds one, a contradiction. The claimed inequality follows.',
r'For oppositely oriented branches uniqueness follows directly by monotonicity. For equally oriented branches, write the first as $x=F^{-1}(y)$: the difference $G(y)-F^{-1}(y)$ has the same nonzero crossing sign at every zero because the derivative product is greater than one. It cannot have two such crossings. Boundary endpoint signs guarantee one interior crossing in each of the $16\cdot24$ branch-pair rectangles, except that the final pair shares $(1,1)$. There is also an interior crossing for that pair: near $b=0$, $H(b)<0$ because $H\prime(0)<0$, while the opposite rectangle endpoint has positive sign. Therefore there are $384$ interior intersections plus the corner, giving $385$.']
q['solution_zh']=[
r'所有解在单位正方形内。对 $0\le u\le1$ 令 $h(u)=4||u-1/2|-1/4|$，其在 $0,1/4,1/2,3/4,1$ 处依次取值 $1,0,1,0,1$。于是 $y=F(x)=h(|\sin2\pi x|)$ 有十六个贯穿高度的单调分支，$x=G(y)=h(|\cos3\pi y|)$ 有二十四个贯穿宽度的分支。唯一边界解为 $(1,1)$。',
r'为严格证明分支交点唯一，先证每个内部解满足 $|F\prime(x)G\prime(y)|=96\pi^2|\cos2\pi x\sin3\pi y|>1$。内部解不在分支端点上。若 $|\cos2\pi x|\le1/20$，则 $|\sin2\pi x|\ge399/400$，所以 $y\ge.99$，进而 $x\ge1-18\pi^2(.01)^2>.982$，这又使 $|\cos2\pi x|>.99$，矛盾。',
r'若导数乘积不超过一，由 $96\pi^2/400>1$，两个三角因子至少有一个不超过 $1/20$。前种已排除，故 $|\sin3\pi y|\le1/20$，从而 $x\ge.99$。令 $a=1-x,b=1-y$，则 $0<a\le.01$，$b=4\sin2\pi a\le.08\pi<.252$。正弦界进一步迫使 $0<b<.01$，因为此范围内靠近的唯一零点为 $y=1$。局部精确方程为 $b=4\sin2\pi a,a=4(1-\cos3\pi b)$。',
r'定义 $H(b)=4(1-\cos3\pi b)-\arcsin(b/4)/(2\pi)$。在 $[0,.01]$，$H\prime\prime(b)=36\pi^2\cos3\pi b-b/[128\pi(1-b^2/16)^{3/2}]>0$。非角点解满足 $H(0)=H(b)=0$，严格凸性给出 $H\prime(b)>0$，即 $12\pi\sin3\pi b>1/(8\pi\cos2\pi a)$，正是导数乘积大于一，与假设矛盾。',
r'方向相反的两分支由单调性至多相交一次。方向相同时，把第一条写成 $x=F^{-1}(y)$，差函数 $G(y)-F^{-1}(y)$ 在每个零点的穿越方向均相同，因为导数乘积大于一，所以不能有两个零点。各分支矩形端点符号保证存在一个内部交点；最后一对分支共享角点 $(1,1)$，但因 $H\prime(0)<0$，角点附近 $H(b)<0$，与矩形另一端的正号相反，因此另有一个内部交点。故内部交点为 $16\cdot24=384$，加角点共 $385$。']
q['review'].update(recomputed=True,notes='Source monotonicity shortcut replaced by derivative-product and strict-convexity proof. Root proposed route; template_audit independently checked bounds, differentiation, crossing signs and boundary uniqueness. Independent final cross-review remains pending.')
q['unresolved_issues']=[]
# Correct an algebraic simplification in the comparison of the other box extremum.
for key in ['solution_en','solution_zh']:
 rows[14][key]=[s.replace('(69+96\\sqrt6)/46','(-21+96\\sqrt6)/23').replace('(equivalent to $\\sqrt6<253/96$)','(use $\\sqrt6<5/2$, giving $s<219/23<39/4$)') for s in rows[14][key]]
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
p=ROOT/'data/batches/2026I.json';rows=json.loads(p.read_text(encoding='utf8'));q=rows[14]
cert=json.loads((ROOT/'audit/2026I15-exact-cover.json').read_text(encoding='utf8'))
assert cert['count']==83 and cert['candidate_loops']==2025
q['review'].update(recomputed=True,notes='Independent exact-cover program enumerated2025 loop masks and93361 search nodes, yielding83 unordered partitions. Certificate audit/2026I15-exact-cover.json includes all83 partitions; no slab-minimum lemma assumed.')
q['unresolved_issues']=[]
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Resolved2024I-Q12 and2026I-Q15; corrected2024I-Q15 alternate-extremum expression.')

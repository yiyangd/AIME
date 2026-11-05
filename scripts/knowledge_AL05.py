from knowledge_helpers_source import method as M,save
C='AL05';ms=[]
ms.append(M(C,1,'Pair arithmetic terms and sum polynomial weights','配对等差项并求多项式权重和',[
(r'Write $a_j=a_1+(j-1)d$ and distinguish the number of terms from the final index.',r'写 $a_j=a_1+(j-1)d$，并区分项数与末下标。'),
(r'Pair terms at complementary indices: their sum is constant. Use $\sum j=n(n+1)/2$, $\sum j^2=n(n+1)(2n+1)/6$, and $\sum j^3=[n(n+1)/2]^2$ when needed.',r'将互补下标项配对，其和恒定。必要时使用 $\sum j=n(n+1)/2,\sum j^2=n(n+1)(2n+1)/6,\sum j^3=[n(n+1)/2]^2$。'),
(r'For alternating signs or repeated patterns, simplify a full block first, then sum the resulting lower-degree expression.',r'对交替符号或重复模式，先化简完整区块，再求所得较低次表达式之和。'),
(r'Restore parity, increasing-order and integer-endpoint conditions after the sum is evaluated.',r'求和后恢复奇偶、递增次序与整数端点条件。')],
(r'In an arithmetic sequence, $a_3+a_8=20$. Find $a_1+a_{10}+a_5+a_6$.',r'等差数列满足 $a_3+a_8=20$，求 $a_1+a_{10}+a_5+a_6$。'),[
(r'Every pair whose indices sum to eleven has value $2a_1+9d$.',r'下标和为十一的每对，其值均为 $2a_1+9d$。'),
(r'Thus both $a_1+a_{10}$ and $a_5+a_6$ equal the given pair sum twenty.',r'所以 $a_1+a_{10}$ 与 $a_5+a_6$ 均等于给定对和二十。'),
(r'The requested total is forty, independent of the individual first term and difference.',r'所求总和为四十，与具体首项及公差无关。')],
('A three-term arithmetic progression is best written as a-d, a, a+d.','三项等差数列宜写成 a-d、a、a+d。'),
'2000-I-Q10 2002-II-Q04 2003-I-Q02 2004-I-Q02 2004-I-Q07 2005-I-Q02 2005-I-Q12 2006-I-Q04 2006-I-Q13 2007-I-Q07 2007-I-Q11 2008-II-Q01 2009-II-Q04 2011-II-Q03 2012-I-Q02 2012-II-Q10 2013-I-Q15 2013-II-Q03 2013-II-Q14 2015-I-Q01 2016-I-Q05 2016-II-Q01 2017-I-Q03 2017-I-Q09 2020-II-Q10 2021-I-Q05 2022-I-Q06 2023-I-Q10 2023-II-Q01 2026-II-Q01',('NT03',),[
(r'To detect a nonconsecutive four-term progression, write its entries as $u,u+d,u+2d,u+3d$ and enumerate the six placements of two fixed entries. Checking only adjacent terms in the original list misses forbidden subsequences.',r'检测非连续出现的四项等差数列，应写成 $u,u+d,u+2d,u+3d$，并枚举两个固定项的六种位置；只检查原列表相邻项会漏掉禁用子序列。')]))
ms.append(M(C,2,'Use geometric blocks and the correct dimension scale','使用等比区块与正确维度的缩放',[
(r'For $n$ terms use $a(1-r^n)/(1-r)$ when $r\ne1$; handle $r=1$ separately.',r'$r\ne1$ 时，$n$ 项和用 $a(1-r^n)/(1-r)$，并单列 $r=1$。'),
(r'An infinite series requires $|r|<1$. Area and volume ratios are the square and cube of a linear similarity ratio.',r'无穷级数须 $|r|<1$；面积比与体积比分别为线性相似比的平方与立方。'),
(r'Group consecutive equal-length blocks when partial sums are given; their block sums inherit a geometric ratio.',r'给定部分和时，可按等长连续区块分组，其区块和继承等比倍率。'),
(r'Before adding areas or volumes, verify the pieces have disjoint interiors at every stage used.',r'面积或体积相加前，须验证所用每阶段的各块内部不相交。')],
(r'Inside a unit disk, successive annuli have radii $1,1/2,1/4,\ldots$. Color annuli numbered $0,3,6,\ldots$ green from the outside. Find the green area fraction.',r'单位圆盘的连续圆环半径为 $1,1/2,1/4,\ldots$。从外侧起将编号 $0,3,6,\ldots$ 的环涂绿，求绿色面积比例。'),[
(r'Annulus $n$ has area fraction $(1-1/4)(1/4)^n$.',r'第 $n$ 环面积比例为 $(1-1/4)(1/4)^n$。'),
(r'The selected annuli form a geometric series with first term $3/4$ and ratio $(1/4)^3=1/64$.',r'选中圆环形成首项 $3/4$、公比 $(1/4)^3=1/64$ 的等比级数。'),
(r'The fraction is $(3/4)/(1-1/64)=16/21$; boundaries have zero area and the annuli interiors are disjoint.',r'比例为 $(3/4)/(1-1/64)=16/21$；边界面积为零，环的内部互不相交。')],
('Equal ratios of lengths and areas are different unless the ratio is zero or one.','长度比与面积比通常不同。'),
'2000-I-Q11 2001-II-Q12 2002-II-Q03 2002-II-Q11 2004-I-Q12 2005-II-Q03 2007-II-Q12 2009-I-Q01 2009-I-Q08 2009-II-Q08 2011-II-Q05 2012-II-Q02 2013-I-Q13 2013-I-Q14 2016-I-Q01 2016-II-Q05 2016-II-Q07 2016-II-Q15 2017-II-Q12 2020-I-Q02 2020-I-Q08 2025-II-Q12',('GE01','AL03'),[
(r'For a replicated geometric construction, multiply the number of pieces by each piece\'s scaled area or volume to obtain the increment ratio. A face count alone is insufficient if pieces overlap or become hidden. The tetrahedron construction in AIME-2001-II-Q12 is certified only through the three requested stages; no infinite non-overlap claim is used.',r'复制几何构造时，用块数乘每块缩放后的面积或体积，求增量倍率。若有重叠或隐藏，仅有面数不足以相加。AIME-2001-II-Q12 的四面体构造仅对所求三个阶段完成认证，不使用无限阶段不重叠的结论。')]))
ms.append(M(C,3,'Find the discrete difference that telescopes','寻找能望远镜消去的离散差分',[
(r'Try to write the summand as $F(k)-F(k+1)$, possibly after a partial-fraction or trigonometric identity.',r'尝试将每项写成 $F(k)-F(k+1)$，必要时先作部分分式或三角恒等变换。'),
(r'Write the uncanceled first and last terms explicitly; a shift larger than one leaves several boundary terms.',r'明确写出未消去的首尾项；位移大于一时会留下多项边界项。'),
(r'For products, telescope ratios instead of differences. For binomial sums use Pascal\'s difference identity.',r'乘积用比值而非差作望远镜；二项式求和使用帕斯卡差分恒等式。'),
(r'If rounding is requested, bound the remaining tail sharply enough to separate it from the rounding boundary.',r'若求舍入结果，须把剩余尾项估计到足以避开舍入边界。')],
(r'Find a formula for $\sum_{k=1}^{N}1/[k(k+1)(k+2)]$.',r'求 $\sum_{k=1}^{N}1/[k(k+1)(k+2)]$ 的公式。'),[
(r'The summand equals $\tfrac12[1/(k(k+1))-1/((k+1)(k+2))]$.',r'每项等于 $\tfrac12[1/(k(k+1))-1/((k+1)(k+2))]$。'),
(r'Every internal reciprocal pair cancels, leaving $\tfrac12[1/2-1/((N+1)(N+2))]$.',r'内部倒数对全部消去，留下 $\tfrac12[1/2-1/((N+1)(N+2))]$。'),
(r'Thus the sum is $1/4-1/[2(N+1)(N+2)]$. Its infinite limit is $1/4$.',r'故和为 $1/4-1/[2(N+1)(N+2)]$，无穷极限为 $1/4$。')],
('Telescope the expression before applying a large-index formula.','应先将表达式望远镜消去，再代大下标。'),
'2000-II-Q14 2000-II-Q15 2002-I-Q04 2002-II-Q06 2006-I-Q15 2009-I-Q07 2014-II-Q07 2015-II-Q13 2008-II-Q08 2022-II-Q10 2025-II-Q04',('AL02','AL08','CO02'),[
(r'Pascal gives $\binom{k+1}{r+1}-\binom{k}{r+1}=\binom{k}{r}$; summing proves the hockey-stick identity, with index endpoints retained.',r'帕斯卡恒等式给出 $\binom{k+1}{r+1}-\binom{k}{r+1}=\binom{k}{r}$；求和即得曲棍球杆恒等式，须保留下标端点。'),
(r'Useful trigonometric differences are $2\sin(h/2)\sin t=\cos(t-h/2)-\cos(t+h/2)$ and $\cot t-\cot(t+h)=\sin h/[\sin t\sin(t+h)]$. Prove nonzero denominators and use one consistent angle unit.',r'常用三角差分为 $2\sin(h/2)\sin t=\cos(t-h/2)-\cos(t+h/2)$ 与 $\cot t-\cot(t+h)=\sin h/[\sin t\sin(t+h)]$。须证明分母非零，并统一角度单位。'),
(r'From $|x_{k+1}|=|x_k+c|$, squaring gives $x_{k+1}^2-x_k^2=2cx_k+c^2$. The sum then depends on the terminal square; an integer-parity argument and an explicit attaining path may still be required.',r'由 $|x_{k+1}|=|x_k+c|$，平方得 $x_{k+1}^2-x_k^2=2cx_k+c^2$，从而和只依赖末端平方；之后仍可能需要整数奇偶论证与明确达到路径。')]))
ms.append(M(C,4,'Sum weighted geometric terms and regroup positive double series','求加权等比和，并重组正项双级数',[
(r'For $|r|<1$, start with $\sum r^k=1/(1-r)$ and derive weighted sums by a shift-and-subtract argument.',r'当 $|r|<1$，从 $\sum r^k=1/(1-r)$ 出发，以平移相减推导加权和。'),
(r'For a tail, shift the index first so the weight becomes a constant plus the new index.',r'尾和先平移下标，使权重变为常数加新下标。'),
(r'Nonnegative double series may be regrouped by the total exponent; prove a tail bound before interpreting coefficients as digits.',r'非负双级数可按总指数重组；把系数解释为数位之前须证明尾项界。')],
(r'Evaluate $\sum_{k=1}^{\infty}k/3^k$ without differentiating a series.',r'不用级数求导，计算 $\sum_{k=1}^{\infty}k/3^k$。'),[
(r'Let $S=\sum_{k\ge1}k r^k$. Multiplying by $r$ shifts its weights by one.',r'设 $S=\sum_{k\ge1}kr^k$，乘 $r$ 后其权重平移一位。'),
(r'Subtracting gives $(1-r)S=\sum_{k\ge1}r^k=r/(1-r)$, justified by absolute convergence.',r'相减得 $(1-r)S=\sum_{k\ge1}r^k=r/(1-r)$，绝对收敛保证操作有效。'),
(r'So $S=r/(1-r)^2$; at $r=1/3$, the value is $3/4$.',r'故 $S=r/(1-r)^2$；代入 $r=1/3$ 得 $3/4$。')],
('A distant series coefficient can create a carry unless the full scaled tail is controlled.','若未控制完整放大尾和，远处系数也可能造成进位。'),
'2009-I-Q08 2026-II-Q07 2026-II-Q09',('NT08','PS02')))
ms.append(M(C,5,'Solve a linear recurrence through fixed points or characteristic roots','以不动点或特征根求解线性递推',[
(r'For $u_{n+1}=ru_n+c$, subtract its fixed point $L=c/(1-r)$ when $r\ne1$.',r'对 $u_{n+1}=ru_n+c$，当 $r\ne1$ 时减去不动点 $L=c/(1-r)$。'),
(r'For a second-order homogeneous recurrence, factor the characteristic quadratic and fit the initial conditions; verify the formula by induction.',r'二阶齐次递推可分解特征二次式并代初值；再用归纳验证公式。'),
(r'For large indices modulo a base, prove a return of the entire determining state before reducing the index.',r'求大下标的模值时，须证明整个决定状态返回，才能约化下标。'),
(r'For variable initial data, express the late term as a linear combination of those data and apply integer bounds to any collision.',r'初值可变时，将后项表示为初值的线性组合，再对重合表示施加整数界。')],
(r'Let $u_0=0,u_{n+1}=3u_n+2$. Find $u_n$.',r'设 $u_0=0,u_{n+1}=3u_n+2$，求 $u_n$。'),[
(r'The fixed point is $-1$. Put $v_n=u_n+1$.',r'不动点为 $-1$，令 $v_n=u_n+1$。'),
(r'Then $v_{n+1}=3v_n$ and $v_0=1$, so $v_n=3^n$.',r'则 $v_{n+1}=3v_n,v_0=1$，所以 $v_n=3^n$。'),
(r'Hence $u_n=3^n-1$, which satisfies both the initial value and recurrence.',r'故 $u_n=3^n-1$，它满足初值与递推。')],
('A repeated characteristic root needs a factor of n in the second independent solution.','特征根重复时，第二个独立解需要乘以 n。'),
'2001-II-Q03 2001-II-Q05 2002-I-Q08 2003-II-Q13 2006-II-Q11 2011-II-Q11 2018-II-Q02 2023-II-Q13',('AL02','NT04'),[
(r'Expanding a tridiagonal determinant with diagonal $a$ and off-diagonal $b$ gives $D_n=aD_{n-1}-b^2D_{n-2}$, with $D_0=1,D_1=a$. Derive the sign and the factor $b^2$ from the minor expansion before solving the recurrence.',r'对角元为 $a$、邻对角元为 $b$ 的三对角行列式展开得 $D_n=aD_{n-1}-b^2D_{n-2}$，初值 $D_0=1,D_1=a$。解递推前须从余子式展开推导负号与 $b^2$。'),
(r'For a nontriangle increasing sequence, $a_{j+2}\ge a_j+a_{j+1}$. The least permitted initial values and equality at every step give a sharp Fibonacci-type lower envelope; prove that envelope itself contains no nondegenerate triangle to establish sharpness.',r'不含三角形的递增数列满足 $a_{j+2}\ge a_j+a_{j+1}$。取最小允许初值并每步取等号，得到准确的 Fibonacci 型下包络；还须证明此包络本身不含非退化三角形，才能说明界准确。')]))
ms.append(M(C,6,'Reduce constant second differences to an arithmetic first difference','把常二阶差分化为等差一阶差分',[
(r'Put $d_n=u_n-u_{n-1}$ when a recurrence contains $u_{n+1}-2u_n+u_{n-1}$.',r'递推出现 $u_{n+1}-2u_n+u_{n-1}$ 时，令 $d_n=u_n-u_{n-1}$。'),
(r'The second-difference equation gives a simple first-difference law for $d_n$.',r'二阶差分方程转为 $d_n$ 的简单一阶差分关系。'),
(r'Sum the differences and use all initial or boundary values to fix the constants.',r'累加差量，并用全部初值或边界值确定常数。')],
(r'If $u_0=2,u_1=5$ and $u_{n+1}-2u_n+u_{n-1}=4$, find $u_n$.',r'若 $u_0=2,u_1=5$ 且 $u_{n+1}-2u_n+u_{n-1}=4$，求 $u_n$。'),[
(r'Let $d_n=u_n-u_{n-1}$. Then $d_1=3$ and $d_{n+1}=d_n+4$.',r'令 $d_n=u_n-u_{n-1}$，则 $d_1=3,d_{n+1}=d_n+4$。'),
(r'Thus $d_n=4n-1$. Sum from one through $n$.',r'所以 $d_n=4n-1$，从一累加到 $n$。'),
(r'$u_n=2+4n(n+1)/2-n=2n^2+n+2$.',r'$u_n=2+4n(n+1)/2-n=2n^2+n+2$。')],
('Boundary equations can differ from the interior recurrence and must be imposed separately.','边界方程可能不同于内部递推，须单独施加。'),
'2003-II-Q08 2016-I-Q13',('PS04',)))
ms.append(M(C,7,'Linearize nonlinear recurrences with ratios, adjacent products or invariants','用比值、相邻乘积或不变量线性化非线性递推',[
(r'Try $r_n=u_n/u_{n-1}$ or $p_n=u_nu_{n-1}$ when the recurrence contains neighboring products or quotients.',r'递推含相邻乘除时，尝试 $r_n=u_n/u_{n-1}$ 或 $p_n=u_nu_{n-1}$。'),
(r'Clear two successive equations and subtract to reveal a preserved expression if direct linearization is not visible.',r'若未直接出现线性关系，可清除连续两式分母后相减，找保持不变的表达式。'),
(r'Solve the transformed arithmetic or geometric recurrence and prove every division remains defined up to the required index.',r'解变换后的等差或等比递推，并证明到所需下标为止每次相除都有定义。'),
(r'Reconstruct the original quantity rather than assume the transformed relation automatically ensures every original condition.',r'重建原目标，不能假定变换后关系自动保证原全部条件。')],
(r'Positive terms satisfy $u_0=1,u_1=2$ and $u_{n+1}u_n=u_nu_{n-1}+2$. Find $u_{10}u_{11}$.',r'正项数列满足 $u_0=1,u_1=2,u_{n+1}u_n=u_nu_{n-1}+2$，求 $u_{10}u_{11}$。'),[
(r'Put $p_n=u_nu_{n-1}$ for $n\ge1$. Then $p_1=2$ and $p_{n+1}=p_n+2$.',r'令 $p_n=u_nu_{n-1}$，其中 $n\ge1$。则 $p_1=2,p_{n+1}=p_n+2$。'),
(r'So $p_n=2n$. Positivity holds inductively since $u_{n+1}=p_{n+1}/u_n>0$.',r'故 $p_n=2n$。因 $u_{n+1}=p_{n+1}/u_n>0$，正性可归纳保持。'),
(r'The desired adjacent product is $p_{11}=22$.',r'所求相邻乘积为 $p_{11}=22$。')],
('The transformed sequence may be simple even when the individual original terms are not.','即使原各项复杂，变换后的数列仍可能很简单。'),
'2005-II-Q11 2007-I-Q14 2008-II-Q06',('AL01',)))
ms.append(M(C,8,'Separate absorbing triggers from an invariant growth region','分开吸收触发与不变增长区域',[
(r'Identify local configurations that force a zero, a repeated term or another absorbing event.',r'找出会迫使零、重复项或其他吸收事件的局部构型。'),
(r'For all other configurations, propose a positive region with a quantitative lower growth or gap bound.',r'对其他构型，提出具有定量增长下界或间隔界的正区域。'),
(r'Prove the update preserves that region inductively, then count only the exceptional starting configurations.',r'归纳证明更新保持该区域，再只统计例外初始构型。')],
(r'Let $u_0=u_1=3$ and $u_{n+2}=u_{n+1}(u_n-1)$. Prove no term vanishes.',r'设 $u_0=u_1=3,u_{n+2}=u_{n+1}(u_n-1)$，证明没有一项为零。'),[
(r'The initial pair lies in the region $u_n,u_{n+1}\ge3$.',r'初始对位于 $u_n,u_{n+1}\ge3$ 区域。'),
(r'Within this region $u_{n+2}\ge2u_{n+1}\ge6$, so the next pair remains in the same region.',r'在该区域内，$u_{n+2}\ge2u_{n+1}\ge6$，故下一对仍位于同一区域。'),
(r'Induction proves every term is at least three, hence none is zero.',r'归纳得每项至少为三，因而没有零项。')],
('Observed growth for a few steps is insufficient; prove an invariant region.','观察几步增长还不够，须证明一个不变区域。'),
'2015-I-Q09',('LO03','CO04')))
ms.append(M(C,9,'Parametrize alternating arithmetic and geometric triples','参数化交替的等差与等比三元组',[
(r'For three geometric positive integers, reduce the ratio and write them as $ca^2,cab,cb^2$.',r'三个正整数成等比时，先约分公比，写成 $ca^2,cab,cb^2$。'),
(r'Use the adjacent arithmetic rule to extend the underlying linear factors by a fixed difference $d=b-a$.',r'用相邻等差规则，使底层线性因子按固定差 $d=b-a$ 延伸。'),
(r'Prove the squared-factor and adjacent-product formulas by induction, then apply integer square-divisor or size constraints.',r'归纳证明平方因子与相邻乘积公式，再使用整数平方约数或大小限制。')],
(r'For $t_j=a+jd$ with $a,d>0$, form $b_{2j+1}=t_j^2$ and $b_{2j+2}=t_jt_{j+1}$. Prove that odd-starting triples are geometric and even-starting triples are arithmetic.',r'对 $t_j=a+jd$，其中 $a,d>0$，作 $b_{2j+1}=t_j^2,b_{2j+2}=t_jt_{j+1}$。证明奇数下标起始三项等比，偶数起始三项等差。'),[
(r'The odd-starting triple is $t_j^2,t_jt_{j+1},t_{j+1}^2$, with common ratio $t_{j+1}/t_j$.',r'奇数起始三项为 $t_j^2,t_jt_{j+1},t_{j+1}^2$，公比为 $t_{j+1}/t_j$。'),
(r'The even-starting triple is $t_jt_{j+1},t_{j+1}^2,t_{j+1}t_{j+2}$. Its two differences are $dt_{j+1}$.',r'偶数起始三项为 $t_jt_{j+1},t_{j+1}^2,t_{j+1}t_{j+2}$，两差均为 $dt_{j+1}$。'),
(r'Positivity makes every ratio defined; $d>0$ also makes the constructed sequence strictly increasing.',r'正性使每个公比有定义，$d>0$ 还使构造的数列严格递增。')],
('A local triple identity needs an induction to describe the entire infinite sequence.','局部三项恒等式需要归纳才能描述整个无限数列。'),
'2003-I-Q08 2004-II-Q09 2009-I-Q01 2016-I-Q10 2016-II-Q09',('NT01','NT05'),[
(r'A single arithmetic-to-geometric transition can be modeled by $a,a+d,a+2d,a+L$, followed by $(a+d)(a+L)=(a+2d)^2$. This is distinct from an infinite alternating rule, but the same positivity and integral-candidate checks remain necessary.',r'仅一次等差到等比转换可写为 $a,a+d,a+2d,a+L$，再用 $(a+d)(a+L)=(a+2d)^2$。这不同于无限交替规则，但仍须正性与整数候选检查。')]))
ms.append(M(C,10,'Prove a rational recurrence period from the full ordered state','从完整有序状态证明有理递推的周期',[
(r'For a second-order recurrence the state is $(u_n,u_{n+1})$, not one term.',r'二阶递推的状态是 $(u_n,u_{n+1})$，而非单项。'),
(r'Compute enough iterates symbolically to return to that state, keeping denominators nonzero.',r'符号计算足够多迭代直到状态返回，并保持分母非零。'),
(r'Reduce the requested index by the proved period and evaluate only the remaining terms.',r'以已证明周期约化所求下标，只计算剩余项。')],
(r'For positive initial values $u_1=2,u_2=3$ and rule $u_{n+2}=1/u_n$, find the least period.',r'给定正初值 $u_1=2,u_2=3$，规则为 $u_{n+2}=1/u_n$，求最小周期。'),[
(r'The terms are $2,3,1/2,1/3,2,3,\ldots$.',r'各项为 $2,3,1/2,1/3,2,3,\ldots$。'),
(r'The ordered pair $(2,3)$ returns after four shifts. All terms are positive, so division is always defined.',r'有序对 $(2,3)$ 在四次移动后返回；各项为正，所以除法始终有定义。'),
(r'The first four terms are distinct, excluding periods one, two and three. The least period is four.',r'前四项互异，排除周期一、二、三，故最小周期为四。')],
('A repeated value may appear before the determining state returns.','决定状态返回之前，单个数值就可能已重复。'),
'2020-II-Q06',('AL09',),[
(r'For the positive Lyness rule $u_{n+2}=(1+u_{n+1})/u_n$, an initial pair $(a,b)$ is followed by $(b+1)/a,(a+b+1)/(ab),(a+1)/b,a,b$. This proves a period dividing five; an exact least-period claim needs a separate distinctness check.',r'对正项 Lyness 规则 $u_{n+2}=(1+u_{n+1})/u_n$，初始对 $(a,b)$ 后依次为 $(b+1)/a,(a+b+1)/(ab),(a+1)/b,a,b$。这证明周期整除五；若声称准确最小周期，还须另检互异性。')]))
ms.append(M(C,11,'Track valid preimages and sum their arithmetic progression','追踪有效原像并求其等差数列之和',[
(r'Under $z=|x-c|$, a target $z$ has preimages $c\pm z$ only when $z\ge0$.',r'在 $z=|x-c|$ 下，目标 $z$ 只有非负时才有原像 $c\pm z$。'),
(r'Filter invalid targets before taking preimages; then form the union and remove duplicates.',r'求原像前先筛掉无效目标，再取并集并去重。'),
(r'If the resulting zeros form an arithmetic progression, prove both endpoints, spacing and complete coverage before using its sum formula.',r'若所得零点为等差数列，须先证明端点、间距与无缺漏覆盖，再用求和公式。')],
(r'Find the sum of distinct real $x$ with $|x-2|\in\{-1,1,3\}$.',r'求满足 $|x-2|\in\{-1,1,3\}$ 的不同实数 $x$ 之和。'),[
(r'The negative target minus one has no preimage, so retain only one and three.',r'负目标负一无原像，只保留一与三。'),
(r'The preimages are $2\pm1$ and $2\pm3$, giving the set $\{-1,1,3,5\}$.',r'原像为 $2\pm1,2\pm3$，得到集合 $\{-1,1,3,5\}$。'),
(r'This four-term progression has mean two, so its sum is eight.',r'此四项等差数列的平均为二，所以和为八。')],
('Negative targets cannot pass through an absolute-value preimage step.','负目标不能通过绝对值原像步骤。'),
'2020-II-Q08',('AL06','AL09')))
ms[1]['question_ids'].remove('AIME-2009-I-Q01')
ms[1]['question_ids'].append('AIME-2019-I-Q01')
ms[0]['question_ids'].append('AIME-2008-I-Q06')
ms[0]['extensions_en'].append(r'Adjacent-sum triangular arrays preserve an arithmetic row. From top entries $a+jd$, after $r$ adjacent-sum steps the entry in position $j$ is $2^r[a+(j+r/2)d]$. The case $r=0$ is immediate; adding consecutive entries gives exactly the same formula with $r$ replaced by $r+1$, proving it by induction.')
ms[0]['extensions_zh'].append(r'相邻求和三角阵会保持每行等差。若顶行是 $a+jd$，经过 $r$ 次相邻求和后，第 $j$ 项为 $2^r[a+(j+r/2)d]$。$r=0$ 显然成立；将连续两项相加，恰得 $r$ 换为 $r+1$ 的同式，故归纳得证。')
save(C,('Look for a sum structure before calculating terms: arithmetic pairs, geometric blocks, a telescoping difference, or a simple transformed recurrence. Every closed formula needs its index convention, domain and initial values checked.','计算各项之前先找求和结构：等差配对、等比区块、望远镜差分，或简单变换后的递推。每个通项公式都须核对下标约定、定义域与初值。'),ms,('AL01','AL02'))

from knowledge_helpers_source import method as M,save
C='AL02';ms=[]
ms.append(M(C,1,'Recover symmetric root expressions directly from coefficients','直接由系数恢复对称根式',[
(r'Normalize the leading coefficient and identify the elementary sums $e_1,e_2,e_3$.',r'先归一首项系数，再识别基本对称和 $e_1,e_2,e_3$。'),
(r'Use $p_2=e_1^2-2e_2$ and $p_3=e_1p_2-e_2p_1+3e_3$, rather than solving roots individually.',r'使用 $p_2=e_1^2-2e_2,p_3=e_1p_2-e_2p_1+3e_3$，避免逐个解根。'),
(r'For two bases with sum $s$ and product $p$, their power sums satisfy $u_{n+2}=su_{n+1}-pu_n$.',r'两个底数的和为 $s$、积为 $p$ 时，其幂和满足 $u_{n+2}=su_{n+1}-pu_n$。'),
(r'Account explicitly for repeated copies of each root, and check real-root feasibility if the original variables are real.',r'明确处理每个根的重复副本；若原变量为实数，还须检查实根可行性。')],
(r'The roots of $x^3-2x^2-3x+1$ are $r,s,t$. Find $r^3+s^3+t^3$.',r'$x^3-2x^2-3x+1$ 的根为 $r,s,t$，求 $r^3+s^3+t^3$。'),[
(r'Vieta gives $e_1=2,e_2=-3,e_3=-1$.',r'韦达关系给出 $e_1=2,e_2=-3,e_3=-1$。'),
(r'The square sum is $p_2=2^2-2(-3)=10$.',r'平方和为 $p_2=2^2-2(-3)=10$。'),
(r'Thus $p_3=e_1p_2-e_2e_1+3e_3=20+6-3=23$.',r'故 $p_3=e_1p_2-e_2e_1+3e_3=20+6-3=23$。')],
('Vieta signs alternate; divide by the leading coefficient first.','韦达符号交替，须先除首项系数。'),
'2001-I-Q03 2002-I-Q06 2005-I-Q08 2008-II-Q07 2011-I-Q15 2015-II-Q06 2015-II-Q14 2019-I-Q08 2019-I-Q10 2021-II-Q07 2021-II-Q04 2026-I-Q06 2026-II-Q11',('AL01',),[
(r'If each root $z_i$ is repeated $k$ times, the sum is $k\sum z_i$, while the pair sum is $\binom{k}{2}\sum z_i^2+k^2\sum_{i<j}z_iz_j$. This counts same-root copies separately from different-root copies.',r'每个根 $z_i$ 重复 $k$ 次时，总和为 $k\sum z_i$，两两积和为 $\binom{k}{2}\sum z_i^2+k^2\sum_{i<j}z_iz_j$；须分开同根副本与异根副本。'),
(r'For square roots $s_1,s_2,s_3$, the product $(s_1+s_2+s_3)(-s_1+s_2+s_3)(s_1-s_2+s_3)(s_1+s_2-s_3)$ equals $4e_2-e_1^2$, where $e_i$ refer to $s_1^2,s_2^2,s_3^2$. A zero sign sum therefore imposes a symmetric coefficient relation. Still check that other sign sums do not collide.',r'对平方根 $s_1,s_2,s_3$，乘积 $(s_1+s_2+s_3)(-s_1+s_2+s_3)(s_1-s_2+s_3)(s_1+s_2-s_3)$ 等于 $4e_2-e_1^2$，其中 $e_i$ 是 $s_1^2,s_2^2,s_3^2$ 的基本对称式。零符号和因此给出系数关系，但仍须检查其他符号和是否重合。')]))
ms.append(M(C,2,'Reduce a polynomial at roots and interchange root products','在根处约化多项式并交换根乘积',[
(r'Divide $A(x)$ by the polynomial $Q(x)$ defining the roots: at each root only the remainder matters.',r'以定义根的多项式 $Q(x)$ 除 $A(x)$；在每个根处只需保留余式。'),
(r'For a sum, use Vieta or power-sum identities on the lower-degree remainder.',r'求和时，对较低次余式使用韦达或幂和恒等式。'),
(r'For a product, factor one polynomial and interchange the two root products, carefully tracking degree-dependent signs and leading coefficients.',r'求积时，分解一个多项式并交换两组根的乘积，仔细追踪次数决定的符号与首项系数。')],
(r'If $r,s$ are the roots of $x^2-x-1$, find $r^4+s^4$ and $(r-2)(s-2)$.',r'若 $r,s$ 是 $x^2-x-1$ 的根，求 $r^4+s^4$ 与 $(r-2)(s-2)$。'),[
(r'At either root $x^2=x+1$, so $x^4=3x+2$. Hence $r^4+s^4=3(r+s)+4=7$.',r'根处 $x^2=x+1$，故 $x^4=3x+2$，从而 $r^4+s^4=3(r+s)+4=7$。'),
(r'The monic factorization is $Q(x)=(x-r)(x-s)$.',r'首一因式分解为 $Q(x)=(x-r)(x-s)$。'),
(r'Thus $(r-2)(s-2)=Q(2)=1$, since two sign reversals cancel.',r'所以 $(r-2)(s-2)=Q(2)=1$，两次反号相消。')],
('At roots of Q, equality modulo Q is exact equality of values.','在 Q 的根处，模 Q 相等就是函数值精确相等。'),
'2003-II-Q09 2023-II-Q08 2024-II-Q13',('AL03',)))
ms.append(M(C,3,'Recognize hidden powers, telescoping products and convolutions','识别隐藏幂、望远镜乘积与卷积',[
(r'Compare coefficients with $(x-h)^k$, a geometric sum, or a product of two short coefficient lists.',r'将系数与 $(x-h)^k$、等比和或两个短系数表的乘积比较。'),
(r'Use difference-of-squares or difference-of-cubes identities to telescope products or rationalize a radical.',r'用平方差或立方差恒等式使乘积望远镜消去，或对根式有理化。'),
(r'If a multiplier such as $x-1$ is introduced, record its zeros and remove only the roots actually introduced by it.',r'若引入 $x-1$ 等乘子，记录其零点，并只删除由该乘子真正引入的根。'),
(r'After factoring, check which factors can vanish on the requested real or complex domain.',r'分解后，检查哪些因子能在所求实数或复数定义域内为零。')],
(r'Find a polynomial $R$ with $R(0)=1$ such that $R(x)^2=1+2x+3x^2+2x^3+x^4$, and prove uniqueness.',r'求满足 $R(0)=1$ 且 $R(x)^2=1+2x+3x^2+2x^3+x^4$ 的多项式 $R$，并证明唯一性。'),[
(r'Degree comparison forces $R=1+ux+vx^2$. The coefficient of $x$ in its square is $2u$, so $u=1$.',r'比较次数得 $R=1+ux+vx^2$；平方的 $x$ 系数为 $2u$，故 $u=1$。'),
(r'The $x^2$ coefficient is $u^2+2v=3$, so $v=1$.',r'$x^2$ 系数为 $u^2+2v=3$，故 $v=1$。'),
(r'The candidate $R=1+x+x^2$ also gives the required $x^3,x^4$ coefficients. Both unknown coefficients were forced, proving uniqueness.',r'候选 $R=1+x+x^2$ 也给出所需的 $x^3,x^4$ 系数；两个未知系数均被迫确定，故唯一。')],
('Convolution explains a triangular coefficient pattern; inspection alone does not establish multiplicities.','卷积解释三角形系数模式；单凭观察不能确定根的重数。'),
'2000-II-Q13 2003-II-Q15 2004-I-Q13 2005-I-Q06 2005-II-Q07 2006-I-Q12 2013-I-Q05 2014-I-Q09 2019-I-Q12 2024-II-Q11',('AL03','AL05')))
ms.append(M(C,4,'Partition preimages and common roots before matching coefficients','比较系数前先划分原像与公共根',[
(r'A degree-$d$ polynomial has at most $d$ distinct roots unless it is zero.',r'非零 $d$ 次多项式至多有 $d$ 个不同根。'),
(r'For a composition or several level values, partition the inputs according to which target root or level they map to.',r'对复合式或多个水平值，按输入映到哪个目标根或水平值来分组。'),
(r'Apply Vieta within each group and compare coefficients that the defining polynomials share.',r'在每组内使用韦达，并比较定义多项式共有的系数。'),
(r'For shared factors, use the degree of the least common multiple, subtract equations to isolate the common root, and verify existence.',r'对公共因子，利用最小公倍多项式的次数，相减方程隔离公共根，并验证存在性。')],
(r'Two monic quadratics differ by a nonzero constant. Can they share a root? Can their two root sums differ?',r'两个首一二次多项式相差非零常数，它们能有公共根吗？两组根和能不同吗？'),[
(r'At a common root their difference would be zero, contradicting the nonzero constant. Hence no root is shared.',r'若有公共根，在该根处两式之差为零，与非零常数矛盾，所以不能共根。'),
(r'The linear coefficients are equal because only the constant changes.',r'因只改变常数项，两式的一次系数相同。'),
(r'Vieta therefore gives equal root sums, even though the two root sets are disjoint.',r'故韦达给出相同根和，尽管两组根集不相交。')],
('Root multiplicity, distinctness and grouping are three separate pieces of information.','重数、互异性与分组是三条不同信息。'),
'2007-I-Q08 2014-II-Q05 2015-I-Q10 2020-I-Q11 2020-I-Q14 2020-II-Q11',('AL01','LO03')))
ms.append(M(C,5,'Lower the degree before interpolation or coefficient elimination','插值或系数消元前先降低次数',[
(r'Add or subtract polynomials whose leading terms cancel; determine the actual remaining degree.',r'将首项可消去的多项式相加或相减，并确定剩余实际次数。'),
(r'A degree bound plus enough values can determine a polynomial; use a root-count argument to prove uniqueness.',r'次数界加足够多函数值可确定多项式；以根数论证证明唯一性。'),
(r'For multivariable polynomials, write the coefficient basis and solve the linear vanishing conditions before seeking universal zeros.',r'多变量多项式先写系数基，并解线性消零条件，再求全体多项式共有的零点。')],
(r'A polynomial $P$ of degree at most three agrees with $x^2$ at $x=0,1,2,3$. Find $P(10)$.',r'次数至多为三的多项式 $P$ 在 $x=0,1,2,3$ 处与 $x^2$ 相等，求 $P(10)$。'),[
(r'Form $R(x)=P(x)-x^2$, whose degree is at most three.',r'作 $R(x)=P(x)-x^2$，其次数至多为三。'),
(r'The four distinct given inputs are roots of $R$. A nonzero polynomial of degree at most three cannot have four roots.',r'四个不同输入均为 $R$ 的根，非零的至多三次多项式不可能有四个不同根。'),
(r'Therefore $R$ is identically zero and $P(10)=10^2=100$.',r'故 $R$ 恒为零，$P(10)=10^2=100$。')],
('A canceled leading term changes the degree used in Vieta as well as interpolation.','首项消去既改变插值次数，也改变韦达所使用的次数。'),
'2001-I-Q03 2003-II-Q08 2008-I-Q13 2022-I-Q01',('AL01',)))
ms.append(M(C,6,'Use integer roots and coefficient bounds as a finite algebraic count','用整数根与系数界作有限代数计数',[
(r'For a monic integer polynomial, rational roots are integers. Factorization into monic rational factors preserves integrality of their coefficients by Gauss\'s lemma.',r'首一整系数多项式的有理根为整数；由高斯引理，其首一有理因子也具有整系数。'),
(r'Convert root sums and products into integer factor pairs or bounded root parameters.',r'把根和与根积转成整数因子对或有界根参数。'),
(r'When counting exactly one distinct integer solution, distinguish a repeated root from a second root coinciding with an already excluded input.',r'恰数一个不同整数解时，区分重根与第二个根恰等于已排除输入。'),
(r'Divide by root permutations only after treating repeated roots; include any unrestricted coefficients as independent factors.',r'处理重根后才能除以根的排列数；无约束系数作为独立因子计入。')],
(r'Count monic quadratics with nonnegative integer roots and constant term $12$.',r'统计根均为非负整数、常数项为 $12$ 的首一二次多项式。'),[
(r'Write $(x-r)(x-s)$ with $rs=12$ and $0\le r\le s$.',r'写为 $(x-r)(x-s)$，其中 $rs=12,0\le r\le s$。'),
(r'The unordered positive factor pairs are $(1,12),(2,6),(3,4)$. Zero cannot occur because the product is positive.',r'无序正因子对为 $(1,12),(2,6),(3,4)$；积为正，所以零不能出现。'),
(r'They give three distinct sums $13,8,7$, hence three distinct polynomials.',r'三对给出不同根和 $13,8,7$，所以有三个不同多项式。')],
('Counting root lists is not automatically the same as counting polynomials.','统计根列表并不自动等于统计多项式。'),
'2005-II-Q13 2010-II-Q06 2010-II-Q10 2013-I-Q10 2013-II-Q12 2014-I-Q06 2018-I-Q01 2023-I-Q09',('NT01','NT05','CO07')))
ms.append(M(C,7,'Use nonnegativity, discriminants and repeated roots at extrema','用非负性、判别式与最值重根',[
(r'A real polynomial nonnegative on an open interval has even multiplicity at each interior zero.',r'实多项式在开区间非负，则每个内部零点的重数为偶数。'),
(r'For a quadratic, use discriminant and sign conditions; for two equal global minima, factor the shifted polynomial by both double roots.',r'二次式用判别式与符号条件；若有两个相等全局最小值，则将平移后的多项式按两个二重根分解。'),
(r'Compare coefficients to derive parameter conditions, then prove the roots are distinct, inside the domain and attain the claimed bound.',r'比较系数得到参数条件，再证明根互异、位于定义域内并达到所求界。'),
(r'For constrained positive roots, establish compactness first and inspect repeated-root boundary configurations.',r'受约束正根的最值，先建立紧致性，再检查重根边界构型。')],
(r'A real quadratic $Q$ satisfies $Q(x)\ge x^2$ for every real $x$ and $Q(2)=4$. Show the form of $Q$.',r'实二次式 $Q$ 对每个实数 $x$ 满足 $Q(x)\ge x^2$，且 $Q(2)=4$，求 $Q$ 的形式。'),[
(r'The polynomial $D(x)=Q(x)-x^2$ is nonnegative and vanishes at two.',r'多项式 $D(x)=Q(x)-x^2$ 非负，且在二处为零。'),
(r'A nonzero linear term at that zero would change sign across it. Thus the zero has even multiplicity, or $D$ is identically zero.',r'若零点只有非零一次项，越过它就会变号，所以零点重数须为偶数，或 $D$ 恒为零。'),
(r'Therefore $Q(x)=x^2+c(x-2)^2$ with $c\ge0$, including $c=0$. Every such polynomial satisfies the requirements.',r'因此 $Q(x)=x^2+c(x-2)^2$，其中 $c\ge0$，包括 $c=0$；每个这种多项式都满足要求。')],
('Repeated-root conditions are necessary at an interior extremum; verify sufficiency and endpoint alternatives.','内部最值的重根条件是必要条件，仍须检验充分性与端点情形。'),
'2005-II-Q15 2010-I-Q06 2014-I-Q14 2018-II-Q06 2021-I-Q15 2024-I-Q15 2025-I-Q11 2025-II-Q15 2026-II-Q08',('AL07','AL06'),[
(r'For positive $a,b,c$ with fixed pair sum and product, an extremum of $a+b+c$ occurs with two variables equal: if the three were distinct positive roots of $t^3-st^2+qt-r$, small changes of $s$ would retain three distinct positive roots by continuity, contradicting an extremum. This argument applies only after compactness and positivity exclude escape to the boundary.',r'正数 $a,b,c$ 的两两积和与积固定时，$a+b+c$ 的最值至少有两个变量相等：若三者为 $t^3-st^2+qt-r$ 的三个不同正根，连续性使 $s$ 小幅变化后仍保留三个不同正根，与最值矛盾。但此前必须以紧致性及正性排除逃向边界。'),
(r'To prove four real roots of a quartic, find four disjoint sign-change intervals, counting any boundary root by its nonzero derivative. To prove there are fewer, combine a positive region with the number of derivative zeros on the remaining region.',r'证明四次式有四个实根，可找四个不相交变号区间；若根落在区间边界，可用非零导数判断变号。证明不足四根，则可把恒正区域与其余区域的导数零点数结合。')]))
ms.append(M(C,8,'Exploit polynomial identities through forced roots and finite root orbits','用被迫根与有限根轨道处理多项式恒等式',[
(r'Compare degrees and leading coefficients before substituting special inputs.',r'代入特殊值之前，先比较次数与首项系数。'),
(r'Use zeros of multipliers to force specific polynomial roots, then factor them out as a polynomial identity.',r'利用乘子零点强迫特定根，再按多项式恒等式将其提出。'),
(r'If a root is mapped to another root, analyze its finite orbit; a modulus that grows without bound contradicts a finite root set.',r'若根被映为另一个根，分析其有限轨道；模长无限增长将与有限根集矛盾。'),
(r'A polynomial with a nonzero real period is constant, since its finite difference otherwise has degree one less with nonzero leading coefficient.',r'具有非零实周期的多项式必为常数，否则有限差分将具有低一次的次数与非零首项系数。')],
(r'If a nonzero polynomial has every root on or inside the unit circle and constant term equal in modulus to its leading coefficient, prove every root has modulus one.',r'若非零多项式的全部根位于单位圆内或圆上，且常数项与首项系数模长相等，证明所有根的模长均为一。'),[
(r'By Vieta, the product of all root moduli is the modulus of the constant-to-leading coefficient ratio, namely one.',r'由韦达，所有根模长之积为常数项与首项系数比的模长，即一。'),
(r'Every factor is at most one. If any were strictly below one, the product would be strictly below one.',r'每个因子均不超过一；若某个严格小于一，乘积就会严格小于一。'),
(r'Hence all moduli equal one. In particular no root is zero.',r'故所有模长均为一，特别地不存在零根。')],
('A root-map argument must show the map remains in the same finite root set.','根映射论证须证明映射始终留在同一有限根集中。'),
'2007-II-Q14 2016-I-Q11',('AL03','AL09')))
ms.append(M(C,9,'Extract coefficients through evaluations and symmetric selections','通过代值与对称选取提取系数',[
(r'The coefficient of $x^k$ in a product is the sum of all selections whose degrees total $k$.',r'乘积中 $x^k$ 系数等于全部所选项次数合计为 $k$ 的选取之和。'),
(r'For pair selections use $\sum_{i<j}u_iu_j=[(\sum u_i)^2-\sum u_i^2]/2$.',r'两两选取可用 $\sum_{i<j}u_iu_j=[(\sum u_i)^2-\sum u_i^2]/2$。'),
(r'An evaluation at one sums coefficients. To sum absolute coefficients, first prove a substitution makes all coefficients nonnegative.',r'代入一可求系数和；若求绝对值和，须先证明某个代换使所有系数非负。')],
(r'Find the sum of the absolute coefficients of $(1-x)^3(1+x^2)$.',r'求 $(1-x)^3(1+x^2)$ 的系数绝对值之和。'),[
(r'Replacing $x$ by $-x$ gives $(1+x)^3(1+x^2)$, whose coefficients are all nonnegative.',r'以 $-x$ 替换 $x$ 得 $(1+x)^3(1+x^2)$，各系数均非负。'),
(r'The replacement multiplies the degree-$j$ coefficient by $(-1)^j$, so these nonnegative coefficients are the original absolute coefficients.',r'该替换把 $j$ 次系数乘 $(-1)^j$，故这些非负系数恰为原系数绝对值。'),
(r'Evaluate at one: the required sum is $2^3\cdot2=16$.',r'代入一，所求和为 $2^3\cdot2=16$。')],
('Evaluating at minus one gives an absolute sum only after a coefficient-sign proof.','只有证明系数符号规律后，代入负一才给出绝对值和。'),
'2004-I-Q07 2016-II-Q06',('CO02',)))
ms[0]['question_ids']+=['AIME-2010-II-Q07','AIME-2002-II-Q15']
ms[2]['question_ids']+=['AIME-2023-II-Q04','AIME-2002-II-Q11','AIME-2015-I-Q03']
save(C,('A polynomial is a structured object: coefficients encode root symmetries, factorization controls multiplicity, and a degree bound makes identities rigid. Reduce the expression before solving roots, and restore all real-domain restrictions afterward.','多项式具有结构：系数编码根的对称性，因式分解控制重数，次数界使恒等式具有刚性。先约化表达式，再求根，最后恢复全部实数定义域限制。'),ms,('AL01',))

from knowledge_helpers_source import method as M,save
C='NT03';ms=[]
ms.append(M(C,1,'Solve a linear congruence and count its bounded representatives','解线性同余并统计有界代表元',[
(r'Write the condition as $ax\equiv b\pmod m$. Let $g=\gcd(a,m)$; solvability requires $g\mid b$.',r'写成 $ax\equiv b\pmod m$。设 $g=\gcd(a,m)$；可解须 $g\mid b$。'),
(r'Divide the entire congruence by $g$, including the modulus, then invert the now coprime coefficient.',r'将同余式整体除以 $g$，包括模数，再对已互质的系数求逆。'),
(r'Write $x=r+kt$ for the resulting modulus $t$ and convert the original interval into exact integer bounds on $k$.',r'对所得模数 $t$ 写 $x=r+kt$，把原区间转为 $k$ 的精确整数界。')],
(r'How many integers $1\le x\le80$ satisfy $6x\equiv9\pmod{15}$?',r'满足 $6x\equiv9\pmod{15}$ 的整数 $1\le x\le80$ 有多少个？'),[
(r'Divide by $3$: $2x\equiv3\pmod5$.',r'整体除以 $3$，得 $2x\equiv3\pmod5$。'),
(r'The inverse of $2$ is $3$ modulo $5$, so $x\equiv4\pmod5$.',r'模 $5$ 下 $2$ 的逆元为 $3$，故 $x\equiv4\pmod5$。'),
(r'The values are $4,9,\ldots,79$, numbering $16$.',r'数值为 $4,9,\ldots,79$，共 $16$ 个。')],
('Canceling a nonunit coefficient changes the modulus.','约去非单位系数时，模数也必须改变。'),
'2001-I-Q11 2007-I-Q04 2008-I-Q06 2009-I-Q11 2011-II-Q03 2012-I-Q04 2012-II-Q01 2013-I-Q15 2018-I-Q10 2022-I-Q04 2026-II-Q03',('NT02',),[
(r'To prove a modular motion criterion sufficient, track the state inside a fixed representative interval, or construct moves generating every allowed lattice point. A congruence invariant gives only necessity until such a construction is supplied.',r'证明模运动判据充分时，须把状态限制在固定代表区间中追踪，或构造能生成每个允许格点的动作。未给构造之前，同余不变量只提供必要性。')]))
ms.append(M(C,2,'Reduce a polynomial remainder and preserve noninvertible information','化简多项式余数并保留不可逆信息',[
(r'Reduce every power or coefficient modulo the proposed divisor before expanding a large expression.',r'在展开大式之前，先对预定除数化简每个幂或系数。'),
(r'For a variable divisor $n+c$, substitute $n\equiv-c$. Clear denominators only when their invertibility is known.',r'可变除数 $n+c$ 下代入 $n\equiv-c$；清分母时须核对可逆性。'),
(r'If multiplication by a denominator produced only a necessary condition, test each surviving candidate in the original expression.',r'若乘分母后只得到必要条件，须把每个存活候选代回原式。')],
(r'Find positive $n$ for which the remainder of $n(n+1)/2$ modulo $n+2$ is $1$.',r'求正整数 $n$，使 $n(n+1)/2$ 除以 $n+2$ 余 $1$。'),[
(r'Put $d=n+2$. Since $n(n+1)\equiv2\pmod d$, twice the desired congruence holds for every $d$. It does not by itself prove the original congruence.',r'令 $d=n+2$。因 $n(n+1)\equiv2\pmod d$，目标同余的两倍对所有 $d$ 都成立，但这不足以证明原同余。'),
(r'Compute exactly: $n(n+1)/2-1=d(d-3)/2$. This is divisible by $d$ exactly when $d-3$ is even.',r'精确计算得 $n(n+1)/2-1=d(d-3)/2$；它被 $d$ 整除当且仅当 $d-3$ 为偶数。'),
(r'Hence $d$ and $n$ are odd. Every positive odd $n$ works, including $n=1$.',r'因此 $d,n$ 均为奇数；每个正奇数 $n$ 都满足，包括 $n=1$。')],
('A multiplied congruence may lose information when the multiplier is not coprime to the modulus.','乘数不与模数互质时，放大后的同余可能丢失信息。'),
'2010-I-Q02 2017-I-Q02 2017-II-Q08 2020-II-Q10 2025-II-Q02',('NT01',)))
ms.append(M(C,3,'Split a composite modulus into prime powers and recombine','把合数模拆为质数幂再合并',[
(r'Factor the modulus into pairwise coprime prime powers.',r'把模数分成两两互质的质数幂。'),
(r'Solve each local condition. If $p^e\mid uv$ with $p\nmid\gcd(u,v)$, the whole power must divide one factor.',r'分别求解局部条件。若 $p^e\mid uv$ 且 $p\nmid\gcd(u,v)$，整块幂须归于一个因子。'),
(r'Combine every compatible local choice by the Chinese remainder theorem, then apply the original range and leading-digit restrictions.',r'以中国剩余定理合并每组相容局部选择，再施加原范围与首位限制。'),
(r'For counting, count complete periods and handle the final partial block explicitly.',r'计数时先统计完整周期，再明确处理最后不完整区块。')],
(r'Find every residue $x\pmod{40}$ satisfying $x^2=x$.',r'求满足 $x^2=x$ 的全部模 $40$ 剩余类。'),[
(r'Factor $40=8\cdot5$. Consecutive factors $x,x-1$ are coprime, so $x$ is $0$ or $1$ modulo each of $8,5$.',r'分解 $40=8\cdot5$。连续因子 $x,x-1$ 互质，故 $x$ 模 $8,5$ 分别只能为 $0$ 或 $1$。'),
(r'The local choices $(0,0),(1,1),(0,1),(1,0)$ give residues $0,1,16,25$ modulo $40$.',r'局部选择 $(0,0),(1,1),(0,1),(1,0)$ 分别给出模 $40$ 的 $0,1,16,25$。'),
(r'All four square to themselves modulo $40$, and CRT proves no other residues exist.',r'四者平方均模 $40$ 等于自身，且中国剩余定理证明无其他解。')],
('Allocate prime powers, not merely individual primes, to coprime factors.','互质因子间应分配整块质数幂，不能只分配单个质数。'),
'2002-II-Q07 2008-II-Q08 2011-II-Q14 2012-I-Q10 2012-II-Q12 2013-I-Q11 2014-I-Q08 2016-II-Q11 2017-I-Q09 2022-II-Q08 2022-II-Q13 2023-I-Q07 2024-II-Q14',('NT01','NT02'),[
(r'When a polynomial coefficient is a nonnegative solution count, congruences modulo complementary primes can force offsets in every variable. Substitute those offsets first; a common residual coefficient may then reduce the count to stars and bars (CO03).',r'若多项式系数转化为非负整数解计数，按互补质数取模可强制各变量的偏移。先代入偏移，剩余公共系数可能使计数化为隔板法（CO03）。')]))
ms.append(M(C,4,'Filter bounded arithmetic and geometry by small residues','用小模数筛选有界算术与几何条件',[
(r'Choose a modulus for which powers, digits, parity or angles have few possible residues.',r'选使幂、数位、奇偶或角度只出现少数剩余的模数。'),
(r'Tabulate the possibilities and translate them into restrictions on the original variables.',r'列出可能剩余，并转为原变量限制。'),
(r'Use the size bounds to shorten the surviving list; then check both the arithmetic and the geometric feasibility.',r'用大小界缩短候选表，再同时检查算术与几何可实现性。')],
(r'Can a triangle with integer sides have side squares summing to a number congruent to $7$ modulo $8$?',r'整数边长三角形的三边平方和能否模 $8$ 余 $7$？'),[
(r'A square is $0,1,$ or $4$ modulo $8$.',r'平方数模 $8$ 只能为 $0,1,4$。'),
(r'Three such residues cannot sum to $7$: with zero, one, two or three odd squares the sums have residues among $0,1,2,3,4,5,6$.',r'三个这样的剩余无法和为 $7$：按奇平方数的个数分类，所得剩余只在 $0,1,2,3,4,5,6$ 中。'),
(r'There are no such integer side lengths even before the triangle inequality is considered.',r'尚未考虑三角不等式，就已排除所有这样的整数边长。')],
('A residue obstruction proves impossibility; a permitted residue does not prove existence.','剩余障碍能证明不可能；允许的剩余却不能单独证明存在。'),
'2001-I-Q10 2003-II-Q02 2004-I-Q01 2005-II-Q09 2008-II-Q15 2012-I-Q01 2012-I-Q15 2013-I-Q02 2014-II-Q04 2015-II-Q03 2016-I-Q12 2016-I-Q14 2016-II-Q09 2022-I-Q02 2022-II-Q05 2024-II-Q07',('NT06',)))
ms.append(M(C,5,'Separate floor and rounding blocks from their residue corrections','把取整与舍入区块和剩余修正分开',[
(r'Write $\lfloor A/m\rfloor=(A-r)/m$ with $r$ the least nonnegative residue.',r'写 $\lfloor A/m\rfloor=(A-r)/m$，其中 $r$ 为最小非负剩余。'),
(r'Sum the smooth part first and tabulate residue corrections over a full period.',r'先求无取整部分之和，再按完整周期列出剩余修正。'),
(r'For uniqueness or maximum remainders, identify the exact integer interval on which a quotient tuple stays constant.',r'对唯一性或最大余数问题，找出商元组保持不变的精确整数区间。'),
(r'Include boundary jumps and compare against integers outside the requested counting range when uniqueness is global.',r'计入边界跳变；若唯一性是全局性质，还须与所统计范围外的整数比较。')],
(r'Calculate $\sum_{n=1}^{12}\lfloor n^2/3\rfloor$.',r'计算 $\sum_{n=1}^{12}\lfloor n^2/3\rfloor$。'),[
(r'The square residue modulo $3$ is zero for multiples of $3$ and one otherwise.',r'平方模 $3$ 在 $3$ 的倍数处为零，其余为一。'),
(r'There are eight nonmultiples of $3$ in the range, while $\sum n^2=650$.',r'范围内有八个非 $3$ 的倍数，而 $\sum n^2=650$。'),
(r'Thus the floor sum is $(650-8)/3=214$.',r'所以取整和为 $(650-8)/3=214$。')],
('Strict and weak interval endpoints can change an entire residue class.','区间端点的严格或非严格形式可能改变整个剩余类。'),
'2007-I-Q05 2013-II-Q14 2015-I-Q14 2022-II-Q08 2023-I-Q10',('AL06',),[
(r'The remainder $n\bmod k$ is bounded by both $k-1$ and $n-qk$ once a quotient lower bound $q$ is known. Compare these intersecting bounds near their crossing, then handle exact-divisibility exceptions separately.',r'若已知商至少为 $q$，余数 $n\bmod k$ 同时不超过 $k-1$ 与 $n-qk$。在两个界的交会附近比较，并单独处理恰好整除的例外。')]))
ms.append(M(C,6,'Reduce a counting problem to residue patterns','将计数问题化为剩余模式',[
(r'Replace each label by its residue, retaining how many original labels realize each class.',r'以剩余替换标签，并保留每类原标签的数量。'),
(r'Use cyclic symmetry, subtraction of adjacent equations, or a reduced polynomial to find all permitted residue patterns.',r'用循环对称、相邻方程相减或约化多项式求全部允许剩余模式。'),
(r'Count the residue patterns first, then restore within-class label permutations and remove symmetry exactly once.',r'先数剩余模式，再恢复类内标签排列，且只消除一次对称。'),
(r'For a coefficient sum in residue classes, work modulo both the prime and $x^m-1$; explain why the reduced coefficient has the intended meaning.',r'对按指数剩余类分组的系数和，同时模质数与 $x^m-1$ 运算，并说明约化系数的含义。')],
(r'How many subsets of $\{1,2,3,4\}$ have sum divisible by $3$?',r'$\{1,2,3,4\}$ 中有多少子集的元素和可被 $3$ 整除？'),[
(r'The element $3$ may be included or excluded freely. For $\{1,2,4\}$ the residue polynomial is $(1+x)^2(1+x^2)$.',r'元素 $3$ 可自由选或不选。对 $\{1,2,4\}$，剩余生成式为 $(1+x)^2(1+x^2)$。'),
(r'Expand and reduce using $x^3=1$: $1+2x+2x^2+2x^3+x^4=3+3x+2x^2$.',r'展开并用 $x^3=1$ 约化：$1+2x+2x^2+2x^3+x^4=3+3x+2x^2$。'),
(r'The constant coefficient is $3$; the free choice of $3$ doubles it to $6$.',r'常数系数为 $3$，元素 $3$ 的自由选择使其加倍为 $6$。')],
('Residue classes may have different multiplicities; restore the actual labels after the residue count.','剩余类的重数未必相同；统计模式后须恢复实际标签。'),
'2007-II-Q13 2011-I-Q05 2011-I-Q07 2018-I-Q12 2021-II-Q03 2023-II-Q10 2025-I-Q05 2026-I-Q08 2026-I-Q13 2026-II-Q15',('CO02','CO06'),[
(r'Over a prime field, $\binom pj\equiv0\pmod p$ for $0<j<p$, so $(1+x)^p=1+x^p$. In a quotient with $x^{p-1}=1$, this becomes $1+x$. Reducing a large exponent by this identity is valid as a polynomial identity in that quotient; it does not assert equality of unreduced integer coefficients.',r'在质数域中，$0<j<p$ 时 $\binom pj\equiv0\pmod p$，故 $(1+x)^p=1+x^p$。若再模 $x^{p-1}-1$，它变为 $1+x$。以此约化大指数是在商环中的多项式恒等式，并非未约化整数系数相等。'),
(r'The seven triples $\{i,i+1,i+3\}$ modulo seven form the Fano-plane lines: every pair occurs in exactly one triple. To use this incidence structure, classify zero positions first, then count the sign products on lines avoiding them. CO06 supplies the incidence and small-graph enumeration; modular reduction alone does not finish that count.',r'模七的七个三元组 $\{i,i+1,i+3\}$ 构成 Fano 平面直线，每一对点恰在一个三元组中。使用此关联结构时，先按零位置分类，再统计避开零点的直线上符号乘积。CO06 提供关联与小图枚举；仅有模约化并未完成该计数。'),
(r'A necessary condition modulo $m-1$ for a sum of powers can become sufficient by repeatedly replacing one $m^j$ by $m$ copies of $m^{j-1}$; each split adds exactly $m-1$ summands. Construct the required number of splits explicitly.',r'幂和模 $m-1$ 的必要条件，可通过反复把一个 $m^j$ 拆为 $m$ 个 $m^{j-1}$ 证明充分；每次拆分使项数恰增加 $m-1$。须明确构造所需拆分次数。')]))
ms.append(M(C,7,'Combine power cycles with local lifting and CRT','结合模幂周期、局部提升与中国剩余定理',[
(r'Handle nonunits modulo a prime power separately from invertible bases.',r'把质数幂模下不可逆的底数与可逆底数分别处理。'),
(r'Use the multiplicative order or a proved exponent cycle to reduce exponents, not the modulus itself.',r'用乘法阶或已证明的指数周期约化指数，不能直接用模数约化。'),
(r'For a root modulo $p$, expand $f(a+pt)$ modulo $p^2$ and solve $f(a)/p+f\prime(a)t\equiv0\pmod p$.',r'对模 $p$ 的根，模 $p^2$ 展开 $f(a+pt)$，求解 $f(a)/p+f\prime(a)t\equiv0\pmod p$。'),
(r'Recombine the resulting residues, and prove the least representative or least exponent really is minimal.',r'合并所得剩余，并证明最小代表元或最小指数确为最小。')],
(r'Lift the root $x\equiv2\pmod7$ of $x^2-4$ to a root modulo $49$.',r'将 $x^2-4$ 的模 $7$ 根 $x\equiv2\pmod7$ 提升为模 $49$ 的根。'),[
(r'Write $x=2+7t$. Then $x^2-4\equiv28t\pmod{49}$.',r'写 $x=2+7t$，则 $x^2-4\equiv28t\pmod{49}$。'),
(r'Division by $7$ gives $4t\equiv0\pmod7$, so $t\equiv0\pmod7$.',r'除以 $7$ 得 $4t\equiv0\pmod7$，故 $t\equiv0\pmod7$。'),
(r'The unique lift in this residue class is $x\equiv2\pmod{49}$. The other root $-2$ belongs to a different initial class.',r'该初始剩余类中唯一提升为 $x\equiv2\pmod{49}$；另一根 $-2$ 属于不同初始类。')],
('Unique lifting requires a nonzero derivative modulo p; otherwise there may be zero, one or many lifts.','唯一提升要求导数模 p 不为零，否则可能无提升、唯一提升或有多个提升。'),
'2001-II-Q14 2009-I-Q07 2011-I-Q11 2017-I-Q14 2018-I-Q06 2018-I-Q11 2019-I-Q14 2019-II-Q10 2021-II-Q13 2023-II-Q15 2024-I-Q13 2025-II-Q13',('NT04','AL02')))
ms.append(M(C,8,'Use least representable amounts in each residue class','使用各剩余类的最小可表示金额',[
(r'Fix a denomination $m$ and find the least representable amount $M_r$ in every residue class modulo $m$.',r'固定面额 $m$，求模 $m$ 每个剩余类中的最小可表示金额 $M_r$。'),
(r'Adding $m$ represents every larger amount in that class. Its largest missing amount is therefore $M_r-m$.',r'不断加 $m$ 可表示该类所有更大金额，故该类最大缺失金额为 $M_r-m$。'),
(r'Prove each proposed minimum by considering all smaller counts of the other denominations, then take the maximum over residues.',r'考虑其他面额的所有较少张数，证明所列最小值，再对剩余类取最大。')],
(r'With unlimited $4$- and $7$-unit stamps, find the largest positive amount that cannot be made.',r'有无限张面值 $4$ 与 $7$ 的邮票，求无法表示的最大正整数金额。'),[
(r'Modulo $4$, the smallest representable amounts for residues $0,1,2,3$ are $0,21,14,7$.',r'模 $4$ 的剩余 $0,1,2,3$ 中，最小可表示金额分别为 $0,21,14,7$。'),
(r'These use respectively $0,3,2,1$ seven-unit stamps; fewer sevens cannot have the required residue.',r'它们分别使用 $0,3,2,1$ 张七元票，更少七元票无法具有相应剩余。'),
(r'The largest missing amount is $\max M_r-4=17$. Each amount above it is reached by adding fours within its residue class.',r'最大缺失金额为 $\max M_r-4=17$；每个更大金额都可在其剩余类内加四得到。')],
('A residue minimum must be proved minimal; finding one representation gives only an upper bound.','剩余类最小值必须证明其最小性；找到一种表示只给出上界。'),
'2019-II-Q14 2025-II-Q08',('NT05','LO03'),[
(r'To compare a greedy coin choice with an optimum, use exchange moves to bound the number of small coins in an optimum. This can restrict the number of large coins to two neighboring possibilities. Compare their exact counts for each residual amount; discard any rival requiring a negative coin count.',r'比较贪心取币与最优取币时，先用交换论证限制最优方案的小面额枚数；这可把大面额枚数限制为相邻两种。按剩余金额比较确切枚数，并排除需要负枚数的对手方案。')]))
ms.append(M(C,9,'Prove a residue invariant is sufficient with a construction','用构造证明剩余不变量的充分性',[
(r'Identify the residues forced by every permitted move or every retained condition.',r'确定每个允许动作或保留条件强制的剩余。'),
(r'Prove that no forbidden residue can occur, using induction or subtraction of neighboring conditions.',r'用归纳或相邻条件相减，证明禁用剩余不可能出现。'),
(r'Give an explicit move, partition or construction for every permitted residue; then count the bounded representatives.',r'对每个允许剩余给出明确动作、分划或构造，最后统计有界代表元。')],
(r'A game permits removing $1$ or $2$ tokens, with the last move winning. Prove the losing pile sizes for the player to move.',r'游戏每次可拿走 $1$ 或 $2$ 枚，拿走最后一枚者胜。证明轮到行动者时的必败堆数。'),[
(r'Zero is losing. From any positive multiple of $3$, either move reaches a number congruent to $1$ or $2$.',r'零为必败态。从任意正的 $3$ 倍数出发，两种动作均到达余 $1$ 或 $2$ 的数。'),
(r'From residue $1$ remove one; from residue $2$ remove two. Both moves reach a smaller multiple of $3$.',r'余 $1$ 时拿一枚，余 $2$ 时拿两枚，均到达更小的 $3$ 倍数。'),
(r'Induction now proves that exactly the multiples of $3$ are losing.',r'因此归纳证明必败态恰为 $3$ 的倍数。')],
('An invariant alone rarely proves reachability or a winning strategy.','单有不变量通常不能证明可达性或必胜策略。'),
'2002-I-Q09 2002-I-Q14 2006-I-Q15 2007-II-Q08 2012-I-Q11 2024-I-Q03',('LO02','LO03')))
save(C,('Choose a modulus for a reason: it should simplify a coefficient, isolate a prime power, or expose a short pattern. Keep necessity and sufficiency separate, especially when clearing denominators or converting a modular invariant into an existence claim.','选模数须有目的：化简系数、隔离质数幂，或揭示短模式。尤其在清分母与把模不变量转为存在结论时，须分清必要性与充分性。'),ms,('NT02',))

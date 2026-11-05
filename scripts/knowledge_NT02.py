from knowledge_helpers_source import method as M,save
C='NT02';ms=[]
ms.append(M(C,1,'Use Euclidean reduction before listing divisors','先作欧几里得化简，再列约数',[
(r'Replace $A\mid B$ by $A\mid(B-qA)$ with a useful integer $q$.',r'以合适整数 $q$ 将 $A\mid B$ 改写为 $A\mid(B-qA)$。'),
(r'For equal remainders, the modulus divides every pairwise difference. For $n+c\mid P(n)$, substitute $n=-c$ into the remainder.',r'余数相等时，模数整除所有两两差；对 $n+c\mid P(n)$，以 $n=-c$ 求余数。'),
(r'List only divisors meeting the original positivity, digit or size restrictions.',r'只列满足原正性、数位或大小限制的约数。'),
(r'Recover the original variables and check the remainder lies between zero and the modulus.',r'还原原变量，并检查余数介于零与模数之间。')],
(r'Find all positive integers $n$ such that $n+3$ divides $n^2+2n+8$.',r'求全部满足 $n+3\mid n^2+2n+8$ 的正整数 $n$。'),[
(r'Divide: $n^2+2n+8=(n+3)(n-1)+11$.',r'相除得 $n^2+2n+8=(n+3)(n-1)+11$。'),
(r'The condition is exactly $n+3\mid11$. Positivity requires $n+3\ge4$.',r'条件恰为 $n+3\mid11$，正性又要求 $n+3\ge4$。'),
(r'Only divisor $11$ qualifies, giving $n=8$. Substitution gives $88$, divisible by $11$.',r'只有约数 $11$ 合格，得 $n=8$；代入为 $88$，确可被 $11$ 整除。')],
('A remainder reduction is an equivalence; preserve both directions.','求余化简须保留充要关系。'),
'2001-I-Q01 2006-I-Q03 2017-I-Q02 2020-I-Q04 2025-I-Q01 2025-II-Q02',('NT06',)))
ms.append(M(C,2,'Reduce ratios and use coprimality to fix integer scale','约分比例并用互质性确定整数尺度',[
(r'Write every rational ratio in lowest terms before assigning an integer scale.',r'设置整数尺度前，先把所有比例约至最简。'),
(r'Use Euclid\'s lemma: if $\gcd(a,b)=1$ and $a\mid bc$, then $a\mid c$.',r'使用欧几里得引理：若 $\gcd(a,b)=1$ 且 $a\mid bc$，则 $a\mid c$。'),
(r'For equal fractions or a reduced numerator-denominator pair, resolve the whole common scale, not just one variable.',r'分数相等或既约分子分母题，应确定整个公因尺度，不能只确定一个变量。'),
(r'Check that the resulting counts or digits are feasible, since integrality alone may not suffice.',r'检验所得人数或数位是否可实现，因为整数性未必充分。')],
(r'A class has boys:girls $=4:7$. After five boys join, the ratio is $3:4$. Find the original class size.',r'某班男女人数比为 $4:7$，加入五名男生后变为 $3:4$。求原班人数。'),[
(r'Since $4,7$ are coprime, write the original counts as $4t,7t$ with positive integer $t$.',r'因 $4,7$ 互质，原人数可写成 $4t,7t$，其中 $t$ 为正整数。'),
(r'The new ratio gives $4(4t+5)=3(7t)$, so $t=4$.',r'新比例给出 $4(4t+5)=3(7t)$，故 $t=4$。'),
(r'The original size is $11t=44$. The final counts $21,28$ indeed have ratio $3:4$.',r'原班共有 $11t=44$ 人；最后人数 $21,28$ 之比确为 $3:4$。')],
('A reduced ratio makes the scale integral; an unreduced one may not.','最简整数比才保证对应尺度为整数。'),
'2000-I-Q03 2012-I-Q06 2013-I-Q08 2015-II-Q01 2019-I-Q07 2022-II-Q01 2023-II-Q05',('AL01',)))
ms.append(M(C,3,'Parametrize multiples and common-divisor constraints','参数化倍数与公约数限制',[
(r'If $a\mid b,c$, write $b=au,c=av$ before using a sum or product condition.',r'若 $a\mid b,c$，先写成 $b=au,c=av$，再代入和或积条件。'),
(r'Combine repeated divisibility conditions with gcd or lcm. Distinguish a divisor bound from a multiple bound.',r'用最大公因数或最小公倍数合并重复整除条件，区分约数界与倍数界。'),
(r'For a fixed parameter, count remaining positive solutions explicitly, or list bounded factor pairs.',r'固定参数后，明确统计剩余正整数解，或列出有界因子对。'),
(r'Prove the parameter list complete and construct the extremal or counted objects.',r'证明参数列表完整，并构造相应最值对象或被统计对象。')],
(r'Count positive ordered pairs $(x,y)$ such that $x\mid y$ and $x+y=24$.',r'统计满足 $x\mid y$ 且 $x+y=24$ 的正整数有序对 $(x,y)$。'),[
(r'Write $y=kx$ with $k\ge1$. Then $x(k+1)=24$.',r'写 $y=kx$，其中 $k\ge1$，则 $x(k+1)=24$。'),
(r'Thus $x$ can be any divisor of $24$ no greater than $12$: $1,2,3,4,6,8,12$.',r'故 $x$ 为 $24$ 的不大于 $12$ 的约数：$1,2,3,4,6,8,12$。'),
(r'Each determines the unique positive $y=24-x$ and satisfies divisibility. There are seven pairs.',r'每个 $x$ 都确定唯一正整数 $y=24-x$ 并满足整除，共七对。')],
('A parameter count must respect strict increase, positivity and ordering.','参数计数须同时尊重严格递增、正性与有序性。'),
'2007-II-Q02 2007-II-Q07 2010-II-Q01 2010-II-Q06 2013-I-Q11 2014-I-Q06 2016-I-Q05 2016-II-Q04 2019-II-Q03 2026-II-Q01',('NT05',)))
ms.append(M(C,4,'Use the gcd to find periods, orbit lengths and primitive segments','用最大公因数求周期、轨道长度与本原格段',[
(r'For motion modulo $n$ by a fixed step $a$, the first return solves $n\mid ka$.',r'模 $n$ 每次走固定步长 $a$ 时，首次返回满足 $n\mid ka$。'),
(r'Dividing by $g=\gcd(a,n)$ gives orbit length $n/g$ and $g$ separate cycles.',r'约去 $g=\gcd(a,n)$，轨道长度为 $n/g$，共有 $g$ 个循环。'),
(r'For lattice displacement $(u,v)$, divide by $\gcd(u,v)$ to get a primitive step; for reflections, compose them to get translations.',r'格点位移 $(u,v)$ 除以 $\gcd(u,v)$ 得本原步长；反射则先复合成平移。'),
(r'For unfolding or multiple modular coordinates, solve all return divisibilities simultaneously; correct shared endpoints when repeating a segment.',r'展开反射或处理多个模坐标时，同时求解全部返回整除条件；重复格段须修正公共端点。')],
(r'A token moves $8$ positions each turn around $30$ labeled positions. How many cycles does this rule form, and how long is each cycle?',r'棋子在 $30$ 个有标签位置组成的环上，每次前进 $8$ 格。该规则形成多少个循环？每个多长？'),[
(r'The return condition is $30\mid8k$. Since $\gcd(30,8)=2$, it is equivalent to $15\mid k$.',r'返回条件为 $30\mid8k$。因 $\gcd(30,8)=2$，等价于 $15\mid k$。'),
(r'Each cycle therefore contains $15$ distinct positions before returning.',r'故每个循环返回前经过 $15$ 个不同位置。'),
(r'The $30$ positions split into $30/15=2$ cycles, namely the two parity classes.',r'$30$ 个位置分为 $30/15=2$ 个循环，恰为奇偶两个类。')],
('Multiplication of residue labels by a is a permutation iff gcd(a,n)=1. Addition by a is always a permutation and has one full orbit iff gcd(a,n)=1.','剩余类标签乘 a 为置换当且仅当 gcd(a,n)=1；加 a 总是置换，而只有 gcd(a,n)=1 时才形成单一满轨道。'),
'2000-I-Q12 2002-I-Q11 2012-I-Q15 2016-I-Q14 2021-I-Q07 2023-I-Q14 2025-II-Q11',('NT03',),[
(r'Bézout gives $ua+vb=\gcd(a,b)$. Hence two integer periods $a,b$ force their gcd to be a period. For reflected function values, retain the residual reflection on the resulting residue classes; period reduction alone does not count the final classes.',r'裴蜀关系 $ua+vb=\gcd(a,b)$ 表明两个整数周期 $a,b$ 会迫使其最大公因数也为周期。反射函数题在约化剩余类后仍须保留剩余反射，单有周期约化并未统计最终等价类。')]))
ms.append(M(C,5,'Track a gcd invariant through reduced-fraction updates','在既约分数更新中追踪最大公因数不变量',[
(r'Write the numerator and denominator update before reduction.',r'先写约分之前的分子分母更新。'),
(r'Find a linear combination preserved by that update, and express the reduction gcd through it and another changing coordinate.',r'寻找更新保持的线性组合，并用它与另一变化坐标表达约分公因数。'),
(r'After division by the gcd, update both auxiliary coordinates; list the exact indices at which cancellation occurs.',r'除以公因数后，同时更新两个辅助坐标，并精确记录发生约分的下标。'),
(r'Prove no later return is possible when the invariant becomes a unit.',r'当不变量变成单位时，证明以后不会再次返回。')],
(r'Reduce $m/n$ after replacing it by $(m+2)/(n+3)$. If $d=n-m$ and $I=3m-2n$, express the next reduced $d,I$ in terms of the cancellation gcd.',r'将 $m/n$ 更新为 $(m+2)/(n+3)$ 后约分。设 $d=n-m,I=3m-2n$，用约分公因数表达新 $d,I$。'),[
(r'Before reduction the difference is $d+1$, while $3(m+2)-2(n+3)=I$.',r'约分前差为 $d+1$，而 $3(m+2)-2(n+3)=I$ 保持不变。'),
(r'The gcd is $g=\gcd(m+2,n+3)=\gcd(m+2,d+1)=\gcd(I,d+1)$, because $I=(m+2)-2(d+1)$.',r'公因数为 $g=\gcd(m+2,n+3)=\gcd(m+2,d+1)=\gcd(I,d+1)$，因 $I=(m+2)-2(d+1)$。'),
(r'Consequently $d_{new}=(d+1)/g$ and $I_{new}=I/g$. If $I=1$, every future gcd is one and $d$ increases forever.',r'因此 $d_{新}=(d+1)/g,I_{新}=I/g$。若 $I=1$，以后公因数恒为一，而 $d$ 永远递增。')],
('Reduction changes the preserved linear combination by division; it is not literally constant across reduced states.','约分会把线性组合也除以公因数，它并非在既约状态间字面保持常数。'),
'2021-I-Q10',('AL05',)))
ms.append(M(C,6,'Combine divisor sets and divide a chain by its first term','组合约数集合，并用首项约化整除链',[
(r'The common divisors of $A,B$ are exactly the divisors of $\gcd(A,B)$; an LCM target requires each full prime-power exponent to appear.',r'$A,B$ 的公约数恰为 $\gcd(A,B)$ 的约数；达到某最小公倍数须让每个完整质数幂指数出现。'),
(r'For subsets, count missing-exponent events and apply inclusion-exclusion.',r'对子集，统计缺少完整指数的事件并用容斥。'),
(r'For an increasing divisibility chain beginning at $d$, divide every later term by $d$ to obtain a smaller-sum instance.',r'对首项为 $d$ 的递增整除链，将以后各项除以 $d$ 得总和更小的问题。'),
(r'Keep base cases and empty/singleton objects explicit so a recurrence is exhaustive.',r'明确递推初值、空对象与单元素对象，保证穷尽。')],
(r'Choose a subset of the six divisors of $12$. How many subsets have LCM exactly $12$?',r'从 $12$ 的六个正约数中选子集，有多少个子集的最小公倍数恰为 $12$？'),[
(r'The divisors are $1,2,3,4,6,12$. A successful subset needs a divisor carrying $2^2$ and one carrying $3$.',r'约数为 $1,2,3,4,6,12$。合格子集需有携带 $2^2$ 的约数及携带 $3$ 的约数。'),
(r'There are $2^6$ subsets; $2^4$ miss the full two-exponent, $2^3$ miss the three-exponent, and $2^2$ miss both.',r'全部为 $2^6$ 个子集；缺完整二指数有 $2^4$ 个，缺三指数有 $2^3$ 个，两者均缺有 $2^2$ 个。'),
(r'Inclusion-exclusion gives $64-16-8+4=44$. The empty subset is automatically excluded by both missing conditions.',r'容斥得 $64-16-8+4=44$；空集已由两个缺失条件自动排除。')],
('A recurrence requires a reversible first-step decomposition, not only a numerical pattern.','递推须来自可逆的首步分解，不能只凭数值规律。'),
'2019-II-Q12 2025-II-Q07 2021-II-Q11',('CO04','CO05'),[
(r'For public-information candidates involving common multiples, first list all admissible bounded runs using the divisibility conditions. A person\'s uncertainty is a statement about how many surviving candidates contain their value; repeat the candidate elimination after each public announcement. The gcd/LCM arithmetic creates the initial list, while the elimination itself belongs to LO03.',r'对涉及公倍数的公开信息候选，先用整除条件列出全部有界连续区间。某人不能确定，表示含有其数值的存活候选不止一个；每次公开声明后须重新筛选候选。最大公因数与最小公倍数算术产生初始列表，筛选本身属于 LO03。')]))
ms.append(M(C,7,'Bound a factorial divisor before testing a quotient','检验阶乘商前先确定阶乘约数的界',[
(r'Factor the expression around one convenient factorial.',r'围绕方便的某个阶乘分解表达式。'),
(r'Use monotonicity of $n!$ to rule out all sufficiently large indices at once.',r'利用 $n!$ 的单调性一次排除所有足够大的下标。'),
(r'Test the few remaining indices by exact integer quotients.',r'用精确整数商检验剩下的少量下标。')],
(r'Find the largest $n$ such that $n!\mid10!+9!$.',r'求使 $n!\mid10!+9!$ 的最大 $n$。'),[
(r'Write $10!+9!=11\cdot9!$, so $9!$ divides the expression.',r'写成 $10!+9!=11\cdot9!$，故 $9!$ 可整除。'),
(r'But division by $10!$ gives $11/10$, which is not an integer.',r'除以 $10!$ 得 $11/10$，不是整数。'),
(r'For $n\ge11$, $n!\ge11!=110\cdot9!>11\cdot9!$. Thus no larger index works, and the answer is $9$.',r'当 $n\ge11$，有 $n!\ge11!=110\cdot9!>11\cdot9!$，所以更大下标均不可能，答案为 $9$。')],
('Magnitude is a useful first filter; divisibility still needs an exact quotient at the boundary.','大小是有效的初筛，但边界处仍须检验精确整除。'),
'2003-I-Q01'))
ms[3]['question_ids'].append('AIME-2007-II-Q05')
ms[3]['extensions_en'].append(r'The segment from $(0,0)$ to positive lattice point $(m,n)$ crosses $m+n-\gcd(m,n)$ open unit-cell interiors. Start with one cell, add the $m-1$ vertical and $n-1$ horizontal grid crossings, and subtract the $\gcd(m,n)-1$ interior lattice crossings counted in both directions. A simultaneous crossing enters only one new diagonal cell.')
ms[3]['extensions_zh'].append(r'从 $(0,0)$ 到正整点 $(m,n)$ 的线段穿过 $m+n-\gcd(m,n)$ 个单位格内部。先计首格，再加 $m-1$ 次竖直与 $n-1$ 次水平格线穿越，减去被两方向重复计算的 $\gcd(m,n)-1$ 个内部整点穿越；同时穿越时只进入一个新的对角格。')
save(C,('Divisibility becomes simpler after a reversible change of variables. Reduce ratios, subtract multiples, and use the gcd to isolate the true scale or period; count only after these structural constraints are fixed.','整除在可逆换元后往往更简单：约分比例、减去倍数，并用最大公因数隔离真正尺度或周期；确定这些结构限制后再计数。'),ms,('NT01',))

from knowledge_helpers_source import method as M,save
C='NT05';ms=[]
ms.append(M(C,1,'Parametrize a linear integer system with its domain bounds','以定义域界参数化线性整数方程组',[
(r'Eliminate variables over the rationals, but retain all integer and positivity restrictions.',r'先在有理数范围消元，同时保留全部整数与正性限制。'),
(r'Solve a remaining congruence and write every solution using one integer parameter.',r'求解剩余同余，并以一个整数参数写出所有解。'),
(r'Intersect all parameter bounds and verify the endpoint candidates in the original model.',r'对全部参数界取交集，再把端点候选代回原模型。')],
(r'Find all positive integer pairs with $7x+4y=65$.',r'求满足 $7x+4y=65$ 的全部正整数有序对。'),[
(r'Modulo $4$, $3x\equiv1$, hence $x=3+4t$.',r'模 $4$ 得 $3x\equiv1$，故 $x=3+4t$。'),
(r'Substitution yields $y=11-7t$. Positivity requires $t\ge0$ and $t\le1$.',r'代入得 $y=11-7t$；正性要求 $0\le t\le1$。'),
(r'The pairs are $(3,11),(7,4)$, both of which satisfy the equation.',r'解为 $(3,11),(7,4)$，均满足原式。')],
('An integer parameter still needs an exact feasible interval.','整数参数仍须有精确可行区间。'),
'2001-II-Q02 2004-II-Q06 2006-I-Q09 2008-I-Q03 2009-I-Q14 2009-II-Q09 2012-I-Q04 2012-II-Q01 2013-II-Q07 2018-I-Q02 2020-I-Q03 2025-I-Q04 2026-II-Q05',('NT03','AL01')))
ms.append(M(C,2,'Turn a square equation into parity-compatible factor pairs','把平方方程转为奇偶相容的因子对',[
(r'Complete a square or subtract two metric square equations to obtain $U^2-V^2=K$.',r'配方，或相减两个度量平方方程，得到 $U^2-V^2=K$。'),
(r'Factor $(U-V)(U+V)=K$. List signed or positive divisor pairs according to the original signs.',r'分解 $(U-V)(U+V)=K$，按原符号列正因子对或带符号因子对。'),
(r'The two factors must have the same parity. Recover the original variables and check strict geometry, nonsquare exclusions and denominator conditions.',r'两个因子须奇偶相同。还原原变量，并检查严格几何、非平方排除与分母条件。')],
(r'Find all integer pairs $(u,v)$ with $u^2-v^2=45$ and $u>v\ge0$.',r'求满足 $u^2-v^2=45,u>v\ge0$ 的全部整数对。'),[
(r'The positive factors $u-v,u+v$ multiply to $45$ and are odd.',r'正因子 $u-v,u+v$ 乘积为 $45$，且都是奇数。'),
(r'The increasing pairs are $(1,45),(3,15),(5,9)$.',r'递增因子对为 $(1,45),(3,15),(5,9)$。'),
(r'Halving their sums and differences gives $(23,22),(9,6),(7,2)$.',r'对和与差分别除二，得 $(23,22),(9,6),(7,2)$。')],
('The parity test is part of the inverse transformation, not an optional final check.','奇偶检验是逆变换的一部分，并非可有可无的末尾检查。'),
'2000-II-Q02 2003-I-Q07 2003-II-Q10 2005-I-Q04 2008-I-Q04 2008-II-Q15 2017-II-Q06 2006-II-Q13',('NT02','NT01'),[
(r'A sum of consecutive positive odd integers is $m^2-k^2$ with $m>k\ge0$. Therefore its representations correspond to factor pairs of equal parity; the smaller factor gives the length. Only after this bijection is proved should a prescribed number of representations be converted into a divisor-count pattern (NT08).',r'连续正奇数之和为 $m^2-k^2$，其中 $m>k\ge0$。所以表示方法对应奇偶相同的因子对，较小因子给出长度。先证明此双射，才可将指定表示数转为约数计数模式（NT08）。')]))
ms.append(M(C,3,'Shift a rational or polynomial constraint into a fixed product','把分式或多项式限制平移为固定乘积',[
(r'Clear denominators within the original nonzero domain, then look for a constant product after adding or subtracting a fixed shift.',r'在原非零定义域内清分母，再寻找加减固定平移后得到的常数乘积。'),
(r'For an integer-coefficient polynomial, use divisibility of $P(a)-P(b)$ by $a-b$ or division by monic integer factors.',r'整系数多项式可用 $a-b\mid P(a)-P(b)$，或除以首一整数因子。'),
(r'Enumerate all fixed-product pairs consistent with the signs, then reverse every substitution.',r'穷尽符合符号的固定乘积因子对，再逆转每个代换。')],
(r'Find positive integer solutions to $1/x+1/y=1/6$ with $x\le y$.',r'求 $1/x+1/y=1/6$ 且 $x\le y$ 的正整数解。'),[
(r'Clearing denominators gives $xy=6x+6y$, hence $(x-6)(y-6)=36$.',r'清分母得 $xy=6x+6y$，故 $(x-6)(y-6)=36$。'),
(r'Both shifts are positive: each reciprocal is smaller than $1/6$. The ordered factor pairs with first no larger are $(1,36),(2,18),(3,12),(4,9),(6,6)$.',r'两平移均为正，因为每个倒数都小于 $1/6$。较小在前的因子对为 $(1,36),(2,18),(3,12),(4,9),(6,6)$。'),
(r'Adding six gives $(7,42),(8,24),(9,18),(10,15),(12,12)$.',r'分别加六，得 $(7,42),(8,24),(9,18),(10,15),(12,12)$。')],
('A fixed product gives a finite list only after signs and zero cases are controlled.','控制符号与零情形后，固定乘积才给出有限列表。'),
'2000-I-Q02 2002-I-Q04 2003-II-Q01 2004-II-Q03 2005-II-Q13 2009-II-Q04 2015-II-Q08 2016-I-Q07 2021-I-Q05 2026-I-Q04',('AL02','NT02')))
ms.append(M(C,4,'Convert rational radicals to integer square conditions','把有理根式转为整数平方条件',[
(r'Isolate a sum, difference or product of radicals and determine whether it must be rational.',r'隔离根式的和、差或积，判断其是否必须为有理数。'),
(r'If an integer has a rational square root, write it in lowest terms and prove the denominator is one.',r'若整数的平方根为有理数，将其约至最简，并证明分母为一。'),
(r'Replace the radicals by integer parameters; keep any nonsquare or strict inequality condition in the resulting finite search.',r'用整数参数替代根式，并在所得有限搜索中保留非平方或严格不等式条件。')],
(r'If $\sqrt a+\sqrt b=7$ for positive integers $a,b$, determine all unordered pairs.',r'若正整数 $a,b$ 满足 $\sqrt a+\sqrt b=7$，求全部无序对。'),[
(r'Squaring $\sqrt b=7-\sqrt a$ gives $\sqrt a=(49+a-b)/14$, which is rational.',r'将 $\sqrt b=7-\sqrt a$ 平方，得 $\sqrt a=(49+a-b)/14$ 为有理数。'),
(r'A reduced $r/s$ with $(r/s)^2=a$ has $s^2\mid r^2$, forcing $s=1$. Thus both radicals are integers.',r'若最简 $r/s$ 满足 $(r/s)^2=a$，则 $s^2\mid r^2$ 迫使 $s=1$，故两个根式均为整数。'),
(r'The positive integer root pairs summing to seven are $(1,6),(2,5),(3,4)$, giving $(a,b)=(1,36),(4,25),(9,16)$.',r'和为七的正整数根对为 $(1,6),(2,5),(3,4)$，故 $(a,b)=(1,36),(4,25),(9,16)$。')],
('A rational sum does not make each summand rational without an additional algebraic argument.','和为有理数并不自动使各项有理，必须补上代数论证。'),
'2000-I-Q06 2003-II-Q10 2013-I-Q10',('NT01','AL03')))
ms.append(M(C,5,'Certify a short integer search from algebraic or geometric bounds','由代数或几何界证明短整数搜索完整',[
(r'Obtain an equation with nonnegative terms, a discriminant square, or a triangle interval.',r'得到非负项方程、平方判别式或三角形范围。'),
(r'Order symmetric variables to avoid duplicates and derive the exact finite bounds for each variable.',r'给对称变量排序以避免重复，并推导每个变量的精确有限界。'),
(r'Test every remaining integer case exactly, then reconstruct coefficients, geometry or probabilities to check attainability.',r'精确检查全部剩余整数情形，再重建系数、几何或概率以检验可达到性。')],
(r'Find positive integers $a\le b\le c$ with $a^2+b^2+c^2=14$.',r'求满足 $a^2+b^2+c^2=14$ 的正整数 $a\le b\le c$。'),[
(r'Ordering implies $3a^2\le14$, so $a=1$ or $2$.',r'排序给出 $3a^2\le14$，故 $a=1$ 或 $2$。'),
(r'For $a=1$, $b^2+c^2=13$ and $1\le b\le2$; only $b=2,c=3$ works.',r'$a=1$ 时 $b^2+c^2=13$ 且 $1\le b\le2$，仅 $b=2,c=3$ 可行。'),
(r'For $a=2$, $b\ge2$ and $b^2+c^2=10$, so $b=2$ would leave six, not a square. The sole triple is $(1,2,3)$.',r'$a=2$ 时 $b\ge2,b^2+c^2=10$，但 $b=2$ 留下六，非平方数。唯一三元组为 $(1,2,3)$。')],
('Record why each bound is sufficient; a spreadsheet search alone does not prove completeness.','应写清每个界为何足够；电子表格搜索本身不能证明穷尽。'),
'2000-I-Q05 2000-II-Q11 2002-II-Q03 2003-I-Q08 2005-II-Q05 2009-II-Q11 2010-II-Q12 2011-I-Q15 2011-II-Q15 2015-I-Q11 2015-II-Q06 2016-I-Q12 2016-II-Q05 2016-II-Q09 2018-II-Q03 2019-I-Q11 2020-II-Q12 2022-I-Q14 2026-II-Q08',('AL01','GE03')))
ms.append(M(C,6,'Prove a discrete minimum with a bound and an attaining construction','用下界与达到下界的构造证明离散最小值',[
(r'Compare any feasible object with a proposed optimum using integrality, factor order or a forced equality.',r'用整数性、因子大小或被迫等号，将任意可行对象与候选最优值比较。'),
(r'If two parameterizations collide, subtract their equations and use coprimality to bound the first possible collision.',r'若两个参数表示重合，先相减，再用互质性确定首次可能重合的下界。'),
(r'Construct an object meeting the bound and verify every domain restriction.',r'构造达到界的对象，并检验全部定义域限制。')],
(r'Prove that $4x+7y=25$ has at most one integer solution in the rectangle $0\le x\le6$, $0\le y\le3$, and determine that solution.',r'证明 $4x+7y=25$ 在矩形 $0\le x\le6,0\le y\le3$ 中至多有一个整数解，并求出该解。'),[
(r'If $(x,y),(u,v)$ are two solutions, then $4(x-u)=7(v-y)$. Coprimality gives $7\mid x-u$.',r'若 $(x,y),(u,v)$ 均为解，则 $4(x-u)=7(v-y)$。由互质性得 $7\mid x-u$。'),
(r'But $|x-u|\le6$, so $x=u$ and then $y=v$. This proves uniqueness from the width bound.',r'而 $|x-u|\le6$，所以 $x=u$，继而 $y=v$；由宽度界证明唯一性。'),
(r'The pair $(1,3)$ lies in the rectangle and satisfies $4+21=25$, so the upper bound of one solution is attained.',r'$(1,3)$ 位于矩形内，且 $4+21=25$，所以一个解的上界可以达到。')],
('An extremum needs both a universal bound and a valid witness.','最值须同时有普遍界与有效达到例。'),
'2002-I-Q08 2004-II-Q09 2009-I-Q13 2010-I-Q05 2020-I-Q10',('NT02','LO02')))
ms.append(M(C,7,'Analyze the gaps between consecutive powers','分析相邻幂之间的间隔',[
(r'Partition integers into blocks between consecutive squares or cubes.',r'按相邻平方数或立方数之间的区间给整数分块。'),
(r'Express the first available next power or the gap length exactly; identify the worst endpoint of a block.',r'精确表达下一个可用幂或间隔长度，并确定块中的最差端点。'),
(r'Prove later blocks satisfy the requirement monotonically, then locate and verify the last failing block.',r'证明后续区块的条件按单调性成立，再定位并检验最后失败区块。')],
(r'Find the least $Q$ such that every integer $n\ge Q$ has a square in $(n,2n]$.',r'求最小 $Q$，使每个整数 $n\ge Q$ 的区间 $(n,2n]$ 中都有平方数。'),[
(r'If $k^2\le n<(k+1)^2$, the next square is $(k+1)^2$ and the largest ratio to $n$ occurs at $n=k^2$.',r'若 $k^2\le n<(k+1)^2$，下一个平方数为 $(k+1)^2$，与 $n$ 的比在 $n=k^2$ 时最大。'),
(r'For $k\ge3$, $(1+1/k)^2\le16/9<2$, so all such blocks work. For $4\le n\le8$, only $n=4$ fails because nine exceeds eight.',r'当 $k\ge3$，$(1+1/k)^2\le16/9<2$，这些区块全可行。在 $4\le n\le8$ 中，仅 $n=4$ 因九大于八而失败。'),
(r'The integers $n=5,6,7,8$ are covered by nine. Thus the last failure is four and $Q=5$.',r'$n=5,6,7,8$ 均由九覆盖。因此最后失败值为四，$Q=5$。')],
('The ratio is tested at the block start, but the final failing integer may lie later in that block.','比值在块起点检查，但最后失败的整数可能在块内更后位置。'),
'2013-II-Q06 2017-I-Q13',('AL07',)))
ms.append(M(C,8,'Minimize a denominator inside a narrow interval','在窄区间中最小化分母',[
(r'Convert a required decimal prefix to a half-open rational interval.',r'把指定小数前缀转为左闭右开的有理区间。'),
(r'Compare with a nearby simple fraction $a/b$ and form the nonzero integer $bm-an$.',r'与附近简单分数 $a/b$ 比较，并形成非零整数 $bm-an$。'),
(r'Use the interval width to bound the denominator, test the first possible denominators, and confirm reduction and endpoint strictness.',r'用区间宽度给分母建立界，检查最先可能的分母，并核对既约性与端点严格性。')],
(r'Find the least denominator of a reduced fraction strictly between $1/3$ and $2/5$.',r'求严格位于 $1/3$ 与 $2/5$ 之间的既约分数的最小分母。'),[
(r'If $m/n>1/3$, then $3m-n\ge1$. If $m/n<2/5$, then $2n-5m\ge1$.',r'由 $m/n>1/3$ 得 $3m-n\ge1$；由 $m/n<2/5$ 得 $2n-5m\ge1$。'),
(r'Multiply the first inequality by five and the second by three; addition gives $n\ge8$.',r'第一不等式乘五、第二乘三，相加得 $n\ge8$。'),
(r'The fraction $3/8$ is reduced and lies strictly between the endpoints, so the minimum denominator is $8$.',r'$3/8$ 既约且严格位于两端之间，所以最小分母为 $8$。')],
('If a digit string starts later, shifting the decimal and reducing can only decrease the denominator.','若数位串在较后位置出现，移动小数点后约分只会使分母不增。'),
'2003-I-Q14',('NT07',)))
ms.append(M(C,9,'Use integer descent to force a rigid recurrence','用整数递降迫使递推具有刚性',[
(r'Clear two neighboring recurrence equations and subtract them to expose a relation between differences.',r'清除相邻两式的分母并相减，找出差量之间的关系。'),
(r'If a nonzero integer difference would shrink by a factor exceeding one forever, derive a contradiction.',r'若某非零整数差将永远按大于一的倍数缩小，则导出矛盾。'),
(r'Force that difference to zero, identify the resulting periodic family, and verify every member satisfies the original recurrence.',r'迫使差为零，识别所得周期族，并验证每个成员满足原递推。')],
(r'An infinite integer sequence satisfies $d_{n+1}=d_n/3$. Prove every term is zero.',r'无限整数列满足 $d_{n+1}=d_n/3$，证明每项均为零。'),[
(r'If $d_1\ne0$, then $|d_n|=|d_1|/3^{n-1}$ remains positive.',r'若 $d_1\ne0$，则 $|d_n|=|d_1|/3^{n-1}$ 始终为正。'),
(r'For sufficiently large $n$ this value is below one, impossible for a nonzero integer.',r'当 $n$ 足够大，该值小于一，不可能是非零整数。'),
(r'Therefore $d_1=0$, and the recurrence makes every subsequent term zero.',r'故 $d_1=0$，由递推其后各项均为零。')],
('Descent requires integrality and an infinite continuation; a finite real sequence gives no contradiction.','递降须有整数性与无限延续；有限实数列不会产生此矛盾。'),
'2009-I-Q13',('AL05',)))
ms.append(M(C,10,'Project a nonnegative integer solution set onto the requested statistic','把非负整数解集投影到目标统计量',[
(r'Parametrize the admissible objects by nonnegative integer multiplicities.',r'用非负整数重数参数化允许对象。'),
(r'Eliminate one variable and express the requested quantity as a linear function of the remaining ones.',r'消去一个变量，将目标量写为其余变量的线性式。'),
(r'For each bounded outer parameter, find the full integer interval of target values; take the union, not the sum of interval lengths.',r'固定每个有界外参数，求目标值的完整整数区间；最后取并集，不能直接累加区间长度。')],
(r'Nonnegative integers satisfy $x+3y+5z=12$. How many distinct values can $x+y+z$ take?',r'非负整数满足 $x+3y+5z=12$，$x+y+z$ 可取多少个不同值？'),[
(r'The target is $12-2y-4z=12-2v$, where $v=y+2z$.',r'目标为 $12-2y-4z=12-2v$，其中 $v=y+2z$。'),
(r'For $z=0,1,2$, the possible $v$ intervals are respectively $[0,4],[2,4],[4,4]$ on the integers.',r'当 $z=0,1,2$，整数 $v$ 区间分别为 $[0,4],[2,4],[4,4]$。'),
(r'Their union is $0,1,2,3,4$, giving five distinct targets $12,10,8,6,4$.',r'并集为 $0,1,2,3,4$，故五个不同目标值为 $12,10,8,6,4$。')],
('Different representations may give the same target; the question may count values rather than representations.','不同表示可能产生同一目标；题目有时数的是值而非表示数。'),
'2004-II-Q14',('CO03',)))
ms[4]['question_ids'].append('AIME-2021-II-Q15')
save(C,('Integrality is a source of structure: it turns a continuous range into factor pairs, residue classes or a finite list. Every search below begins with a bound and ends with a reconstruction of the original object.','整数性本身提供结构：它把连续范围化为因子对、剩余类或有限列表。这里每次搜索都以界开始，以重建原对象结束。'),ms,('NT01','NT02','NT03'))

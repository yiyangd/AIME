from knowledge_helpers_source import method as M,save
C='NT01'
ms=[]
ms.append(M(C,1,'Compare prime exponents, then round the required threshold','比较质指数，再向上取整门槛',[
(r'Factor the fixed integer and write each unknown prime exponent explicitly.',r'分解固定整数，并明确写出每个未知质指数。'),
(r'Use $A\mid B\iff v_p(A)\le v_p(B)$ for every prime; a $k$th power has every exponent divisible by $k$.',r'对每个质数使用 $A\mid B\iff v_p(A)\le v_p(B)$；$k$ 次幂的每个指数均为 $k$ 的倍数。'),
(r'For $D\mid x^k$, require $v_p(x)\ge\lceil v_p(D)/k\rceil$. Keep any extra positivity or size bounds.',r'由 $D\mid x^k$ 得 $v_p(x)\ge\lceil v_p(D)/k\rceil$，并保留正性或大小限制。'),
(r'Build a candidate from these exponents and verify all original conditions, including minimality.',r'由这些指数构造候选，并验证原条件及最小性。')],
(r'Find the least positive integer $u$ such that $72u$ is a cube and $u$ is a square.',r'求最小正整数 $u$，使 $72u$ 是立方数且 $u$ 是平方数。'),[
(r'Write $72=2^3 3^2$ and $u=2^a3^b$; introducing any other prime cannot reduce the minimum.',r'写成 $72=2^3 3^2,u=2^a3^b$；增加其他质数不会使最小值更小。'),
(r'Squareness requires even $a,b$. Cubeness requires $a+3\equiv0$ and $b+2\equiv0\pmod3$.',r'平方条件要求 $a,b$ 为偶数；立方条件要求 $a+3\equiv0,b+2\equiv0\pmod3$。'),
(r'The smallest choices are $a=0,b=4$, giving $u=81$. Indeed $72\cdot81=18^3$ and $81=9^2$.',r'最小选择为 $a=0,b=4$，故 $u=81$；确有 $72\cdot81=18^3$ 且 $81=9^2$。')],
('Exponent conditions are simultaneous; satisfying one prime is insufficient.','各质数的指数条件必须同时满足。'),
'2002-II-Q05 2007-I-Q01 2016-I-Q10 2016-II-Q07 2018-II-Q07 2020-I-Q10 2020-II-Q01 2021-II-Q15 2026-II-Q10'))
ms.append(M(C,2,'Count valuation layers in factorials and weighted products','按赋值层统计阶乘与加权乘积',[
(r'Use $v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$; stop when $p^j>n$.',r'使用 $v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$，当 $p^j>n$ 时停止。'),
(r'For a product with repeated factors, count how often each factor occurs before summing its valuation.',r'若乘积中因子重复出现，先统计每个因子的出现次数，再累加赋值。'),
(r'For a factorial quotient, subtract denominator valuations prime by prime; for trailing zeros take the smaller of the two- and five-adic valuations.',r'阶乘商按质数相减分母赋值；末尾零数取二与五赋值的较小者。'),
(r'If a sum has different powers of one prime in its denominators, test whether the largest denominator term is uniquely odd after clearing denominators.',r'若和式各分母含同一质数的不同幂，清分母后检查最大分母对应项是否唯一不被该质数整除。')],
(r'Nine labeled objects are partitioned into three unlabeled groups of three. What is the exponent of $3$ in the number of partitions?',r'把九个有标签物品分为三个无标签三元组，分法总数中的质因数 $3$ 的指数是多少？'),[
(r'The count is $N=9!/((3!)^3 3!)$. The last $3!$ removes the ordering of the three groups.',r'总数为 $N=9!/((3!)^3 3!)$；最后的 $3!$ 消去三个组的次序。'),
(r'Legendre gives $v_3(9!)=3+1=4$ and $v_3(3!)=1$.',r'勒让德公式给出 $v_3(9!)=3+1=4$，而 $v_3(3!)=1$。'),
(r'Hence $v_3(N)=4-3-1=0$. In fact $N=280$, consistent with the valuation.',r'所以 $v_3(N)=4-3-1=0$；实际 $N=280$，与赋值一致。')],
('A multiple of $p^j$ contributes at every layer up to $j$.','$p^j$ 的倍数会在前 $j$ 层各贡献一次。'),
'2006-I-Q04 2006-II-Q03 2009-II-Q07 2010-II-Q03 2020-I-Q07 2023-I-Q04 2025-I-Q10',('CO02',)))
ms.append(M(C,3,'Use exponent parity and squarefree parts','使用指数奇偶与无平方因子部分',[
(r'Write $n=s t^2$ with squarefree $s$ by separating the odd exponent of each prime.',r'把每个质数指数的奇数部分分离，写成 $n=st^2$，其中 $s$ 无平方因子。'),
(r'A product is square exactly when each total prime exponent is even; encode these parities as bits if many factors are chosen.',r'乘积为平方数当且仅当各质指数总和均为偶数；多次选择时可把奇偶编码为二元位。'),
(r'For rational square roots, reduce the fraction first: numerator and denominator must each be squares.',r'有理数平方根问题先约分，既约分子的分母必须各为平方数。'),
(r'Count or bound each allowed parity pattern and confirm its realization.',r'对允许的奇偶模式逐个计数或估界，并检验可实现性。')],
(r'What is the least positive rational number $r$ such that $18r^2$ is an integer square?',r'求最小正有理数 $r$，使 $18r^2$ 为整数平方。'),[
(r'If $18r^2=k^2$ for a positive integer $k$, then $\sqrt{18}=k/r$ would be rational.',r'若 $18r^2=k^2$，其中 $k$ 为正整数，则 $\sqrt{18}=k/r$ 必为有理数。'),
(r'But $18=2\cdot3^2$ has odd exponent of $2$, so $\sqrt{18}=3\sqrt2$ is irrational.',r'然而 $18=2\cdot3^2$ 的质因数 $2$ 指数为奇数，故 $\sqrt{18}=3\sqrt2$ 无理。'),
(r'There is no such positive rational $r$. Multiplying by a rational square cannot change the parity of a prime exponent.',r'不存在这样的正有理数 $r$；乘有理平方数不会改变质指数的奇偶。')],
('A parity obstruction can prove impossibility before any enumeration.','赋值奇偶障碍可在枚举之前证明不可能。'),
'2015-I-Q13 2019-II-Q04',('PS01',)))
ms.append(M(C,4,'Allocate prime exponents independently','独立分配各质数的指数',[
(r'For $N=\prod p^{e_p}$, encode each factor by its exponent for each prime.',r'对 $N=\prod p^{e_p}$，用各质数的指数编码每个因子。'),
(r'Apply the local rule: bounded intervals for divisors, weak compositions for ordered products, or one-sided allocation for coprimality.',r'按局部规则计数：约数对应有界区间，有序乘积对应弱拆分，互质对应单侧分配。'),
(r'Multiply independent prime contributions. If factors are unordered, remove repeated-factor exceptions before dividing by permutations.',r'独立质数的贡献相乘；若因子无序，先处理重复因子例外，再除排列数。'),
(r'For sums rather than counts, factor the sum into finite geometric series; signed exponents also encode reduced rational factors.',r'若求和而非计数，则将和分解为有限等比级数；带符号指数还可编码既约有理因子。')],
(r'How many divisors $d$ of $360$ satisfy $\gcd(d,360/d)=1$? Also find their sum.',r'有多少个 $360$ 的约数 $d$ 满足 $\gcd(d,360/d)=1$？并求这些约数之和。'),[
(r'Factor $360=2^3 3^2 5$. Coprimality forces the entire power of each prime into exactly one side.',r'分解 $360=2^3 3^2 5$；互质要求每个质数的整块幂只放到一侧。'),
(r'Each of the three prime powers has two independent destinations, so there are $2^3=8$ divisors.',r'三块质数幂各有两种独立归属，故共有 $2^3=8$ 个约数。'),
(r'Their sum is $(1+8)(1+9)(1+5)=540$, by expanding one choice from each factor.',r'从各因子各选一项展开，约数和为 $(1+8)(1+9)(1+5)=540$。')],
('Prime choices are independent; ordering of whole factors is a separate issue.','质指数的独立性与整个因子的有序性是不同问题。'),
'2000-I-Q11 2000-II-Q02 2000-II-Q04 2010-II-Q10 2016-II-Q08 2019-I-Q09 2019-II-Q09 2020-I-Q09 2024-II-Q14',('CO03','NT08')))
ms.append(M(C,5,'Force prime structure and prove finite prime bounds','强迫质因数结构并证明有限质数界',[
(r'Factor an identity or exclude small prime divisors by residue tables.',r'分解恒等式，或用剩余表排除小质因数。'),
(r'Use primality to force one factor to be one, or use the least permitted primes to bound a product.',r'利用质性迫使某因子为一，或用最小允许质数为乘积建立下界。'),
(r'Prove that the remaining candidate list is exhaustive before testing it.',r'测试候选之前先证明剩余列表穷尽。'),
(r'Certify each claimed prime by trial division only through its square root, then substitute into the original identity.',r'对声称为质数的候选只需试除至其平方根，再代回原恒等式。')],
(r'An integer has exactly three prime factors counted with multiplicity, each at least $7$, and is not a cube. Find its smallest possible value.',r'某整数恰有三个质因数（计重），各不小于 $7$，且它不是立方数。求其最小值。'),[
(r'The unrestricted least product is $7^3$, which is forbidden because it is a cube.',r'无限制最小乘积为 $7^3$，但它是立方数而被排除。'),
(r'At least one prime must therefore be at least $11$, the next prime after $7$. The product is at least $7^2\cdot11$.',r'至少一个质因数须不小于 $7$ 后的下一质数 $11$，故乘积至少为 $7^2\cdot11$。'),
(r'The value $539=7^2\cdot11$ satisfies every condition. It is therefore the minimum.',r'$539=7^2\cdot11$ 满足全部条件，因此为最小值。')],
('A prime search needs a certified bound, not a long unchecked list.','搜索质数须有已证明的界，不能只列一长串未核验候选。'),
'2000-I-Q01 2015-I-Q03 2016-I-Q12 2023-I-Q15 2026-I-Q04',('NT03',)))
ms.append(M(C,6,'Use a valuation to distinguish values and control cancellation','用赋值区分数值并控制消去',[
(r'Choose a prime for which one factor is always a unit. Its valuation isolates the remaining exponent.',r'选择使某个因子恒不被整除的质数，其赋值便可隔离另一指数。'),
(r'If two expressions are equal, compare valuations first, then divide out the common prime power.',r'若两个表达式相等，先比较赋值，再除去共同质数幂。'),
(r'Use the remaining odd or unit part to recover the other parameters, proving no duplicate counting.',r'由剩下的奇数部分或单位部分恢复其他参数，证明计数无重复。'),
(r'For an extremal power representation, translate the condition into exponent inequalities before a finite search.',r'幂表示最值题应先把条件转为指数不等式，再进行有限搜索。')],
(r'Each positive integer is written as $2^a u$ with $u$ odd. Prove that numbers with different pairs $(a,u)$ cannot coincide, and count such numbers below $17$ with $a\ge2$.',r'将正整数写成 $2^a u$，其中 $u$ 为奇数。证明不同 $(a,u)$ 不会表示同一数，并统计小于 $17$ 且 $a\ge2$ 的这些整数。'),[
(r'If $2^a u=2^b v$ and $a<b$, dividing by $2^a$ would make the odd number $u$ even. Hence $a=b$.',r'若 $2^a u=2^b v$ 且 $a<b$，约去 $2^a$ 将使奇数 $u$ 变为偶数，矛盾，所以 $a=b$。'),
(r'Division now gives $u=v$, proving uniqueness.',r'再相除得到 $u=v$，唯一性得证。'),
(r'For $a=2$, the odd parts are $1,3$; for $a=3,4$, only $1$ works. The four values are $4,12,8,16$.',r'$a=2$ 时奇数部分为 $1,3$；$a=3,4$ 时只可为 $1$。共四个值 $4,12,8,16$。')],
('The valuation proves uniqueness before a parameter count is summed.','应先用赋值证明唯一性，再累加参数计数。'),
'2009-I-Q08 2021-I-Q03 2021-II-Q09',('NT04',)))
ms.append(M(C,7,'Translate logarithmic and divisor constraints into exponent systems','把对数与约数条件转为指数方程组',[
(r'Exponentiate a logarithmic identity before assigning prime exponents.',r'先把对数恒等式指数化，再设置质指数。'),
(r'Use $v_p(\gcd(x,y))=\min(a,b)$ and $v_p(\operatorname{lcm}(x,y))=\max(a,b)$.',r'使用 $v_p(\gcd(x,y))=\min(a,b)$ 与 $v_p(\operatorname{lcm}(x,y))=\max(a,b)$。'),
(r'Split the order cases for these minima and maxima; reject negative or nonintegral exponent solutions.',r'按最小值与最大值的大小关系分类，剔除负数或非整数指数解。'),
(r'Reconstruct the numbers or count bounded lattice solutions in the exponent variables.',r'重建原数，或统计指数变量中的有界整点解。')],
(r'Positive integers $x,y$ satisfy $x\gcd(x,y)=2^8$ and $y/\gcd(x,y)=2^2$. Find all ordered pairs.',r'正整数 $x,y$ 满足 $x\gcd(x,y)=2^8$ 且 $y/\gcd(x,y)=2^2$，求全部有序对。'),[
(r'No odd prime divides $x$. Write $x=2^a$ and $g=\gcd(x,y)=2^c$; the second equation gives $y=2^{c+2}$.',r'没有奇质数可整除 $x$。写 $x=2^a,g=\gcd(x,y)=2^c$，第二式给出 $y=2^{c+2}$。'),
(r'The conditions become $a+c=8$ and $c=\min(a,c+2)$. Since $c<c+2$, the latter forces $a=c$.',r'条件化为 $a+c=8,c=\min(a,c+2)$。因 $c<c+2$，后者迫使 $a=c$。'),
(r'Thus $a=c=4$, giving $(x,y)=(16,64)$. Direct substitution verifies both equations.',r'所以 $a=c=4$，得 $(x,y)=(16,64)$，代回可验证两式。')],
('A prime absent from one side of a product identity must be absent from every positive integral factor.','乘积一侧不存在的质因数，不会出现在另一侧任一正整数因子中。'),
'2006-I-Q09 2006-I-Q13 2006-II-Q14 2013-II-Q02 2019-I-Q07',('AL04','NT02')))
ms.append(M(C,8,'Lift odd-prime valuations and split multiplicative costs','提升奇质数赋值与拆分乘法代价',[
(r'For exponential differences, first find a power for which the two bases agree modulo the prime.',r'对指数差，先找使两底数模该质数相等的幂次。'),
(r'For odd $p$ with $p\mid A-B$ and $p\nmid AB$, use $v_p(A^k-B^k)=v_p(A-B)+v_p(k)$. Check these hypotheses each time.',r'若奇质数 $p\mid A-B$ 且 $p\nmid AB$，使用 $v_p(A^k-B^k)=v_p(A-B)+v_p(k)$，每次核对前提。'),
(r'In a multiplicative construction, compare the cost of a composite factor with the costs of its smaller factors.',r'在乘法构造中，比较合数因子的代价与其较小因子拆分后的总代价。'),
(r'Combine local necessities, then construct an object attaining all of them simultaneously.',r'合并局部必要条件，再构造同时达到所有条件的对象。')],
(r'Find the least positive $k$ such that $3^4\mid10^k-1$.',r'求使 $3^4\mid10^k-1$ 的最小正整数 $k$。'),[
(r'Here $3\mid10-1$ and $3\nmid10$, so the odd-prime lifting hypotheses hold.',r'这里 $3\mid10-1$ 且 $3\nmid10$，满足奇质数赋值提升条件。'),
(r'Therefore $v_3(10^k-1)=v_3(9)+v_3(k)=2+v_3(k)$.',r'因此 $v_3(10^k-1)=v_3(9)+v_3(k)=2+v_3(k)$。'),
(r'The exact requirement is $9\mid k$, whose least positive solution is $k=9$.',r'准确要求为 $9\mid k$，最小正解为 $k=9$。')],
('The lifting formula for odd primes is not a general substitute for the special $p=2$ formula.','奇质数赋值提升公式不能直接替代 $p=2$ 的特殊公式。'),
'2020-I-Q12 2025-I-Q15 2026-II-Q13 2014-II-Q15',('NT04',),[
(r'For odd $p$, write $A=B+pc$ and expand. If $p\nmid k$, the first binomial term has the least valuation; replacing $k$ by $pk$ raises the valuation by one. Factoring $k=p^e u$ proves the displayed lifting rule. At $p=3$ for cubes, this also shows that two unit inputs congruent modulo $3^6$ have cubes congruent modulo $3^7$, while the induced map on the relevant residue representatives is injective.',r'对奇质数 $p$，写 $A=B+pc$ 后展开；当 $p\nmid k$ 时，首个二项式项赋值最低，将 $k$ 换为 $pk$ 则赋值增加一。写 $k=p^eu$ 即得所述公式。对 $p=3$ 的立方，这还表明模 $3^6$ 相等的单位输入之立方模 $3^7$ 相等，而相关代表元所诱导的立方映射为单射。'),
(r'For product $N=\prod f_i$ with cost $\sum(f_i-1)$, splitting $gh$ into $g,h>1$ reduces cost by $(g-1)(h-1)>0$. Thus a minimum splits completely into prime factors. This is a cost theorem only after the combinatorial construction has proved that the factors act independently.',r'若乘积 $N=\prod f_i$ 的代价为 $\sum(f_i-1)$，将 $gh$ 拆成 $g,h>1$ 可减少 $(g-1)(h-1)>0$。故最小代价必须完全拆成质因数；但只有先证明组合构造的各因子独立，这一代价定理才能适用。'),
(r'A prime-index update can encode binary carries: if a state contains each prime at most once, removing all primes before the first missing prime and inserting that prime implements an increment of its binary indicator. Prove squarefreeness and this invariant by induction before decoding an index.',r'质数索引更新可编码二进制进位：若每个质数最多出现一次，删除首个缺失质数前的全部质数并加入该质数，就使其二元指示数加一。解码下标之前须归纳证明无平方因子性与此不变量。')]))
ms[0]['question_ids']+=['AIME-2002-II-Q07','AIME-2015-I-Q13']
ms[2]['question_ids'].remove('AIME-2015-I-Q13')
ms[4]['question_ids']+=['AIME-2013-I-Q11','AIME-2004-I-Q15']
ms[0]['question_ids'].remove('AIME-2021-II-Q15')
save(C,('Prime exponents turn multiplicative conditions into independent arithmetic constraints. Use exact valuation rules for divisibility, parity for powers, and a certified bound before any finite search.','质指数可把乘法条件化为独立的算术限制：整除用精确赋值，幂次用指数奇偶，有限搜索之前先证明界。'),ms,('NT02',))

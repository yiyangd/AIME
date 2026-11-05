from knowledge_helpers_source import method as M,save
C='NT08';ms=[]
ms.append(M(C,1,'Count and sum divisors by independent prime exponents','以独立质指数统计约数及约数和',[
(r'Factor $N=\prod p^{e_p}$ and list each exponent choice $0,1,\ldots,e_p$.',r'分解 $N=\prod p^{e_p}$，每个质数指数可选 $0,1,\ldots,e_p$。'),
(r'Use $\tau(N)=\prod(e_p+1)$ and $\sigma(N)=\prod(1+p+\cdots+p^{e_p})$.',r'使用 $\tau(N)=\prod(e_p+1)$ 与 $\sigma(N)=\prod(1+p+\cdots+p^{e_p})$。'),
(r'If only certain exponents are allowed, replace each local factor by that permitted count or sum.',r'若只允许某些指数，将每个局部因子替换为允许指数的个数或幂和。'),
(r'Only after the exact divisor count is known should it be inserted into a probability or a later equation.',r'明确精确约数数目之后，才代入概率或后续方程。')],
(r'For $N=2^4 3^2$, count its square divisors and find their sum.',r'对 $N=2^4 3^2$，求平方约数的个数及其总和。'),[
(r'Square exponents are $0,2,4$ for two and $0,2$ for three, so there are $3\cdot2=6$ square divisors.',r'二的平方指数为 $0,2,4$，三的为 $0,2$，所以共有 $3\cdot2=6$ 个平方约数。'),
(r'The sum factors as $(1+2^2+2^4)(1+3^2)$.',r'其和分解为 $(1+2^2+2^4)(1+3^2)$。'),
(r'The value is $21\cdot10=210$.',r'结果为 $21\cdot10=210$。')],
('Restrictions belong on exponents; listing divisors is usually unnecessary.','限制应施加于指数，通常无需逐个列约数。'),
'2005-I-Q02 2010-I-Q01 2011-I-Q07 2019-II-Q03 2023-I-Q04 2023-II-Q10 2026-I-Q06 2026-I-Q08',('NT01',)))
ms.append(M(C,2,'Invert a divisor count into prime-exponent patterns','将约数个数反解为质指数模式',[
(r'Write the required count as a product of factors $e_i+1>1$.',r'将指定约数个数写成若干 $e_i+1>1$ 的乘积。'),
(r'List every multiplicative partition, then impose prime restrictions and numerical bounds.',r'列出全部乘法拆分，再施加质数限制与数值界。'),
(r'To minimize an integer with fixed exponents, assign larger exponents to smaller primes; swapping proves this rule.',r'固定指数求最小整数时，将较大指数配较小质数；交换可证明此规则。'),
(r'For constrained divisors of a large power, check that every recovered exponent lies in the original range.',r'对大幂的受限约数，核对每个还原指数均在原范围内。')],
(r'Find the least positive integer with exactly eight positive divisors.',r'求恰有八个正约数的最小正整数。'),[
(r'The exponent patterns are $7$, $(3,1)$ and $(1,1,1)$, from $8$, $4\cdot2$ and $2\cdot2\cdot2$.',r'由 $8,4\cdot2,2\cdot2\cdot2$ 得指数模式 $7,(3,1),(1,1,1)$。'),
(r'Their least values are $2^7=128$, $2^3\cdot3=24$ and $2\cdot3\cdot5=30$.',r'各模式最小值为 $2^7=128,2^3\cdot3=24,2\cdot3\cdot5=30$。'),
(r'The minimum is $24$, with divisor count $(3+1)(1+1)=8$.',r'最小值为 $24$，其约数数为 $(3+1)(1+1)=8$。')],
('Include repeated exponents and the case of a single prime power.','须包含重复指数与只有一个质数幂的情形。'),
'2000-II-Q04 2004-II-Q08 2005-I-Q03 2006-II-Q13 2019-I-Q09 2019-II-Q09',('NT01','NT05'),[
(r'For consecutive integers with a small prescribed sum of divisor counts, classify the possible count pairs first. A count of three forces a prime square, five forces a prime fourth power, and four forces $p^3$ or $pq$. This turns a long integer search into a bounded search around prime powers.',r'相邻整数的约数数目之和为小定值时，先分类可能的计数对。约数数为三迫使质数平方，为五迫使质数四次幂，为四迫使 $p^3$ 或 $pq$。这能把很长的整数搜索化为质数幂附近的有界搜索。')]))
ms.append(M(C,3,'Characterize divisor counts of kth powers','刻画 k 次幂的约数个数',[
(r'If $a=\prod p_i^{e_i}$, then $\tau(a^k)=\prod(ke_i+1)$.',r'若 $a=\prod p_i^{e_i}$，则 $\tau(a^k)=\prod(ke_i+1)$。'),
(r'Every factor is one modulo $k$, giving a necessary congruence on the divisor count.',r'每个因子都模 $k$ 余一，从而得到约数个数的必要同余。'),
(r'To prove sufficiency, realize a count $N=ke+1$ using a single prime power $a=p^e$, including $e=0$.',r'证明充分性时，用单一质数幂 $a=p^e$ 实现个数 $N=ke+1$，并包括 $e=0$。')],
(r'Which positive integers can be the number of divisors of an integer fourth power?',r'哪些正整数可以是某整数四次幂的正约数个数？'),[
(r'Every such count is $\prod(4e_i+1)\equiv1\pmod4$.',r'每个这样的个数均为 $\prod(4e_i+1)\equiv1\pmod4$。'),
(r'Conversely, for $N=4e+1$, the fourth power of $2^e$ has exactly $4e+1=N$ divisors.',r'反之，对 $N=4e+1$，$2^e$ 的四次幂恰有 $4e+1=N$ 个约数。'),
(r'Thus exactly the positive integers congruent to one modulo four occur, including one from the integer one.',r'所以恰为模四余一的正整数，包括整数一产生的个数一。')],
('Necessity from a product congruence needs a separate realization for sufficiency.','乘积同余给出的必要性，须另给实现才能证明充分性。'),
'2016-II-Q11',('NT03',)))
ms.append(M(C,4,'Count coprime classes with the totient and a symmetry pairing','用欧拉函数与对称配对统计互质类',[
(r'For $N=\prod p^e$, inclusion-exclusion gives $\varphi(N)=N\prod_{p\mid N}(1-1/p)$.',r'对 $N=\prod p^e$，容斥给出 $\varphi(N)=N\prod_{p\mid N}(1-1/p)$。'),
(r'When an interval contains full residue periods, count those periods and then the boundary remainder.',r'区间含完整剩余周期时，先数完整周期，再处理边界余段。'),
(r'Before halving a count by $a\leftrightarrow N-a$, prove the map has no fixed admissible element.',r'用 $a\leftrightarrow N-a$ 将个数减半前，证明没有合格不动点。'),
(r'If some primes may divide the numerator, partition by those primes and apply the largest permitted coprime denominator bound.',r'若某些质数允许整除分子，按这些质数分类，并施加最大允许互质分母界。')],
(r'Choose a residue uniformly from $0,\ldots,29$. Given that it is odd, what is the probability it has a multiplicative inverse modulo $30$?',r'从 $0,\ldots,29$ 等可能选一个剩余。已知它是奇数，其模 $30$ 可逆的概率是多少？'),[
(r'Invertibility means coprimality with $30=2\cdot3\cdot5$.',r'可逆等价于与 $30=2\cdot3\cdot5$ 互质。'),
(r'There are $\varphi(30)=30(1-1/2)(1-1/3)(1-1/5)=8$ invertible residues, all odd.',r'可逆剩余有 $\varphi(30)=30(1-1/2)(1-1/3)(1-1/5)=8$ 个，且全为奇数。'),
(r'The conditioning leaves fifteen odd residues, so the probability is $8/15$.',r'条件下共有十五个奇数剩余，故概率为 $8/15$。')],
('Totient counts all coprime residues, not automatically only half of an interval.','欧拉函数统计全部互质剩余，并非自动给出某区间的一半。'),
'2004-I-Q08 2014-I-Q03 2022-I-Q13',('NT02','CO04')))
ms.append(M(C,5,'Use divisor pairing to track parity through square blocks','用约数配对按平方区块追踪奇偶',[
(r'Pair every divisor $d$ with $n/d$; an unpaired divisor exists exactly when $n$ is square.',r'把每个约数 $d$ 与 $n/d$ 配对；仅平方数有未配对约数。'),
(r'Therefore $\tau(n)$ is odd exactly at squares, and a cumulative divisor-count sum changes parity only there.',r'因此 $\tau(n)$ 恰在平方数时为奇数，累积约数计数和也仅在此改变奇偶。'),
(r'Count entire intervals between consecutive squares and then the final partial interval.',r'统计连续平方数之间的完整区间，再处理最后不完整区间。')],
(r'Among $1\le n\le20$, for how many $n$ is $\sum_{j=1}^n\tau(j)$ odd?',r'在 $1\le n\le20$ 中，有多少个 $n$ 使 $\sum_{j=1}^n\tau(j)$ 为奇数？'),[
(r'The parity is the parity of the number of squares at most $n$, namely $\lfloor\sqrt n\rfloor$.',r'其奇偶等于不超过 $n$ 的平方数数目，即 $\lfloor\sqrt n\rfloor$ 的奇偶。'),
(r'Odd square-root floors occur on $1\le n\le3$ and $9\le n\le15$.',r'平方根下取整为奇数的区间是 $1\le n\le3$ 与 $9\le n\le15$。'),
(r'These contain $3+7=10$ integers.',r'共含 $3+7=10$ 个整数。')],
('A square switches the cumulative parity at the square itself.','累积奇偶从平方数本身起切换。'),
'2005-I-Q12',('AL06',)))
ms.append(M(C,6,'Intersect divisor sets with gcds and use multiplicativity carefully','以最大公因数求约数集交，并谨慎使用积性',[
(r'Divisors common to several integers are exactly divisors of their gcd.',r'若干整数的公共约数恰为其最大公因数的约数。'),
(r'Count unions by inclusion-exclusion, including the divisor one in every intersection.',r'用容斥统计并集，并在每个交集中包括约数一。'),
(r'For $\sigma$ or $\tau$ of a product, multiply values only when the factors are coprime, or merge their prime exponents first.',r'乘积的 $\sigma$ 或 $\tau$ 只有在因子互质时才可相乘，否则须先合并质指数。')],
(r'How many positive integers divide $18$ or $24$?',r'有多少正整数整除 $18$ 或 $24$？'),[
(r'$\tau(18)=(1+1)(2+1)=6$ and $\tau(24)=(3+1)(1+1)=8$.',r'$\tau(18)=(1+1)(2+1)=6,\tau(24)=(3+1)(1+1)=8$。'),
(r'The intersection is the divisor set of $\gcd(18,24)=6$, containing $\tau(6)=4$ values.',r'交集为 $\gcd(18,24)=6$ 的约数集，有 $\tau(6)=4$ 个值。'),
(r'The union count is $6+8-4=10$.',r'并集个数为 $6+8-4=10$。')],
('The functions are multiplicative on coprime inputs, not on every product.','这些函数只对互质输入具有积性，并非对任意乘积都可相乘。'),
'2005-II-Q04 2021-I-Q14',('NT02','CO04','NT04')))
ms.append(M(C,7,'Regroup a positive series into divisor coefficients and bound its tail','把正项级数重组为约数系数，并估计尾项',[
(r'Expand each geometric denominator into a nonnegative series. Nonnegativity justifies regrouping by exponent.',r'把每个等比分母展开为非负级数；非负性允许按指数重组。'),
(r'An exponent $n$ receives one contribution for each factorization $n=jk$, giving coefficient $\tau(n)$.',r'指数 $n$ 对每种 $n=jk$ 的分解得到一次贡献，因此系数为 $\tau(n)$。'),
(r'After scaling by a base power, separate the integral prefix from the tail and prove the tail is below the next integer before reading digits.',r'乘以底数幂后，将整数前缀与尾项分开；读取数位之前先证明尾项未达到下一整数。'),
(r'Use an elementary bound such as $\tau(n)\le n$ for distant terms, while calculating the first few tail coefficients exactly.',r'对远处项使用 $\tau(n)\le n$ 等简单界，对尾项开头若干系数则精确计算。')],
(r'For $T=\sum_{k\ge1}1/(100^k-1)$, identify the coefficient of $100^{-6}$ and prove $T<1$.',r'对 $T=\sum_{k\ge1}1/(100^k-1)$，求 $100^{-6}$ 的系数，并证明 $T<1$。'),[
(r'Expand $1/(100^k-1)=\sum_{j\ge1}100^{-kj}$. Exponent six arises from $k=1,2,3,6$, so its coefficient is four.',r'展开 $1/(100^k-1)=\sum_{j\ge1}100^{-kj}$。指数六来自 $k=1,2,3,6$，故系数为四。'),
(r'Thus $T=\sum_{n\ge1}\tau(n)100^{-n}\le\sum_{n\ge1}n100^{-n}$.',r'所以 $T=\sum_{n\ge1}\tau(n)100^{-n}\le\sum_{n\ge1}n100^{-n}$。'),
(r'The last sum equals $(1/100)/(1-1/100)^2=100/9801<1$.',r'最后一和为 $(1/100)/(1-1/100)^2=100/9801<1$。')],
('Coefficients exceeding the base may carry; a series coefficient is not automatically a digit.','系数超过底数时会进位，级数系数并不自动等于数位。'),
'2026-II-Q09',('AL05',)))
save(C,('Divisor functions are products of local exponent choices. Learn the formulas together with their inverse patterns, parity exceptions, coprimality restrictions and exact tail bounds; these are what make the formulas useful in contest questions.','约数函数是局部指数选择的乘积。公式须与反向指数模式、奇偶例外、互质限制及精确尾项界一起掌握，才能在竞赛题中真正使用。'),ms,('NT01','NT02'))

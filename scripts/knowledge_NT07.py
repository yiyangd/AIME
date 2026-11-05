from knowledge_helpers_source import method as M,save
C='NT07';ms=[]
ms.append(M(C,1,'Convert a repeating block to an exact fraction','将循环节转为精确分数',[
(r'If a length-$k$ block represents integer $A$ in base $b$, then $0.\overline{A}_b=A/(b^k-1)$.',r'若底数 $b$ 下长度 $k$ 的块表示整数 $A$，则 $0.\overline{A}_b=A/(b^k-1)$。'),
(r'Leading zeroes in the block are legal; a shorter actual period may still be represented by the full block.',r'循环块开头允许零，实际周期较短者仍可用完整循环块表示。'),
(r'For sums over digit permutations, count how often each digit occupies each position before reducing fractions.',r'对数位排列求和时，先统计每个数字在每个位置的出现次数，再约分。')],
(r'Find the sum of $0.\overline{12}$, $0.\overline{21}$ and $0.\overline{03}$.',r'求 $0.\overline{12},0.\overline{21},0.\overline{03}$ 之和。'),[
(r'The common denominator for a two-digit block is $99$.',r'两位循环块的共同分母为 $99$。'),
(r'The numerators are $12,21,3$, including the leading-zero block $03$.',r'分子为 $12,21,3$，其中包括开头为零的循环块 $03$。'),
(r'The sum is $36/99=4/11$.',r'和为 $36/99=4/11$。')],
('The block length is fixed even when its integer value has fewer digits.','即使循环块的整数值位数较少，循环块长度仍固定。'),
'2006-I-Q06 2014-II-Q04',('NT06','CO01')))
ms.append(M(C,2,'Control reduction with a gcd and denominator prime structure','用最大公因数与分母质因数结构控制约分',[
(r'Write $r=a/b$ in lowest terms and compute explicitly the gcd introduced by a multiplier or common denominator.',r'将 $r=a/b$ 写成既约形式，并明确计算乘数或公分母引入的最大公因数。'),
(r'After multiplying by $c$, the cancellation is $\gcd(c,b)$ because $\gcd(a,b)=1$.',r'乘以 $c$ 后，约分公因数为 $\gcd(c,b)$，因为 $\gcd(a,b)=1$。'),
(r'For an integrality condition, every prime-power in the reduced denominator must be supplied by the numerator; use valuation bounds to prove the first possible index.',r'整数条件要求分子提供既约分母的每个质数幂，用赋值界证明最早可能下标。'),
(r'With a fixed numerator-plus-denominator sum, replace their gcd by the gcd with that fixed sum.',r'若分子分母之和固定，可将其公因数改写为与固定和的公因数。')],
(r'A reduced fraction $a/b$ becomes a fraction with denominator $b/6$ after multiplication by $18$. Characterize $b$.',r'既约分数 $a/b$ 乘以 $18$ 后，最简分母为 $b/6$。刻画 $b$。'),[
(r'The new denominator is $b/\gcd(18,b)$, so the condition is $\gcd(18,b)=6$.',r'新分母为 $b/\gcd(18,b)$，所以条件为 $\gcd(18,b)=6$。'),
(r'Since $18=2\cdot3^2$, this requires $v_2(b)\ge1$ and $v_3(b)=1$; other primes are unrestricted.',r'因 $18=2\cdot3^2$，须 $v_2(b)\ge1,v_3(b)=1$，其他质数不受限制。'),
(r'Equivalently $b=6t$ with $3\nmid t$. Any $a$ coprime to such a $b$ realizes the stated cancellation.',r'等价于 $b=6t$ 且 $3\nmid t$；任取与该 $b$ 互质的 $a$ 均实现所述约分。')],
('Compute the cancellation gcd before comparing reduced numerators and denominators.','比较最简分子分母前，先算约分公因数。'),
'2006-II-Q14 2014-I-Q03 2023-II-Q05',('NT01','NT02','NT08')))
ms.append(M(C,3,'Characterize the possible reduced numerators using divisor denominators','用约数分母刻画可能的最简分子',[
(r'For fractions $k/N$, every reduced denominator is a divisor $D$ of $N$.',r'对分数 $k/N$，每个最简分母都是 $N$ 的约数 $D$。'),
(r'A positive numerator $m$ occurs exactly when some such $D$ satisfies $m\le D$ and $\gcd(m,D)=1$.',r'正分子 $m$ 出现，当且仅当某个这样的 $D$ 满足 $m\le D,\gcd(m,D)=1$。'),
(r'Partition $m$ by which primes of $N$ divide it. In each class choose the largest divisor of $N$ avoiding those primes, then count under that bound.',r'按 $N$ 的哪些质数整除 $m$ 分类。每类选避开这些质数的最大约数作分母，再在该上界下计数。')],
(r'Among $k/12$ for $1\le k\le12$, which positive reduced numerators occur?',r'在 $1\le k\le12$ 的 $k/12$ 中，会出现哪些正的最简分子？'),[
(r'If $m$ is coprime to $6$, choose denominator $12$; the allowed numerators are $1,5,7,11$.',r'若 $m$ 与 $6$ 互质，可取分母 $12$，得到 $1,5,7,11$。'),
(r'If $2\mid m$ but $3\nmid m$, the largest coprime divisor denominator is $3$, giving only $m=2$.',r'若 $2\mid m$ 而 $3\nmid m$，最大互质约数分母为 $3$，只得到 $m=2$。'),
(r'If $3\mid m$ but $2\nmid m$, denominator $4$ permits only $m=3$. A numerator divisible by both primes is too large for denominator one. Thus the set is $\{1,2,3,5,7,11\}$.',r'若 $3\mid m$ 而 $2\nmid m$，分母 $4$ 只允许 $m=3$。同时被两质数整除的分子对分母一而言太大。故集合为 $\{1,2,3,5,7,11\}$。')],
('Count distinct reduced numerators, not unreduced blocks or fraction representations.','应数不同最简分子，而非未约分循环块或分数表示。'),
'2022-I-Q13',('NT08','CO04')))
ms.append(M(C,4,'Use a decimal interval to bound a reduced denominator','用小数区间限制最简分母',[
(r'Turn a fixed length-$k$ prefix $A$ into $[A/10^k,(A+1)/10^k)$.',r'将固定长度 $k$ 的前缀 $A$ 转为 $[A/10^k,(A+1)/10^k)$。'),
(r'If the prefix begins later, shift the decimal and take the fractional part; its reduced denominator divides the original denominator.',r'若前缀在较后位置开始，移动小数点并取小数部分；其最简分母整除原分母。'),
(r'Compare with a nearby simple fraction and exploit a nonzero integer cross-product difference to get a lower bound.',r'与附近简单分数比较，并利用非零整数交叉乘积差得到下界。')],
(r'Prove no reduced fraction with denominator at most $10$ lies in $[0.501,0.510)$.',r'证明分母不超过 $10$ 的既约分数不可能位于 $[0.501,0.510)$。'),[
(r'Such a fraction $m/n$ is strictly above $1/2$, so $2m-n\ge1$.',r'这样的分数 $m/n$ 严格大于 $1/2$，所以 $2m-n\ge1$。'),
(r'Its distance above $1/2$ is at least $1/(2n)\ge1/20=0.05$.',r'它与 $1/2$ 的距离至少为 $1/(2n)\ge1/20=0.05$。'),
(r'But the stated interval requires that distance be below $0.010$. This contradiction excludes every such denominator.',r'而给定区间要求该距离小于 $0.010$，矛盾，故排除所有这些分母。')],
('The strict upper endpoint is essential when the next decimal prefix begins there.','右端点正是下一小数前缀开始处，严格性不可忽略。'),
'2003-I-Q14',('NT05',)))
ms.append(M(C,5,'Locate the unique least valuation in a rational sum','定位有理和中唯一最低赋值项',[
(r'Reduce each summand and compare its exponent of a chosen prime in the denominator.',r'约分每项，并比较所选质数在分母中的指数。'),
(r'Clear the largest denominator power. If exactly one resulting numerator is a unit modulo the prime, the total cannot cancel that prime.',r'清除最大分母幂。若所得分子中恰有一项模该质数为单位，则总和不能约去该质数。'),
(r'Compute the exact surviving denominator exponent; use a factorial valuation formula when needed.',r'算出保留的精确分母指数，必要时使用阶乘赋值公式。')],
(r'Find the power of $2$ in the reduced denominator of $1/2+3/8+5/32$.',r'求 $1/2+3/8+5/32$ 的最简分母中 $2$ 的指数。'),[
(r'The common denominator is $32$, giving numerator $16+12+5$.',r'共同分母为 $32$，分子为 $16+12+5$。'),
(r'Only the last contribution is odd, so the total numerator $33$ is odd.',r'只有最后一项贡献为奇数，故总分子 $33$ 为奇数。'),
(r'No two-factor cancellation occurs: the reduced denominator remains $32=2^5$.',r'不能约去任何因子二，所以最简分母仍为 $32=2^5$。')],
('If two terms share the lowest valuation, cancellation may occur and needs another analysis.','若两项共享最低赋值，则可能相消，须另作分析。'),
'2009-II-Q07',('NT01',)))
save(C,('A fraction problem is usually controlled by reduction, not by decimal approximation. Keep denominators exact, identify the cancellation gcd, and separate distinct values from different representations of the same value.','分数题通常由约分控制，而非小数近似控制。保留精确分母，确定约分公因数，并区分不同数值与同一数值的不同表示。'),ms,('NT01','NT02'))

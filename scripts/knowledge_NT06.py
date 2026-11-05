from knowledge_helpers_source import method as M,save
C='NT06';ms=[]
ms.append(M(C,1,'Expand place values and enforce the common digit range','展开位值并施加共同数位范围',[
(r'Write a base-$b$ numeral as $\sum d_i b^i$, with fractional positions using negative powers.',r'把 $b$ 进制数写成 $\sum d_i b^i$，小数位使用负指数。'),
(r'A digit shared between bases must be valid in every base in which it occurs; each leading digit is nonzero.',r'跨进位制共用数字须在每个出现的进位制中有效，且每个首位非零。'),
(r'Eliminate variables, use a small congruence or a power bound, then test the remaining digits exactly.',r'消元后使用小模数或幂的范围界，再精确检查剩余数字。'),
(r'When all digits are nonnegative, compare the value monotonically as the base changes.',r'所有数位非负时，可按底数变化单调比较数值。')],
(r'The numeral $\overline{1d2}_b$ has value $2b^2$ for an integer base $b>2$. Find all valid $(b,d)$.',r'整数底数 $b>2$ 下，数码 $\overline{1d2}_b$ 的值为 $2b^2$。求全部有效 $(b,d)$。'),[
(r'Place value gives $b^2+db+2=2b^2$, or $b(b-d)=2$.',r'位值给出 $b^2+db+2=2b^2$，即 $b(b-d)=2$。'),
(r'Because $0\le d<b$, the integer $b-d$ is positive, so $b$ must divide $2$.',r'因 $0\le d<b$，整数 $b-d$ 为正，故 $b$ 须整除 $2$。'),
(r'This contradicts $b>2$. There are no valid digit/base pairs.',r'这与 $b>2$ 矛盾，故无有效数位底数对。')],
('A decimal-looking symbol is a digit string until its base has been specified.','外观像十进制数的符号，在底数确定前只是数位串。'),
'2001-I-Q08 2001-I-Q01 2004-I-Q01 2009-I-Q01 2017-I-Q05 2018-I-Q02 2018-II-Q03 2020-I-Q03 2022-I-Q02 2025-I-Q01 2026-II-Q04 2024-II-Q14',('AL01','NT05')))
ms.append(M(C,2,'Isolate a prefix or suffix and reduce digit changes modulo a divisor','隔离前缀或后缀，并对数位变化取模',[
(r'For a suffix of length $k$, write $N=b^k q+r$ with $0\le r<b^k$.',r'对长度为 $k$ 的后缀，写 $N=b^kq+r$，其中 $0\le r<b^k$。'),
(r'Deletion or replacement changes a known place-value term; reduce the resulting equation or divisibility before enumerating.',r'删位或替换数位会改变已知位值项；枚举之前先约化所得方程或整除式。'),
(r'For a square suffix, solve the congruence for its root modulo prime powers and order the roots, not the suffixes.',r'平方数后缀题应按质数幂求根的同余，并给根排序，而非仅给后缀排序。'),
(r'Check leading zeros, positivity of the remaining prefix and any boundary block separately.',r'单独检查首位零、剩余前缀正性及边界区块。')],
(r'If $100q+37$ is divisible by $7$, find $q\pmod7$. Can $100q+12$ also be divisible by $7$?',r'若 $100q+37$ 可被 $7$ 整除，求 $q$ 模 $7$ 的剩余。$100q+12$ 也能被 $7$ 整除吗？'),[
(r'Modulo seven, $100q+37\equiv2q+2$, so $q\equiv-1\equiv6$.',r'模七有 $100q+37\equiv2q+2$，所以 $q\equiv-1\equiv6$。'),
(r'The two integers differ by $25$, which is not divisible by seven.',r'两整数之差为 $25$，不能被七整除。'),
(r'Thus they cannot both be divisible by seven. In fact $100q+12\equiv2\cdot6+5\equiv3\pmod7$.',r'因此它们不能同时被七整除；实际 $100q+12\equiv2\cdot6+5\equiv3\pmod7$。')],
('A suffix may contain initial zeroes even though the whole numeral may not.','后缀允许开头为零，整个整数的首位则不允许。'),
'2000-I-Q01 2006-I-Q03 2008-I-Q07 2012-I-Q10 2014-I-Q08 2020-I-Q04 2024-II-Q07',('NT02','NT03'),[
(r'For blocks $[b^kq,b^k(q+1)-1]$, power-gap analysis (NT05) decides whether a square can occur. Separate the range where every block contains a square from the range where each block contains at most one; only then count empty blocks.',r'对区块 $[b^kq,b^k(q+1)-1]$，幂间隔分析（NT05）决定是否有平方数。须分开每块必含平方数的范围与每块至多含一个的范围，才可统计空区块。')]))
ms.append(M(C,3,'Use reversal and palindrome symmetry before counting digits','计数前先使用翻转与回文对称',[
(r'Expand a numeral and its reversal; paired places often cancel or acquire equal coefficients.',r'展开原数及其翻转，成对位值常会消去或得到相同系数。'),
(r'A palindrome is determined by its left half and, for odd length, its center digit.',r'回文数由左半部分及奇数长度时的中央数字决定。'),
(r'Apply nonzero-leading and digit-sum parity restrictions, then count the independent positions.',r'施加首位非零与数位和奇偶限制，再统计独立位置。'),
(r'For averages, average each free digit separately; for two bases, first bound the possible lengths.',r'求平均时分别平均每个自由数字；跨进位制时先限制可能长度。')],
(r'How many three-digit decimal palindromes are divisible by $3$, and what is their mean?',r'有多少个三位十进制回文数可被 $3$ 整除？它们的平均数是多少？'),[
(r'Write $N=101a+10b$, with $1\le a\le9,0\le b\le9$. Divisibility requires $2a+b\equiv0\pmod3$.',r'写 $N=101a+10b$，其中 $1\le a\le9,0\le b\le9$。整除要求 $2a+b\equiv0\pmod3$。'),
(r'For $a\equiv0$ there are four possible $b$; for the other two classes there are three. Each $a$ class has three members, giving $3\cdot4+6\cdot3=30$.',r'$a\equiv0$ 时 $b$ 有四种，另两类各三种；每类 $a$ 有三个值，故共 $3\cdot4+6\cdot3=30$ 个。'),
(r'Over these thirty choices, $\sum a=3(1+\cdots+9)+(3+6+9)=153$, while the three residue classes give $\sum b=3(18+12+15)=135$. The mean is $(101\cdot153+10\cdot135)/30=5601/10$.',r'这三十组选取中，$\sum a=3(1+\cdots+9)+(3+6+9)=153$，三类剩余给出 $\sum b=3(18+12+15)=135$。平均数为 $(101\cdot153+10\cdot135)/30=5601/10$。')],
('Do not impose distinct digits unless the question says so.','题目未要求时，不应额外施加数字互异。'),
'2002-I-Q03 2002-II-Q01 2012-I-Q01 2021-II-Q01 2023-II-Q02 2026-I-Q02',('CO03','PS06')))
ms.append(M(C,4,'Make carries explicit in column sums and digit-sum changes','明确逐列进位与数位和变化',[
(r'Write one equation per column, introducing the carry entering and leaving it.',r'每列写一式，设置进入与离开的进位。'),
(r'In base $b$, every carry reduces the naive digit sum by $b-1$; include carries created by incoming carries.',r'$b$ 进制中每次进位使原始数位和减少 $b-1$，并须计入由前列进位诱发的进位。'),
(r'Translate fixed totals into constraints on column digit sums, then optimize or count their allowed digit assignments.',r'把固定总数转为各列数位和限制，再优化或统计允许数位分配。'),
(r'Verify the complete numeral at the end, including any new leading carry.',r'末尾检验整个数值，包括新产生的最高位进位。')],
(r'For binary integers of fixed length, characterize when adding one leaves the number of ones unchanged.',r'对固定长度二进制整数，刻画何时加一后的一位数目保持不变。'),[
(r'If the number ends in $t$ ones, adding one changes those $t$ ones to zeroes and the preceding zero to one.',r'若末尾连续有 $t$ 个一，加一会把它们变成零，并把此前的零变成一。'),
(r'The net change in weight is $1-t$. Equality of weights requires exactly one trailing one.',r'一的数目净变化为 $1-t$，保持不变要求恰有一个末尾一。'),
(r'Thus the numeral must end in $01$ and become a numeral ending in $10$; an overflow from an all-one string cannot qualify.',r'故原数须以 $01$ 结尾，更新后以 $10$ 结尾；全一串的溢出不合格。')],
('Count carry events, not the number of columns whose original digit sum exceeds the base.','应统计实际进位事件，不能只数原数位和超过底数的列。'),
'2006-II-Q07 2012-I-Q05 2015-I-Q08 2016-I-Q08 2019-I-Q01 2024-II-Q03 2010-I-Q10',('CO01','AL01')))
ms.append(M(C,5,'Count and unrank digit strings under an upper bound','统计并反向定位上界内的数位串',[
(r'Count shorter lengths first, fixing a nonzero leading digit unless zero padding is explicitly allowed.',r'先统计较短长度；除非明确允许补零，首位须非零。'),
(r'For equal lengths, scan from the leading position and count all allowed smaller-prefix blocks before following the bound.',r'等长时从高位扫描，先统计所有允许的较小前缀块，再沿上界前缀继续。'),
(r'For a specified rank, subtract entire block counts until the desired rank lies in one block, then continue recursively.',r'给定排名时，逐块减去完整块数，直到目标位于某块，再递归处理。'),
(r'Use binomial coefficients for a fixed digit weight and handle partial final blocks exactly.',r'固定数位重数时用二项式系数，并精确处理最后不完整块。')],
(r'List the fifth nonnegative binary string of length six with exactly two ones, when strings are ordered by value.',r'六位二进制串（允许前补零）恰有两个一，按数值排序的第五个是什么？'),[
(r'The first four are $000011,000101,000110,001001$. A prefix block can be counted by choosing remaining one positions.',r'前四个为 $000011,000101,000110,001001$；每个前缀块的大小可由剩余一的位置选择数求出。'),
(r'Among strings beginning $00$, those beginning $000$ contribute $\binom32=3$, and the next prefix $001$ contributes $\binom31=3$.',r'在以 $00$ 开头的串中，前缀 $000$ 贡献 $\binom32=3$，随后前缀 $001$ 贡献 $\binom31=3$。'),
(r'Rank five is the second member of the latter block: $001010_2=10$.',r'第五名是后块第二个：$001010_2=10$。')],
('Numerical order equals lexicographic order only after the length is fixed.','只有固定长度后，数值顺序才等于字典序。'),
'2003-I-Q13 2012-II-Q07 2017-II-Q04 2004-II-Q10',('CO02','NT04')))
ms.append(M(C,6,'Optimize a numeral by digit mass and lexicographic priority','按数位质量与字典序优先级优化整数',[
(r'Compare lengths first: every valid longer positive numeral exceeds every shorter one.',r'先比较长度：每个有效的更长正整数都大于较短者。'),
(r'For a minimum with a prescribed digit sum, use the fewest positions and place as much mass as possible in low positions.',r'给定数位和求最小时，使用最少位数，并尽量把数位质量放在低位。'),
(r'For a maximum with suffix constraints, maximize the earliest digit whose choice still permits a valid completion.',r'带后缀限制求最大时，优先最大化仍允许合法补全的最早一位。'),
(r'Use divisibility or geometric-progression constraints to certify that no rejected earlier prefix can work.',r'用整除或等比限制证明被舍弃的更优前缀均不可能。')],
(r'Find the smallest base-five numeral with digit sum $11$.',r'求数位和为 $11$ 的最小五进制正整数。'),[
(r'Two positions hold digit sum at most $8$, so at least three positions are needed.',r'两位的数位和至多为 $8$，故至少需要三位。'),
(r'To minimize the leading digit, the two lower digits should total as much as possible, namely eight. The leading digit is therefore three.',r'为最小化首位，低两位应合计最大值八，所以首位为三。'),
(r'The unique minimum is $344_5=99$; any larger length or earlier larger digit increases the value.',r'唯一最小值为 $344_5=99$；更长位数或更大高位均会增大数值。')],
('A greedy prefix choice needs a feasible completion, not just an attractive leading digit.','贪心选择前缀须有合法补全，不能只看首位大小。'),
'2003-II-Q02 2009-I-Q01 2010-II-Q01 2015-II-Q03 2020-II-Q05',('NT03','LO02')))
ms.append(M(C,7,'Model local digit rules by a directed transition graph','用有向转移图建模局部数位规则',[
(r'Use digits or the necessary recent-digit memory as states, and draw every allowed next-digit transition.',r'以数字或所需最近数位记忆为状态，画出每个允许后继转移。'),
(r'For a largest unrestricted-length numeral, check whether a reachable directed cycle permits arbitrarily long strings.',r'位数不受限求最大数时，先检查可达有向循环是否允许任意长串。'),
(r'For a fixed length, count paths by a recurrence or by a uniform predecessor count; enforce the initial nonzero rule.',r'固定位数时，以递推或统一前驱数统计路径，并施加首位非零。')],
(r'Count four-digit binary strings with no adjacent ones, allowing initial zeros.',r'统计无相邻一的四位二进制串，允许前补零。'),[
(r'Use the last digit as the state. A zero permits either next digit; a one permits only zero.',r'以末位为状态；零允许后接零或一，一只允许后接零。'),
(r'If $a_n$ is the total count, final zero contributes $a_{n-1}$ and final $01$ contributes $a_{n-2}$. Thus $a_n=a_{n-1}+a_{n-2}$.',r'设总数为 $a_n$，以零结尾贡献 $a_{n-1}$，以 $01$ 结尾贡献 $a_{n-2}$，故 $a_n=a_{n-1}+a_{n-2}$。'),
(r'With $a_0=1,a_1=2$, the counts are $a_2=3,a_3=5,a_4=8$.',r'初值 $a_0=1,a_1=2$，得 $a_2=3,a_3=5,a_4=8$。')],
('Counting an acyclic longest path differs from counting all paths of a fixed length.','无环图的最长路径与固定长度全部路径是不同计数问题。'),
'2001-II-Q01 2007-II-Q06',('CO05','CO06')))
ms.append(M(C,8,'Prove uniqueness and carries in nonstandard positional systems','证明非标准位值系统的唯一性与进位',[
(r'Identify the legal digit range and the carry identity for the system.',r'确定系统的合法数位范围与进位恒等式。'),
(r'Reduce modulo the smallest radix to determine the final digit, subtract it and divide to prove uniqueness inductively.',r'模最低进位基数确定末位，减去后相除，以归纳证明唯一性。'),
(r'Use the carry rule to normalize signed digits or encode a combinatorial state, checking that supports do not overlap unexpectedly.',r'用进位规则规范带符号数位或编码组合状态，并检查数位支撑不会意外重叠。')],
(r'Write $8$ in balanced ternary, with digits $-1,0,1$, and explain why the last digit is forced.',r'把 $8$ 写成数位为 $-1,0,1$ 的平衡三进制，并说明末位为何被迫确定。'),[
(r'Modulo three, $8\equiv-1$, so its final balanced digit is $-1$.',r'模三有 $8\equiv-1$，故末位必为 $-1$。'),
(r'Subtracting and dividing gives $(8+1)/3=3$. Its last digit is zero, followed by leading one.',r'减去末位再相除得 $(8+1)/3=3$；它的末位为零，再往上为一。'),
(r'Thus $8=3^2-1$, with balanced digits $(1,0,-1)$. Repeating the forced-residue argument proves uniqueness.',r'所以 $8=3^2-1$，平衡数位为 $(1,0,-1)$；反复使用被迫剩余的论证可证明唯一性。')],
('Uniqueness comes from legal digit ranges; an arbitrary signed expansion need not be unique.','唯一性来自合法数位范围，任意带符号展开未必唯一。'),
'2000-II-Q14 2008-II-Q04 2014-II-Q15 2024-II-Q06',('NT01','AL05'),[
(r'Factorial digits satisfy $0\le f_i\le i$ because $(i+1)!= (i+1)i!$. The telescoping identity $a!-b!=\sum_{i=b}^{a-1}i\,i!$ produces a legal block of maximal digits; verify disjoint blocks before adding such expansions.',r'阶乘数位满足 $0\le f_i\le i$，因为 $(i+1)!=(i+1)i!$。望远镜恒等式 $a!-b!=\sum_{i=b}^{a-1}i\,i!$ 产生一块合法最大数位；叠加展开之前须验证各块不相交。'),
(r'A set-count or prime-index state may encode each allowed element by a binary bit. Prove the update changes trailing one-bits to zero and the next zero to one; the claimed index then follows by binary uniqueness, not by guessing successive terms.',r'集合计数或质数索引状态可用二进制位编码每个允许元素。须证明更新把末尾连续一变零、随后一个零变一；所求下标来自二进制唯一性，而非猜测逐项数值。')]))
ms.append(M(C,9,'Count digit patterns with leading-zero and multiplicity corrections','按首位零与重复数位修正数位模式计数',[
(r'Choose a pattern invariant: digit set, common digit sum, alternating order or palindrome half.',r'选择模式不变量：数字集合、共同数位和、交替大小或回文半串。'),
(r'Count each pattern before substituting actual digit values, separating whether zero is present.',r'代入实际数字值前先数模式，并区分是否含零。'),
(r'Apply bounded compositions or combinations only after checking that no digit exceeds its base limit; subtract repeated descriptions exactly once.',r'使用有界拆分或组合前，先核对数位不超过底数限制；重复描述只消除一次。')],
(r'How many two-digit decimal integers have digit sum $9$ and distinct digits?',r'有多少个两位十进制整数的数位和为 $9$ 且两位不同？'),[
(r'Write $10a+b$ with $1\le a\le9$ and $b=9-a$.',r'写为 $10a+b$，其中 $1\le a\le9,b=9-a$。'),
(r'Every such $a$ gives a valid digit $b$ in $0,\ldots,8$. Equality $a=b$ would require $2a=9$, impossible.',r'每个 $a$ 都给出 $0,\ldots,8$ 中有效数字 $b$；若 $a=b$ 则 $2a=9$，不可能。'),
(r'There are nine values. Zero is permitted in the units place, so $90$ is included.',r'共有九个值；个位允许零，故包括 $90$。')],
('Leading-zero restrictions act on positions; repeated-digit restrictions act on values.','首位零限制针对位置，重复数位限制针对数值。'),
'2003-I-Q09 2004-I-Q06 2004-II-Q04 2004-II-Q14 2013-I-Q02 2014-II-Q04 2024-II-Q03 2026-I-Q02',('CO01','CO02','CO03')))
ms.append(M(C,10,'Count each digit uniformly by zero-padding a full block','补零成完整区块以均匀统计各数位',[
(r'Write all integers from $0$ through $b^k-1$ as strings of exactly $k$ digits.',r'将 $0$ 到 $b^k-1$ 的整数全部写成恰有 $k$ 位的数位串。'),
(r'In any fixed position, each digit occurs exactly $b^{k-1}$ times; sum a digit contribution position by position.',r'每个固定位置上，各数字恰出现 $b^{k-1}$ 次；逐位求数字贡献之和。'),
(r'If leading zeroes have zero contribution they cause no change; otherwise correct them explicitly, and add or remove the interval endpoints.',r'若首补零贡献为零，则不改变结果；否则须明确修正，并增删区间端点。')],
(r'Find the sum of the decimal digit sums of all integers from $0$ through $999$.',r'求 $0$ 到 $999$ 各整数的十进制数位和之总和。'),[
(r'Pad every numeral to three digits; zero padding does not change its digit sum.',r'每个数补为三位，补零不会改变数位和。'),
(r'At each of three positions, every digit appears $100$ times and the digits total $45$.',r'三个位置的每一个位置上，每个数字出现 $100$ 次，而所有数字之和为 $45$。'),
(r'The total is $3\cdot100\cdot45=13500$.',r'所以总和为 $3\cdot100\cdot45=13500$。')],
('For reciprocal-digit sums, define the contribution of zero separately rather than divide by zero.','倒数数位和须单独定义零的贡献，不能除以零。'),
'2006-II-Q14',('NT01',)))
ms[1]['question_ids'].remove('AIME-2008-I-Q07')
ms[1]['extensions_en']=[];ms[1]['extensions_zh']=[]
save(C,('Expand the numeral before manipulating it, and distinguish digit values from their place weights. Digit bounds, leading zeros and carry behavior belong in the model from the first line.','运算前先展开数码，区分数字值与位权。数位范围、首位零与进位行为从建模第一行就应明确。'),ms,('NT02','NT03'))

from knowledge_helpers_source import method as M,save
C='NT04';ms=[]
ms.append(M(C,1,'Certify the multiplicative order before reducing exponents','约化指数前先确认乘法阶',[
(r'For $\gcd(a,m)=1$, define the order as the least positive $d$ with $a^d\equiv1\pmod m$.',r'当 $\gcd(a,m)=1$，乘法阶为使 $a^d\equiv1\pmod m$ 的最小正整数 $d$。'),
(r'Find a candidate exponent from a known group bound or direct calculation. For each prime $q\mid d$, verify $a^{d/q}\not\equiv1$ to certify exactness.',r'由群阶界或直接计算找候选指数。对每个质因数 $q\mid d$，检验 $a^{d/q}\not\equiv1$，以确认准确阶数。'),
(r'Then $a^n=1$ precisely when $d\mid n$; a prescribed minus-one power also constrains the two-part of $d$.',r'此后 $a^n=1$ 恰当 $d\mid n$；指定幂为负一还会限制 $d$ 的二因子部分。'),
(r'For prime moduli, use $d\mid p-1$ to restrict prime candidates, and verify the surviving prime.',r'质数模下以 $d\mid p-1$ 限制质数候选，再验证存活质数。')],
(r'Find the order of $3$ modulo $13$ and decide whether $13\mid3^{100}+1$.',r'求 $3$ 模 $13$ 的乘法阶，并判断 $13\mid3^{100}+1$ 是否成立。'),[
(r'$3^3=27\equiv1\pmod{13}$, while $3\not\equiv1$, so the order is exactly $3$.',r'$3^3=27\equiv1\pmod{13}$，而 $3\not\equiv1$，故阶恰为 $3$。'),
(r'Since $100\equiv1\pmod3$, one has $3^{100}\equiv3\pmod{13}$.',r'因 $100\equiv1\pmod3$，有 $3^{100}\equiv3\pmod{13}$。'),
(r'The expression is congruent to $4$, so divisibility fails. A power of odd order cannot equal $-1$ modulo an odd prime.',r'原式余 $4$，故不能整除；在奇质数模下，奇数阶的幂也不可能等于 $-1$。')],
('Euler gives an exponent that works; it need not be the least one.','欧拉定理给出可行指数，但未必是最小指数。'),
'2001-II-Q10 2002-I-Q07 2004-II-Q10 2019-I-Q14 2021-II-Q09',('NT03',),[
(r'If $a^m\equiv-1\pmod p$ for odd prime $p$, then the order divides $2m$ but not $m$. Therefore its two-adic valuation is exactly $v_2(m)+1$. Conversely, factor identities such as $x^{2t}-1$ and $x^{2t+1}+1$ can construct a common divisor; an order obstruction by itself proves only necessity.',r'若奇质数 $p$ 下 $a^m\equiv-1$，阶整除 $2m$ 却不整除 $m$，故其二赋值恰为 $v_2(m)+1$。反过来，可用 $x^{2t}-1$ 与 $x^{2t+1}+1$ 等分解恒等式构造公约数；单有阶的障碍只证明必要性。')]))
ms.append(M(C,2,'Prove a cycle by returning to the full determining state','回到完整决定状态来证明周期',[
(r'Identify how much information determines the next term: one residue, a pair, or a longer consecutive tuple.',r'确定下一项由多少信息决定：一个剩余、一对数，或更长连续元组。'),
(r'Compute successive full states until the initial or a later state repeats. A repeated output alone does not prove a cycle.',r'计算完整状态直到初始或后续状态重复；单个输出重复不能证明周期。'),
(r'Separate any nonperiodic prefix, then count complete cycles and the final partial cycle.',r'分开非周期前缀，再数完整周期与最后不完整周期。'),
(r'For a polynomial sequence, prove a period algebraically by showing its difference at shifted indices vanishes modulo the base.',r'多项式数列应通过证明平移下标后的差模底数为零来确认周期。')],
(r'Let $u_0=0,u_1=1$ and $u_{n+2}\equiv u_{n+1}+u_n\pmod2$. Find $u_{100}$.',r'设 $u_0=0,u_1=1,u_{n+2}\equiv u_{n+1}+u_n\pmod2$，求 $u_{100}$。'),[
(r'The determining pairs are $(0,1),(1,1),(1,0),(0,1)$.',r'决定状态对依次为 $(0,1),(1,1),(1,0),(0,1)$。'),
(r'The first pair returns after three updates, so the terms repeat $0,1,1$.',r'初始状态对三次更新后返回，故数列重复 $0,1,1$。'),
(r'Since $100\equiv1\pmod3$, the answer is $u_{100}=1$.',r'因 $100\equiv1\pmod3$，故 $u_{100}=1$。')],
('A recurrence of order k normally needs k consecutive residues as its state.','k 阶递推通常需要连续 k 个剩余组成状态。'),
'2017-I-Q03 2018-II-Q02 2023-II-Q13 2023-II-Q15',('AL05',)))
ms.append(M(C,3,'Split nonunit prefixes and use CRT for a composite modulus','分离不可逆前缀，并对合数模使用中国剩余定理',[
(r'Factor the modulus into prime powers. If the base shares a prime factor, first find when its power becomes zero locally.',r'将模数分为质数幂；底数若含相同质因数，先求其幂何时在该局部变为零。'),
(r'For the remaining unit parts, reduce exponents by a certified order or Euler period.',r'其余可逆部分，以确认的阶或欧拉周期约化指数。'),
(r'Combine local residues by CRT. For a sum of distinct residues, look for a fixed-point-free pairing such as $r\mapsto m-r$.',r'用中国剩余定理合并局部剩余。对不同剩余之和，可寻找 $r\mapsto m-r$ 等无不动点配对。')],
(r'Find $6^{20}\pmod{40}$.',r'求 $6^{20}$ 模 $40$ 的余数。'),[
(r'Modulo $8$, every power from the third onward is zero, so $6^{20}\equiv0$.',r'模 $8$ 时，从三次幂起均为零，故 $6^{20}\equiv0$。'),
(r'Modulo $5$, the base is one, so $6^{20}\equiv1$.',r'模 $5$ 时底数为一，故 $6^{20}\equiv1$。'),
(r'The unique residue modulo $40$ that is zero modulo $8$ and one modulo $5$ is $16$.',r'模 $40$ 唯一满足模 $8$ 余零、模 $5$ 余一的剩余为 $16$。')],
('Do not apply Euler to a base that is not coprime to the local modulus.','底数不与局部模数互质时不能使用欧拉定理。'),
'2011-I-Q11 2017-I-Q14',('NT03',)))
ms.append(M(C,4,'Lift an order or a root to a prime-square modulus','把阶或根提升到质数平方模',[
(r'Find the root or exact order modulo the prime first.',r'先求模该质数的根或准确乘法阶。'),
(r'For an order $d$, expand $(a^d)^t=(1+pc)^t$ modulo $p^2$; if $p\nmid c$, the order multiplies by $p$.',r'若模质数阶为 $d$，将 $(a^d)^t=(1+pc)^t$ 模 $p^2$ 展开；若 $p\nmid c$，则阶乘以 $p$。'),
(r'For a root $a$, write $a+pt$ and solve the resulting linear derivative congruence; inspect every initial root.',r'对根 $a$ 写成 $a+pt$，求所得导数线性同余，并检查每个初始根。'),
(r'For higher powers use an explicitly justified lifting valuation, and keep singular derivative cases separate.',r'更高次质数幂须使用已证明的赋值提升，并单列导数为零的奇异情形。')],
(r'Find the order of $2$ modulo $25$.',r'求 $2$ 模 $25$ 的乘法阶。'),[
(r'The order modulo $5$ is $4$, since $2^2=-1$ modulo $5$. Any order modulo $25$ is a multiple of $4$.',r'模 $5$ 的阶为 $4$，因 $2^2=-1$；所以模 $25$ 的阶必为 $4$ 的倍数。'),
(r'$2^{4t}=16^t=(1+15)^t\equiv1+15t\pmod{25}$.',r'$2^{4t}=16^t=(1+15)^t\equiv1+15t\pmod{25}$。'),
(r'This is one precisely when $5\mid t$, proving the least exponent is $20$.',r'它等于一当且仅当 $5\mid t$，故最小指数为 $20$。')],
('A root may lift uniquely even though its order calculation uses a different argument.','根的唯一提升与阶的计算可能需要不同论证。'),
'2018-I-Q11 2020-I-Q12 2024-I-Q13 2025-I-Q15',('NT01','NT03'),[
(r'For odd $p$, $p\mid A-B$ and $p\nmid AB$ imply $v_p(A^t-B^t)=v_p(A-B)+v_p(t)$. The binomial expansion proves the rule first for $p\nmid t$, then for each additional factor of $p$.',r'对奇质数 $p$，若 $p\mid A-B,p\nmid AB$，则 $v_p(A^t-B^t)=v_p(A-B)+v_p(t)$。先用二项式展开证明 $p\nmid t$ 的情况，再逐次加入 $p$ 因子即得。'),
(r'Cubing on units modulo powers of $3$ is singular: for units $a,b$ with $a\equiv b\pmod3$, $v_3(a^3-b^3)=v_3(a-b)+1$. Thus representatives modulo $3^k$ map injectively by cubing into the unit cube classes modulo $3^{k+1}$, precisely the classes congruent to $\pm1\pmod9$. The image has $2\cdot3^{k-1}$ elements, equal to the number of inputs.',r'模 $3$ 幂的单位立方映射是奇异情形：若单位 $a,b$ 满足 $a\equiv b\pmod3$，则 $v_3(a^3-b^3)=v_3(a-b)+1$。故模 $3^k$ 代表元的立方单射到模 $3^{k+1}$ 的单位立方类，后者恰为模 $9$ 余 $\pm1$ 的类；其元素数 $2\cdot3^{k-1}$ 与输入数相同。')]))
ms.append(M(C,5,'Refine an exponent fixed point one prime-power layer at a time','逐层细化指数不动点的剩余',[
(r'Split the target congruence into coprime prime powers and obtain a first constraint on the exponent itself.',r'将目标同余拆为互质质数幂，并先得到指数本身的初步限制。'),
(r'Use that constraint to reduce the power modulo a small prime power, obtaining a stronger residue class for the exponent.',r'用该限制约化小质数幂模下的幂，得到指数更强的剩余类。'),
(r'Repeat only while the established exponent period justifies the next refinement, then recombine and verify the original equation.',r'只有已知指数周期允许时才继续细化，最后合并并验证原方程。')],
(r'Find all residues $n\pmod{20}$ satisfying $n\equiv3^n\pmod{10}$.',r'求满足 $n\equiv3^n\pmod{10}$ 的全部模 $20$ 剩余类。'),[
(r'The right side is odd, so $n$ is odd. Powers of $3$ have period four modulo $10$.',r'右侧为奇数，故 $n$ 为奇数；$3$ 的幂模 $10$ 的周期为四。'),
(r'If $n\equiv1\pmod4$, the equation requires $n\equiv3\pmod{10}$, giving $n\equiv13\pmod{20}$.',r'若 $n\equiv1\pmod4$，原式要求 $n\equiv3\pmod{10}$，得 $n\equiv13\pmod{20}$。'),
(r'If $n\equiv3\pmod4$, it requires $n\equiv7\pmod{10}$, giving $n\equiv7\pmod{20}$. Both classes work, and the parity split exhausts all cases.',r'若 $n\equiv3\pmod4$，则须 $n\equiv7\pmod{10}$，得 $n\equiv7\pmod{20}$。两类均成立，奇偶分类已穷尽。')],
('Each stronger exponent class must follow from the previous one; guessing a long cycle is not a proof of minimality.','更强的指数剩余类须由前一步推出，猜测长周期不能证明最小性。'),
'2021-II-Q13',('NT03',)))
ms.append(M(C,6,'Make a universal geometric sum vanish in every local case','使全称等比和在每种局部情形均消失',[
(r'Use multiplicativity to reduce a divisor-sum condition to $1+a+\cdots+a^N$ for prime-power factors.',r'用积性把约数和条件约为质数幂因子的 $1+a+\cdots+a^N$。'),
(r'Modulo a prime, separate $a=0$, $a=1$, and $a\ne0,1$; the last case permits division by $a-1$.',r'模质数分别处理 $a=0,a=1,a\ne0,1$；最后一种才可除以 $a-1$。'),
(r'For a least universal exponent, prove necessity with actual admissible inputs attaining the required residues or orders.',r'求最小全称指数时，须用确实可取且达到所需剩余或阶的输入证明必要性。')],
(r'Find the least positive $N$ such that $a+a^2+\cdots+a^N\equiv0\pmod5$ for every integer $a$.',r'求最小正整数 $N$，使每个整数 $a$ 都满足 $a+a^2+\cdots+a^N\equiv0\pmod5$。'),[
(r'At $a=1$, necessity gives $5\mid N$. At $a=2$, the geometric formula gives $2^N=1$, so $4\mid N$.',r'$a=1$ 给出 $5\mid N$；$a=2$ 时等比公式给出 $2^N=1$，故 $4\mid N$。'),
(r'Thus $20\mid N$. For $N=20$, $a=0$ is automatic and $a=1$ gives a multiple of $5$.',r'故 $20\mid N$。当 $N=20$，$a=0$ 自动成立，$a=1$ 得 $5$ 的倍数。'),
(r'For the other nonzero residues, $a^4=1$ and $a-1$ is invertible, so $a(a^{20}-1)/(a-1)=0$. The minimum is $20$.',r'其余非零剩余满足 $a^4=1$，且 $a-1$ 可逆，故 $a(a^{20}-1)/(a-1)=0$；最小值为 $20$。')],
('A universal assertion needs all residue cases, including the one where the geometric denominator vanishes.','全称结论须覆盖所有剩余情形，包括等比公式分母为零者。'),
'2021-I-Q14',('NT08','AL05')))
ms.append(M(C,7,'Translate an iterate identity into permitted permutation cycles','把迭代恒等式转为允许的置换循环长度',[
(r'An onto map of a finite set to itself is a permutation.',r'有限集合到自身的满射必为置换。'),
(r'On a cycle of length $d$, the $k$th iterate is identity exactly when $d\mid k$.',r'在长度为 $d$ 的循环上，$k$ 次迭代为恒等当且仅当 $d\mid k$。'),
(r'List the allowed cycle types and count their labeled realizations, correcting repeated cycle lengths.',r'列出允许的循环型，并统计有标签实现，修正重复循环长度。')],
(r'How many onto maps on a three-element labeled set satisfy $f^3=\mathrm{id}$?',r'三元素有标签集合上的满射中，有多少个满足 $f^3=\mathrm{id}$？'),[
(r'Only cycle lengths dividing $3$ are allowed: $1$ and $3$.',r'只允许整除 $3$ 的循环长度，即 $1,3$。'),
(r'The identity has three singleton cycles and contributes one.',r'恒等置换有三个单点循环，贡献一个。'),
(r'A three-cycle has $(3-1)!=2$ orientations, giving total $1+2=3$.',r'三循环有 $(3-1)!=2$ 种，故总数为 $1+2=3$。')],
('Order of a permutation is the lcm of its cycle lengths.','置换的阶是其各循环长度的最小公倍数。'),
'2026-I-Q07',('CO07',)))
ms[2]['question_ids'].append('AIME-2025-II-Q13')
ms[2]['extensions_en'].append(r'For a power tower $a^{b^N}$, first find an exponent period $h$ for the outer unit base and only then reduce $b^N$ modulo $h$. If $b$ is not coprime to $h$, split $h$ into prime powers and handle its zero-producing local prefix before using any order.')
ms[2]['extensions_zh'].append(r'对幂塔 $a^{b^N}$，先求外层单位底数的指数周期 $h$，再将 $b^N$ 模 $h$ 约化。若 $b$ 不与 $h$ 互质，须将 $h$ 分为质数幂，先处理产生零的局部前缀，再使用乘法阶。')
ms=[m for m in ms if m['method_id']!='NT04-M07']
save(C,('A residue cycle must be proved at the correct state level. Multiplicative order handles units; prime-power valuations handle nonunits and lifting. Separate these roles before combining them by CRT.','剩余周期须在正确的状态层面证明。乘法阶处理单位，质数幂赋值处理不可逆部分与提升；先区分这些作用，再用中国剩余定理合并。'),ms,('NT03','NT01'))

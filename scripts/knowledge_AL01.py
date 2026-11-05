from knowledge_helpers_source import method as M,save
C='AL01';ms=[]
ms.append(M(C,1,'Write conservation equations for proportions, mixtures and averages','为比例、混合与平均数建立守恒方程',[
(r'Choose the conserved amount: people, pure ingredient, total sum, or probability mass.',r'选择守恒量：人数、纯物质量、总和或概率质量。'),
(r'Express each percentage as amount divided by the correct current total; distinguish original and new totals.',r'把每个百分率写成数量除以对应时刻总量，区分原总数与新总数。'),
(r'Eliminate the shared total or scale, then verify nonnegative component amounts and any integer restrictions.',r'消去共同总量或尺度，再核对分量非负与整数限制。')],
(r'A $30\%$ solution and a $70\%$ solution are mixed to make $12$ liters at $45\%$. Find the amount of each.',r'将 $30\%$ 与 $70\%$ 溶液混合成 $12$ 升 $45\%$ 溶液，求各用多少。'),[
(r'If $x$ liters are from the first solution, the second contributes $12-x$ liters.',r'若第一种用 $x$ 升，第二种便用 $12-x$ 升。'),
(r'Conserve pure ingredient: $0.3x+0.7(12-x)=0.45\cdot12$.',r'纯物质守恒给出 $0.3x+0.7(12-x)=0.45\cdot12$。'),
(r'Thus $x=7.5$ and the other amount is $4.5$ liters, both nonnegative and totaling twelve.',r'得 $x=7.5$，另一种为 $4.5$ 升，均非负且合计十二升。')],
('Percentages cannot be averaged without weighting by their amounts.','百分率不能脱离其对应数量直接平均。'),
'2001-I-Q02 2008-I-Q01 2009-II-Q01 2011-I-Q01 2011-II-Q01 2013-II-Q01 2014-I-Q02 2022-II-Q01',('PS06','NT02')))
ms.append(M(C,2,'Add work and time over the actual operating stages','按实际阶段累加工作量与时间',[
(r'Normalize the whole job and express each rate in a single common time unit.',r'将总工作量归一，并以统一时间单位表达各效率。'),
(r'For each stage write work equals rate times time; add rates for simultaneous workers, and count pauses only when they occur.',r'逐阶段写工作量等于效率乘时间；同时工作时效率相加，休息只按实际发生次数统计。'),
(r'Use the remaining deadline to solve the required final rate; round a workforce upward only after the real threshold is established.',r'用剩余期限求最终所需效率；确定实数门槛后才把人数向上取整。'),
(r'Check all stage lengths and final staffing are positive and feasible.',r'检查各阶段长度与最终人数均为正且可实现。')],
(r'A machine does one third of a job in two hours, then works at half its original rate. How long is the full job?',r'机器先用两小时完成三分之一工作，再以原效率的一半继续，全部工作需要多久？'),[
(r'The original rate is $1/6$ job per hour.',r'原效率为每小时 $1/6$ 个工作。'),
(r'The later rate is $1/12$; the remaining $2/3$ job takes $(2/3)/(1/12)=8$ hours.',r'后段效率为 $1/12$，剩余 $2/3$ 工作需 $(2/3)/(1/12)=8$ 小时。'),
(r'Total time is $2+8=10$ hours. Averaging the two rates without duration weights would be incorrect.',r'总时间为 $2+8=10$ 小时；不按持续时间加权平均效率会出错。')],
('The last arrival often occurs before the final scheduled rest.','最后一次到达通常发生在最后一次休息之前。'),
'2004-II-Q05 2007-II-Q04 2008-II-Q02 2013-I-Q01 2014-II-Q01 2013-II-Q07',('NT05',)))
ms.append(M(C,3,'Use position functions and relative velocity vectors','使用位置函数与相对速度向量',[
(r'Choose a common clock and write each position using its actual starting time.',r'选择共同计时起点，并按各自实际出发时间写位置。'),
(r'For a meeting or midpoint, equate positions or twice the middle position to the sum of the outer positions.',r'相遇时位置相等，中点条件则为中间位置的两倍等于外侧位置之和。'),
(r'For motion in a current, subtract the current velocity vector before applying the given speed norm; subtract squared equations when they share a component.',r'水流中运动须先减去水流速度向量，再使用给定速率的范数；有共同分量时相减平方方程。'),
(r'Reject solutions before a departure, after a finish, or on the wrong overtaking branch.',r'剔除出发前、结束后或错误追赶分支上的解。')],
(r'A boat moves across a river at velocity $(3,4)$ km/h relative to shore; the current is $(1,0)$. What is its speed relative to water?',r'船相对岸的速度为 $(3,4)$ 千米每小时，水流为 $(1,0)$，求船相对水的速率。'),[
(r'Velocities add as vectors: $v_{shore}=v_{water}+v_{current}$.',r'速度按向量相加：$v_{岸}=v_{水}+v_{流}$。'),
(r'Thus $v_{water}=(3,4)-(1,0)=(2,4)$.',r'故 $v_{水}=(3,4)-(1,0)=(2,4)$。'),
(r'The speed is $\sqrt{2^2+4^2}=2\sqrt5$, rather than $5-1$.',r'速率为 $\sqrt{2^2+4^2}=2\sqrt5$，而非 $5-1$。')],
('Subtract velocities as vectors, not their magnitudes.','速度须以向量相减，不能直接相减其大小。'),
'2007-I-Q02 2012-I-Q04 2012-II-Q04 2014-I-Q04 2018-II-Q01 2022-I-Q05 2024-I-Q01 2026-I-Q01',('GE07','GE03')))
ms.append(M(C,4,'Exploit a shared total before solving a linear system','解线性方程组前先利用共同总量',[
(r'Identify repeated sums or boundary totals and give each one a single variable.',r'找出反复出现的和或边界总长，并为每个总量设置一个变量。'),
(r'Add or subtract the equations to isolate the shared total before individual coordinates.',r'先通过方程相加或相减隔离共同总量，再解单独坐标。'),
(r'In a tiling, match each entire boundary consistently; in a coefficient problem, compare independent coefficients.',r'铺砌中须一致匹配整条边界；系数问题则比较独立系数。'),
(r'If integer scale is required, reduce the resulting ratio and check every constructed variable.',r'若要求整数尺度，约分所得比例，并检查构造中的每个变量。')],
(r'Positive $x,y,z$ satisfy $x+y=4$, $y+z=9$, $z+x=7$. Find $x^2+y^2+z^2$.',r'正数 $x,y,z$ 满足 $x+y=4,y+z=9,z+x=7$，求 $x^2+y^2+z^2$。'),[
(r'Let $S=x+y+z$. Adding the equations gives $2S=20$, so $S=10$.',r'设 $S=x+y+z$。相加得 $2S=20$，所以 $S=10$。'),
(r'Each coordinate is the total minus the opposite pair sum: $x=10-9=1,y=10-7=3,z=10-4=6$.',r'每个坐标等于总和减去另外两项之和：$x=10-9=1,y=10-7=3,z=10-4=6$。'),
(r'The requested value is $1+9+36=46$; all coordinates are positive and satisfy the data.',r'所求为 $1+9+36=46$；各坐标均为正且满足给定条件。')],
('Do not solve for many coordinates when one total closes the system.','若一个总量即可闭合方程组，无需逐个求大量坐标。'),
'2000-I-Q04 2000-I-Q10 2001-I-Q11 2004-II-Q06 2008-I-Q03 2008-I-Q13 2009-I-Q14',('NT02','NT05','AL02')))
ms.append(M(C,5,'Replace variables by the symmetric invariants actually requested','以目标真正需要的对称不变量换元',[
(r'Introduce a sum $s$, product $p$, or common cyclic expression instead of immediately solving each variable.',r'设置和 $s$、积 $p$ 或共同循环表达式，而不立即逐个求变量。'),
(r'Use $x^2+y^2=s^2-2p$ and $x^3+y^3=s^3-3ps$, or multiply a product-constrained system to eliminate individual variables.',r'使用 $x^2+y^2=s^2-2p,x^3+y^3=s^3-3ps$，或对带积约束的方程组相乘以消元。'),
(r'Solve only the invariant equations needed for the target; track any division by $s,p$ and check zero branches.',r'只解目标所需的不变量方程，追踪所有除以 $s,p$ 的操作，并检查零分支。'),
(r'If real variables must exist, require the corresponding quadratic discriminant to be nonnegative and reconstruct a valid instance.',r'若要求实变量存在，须对应二次判别式非负，并重建有效实例。')],
(r'Real $x,y$ satisfy $x+y=5$ and $xy=3$. Find $x^4+y^4$ without finding $x,y$.',r'实数 $x,y$ 满足 $x+y=5,xy=3$，不逐个求 $x,y$，求 $x^4+y^4$。'),[
(r'$x^2+y^2=25-6=19$.',r'$x^2+y^2=25-6=19$。'),
(r'Square again: $x^4+y^4=(x^2+y^2)^2-2x^2y^2=361-18=343$.',r'再平方得 $x^4+y^4=(x^2+y^2)^2-2x^2y^2=361-18=343$。'),
(r'The quadratic $t^2-5t+3$ has discriminant $13>0$, so real values realizing the conditions exist.',r'二次式 $t^2-5t+3$ 的判别式为 $13>0$，所以存在满足条件的实数。')],
('An invariant equation can have branches that do not correspond to real original variables.','不变量方程可能有不对应实数原变量的分支。'),
'2000-I-Q07 2001-I-Q09 2010-I-Q09 2010-II-Q05 2013-I-Q03 2014-I-Q13 2014-II-Q05 2015-II-Q14 2016-II-Q01 2018-II-Q05 2021-II-Q07 2012-II-Q08',('AL02',)))
ms.append(M(C,6,'Subtract equations to reveal equality branches and complementary pairs','相减方程以揭示相等分支与互补配对',[
(r'Subtract two similarly structured equations before expanding the full system.',r'完整展开之前，先相减两个结构相似的方程。'),
(r'Factor the difference and split all resulting cases, retaining overlaps only once.',r'将差因式分解并分类处理所有分支，重叠只保留一次。'),
(r'For pair sums of four numbers, pair complementary edges: each complementary pair has the same total.',r'四数两两和问题中，将互补边配对，每对具有相同总和。'),
(r'Reconstruct distinct or real variables to establish that a maximum or a candidate set is attained.',r'重建互异或实数变量，证明最大值或候选集合可以实现。')],
(r'Classify real triples with $xy+z=yz+x=zx+y$ and $x+y+z=0$.',r'分类满足 $xy+z=yz+x=zx+y$ 且 $x+y+z=0$ 的实数三元组。'),[
(r'If all three variables are equal, the sum gives $(0,0,0)$. Otherwise relabel an unequal pair as $x\ne z$.',r'若三变量相等，则由总和得 $(0,0,0)$；否则可重新命名，使 $x\ne z$。'),
(r'Subtracting the first two expressions gives $(y-1)(x-z)=0$, so $y=1$. Equality with the third then gives $(x-1)(z-1)=0$.',r'前两式相减得 $(y-1)(x-z)=0$，故 $y=1$；再与第三式比较，得 $(x-1)(z-1)=0$。'),
(r'Thus two coordinates are one and the third is minus two. These permutations and $(0,0,0)$ all satisfy the equations.',r'所以两坐标为一，第三个为负二；这些排列与 $(0,0,0)$ 均满足原方程。')],
('A factored difference gives alternative cases, not permission to assume all variables equal.','差的因式分解给出不同分支，不允许直接假设全部变量相等。'),
'2017-II-Q05 2018-II-Q12 2023-II-Q04',('LO03',)))
ms.append(M(C,7,'Isolate radicals and reverse-check every squaring step','隔离根式，并逆向检查每次平方',[
(r'Write all radicand and sign restrictions before squaring.',r'平方之前先写全部被开方式与符号限制。'),
(r'Isolate one radical, square, simplify, and repeat only when the isolated side has the required sign.',r'隔离一个根式后平方并化简；只有隔离侧具有所需符号时才重复。'),
(r'Solve the resulting polynomial equation, then substitute every candidate into the original unsquared equation.',r'解所得多项式方程，再把每个候选代回原未平方方程。'),
(r'For geometric models also check containment and the chosen internal/external tangency branch.',r'几何模型还须检查包含关系与内外切所选分支。')],
(r'Solve $\sqrt{x+4}-\sqrt x=1$ over the reals.',r'在实数范围解 $\sqrt{x+4}-\sqrt x=1$。'),[
(r'The domain is $x\ge0$. Isolate $\sqrt{x+4}=1+\sqrt x$, whose right side is positive.',r'定义域为 $x\ge0$。隔离为 $\sqrt{x+4}=1+\sqrt x$，右侧为正。'),
(r'Squaring yields $x+4=1+2\sqrt x+x$, so $\sqrt x=3/2$ and $x=9/4$.',r'平方得 $x+4=1+2\sqrt x+x$，故 $\sqrt x=3/2,x=9/4$。'),
(r'Substitution gives $5/2-3/2=1$, proving this candidate satisfies the original equation.',r'代入得 $5/2-3/2=1$，证明该候选满足原方程。')],
('A squared equation is generally weaker until the lost sign condition is restored.','恢复丢失的符号条件之前，平方方程一般只是较弱条件。'),
'2004-II-Q12 2020-I-Q06 2022-I-Q15',('GE06','AL08')))
ms.append(M(C,8,'Compare independent radical coefficients consistently','一致比较独立根式的系数',[
(r'First confirm that the unknown coefficients are rational, as in an integer-coefficient problem. Choose a radical basis linearly independent over $\mathbb Q$, often $1,\sqrt p,\sqrt q,\sqrt{pq}$.',r'先确认未知系数为有理数，例如题目要求整数系数。选择在 $\mathbb Q$ 上线性无关的根式基，常为 $1,\sqrt p,\sqrt q,\sqrt{pq}$。'),
(r'Expand the proposed radical expression and match each basis coefficient separately.',r'展开待定根式表达式，分别比较每个基的系数。'),
(r'Use products of pairwise coefficient equations to recover the required invariant, then check the constant coefficient and original signs.',r'将两两系数方程相乘以恢复所求不变量，再核对常数系数及原符号。')],
(r'If positive integers $a,b$ satisfy $(a\sqrt2+b\sqrt3)^2=35+12\sqrt6$, find $a^2b^2$.',r'若正整数 $a,b$ 满足 $(a\sqrt2+b\sqrt3)^2=35+12\sqrt6$，求 $a^2b^2$。'),[
(r'Expansion gives $2a^2+3b^2+2ab\sqrt6$. Independence of $1,\sqrt6$ requires $2ab=12$.',r'展开得 $2a^2+3b^2+2ab\sqrt6$；由 $1,\sqrt6$ 独立，须 $2ab=12$。'),
(r'Thus $a^2b^2=36$. To verify existence, put $a^2=t,b^2=36/t$ in the constant equation.',r'故 $a^2b^2=36$。检验存在性时，设 $a^2=t,b^2=36/t$ 代入常数方程。'),
(r'Then $2t+108/t=35$, with roots $t=4,27/2$. Only $t=4$ is an integer square, giving $a=2,b=3$ and verifying the constant coefficient.',r'得 $2t+108/t=35$，根为 $t=4,27/2$。只有 $t=4$ 是整数平方，给出 $a=2,b=3$，并验证常数系数。')],
('Matching cross terms does not remove the need to check the constant term.','比较交叉项后，仍须核对常数项。'),
'2006-I-Q05',('NT01',)))
ms.append(M(C,9,'Count roots only after restoring domains and real feasibility','恢复定义域与实数可行性后才数根',[
(r'Translate the model to a polynomial equation while recording all logarithm, positivity or interval restrictions.',r'将模型转为多项式方程，同时记录全部对数、正性或区间限制。'),
(r'Use discriminants, root signs or monotonicity on the permitted interval to count valid roots.',r'在允许区间内用判别式、根的符号或单调性统计有效根。'),
(r'A repeated algebraic root counts as one real solution; an excluded boundary or pole counts as none.',r'代数重根算一个实数解，被排除的边界或极点不算解。')],
(r'For which real $k$ does $\log(x)=\log(k-x)$ have a real solution?',r'实参数 $k$ 取何值时，$\log x=\log(k-x)$ 有实数解？'),[
(r'The domain requires $0<x<k$. Equal logarithms require $x=k-x$.',r'定义域要求 $0<x<k$；对数相等要求 $x=k-x$。'),
(r'The only candidate is $x=k/2$. It is in the domain exactly when $k>0$.',r'唯一候选为 $x=k/2$，它属于定义域当且仅当 $k>0$。'),
(r'Therefore there is exactly one real solution for every $k>0$ and no real solution otherwise.',r'所以每个 $k>0$ 恰有一个实数解，其余均无实数解。')],
('Algebraic root count and admissible solution count are different until the domain is checked.','检验定义域之前，代数根数与可接受解数是不同概念。'),
'2011-I-Q06 2016-II-Q03 2017-I-Q06 2017-II-Q07 2018-I-Q05',('AL04','AL07')))
ms.append(M(C,10,'Center symmetric rational expressions and preserve divided-out cases','将对称分式中心化，并保留被除去的分支',[
(r'Locate a common midpoint among denominator offsets and substitute $t=x-h$.',r'寻找分母偏移的共同中点，并代换 $t=x-h$。'),
(r'Pair denominators $t-a,t+a$; their reciprocal sum is $2t/(t^2-a^2)$.',r'将分母 $t-a,t+a$ 配对，其倒数和为 $2t/(t^2-a^2)$。'),
(r'Before dividing by $t$ or another shared factor, test its zero case in the original equation.',r'除以 $t$ 或其他共同因子前，先把零情形代回原方程。'),
(r'If the result uses only $t^2$, set $u=t^2$, solve, then restore both signs and reject original poles.',r'若结果只含 $t^2$，令 $u=t^2$ 求解，再恢复正负号并剔除原极点。')],
(r'Solve $1/(x-1)+1/(x+1)=x$ over the reals.',r'在实数范围解 $1/(x-1)+1/(x+1)=x$。'),[
(r'The poles $x=\pm1$ are excluded. Pairing gives $2x/(x^2-1)=x$.',r'排除极点 $x=\pm1$，配对得 $2x/(x^2-1)=x$。'),
(r'Test $x=0$ before division: it works. For $x\ne0$, $2/(x^2-1)=1$, hence $x^2=3$.',r'相除之前检查 $x=0$，它成立。对 $x\ne0$，得 $2/(x^2-1)=1$，故 $x^2=3$。'),
(r'The complete solution set is $\{0,\sqrt3,-\sqrt3\}$, with no pole included.',r'完整解集为 $\{0,\sqrt3,-\sqrt3\}$，均非极点。')],
('Centering removes clutter; it does not permit dropping the zero branch.','中心化可减少繁杂，但不能丢弃零分支。'),
'2000-I-Q09 2014-I-Q14',('AL02','AL04')))
ms[4]['question_ids'].remove('AIME-2014-II-Q05')
save(C,('Build equations around the quantity that is conserved or shared. A useful model includes units and domains as well as equations; solving an eliminated equation is only the middle of the argument, followed by reconstruction and feasibility.','围绕守恒量或共同量建立方程。有效模型既包括方程，也包括单位与定义域；求解消元后的方程只在论证中途，之后还须重建与检查可行性。'),ms,('NT02',))

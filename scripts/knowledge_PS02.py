from knowledge_helpers_source import method as M,save
C='PS02';ms=[]
ms.append(M(C,1,'Renormalize the sample space after information is given','给定信息后重新归一样本空间',[
(r'Name the conditioning event $B$ and require $P(B)>0$.',r'命名条件事件 $B$，并要求 $P(B)>0$。'),
(r'Use $P(A\mid B)=P(A\cap B)/P(B)$; in a uniform model count only outcomes surviving $B$.',r'使用 $P(A\mid B)=P(A\cap B)/P(B)$；均匀模型中只统计条件 $B$ 下保留的结果。'),
(r'Express structural information through gaps, degrees, repeated positions or disjoint Venn regions before counting.',r'计数前先用间隙、度数、重复位置或互斥 Venn 区域表达结构信息。'),
(r'Check the restricted outcomes remain equally likely; do not inherit independence without proof.',r'检查受限结果仍等概率，不能未经证明沿用独立性。')],
(r'Two fair dice are rolled. Given their sum is even, find the chance that both are odd.',r'投两枚公平骰子，已知和为偶数，求两枚都为奇数的概率。'),[
(r'Even sum means both odd or both even. Each class has $3\cdot3=9$ ordered outcomes.',r'和为偶数表示同奇或同偶，每类均有 $3\cdot3=9$ 个有序结果。'),
(r'The restricted sample space therefore has eighteen equally likely outcomes, with nine favorable.',r'条件样本空间有十八个等可能结果，其中九个有利。'),
(r'The conditional probability is $1/2$. The oddness events are dependent after conditioning, since knowing one determines the other.',r'条件概率为 $1/2$；条件下两个奇偶事件相关，因为知道一个就确定另一个。')],
('Conditional denominators count the information event, not the original whole space.','条件概率的分母统计已知信息事件，而非原整个空间。'),
'2010-II-Q13 2011-I-Q12 2014-II-Q02 2015-II-Q02 2017-II-Q09 2024-I-Q04 2026-I-Q09',('CO01','CO02','CO06'),[
(r'For a uniformly chosen bipartite edge set covering all vertices with one extra edge, the repeated degree-two row and column control whether an edge is removable. Prove uniqueness of the removable edge before using a matching-plus-extra-edge count; otherwise that construction can overcount.',r'均匀选取的二部边集若覆盖全部顶点且只多一条边，重复的二度行与列决定是否有边可删。用“匹配加一条边”计数前，须证明可删边唯一，否则该构造会重复计数。'),
(r'Visibility of a sticker attached at time $j$ means that no later roll uses its face. Convert each visibility statement into forbidden equalities of roll positions, then count the allowed sequences under all conditions simultaneously.',r'时刻 $j$ 贴上的贴纸最终可见，表示后续投掷都未使用其所在面。把每个可见声明转为投掷位置之间被禁止的相等关系，再同时满足全部条件计数。'),
(r'For conditioned runs in a random lineup, place blocks in the gaps around the other group and enumerate every ordered composition of the block sizes. Cancel common internal-label factors only after verifying they are shared by all retained patterns.',r'随机队列的条件连续段问题，可将各块放入另一组周围的间隙，并枚举全部有序块长拆分。只有确认保留模式共享相同类内标签因子后，才能将它们约去。')]))
ms.append(M(C,2,'Update a hidden model with Bayes before predicting again','再次预测前先用贝叶斯更新隐藏模型',[
(r'List the possible hidden models $H_i$ and their prior probabilities.',r'列出可能隐藏模型 $H_i$ 及先验概率。'),
(r'Multiply each prior by the likelihood of the observed evidence and normalize the resulting weights.',r'将每个先验乘观测证据的似然，再归一所得权重。'),
(r'Average the next-event probability using these posterior weights; conditional independence given a model need not survive averaging over models.',r'以后验权重平均下一事件概率；给定模型的条件独立，未必在对模型平均后仍成立。')],
(r'Choose equally between a fair coin and an always-heads coin, then observe one head. Are the next two tosses independent given that observation?',r'等可能选择公平硬币或总为正面的硬币，观察到一次正面后，接下来两次投掷在此条件下独立吗？'),[
(r'The evidence likelihoods are $1/2$ and one, so posterior probabilities are fair $1/3$, always-heads $2/3$.',r'证据似然分别为 $1/2$ 与一，故后验为公平币 $1/3$、总正面币 $2/3$。'),
(r'Each future toss is heads with probability $(1/3)(1/2)+(2/3)=5/6$.',r'每次未来投掷为正面的概率为 $(1/3)(1/2)+(2/3)=5/6$。'),
(r'Two future heads have probability $(1/3)(1/4)+(2/3)=3/4$.',r'未来两次均正面的概率为 $(1/3)(1/4)+(2/3)=3/4$。'),
(r'Since $3/4\ne(5/6)^2$, the future tosses are dependent under the observed-information condition.',r'因 $3/4\ne(5/6)^2$，在已观察信息条件下，两次未来投掷相关。')],
('Evidence changes the model weights even when the physical die or coin remains unchanged.','即使实际骰子或硬币不变，证据仍会改变各模型权重。'),
'2014-II-Q06',('PS01',)))
ms.append(M(C,3,'Condition on a complete first-stage partition','按完整的第一阶段分类取条件',[
(r'Choose disjoint cases $H_i$ whose union is the whole space, such as opponents, bracket pairings or geometric regions.',r'选择互斥且并为全空间的情形 $H_i$，例如对手、赛程配对或几何区域。'),
(r'Compute $P(A\mid H_i)$ within each case, using the probabilities that hold there.',r'在各情形内计算 $P(A\mid H_i)$，使用该情形实际成立的概率。'),
(r'Combine by $P(A)=\sum_iP(H_i)P(A\mid H_i)$. This also gives an equation for unknown conditional rates.',r'以 $P(A)=\sum_iP(H_i)P(A\mid H_i)$ 合并，也可由此求未知条件概率。'),
(r'If coordinates are claimed independent after conditioning, identify the product region or independent coordinate variables that justify it.',r'若声称取条件后坐标独立，须指出相应乘积区域或独立坐标变量。')],
(r'A mode is selected: mode $A$ with probability $1/4$, otherwise mode $B$. Success rates are $1/2$ and $1/3$. Find the overall success probability and the posterior chance of mode $A$ after success.',r'先选模式：概率 $1/4$ 选 $A$，否则选 $B$；成功率分别为 $1/2,1/3$。求总体成功率及成功后为模式 $A$ 的概率。'),[
(r'The disjoint success contributions are $(1/4)(1/2)=1/8$ and $(3/4)(1/3)=1/4$.',r'两种互斥成功贡献为 $(1/4)(1/2)=1/8$ 与 $(3/4)(1/3)=1/4$。'),
(r'The total success probability is $1/8+1/4=3/8$.',r'总成功率为 $1/8+1/4=3/8$。'),
(r'Of that success mass, mode $A$ contributes $1/8$, so its posterior probability is $(1/8)/(3/8)=1/3$.',r'成功质量中模式 $A$ 贡献 $1/8$，故其后验概率为 $(1/8)/(3/8)=1/3$。')],
('Use the probability of reaching a branch as well as its conditional success rate.','既要乘分支内成功率，也要乘到达该分支的概率。'),
'2016-II-Q02 2017-II-Q02 2022-II-Q02 2023-II-Q06',('PS01','PS03')))
ms.append(M(C,4,'Normalize independent weights and convolve their distributions','归一独立权重并卷积其分布',[
(r'Turn proportional weights into probabilities by dividing by their total.',r'将成比例权重除以总权重，化为概率。'),
(r'For independent variables, multiply probabilities of elementary coordinate outcomes and sum disjoint ways to reach the target.',r'独立变量的基本坐标结果概率相乘，再对达到目标的互斥方式求和。'),
(r'A probability-generating polynomial encodes a nonnegative integer count; multiply polynomials for independent sums.',r'概率生成多项式编码非负整数计数；独立和对应多项式相乘。'),
(r'Matching two independent identical distributions gives $\sum p_k^2$; transformed walk coordinates require proof that their joint one-step signs are uniform.',r'两个独立同分布计数相等的概率为 $\sum p_k^2$；变换后的随机游走坐标则须证明每步联合符号均匀。')],
(r'Independent coins have head probabilities $1/2$ and $1/3$. Find the probability of exactly one head using a generating polynomial.',r'两枚独立硬币正面率为 $1/2,1/3$，以生成多项式求恰一次正面的概率。'),[
(r'The two head-count polynomials are $(1+t)/2$ and $(2+t)/3$.',r'两枚硬币的正面计数多项式为 $(1+t)/2,(2+t)/3$。'),
(r'Their product is $(2+3t+t^2)/6$.',r'乘积为 $(2+3t+t^2)/6$。'),
(r'The coefficient of $t$ is $3/6=1/2$, agreeing with $(1/2)(2/3)+(1/2)(1/3)$.',r'$t$ 的系数为 $3/6=1/2$，也等于 $(1/2)(2/3)+(1/2)(1/3)$。')],
('Independence is a property to prove or a stated assumption, not a consequence of naming two variables.','独立性须有已知条件或证明，并非命名两个变量后便自动成立。'),
'2006-II-Q05 2010-I-Q04 2014-I-Q02 2014-I-Q11 2016-I-Q02 2023-II-Q06',('PS01','CO02')))
ms.append(M(C,5,'Update the remaining population or use an exchangeable full deal','更新剩余总体，或使用可交换的完整分配',[
(r'After each draw, record the remaining multiplicities; without replacement changes later probabilities.',r'每次抽取后记录剩余重数，不放回会改变后续概率。'),
(r'Multiply the next-step conditional probabilities along a path and add disjoint draw patterns.',r'沿路径乘下一步条件概率，再对互斥抽取模式求和。'),
(r'If chronological cases are cumbersome, deal all labeled objects in advance and prove permuting batch labels preserves uniformity.',r'若按时间分类繁琐，可先完整分配所有有标签物品，并证明批次标签置换保持均匀性。'),
(r'Track the number of complete groups left after a mismatch, rather than assume each unobserved pair is equally intact.',r'不匹配后须追踪剩余完整组数，不能假设所有未见配对仍完整。')],
(r'An urn has two red and two blue balls. Draw two without replacement. Show that the events first-red and second-red are not independent.',r'袋中有二红二蓝，不放回抽两球。证明首次红与第二次红两个事件不独立。'),[
(r'The first-red probability is $1/2$, and by exchangeability so is the marginal second-red probability.',r'首次红概率为 $1/2$，由可交换性，第二次红的边缘概率也为 $1/2$。'),
(r'Given the first is red, only one red remains among three balls, so $P(R_2\mid R_1)=1/3$.',r'已知首次红，剩余三球仅一红，故 $P(R_2\mid R_1)=1/3$。'),
(r'This differs from the marginal $1/2$; equivalently $P(R_1\cap R_2)=1/6\ne1/4$.',r'它不同于边缘概率 $1/2$；等价地 $P(R_1\cap R_2)=1/6\ne1/4$。')],
('Exchangeability of batch labels does not mean independence of the batches.','批次标签可交换，并不意味着各批次独立。'),
'2004-II-Q02 2015-I-Q05',('PS01','CO01')))
ms.append(M(C,6,'Condition on the minimal memory state and track parity if needed','按最小记忆状态取条件，必要时追踪奇偶',[
(r'Choose the shortest memory that determines the next transition probabilities, such as the previous winner or a matched pattern prefix.',r'选择决定下一步转移概率的最短记忆，例如前次胜者或已匹配模式前缀。'),
(r'For a fixed finite event, multiply transition probabilities along each allowed state path, counting switches rather than assuming independent outcomes.',r'固定有限事件沿各允许状态路径乘转移概率，并统计切换次数，不能假设结果独立。'),
(r'For a stopping parity, let $u_s=E((-1)^R)$ for remaining time $R$; each next step changes sign, and immediate stopping contributes $-1$.',r'停时奇偶可设 $u_s=E((-1)^R)$，其中 $R$ 为剩余步数；每前进一步变号，立即停止贡献 $-1$。'),
(r'Solve the first-step equations and convert $u$ to odd probability $(1-u)/2$; establish almost-sure stopping.',r'解首步方程，并以 $(1-u)/2$ 转为奇数概率；同时证明几乎必然停止。')],
(r'Toss a fair coin until two consecutive heads. Find the probability that the stopping time is odd.',r'投公平硬币，直到连续两次正面，求停止次数为奇数的概率。'),[
(r'Use states $0$ (no trailing head) and $1$ (one trailing head). Let $u_0,u_1$ be signed remaining-time expectations.',r'取状态 $0$（无末尾正面）与 $1$（末尾一个正面），设 $u_0,u_1$ 为带符号剩余时间期望。'),
(r'First-step conditioning gives $u_0=-(u_0+u_1)/2$ and $u_1=-(u_0+1)/2$.',r'首步取条件得 $u_0=-(u_0+u_1)/2,u_1=-(u_0+1)/2$。'),
(r'Thus $u_1=-3u_0$ and $u_0=1/5$, so the odd probability is $(1-1/5)/2=2/5$.',r'故 $u_1=-3u_0,u_0=1/5$，奇数概率为 $(1-1/5)/2=2/5$。'),
(r'Each disjoint two-toss block has probability $1/4$ of being HH, so the chance of avoiding a stop forever is zero.',r'每个互不相交的两投块有 $1/4$ 概率为 HH，故永远不停止的概率为零。')],
('A failed prefix may retain a shorter matching suffix; recalculate the state rather than always resetting to zero.','前缀失败后可能保留较短匹配后缀，应重新确定状态，不能总是归零。'),
'2018-II-Q13 2021-I-Q01',('PS05','AL05')))
save(C,('Information changes the probability space. Keep prior weights, evidence likelihoods, conditional cases and independence assumptions explicit; the formulas are short once the correct restricted or state-based model is chosen.','信息会改变概率空间。明确写出先验权重、证据似然、条件分类与独立假设；选对受限模型或状态模型后，公式本身通常很短。'),ms,('PS01','CO01'))

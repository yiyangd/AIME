from knowledge_helpers_source import method as M,save
C='PS01';ms=[]
ms.append(M(C,1,'Choose equally likely labeled samples before counting colors','统计颜色前先选择等可能的有标签样本',[
(r'Decide whether the elementary outcome is an ordered draw, an unordered subset, a permutation, or a full deal.',r'确定基本结果是有序抽取、无序子集、排列还是完整分配。'),
(r'For $k$ draws without replacement from $N$ distinct objects, use $\binom Nk$ unordered outcomes or $N(N-1)\cdots(N-k+1)$ ordered outcomes consistently.',r'从 $N$ 个不同物品不放回取 $k$ 个时，一致使用 $\binom Nk$ 个无序结果，或 $N(N-1)\cdots(N-k+1)$ 个有序结果。'),
(r'Count favorable group multiplicities with products of binomial coefficients; color words with different multiplicities need not have equal probability.',r'用二项式系数之积统计有利类别重数；重数不同的颜色串未必等概率。'),
(r'Divide favorable by total outcomes only after proving the chosen elementary outcomes are uniform.',r'证明所选基本结果均匀后，才能以有利数除以总数。')],
(r'An urn contains four red and three blue distinct balls. Find the chance that a uniformly chosen three-ball subset has exactly two red balls.',r'袋中有四个红球和三个蓝球，球均可区分。均匀选择三球子集，恰有两红的概率是多少？'),[
(r'There are $\binom73=35$ equally likely subsets.',r'共有 $\binom73=35$ 个等可能子集。'),
(r'Choose two of the four red balls and one of the three blue balls: $\binom42\binom31=18$.',r'从四红中选二、三蓝中选一，有 $\binom42\binom31=18$ 种。'),
(r'The probability is $18/35$.',r'概率为 $18/35$。')],
('Different color words can correspond to different numbers of labeled outcomes.','不同颜色串可能对应不同数量的有标签结果。'),
'2000-II-Q03 2005-II-Q02 2010-I-Q01 2013-I-Q06 2015-I-Q02 2015-I-Q05 2018-I-Q03 2026-II-Q05',('CO01','CO02','NT05')))
ms.append(M(C,2,'Count discrete geometric pairs through edges, gaps or position sets','用边、间隔或位置集合统计离散几何配对',[
(r'Represent the sampled geometric objects by labeled vertices or position subsets.',r'用有标签顶点或位置子集表示被抽取的几何对象。'),
(r'Count admissible pairs by graph edges or by separation, preserving ordered versus unordered sampling.',r'按图的边或间隔统计允许配对，并保持有序或无序抽样一致。'),
(r'For a cyclic configuration, identify a unique anchor or a family of disjoint opposite-position pairs to avoid overcounting.',r'循环构型须确定唯一锚点，或使用互不相交的对位配对，避免重复计数。'),
(r'Use exact endpoint conventions for open semicircles and strict triangle inequalities.',r'对开半圆与严格三角不等式使用准确端点约定。')],
(r'A graph on vertices $1,2,3,4$ has edges $12,23,31,34$. Choose two distinct vertices uniformly. What is the probability they are joined by an edge?',r'顶点为 $1,2,3,4$ 的图具有边 $12,23,31,34$。均匀选两个不同顶点，它们有边相连的概率是多少？'),[
(r'The unordered sample space has $\binom42=6$ pairs.',r'无序样本空间有 $\binom42=6$ 对。'),
(r'The four listed edges are four distinct favorable pairs.',r'所列四条边是四个不同的有利配对。'),
(r'The probability is $4/6=2/3$. Ordered sampling doubles both counts and gives the same result.',r'概率为 $4/6=2/3$；有序抽样会同时使分子分母加倍，结果相同。')],
('A discrete geometry question uses counts of choices; lengths alone do not weight the sample space.','离散几何题使用选择个数；长度本身不会给样本空间加权。'),
'2010-II-Q04 2011-I-Q10 2015-II-Q05 2019-I-Q02 2023-I-Q01',('CO06','GE04'),[
(r'An obtuse inscribed triangle has its vertices in an open semicircle, with a unique first clockwise vertex. For an even polygon the antipodal endpoint is excluded, removing right triangles; for an odd polygon no vertex is exactly antipodal. Derive the two half-circle counts separately.',r'钝角内接三角形的顶点位于一个开半圆中，且有唯一顺时针首顶点。偶数边形须排除对径端点以去掉直角三角形；奇数边形没有恰好对径的顶点。应分别推导两种半圆计数。')]))
ms.append(M(C,3,'Use product coordinates and inclusion-exclusion on event unions','在事件并集中使用乘积坐标与容斥',[
(r'Encode each independent elementary choice locally, such as membership bits or cell colors.',r'将每个独立基本选择作局部编码，例如成员位或格子颜色。'),
(r'Count an intersection by the union of all forced conditions; shared objects are forced once, not once per event.',r'交集须按全部被迫条件之并计数；共用对象只被固定一次，不能按事件重复固定。'),
(r'Apply inclusion-exclusion for overlapping good or bad events, and use a complement when simpler.',r'对重叠好事件或坏事件使用容斥；补集较简单时先数补集。'),
(r'For a uniform random subset, every membership bit is independent with probability one half; conditioning on size changes that model.',r'均匀随机子集的成员位独立且各为二分之一；若附加大小条件，模型便改变。')],
(r'Choose two independent uniform subsets $A,B$ of a four-element set. Find $\Pr(|A\cap B|=1)$.',r'从四元素集合的所有子集中独立均匀选 $A,B$，求 $\Pr(|A\cap B|=1)$。'),[
(r'At each element the four membership pairs are equally likely, and only the pair $(1,1)$ enters the intersection.',r'每个元素的四种成员位对等可能，仅 $(1,1)$ 进入交集。'),
(r'The four elements act independently, so exactly one intersection element has probability $\binom41(1/4)(3/4)^3$.',r'四元素彼此独立，恰一个交集元素的概率为 $\binom41(1/4)(3/4)^3$。'),
(r'This simplifies to $27/64$.',r'化简为 $27/64$。')],
('Inclusion-exclusion concerns overlapping events, even when the underlying random choices are independent.','即使基本随机选择独立，由它们构成的事件仍可能重叠而需要容斥。'),
'2001-II-Q09 2002-I-Q01 2007-II-Q10 2011-II-Q12 2014-I-Q12 2025-II-Q07 2024-I-Q11',('CO04','CO02','CO06')))
ms.append(M(C,4,'Compress outcomes into weighted residue or exponent classes','将结果压缩为带权剩余类或指数类',[
(r'Choose a class label that exactly determines the event, such as parity, a prime-exponent vector or a residue sum.',r'选择能准确决定事件的类别标签，例如奇偶、质指数向量或剩余和。'),
(r'Attach the correct weight to each class: the number or total probability of its elementary outcomes.',r'为每类附上正确权重，即其基本结果数量或总概率。'),
(r'Count permitted class patterns, restoring multinomial ordering and class weights; remove repeated-object samples if distinctness is required.',r'统计允许类别模式，并恢复多项式排列权重与类权重；若要求对象不同，剔除重复抽到同一对象的样本。'),
(r'For independent uniform exponent coordinates, count nondecreasing exponent tuples by combinations with repetition.',r'指数坐标独立均匀时，用可重复组合统计非降指数元组。')],
(r'Two fair dice are rolled. Find the probability that their faces have the same parity but are unequal.',r'投两枚公平骰子，求点数奇偶相同但数值不同的概率。'),[
(r'There are $36$ equally likely ordered outcomes. Each parity class has three faces.',r'共有 $36$ 个等可能有序结果，每个奇偶类有三个点数。'),
(r'Within either class, the first face has three choices and the distinct second face two choices, giving $2\cdot3\cdot2=12$ favorable outcomes.',r'每类首点数有三种，不同的第二点数有两种，有利结果为 $2\cdot3\cdot2=12$。'),
(r'The probability is $12/36=1/3$.',r'概率为 $12/36=1/3$。')],
('Compressing outcomes does not make the compressed classes equally likely.','压缩结果并不会使各压缩类别自动等概率。'),
'2000-I-Q05 2001-I-Q06 2001-I-Q10 2004-II-Q10 2016-I-Q02 2018-I-Q12 2019-II-Q04 2020-I-Q09',('NT01','NT03','CO03'),[
(r'For a square product, encode the parity of every prime exponent and require their coordinatewise sum to vanish modulo two. A face or number with zero parity vector may have more than one elementary representative and must retain that multiplicity.',r'乘积为平方数时，编码每个质指数的奇偶，并要求逐坐标和模二为零。零奇偶向量可能对应不止一个点数或数字，必须保留其重数。'),
(r'For $k$ equally likely exponent values, a nondecreasing $r$-tuple has $\binom{k+r-1}{r}$ possibilities out of $k^r$. Do not divide by $r!$, since tuples with repeated exponents have different orbit sizes.',r'指数有 $k$ 个等可能值时，非降 $r$ 元组有 $\binom{k+r-1}{r}$ 个，总数为 $k^r$。不能直接除以 $r!$，因为含重复指数的元组轨道大小不同。')]))
ms.append(M(C,5,'Count invariant colorings and independent orientation types','统计不变涂色与独立朝向类型',[
(r'For a fixed symmetry, partition positions into its permutation orbits.',r'对固定对称，将位置分成其置换轨道。'),
(r'An invariant coloring is constant on every orbit; if a color total is fixed, sum the orbit sizes rather than choose colors independently.',r'不变涂色在每个轨道内恒定；若某颜色总数固定，须按轨道大小求和，不能独立选色。'),
(r'For many independent oriented objects, classify positions by how many outward constraints they impose and multiply the correctly weighted success probabilities.',r'对许多独立定向物体，按位置施加的外露限制分类，再乘正确加权的成功概率。'),
(r'For existence of some symmetry, count the union of successful symmetry families and resolve their intersections.',r'若要求存在某个对称，须数各成功对称族的并，并处理其交集。')],
(r'Color the vertices of a square independently red or blue with equal probabilities. What is the probability of invariance under the reflection fixing one diagonal?',r'独立以相等概率把正方形顶点涂红或蓝，求涂色在固定某条对角线的反射下不变的概率。'),[
(r'The reflection fixes two vertices and exchanges the other two, giving orbit sizes $1,1,2$.',r'该反射固定两个顶点，交换另两个，轨道大小为 $1,1,2$。'),
(r'Each of three orbits can choose either color, so there are $2^3=8$ invariant colorings.',r'三个轨道各可任选两色，故不变涂色有 $2^3=8$ 种。'),
(r'All $2^4=16$ vertex colorings are equally likely, so the probability is $1/2$.',r'全部 $2^4=16$ 个顶点涂色等可能，故概率为 $1/2$。')],
('Fixed color totals make the sample space a subset layer rather than independent bits.','固定颜色总数时，样本空间是固定大小子集层，而非独立成员位。'),
'2005-I-Q09 2013-I-Q04 2024-I-Q11',('CO07','GE10','CO06')))
ms.append(M(C,6,'Weight stopped paths by length and count constrained paths by state','按长度加权停时路径，并按状态统计受限路径',[
(r'Describe a terminal path including its stopping step; paths of different lengths generally have different probabilities.',r'描述终止路径时包括停止步骤；不同长度路径通常具有不同概率。'),
(r'For a fixed step multiplicity, use a multinomial count and multiply by that path\'s step probabilities.',r'固定步型重数后，用多项式系数计数并乘该路径逐步概率。'),
(r'For distinct-vertex or closing constraints, use a state recording the visited subset and last vertex, then test the closing edge.',r'对顶点互异或闭合限制，使用记录已访问子集及末顶点的状态，再检验闭合边。'),
(r'Divide by a uniform total only when all retained elementary paths are equally likely.',r'只有保留的基本路径均等概率时，才能除以统一总数。')],
(r'Toss a fair coin until the first head or three tosses, whichever occurs first. What is the probability that the terminal sequence contains more tails than heads?',r'投公平硬币，直到首次正面或已投三次即停止。求终止串中反面多于正面的概率。'),[
(r'The terminal paths are $H,TH,TTH,TTT$, with probabilities $1/2,1/4,1/8,1/8$.',r'终止路径为 $H,TH,TTH,TTT$，概率分别为 $1/2,1/4,1/8,1/8$。'),
(r'Only $TTH$ and $TTT$ have more tails than heads.',r'只有 $TTH,TTT$ 的反面数多于正面数。'),
(r'Add their probabilities to get $1/4$. Counting two favorable paths out of four would incorrectly treat unequal paths as uniform.',r'相加得 $1/4$；按四条路径中两条有利计数会错误地把不等概率路径看成均匀。')],
('The stopping rule is part of the sample-space definition.','停止规则本身就是样本空间定义的一部分。'),
'2001-I-Q15 2019-I-Q05',('CO03','CO05','CO06')))
ms.append(M(C,7,'Model pairings and ownership constraints as permutations or matchings','把配对与归属限制建模为置换或匹配',[
(r'For a left-right bijection use a permutation; for arbitrary unordered pairings use a perfect matching with $(2n-1)!!$ outcomes.',r'左右两类一一配对使用置换；任意无序配对使用完美匹配，共 $(2n-1)!!$ 种。'),
(r'Translate a closed collection of owners into a union of permutation cycles, or a sorted pair condition into a restriction on smaller endpoints.',r'将归属封闭子集转为置换循环之并，或将排序配对条件转为较小端点限制。'),
(r'Count allowable cycle types or pairing cases, correcting indistinguishable cycles and case intersections.',r'统计允许循环型或配对情形，并修正不可区分循环与分类交集。'),
(r'For repeated-color rows, use a uniform labeled model or prove every color pattern has the same number of labeled realizations.',r'对重复颜色行，使用均匀有标签模型，或证明每个颜色模式具有同数目的有标签实现。')],
(r'Choose a uniform permutation of four labels. Find the probability that it has exactly one fixed point.',r'均匀选择四个标签的一个置换，求恰有一个不动点的概率。'),[
(r'Choose the fixed label in four ways.',r'固定标签有四种选择。'),
(r'The remaining three labels must have no fixed point, so they form one of the two three-cycles.',r'其余三个标签不能固定，因此构成两个三循环之一。'),
(r'There are $8$ favorable permutations out of $4!=24$, giving probability $1/3$.',r'有利置换为八个，全部为 $4!=24$ 个，故概率为 $1/3$。')],
('A pairing count and a permutation count use different elementary outcomes.','匹配计数与置换计数使用不同的基本结果。'),
'2014-II-Q13 2022-I-Q09 2025-I-Q07',('CO01','CO07')))
save(C,('Start by proving what is equally likely. Labeled samples, color patterns, multisets and stopped paths are different sample spaces; use the representation that makes the event easiest to count while preserving its weights.','首先证明什么结果等可能。有标签样本、颜色模式、多重集与停时路径属于不同样本空间；应选择最便于统计事件且保留权重的表示。'),ms,('CO01','CO02'))

from knowledge_helpers_source import method as M,save
C='PS03';ms=[]
ms.append(M(C,1,'Measure the valid parameter intervals after algebraic reduction','代数约化后度量有效参数区间',[
(r'Keep the exact uniform parameter and its interval; a transformed variable is not automatically uniform.',r'保留实际均匀参数及其区间，变换后的变量不自动均匀。'),
(r'Translate the event into algebraic or trigonometric inequalities, discriminants, or floor-constant intervals.',r'将事件转为代数或三角不等式、判别式条件，或取整恒定的区间。'),
(r'Find every favorable subinterval with the original domains restored, then divide its total length by the sample length.',r'恢复原定义域后找出所有有利子区间，再以总长度除以样本长度。'),
(r'Isolated endpoints have zero probability in a continuous uniform interval, but the interval interiors must be correct.',r'连续均匀区间中孤立端点概率为零，但区间内部必须判断正确。')],
(r'Choose $\theta$ uniformly from $[0,\pi/2]$. Find $P(\sin\theta\ge\cos2\theta)$.',r'从 $[0,\pi/2]$ 均匀选择 $\theta$，求 $P(\sin\theta\ge\cos2\theta)$。'),[
(r'Put $s=\sin\theta\in[0,1]$ only to solve the inequality: $s\ge1-2s^2$.',r'仅为解不等式而令 $s=\sin\theta\in[0,1]$，得 $s\ge1-2s^2$。'),
(r'Factor $(2s-1)(s+1)\ge0$, so $s\ge1/2$ and $\theta\in[\pi/6,\pi/2]$.',r'分解得 $(2s-1)(s+1)\ge0$，故 $s\ge1/2,\theta\in[\pi/6,\pi/2]$。'),
(r'The probability is the angle-length ratio $(\pi/2-\pi/6)/(\pi/2)=2/3$, rather than a length ratio in $s$.',r'概率为角度长度比 $(\pi/2-\pi/6)/(\pi/2)=2/3$，而非 $s$ 区间的长度比。')],
('Uniform angle does not mean uniform sine or uniform chord length.','角度均匀不代表正弦值均匀或弦长均匀。'),
'2003-I-Q11 2011-II-Q15 2018-II-Q06',('AL01','AL02','AL06','AL08'),[
(r'If a floor expression is constant on $[n,n+1)$, first check whether the other side can have the required integer value. For each surviving integer $n$, solve the exact monotone threshold where the floor changes, and intersect it with that unit interval.',r'若某取整表达式在 $[n,n+1)$ 恒定，先检查另一侧是否能取所需整数值。对每个存活整数 $n$，求取整改变时的精确单调门槛，并与该单位区间相交。')]))
ms.append(M(C,2,'Clip the correct feasible region by half-planes and distance strips','以半平面与距离带裁切正确可行区域',[
(r'Identify the actual sampling region; a moving disk center must stay its radius away from every container side.',r'确定实际抽样区域；移动圆盘的圆心须距容器每边至少其半径。'),
(r'Expand squared-distance comparisons to linear half-planes, or use distance to a line $|ax+by+c|/\sqrt{a^2+b^2}$.',r'展开距离平方比较得到线性半平面，或使用点线距离 $|ax+by+c|/\sqrt{a^2+b^2}$。'),
(r'When dividing by a coordinate difference to test slope, split its positive and negative cases before changing inequality direction.',r'以坐标差相除判断斜率时，先按其正负分类，再决定不等号方向。'),
(r'Find the clipped polygon vertices, calculate its area, and divide by the area of the feasible sampling region.',r'求裁切多边形顶点、计算面积，并除以可行抽样区域面积。')],
(r'Choose a point uniformly from $[0,3]\times[0,2]$. Find the probability that $x\ge1/2$ and $x+y\le2$.',r'从 $[0,3]\times[0,2]$ 按面积均匀选点，求 $x\ge1/2$ 且 $x+y\le2$ 的概率。'),[
(r'The rectangle has area six. The two inequalities clip out a right triangle.',r'矩形面积为六，两不等式裁出一个直角三角形。'),
(r'Its vertices are $(1/2,0),(2,0),(1/2,3/2)$, so its area is $\tfrac12(3/2)^2=9/8$.',r'三顶点为 $(1/2,0),(2,0),(1/2,3/2)$，面积为 $\tfrac12(3/2)^2=9/8$。'),
(r'The probability is $(9/8)/6=3/16$.',r'概率为 $(9/8)/6=3/16$。')],
('Normalize by where the point or center was actually sampled.','分母须为点或圆心实际被抽取的区域。'),
'2004-I-Q10 2010-II-Q02 2017-II-Q03 2020-II-Q02',('GE02','GE07')))
ms.append(M(C,3,'Use the parameter square for two independent uniform choices','对两个独立均匀选择使用参数正方形',[
(r'The two original parameters form a uniform rectangle because they are independent.',r'两个原参数独立，因此形成均匀参数矩形。'),
(r'Use geometry to translate a chord or distance condition into a condition on their sum or difference.',r'用几何将弦长或距离条件转为两参数和差的条件。'),
(r'Draw the resulting diagonal half-planes or band and use a complementary triangle count where possible.',r'画出所得对角半平面或带状区域，可能时用补三角形求面积。'),
(r'Keep any angle range needed for the monotonicity of sine or another inverse transformation.',r'保留保证正弦或其他逆变换单调的角度范围。')],
(r'Independent $U,V$ are uniform on $[0,1]$. Find $P(U+V\ge1,\ U-V\le1/2)$.',r'$U,V$ 独立且均匀分布于 $[0,1]$，求 $P(U+V\ge1,\ U-V\le1/2)$。'),[
(r'The joint sample square has area one. The condition $U+V\ge1$ leaves a triangle of area $1/2$.',r'联合样本正方形面积为一；条件 $U+V\ge1$ 留下面积 $1/2$ 的三角形。'),
(r'Within it the forbidden region $U-V>1/2$ is the triangle with vertices $(3/4,1/4),(1,0),(1,1/2)$, of area $1/16$.',r'其中禁用区 $U-V>1/2$ 是顶点为 $(3/4,1/4),(1,0),(1,1/2)$ 的三角形，面积为 $1/16$。'),
(r'The required probability is $1/2-1/16=7/16$.',r'所求概率为 $1/2-1/16=7/16$。')],
('The natural probability coordinates may be angles even when the picture is a circle.','即使图形为圆，天然概率坐标仍可能是角度。'),
'2017-I-Q08',('GE04','GE03')))
ms.append(M(C,4,'Translate chord events into cyclic endpoint order and arc masses','把弦事件转为端点循环次序与弧质量',[
(r'For endpoints uniform on a circle, an arc is selected with probability equal to its fraction of circumference.',r'端点在圆周均匀时，选到某弧的概率等于该弧占周长的比例。'),
(r'A chord misses a convex inscribed polygon exactly when both endpoints lie on one vertex gap arc, apart from boundaries.',r'除边界外，弦不交凸内接多边形，当且仅当两端点落在同一顶点间隙弧。'),
(r'Two chords cross internally exactly when their four distinct endpoints alternate cyclically.',r'两弦内部相交当且仅当四个互异端点在圆周上交替出现。'),
(r'Under arc or quadrant conditioning, enumerate arc-pair cases first, then use symmetry of endpoint order within any shared arc.',r'附加弧或象限条件时，先枚举弧配对情形，再使用共用弧内端点次序的对称性。')],
(r'A fixed chord cuts the circumference into arcs of fractions $1/3$ and $2/3$. Another chord has two independent uniform endpoints. Find its probability of crossing the fixed chord internally.',r'固定弦把圆周分成比例为 $1/3,2/3$ 的两弧。另一条弦的两端点独立且圆周均匀，求它与固定弦内部相交的概率。'),[
(r'Crossing requires one endpoint on each of the two open arcs.',r'相交要求两个端点各在一条开弧上。'),
(r'The two ordered endpoint cases have probabilities $(1/3)(2/3)$ and $(2/3)(1/3)$.',r'两种有序端点情形概率为 $(1/3)(2/3)$ 与 $(2/3)(1/3)$。'),
(r'The total is $4/9$. Coincident endpoints have probability zero.',r'合计为 $4/9$，端点重合概率为零。')],
('Specify the chord-generation rule; uniform perimeter endpoints is a particular model.','须明确弦的生成规则；圆周端点均匀是一种特定模型。'),
'2017-I-Q06 2025-I-Q13',('GE04','CO06','PS02'),[
(r'For four equal arcs and chords conditioned to use two different arcs, each chord has six equiprobable unordered arc pairs. For two chords, among the $36$ ordered pair choices, two disjoint alternating choices force crossing, four disjoint nonalternating choices forbid it, and the remaining thirty have crossing probability $1/2$ by reversal of order in a shared arc. The resulting crossing probability is $(2+30/2)/36=17/36$.',r'圆周分为四条等弧，弦端点条件为落在不同弧时，每弦有六种等可能无序弧对。两弦共有 $36$ 种有序弧对选择：两种互不共弧且交替的选择必相交，四种互不共弧且不交替的选择必不相交，其余三十种由共用弧内端点顺序反转而各有 $1/2$ 概率相交。故交叉概率为 $(2+30/2)/36=17/36$。')]))
ms.append(M(C,5,'Condition on geometric pieces with their area weights','按几何分区及其面积权重取条件',[
(r'Partition a nonrectangular region into disjoint pieces of known areas; their selection probabilities are proportional to area.',r'将非矩形区域分为已知面积的互不相交部分，各部分被选概率与面积成正比。'),
(r'For two independent points, ordered piece choices have product probabilities.',r'两个独立点的有序分区选择，其概率为两分区概率之积。'),
(r'Within a rectangular piece, coordinates are independent uniform variables; justify any further coordinate independence after conditioning.',r'矩形分区内坐标为独立均匀变量；若继续取条件，须证明后续坐标独立性。'),
(r'Compute the event inside each feasible piece pair and combine by total probability, often using the complement.',r'在每个可行分区对内求事件概率，再以全概率合并，通常可先求补事件。')],
(r'A region consists of two disjoint rectangles of areas one and three. Choose two independent uniform points in their union. Find the chance that they occupy different rectangles.',r'某区域由面积一与三的两个互不相交矩形组成。在其并集中独立均匀选两点，求两点分属不同矩形的概率。'),[
(r'The piece probabilities are $1/4$ and $3/4$, rather than one half each.',r'两分区概率为 $1/4,3/4$，而非各二分之一。'),
(r'The two disjoint ordered cases are first-small/second-large and first-large/second-small.',r'两种互斥有序情形为先小后大、先大后小。'),
(r'Their probabilities sum to $2(1/4)(3/4)=3/8$.',r'相加得 $2(1/4)(3/4)=3/8$。')],
('A region made of equal-area pieces gives uniform piece labels; unequal pieces require weights.','等面积分区才给出均匀分区标签；面积不等必须加权。'),
'2023-II-Q06',('PS02','GE02')))
save(C,('Continuous uniform probability is a ratio of measures in the original sampling coordinates. Draw the feasible region first, translate the event exactly, and justify all conditioning or coordinate changes before using symmetry.','连续均匀概率是原抽样坐标中的度量比。先画可行区域，再精确转化事件；使用对称之前，须证明条件化或坐标变换成立。'),ms,('GE02','GE07','PS02'))

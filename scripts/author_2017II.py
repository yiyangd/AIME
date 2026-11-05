from content_helpers import Batch
b=Batch('2017II')
b.add(1,'CO04',[('CO02',0)],
r'Count subsets of $\{1,\ldots,8\}$ that are contained in neither $\{1,2,3,4,5\}$ nor $\{4,5,6,7,8\}$.',
r'求 $\{1,\ldots,8\}$ 的子集中，既不包含于 $\{1,2,3,4,5\}$ 也不包含于 $\{4,5,6,7,8\}$ 的个数。',
[r'There are $2^8=256$ subsets. Each forbidden containment class has $2^5=32$ members.',r'The overlap consists of subsets of the intersection $\{4,5\}$, giving4. Inclusion-exclusion therefore leaves $256-32-32+4=196$.'],
[r'全部子集有 $2^8=256$ 个，两个被禁止的包含类各有 $2^5=32$ 个。',r'重叠为交集 $\{4,5\}$ 的子集，共4个。容斥得 $256-32-32+4=196$。'])
b.add(2,'PS02',[],
r'Teams $T_1,T_4$ contest one semifinal, while $T_2,T_3$ contest the other; winners meet in a final. In any match, $T_i$ beats $T_j$ with probability $i/(i+j)$, independently of other matches. If $T_4$ wins the title with reduced probability $p/q$, find $p+q$.',
r'半决赛由 $T_1$ 对 $T_4$、$T_2$ 对 $T_3$，胜者进入决赛。任一场 $T_i$ 对 $T_j$ 的胜率为 $i/(i+j)$，各场独立。若 $T_4$ 夺冠概率为最简分数 $p/q$，求 $p+q$。',
[r'Team4 reaches the final with probability $4/5$. Its opponent is team2 with probability $2/5$ and team3 with probability $3/5$.',r'Conditioning on that opponent, the title probability is $(4/5)[(2/5)(2/3)+(3/5)(4/7)]=256/525$. The numerator is a power of2 and the denominator odd, so the reduced sum is $781$.'],
[r'队4以 $4/5$ 的概率进决赛，对手为队2、队3的概率分别为 $2/5,3/5$。',r'按决赛对手分类，夺冠概率为 $(4/5)[(2/5)(2/3)+(3/5)(4/7)]=256/525$。分子为2的幂，分母为奇数，已最简，和为781。'])
b.add(3,'PS03',[('GE07',0),('GE02',1)],
r'Choose a point uniformly by area inside triangle with vertices $(0,0),(12,0),(8,10)$. If its probability of being nearer $(12,0)$ than either other vertex is reduced $p/q$, find $p+q$.',
r'在顶点为 $(0,0),(12,0),(8,10)$ 的三角形内按面积均匀取点。若该点到 $(12,0)$ 比到其余两个顶点都近的概率为最简分数 $p/q$，求 $p+q$。',
[r'Comparing squared distances gives the half-planes $x>6$ and $y<(2/5)x+1$. Intersecting these with the triangle produces vertices $(6,0),(12,0),(10,5),(6,17/5)$.',r'The quadrilateral area is $15+34/5=109/5$, by splitting along the diagonal from $(6,0)$ to $(10,5)$. The original triangle area is60.',r'The probability is $(109/5)/60=109/300$, giving $p+q=409$. Boundary equalities have area zero.'],
[r'比较距离平方，得两个半平面 $x>6$、$y<(2/5)x+1$。与三角形相交后，区域顶点为 $(6,0),(12,0),(10,5),(6,17/5)$。',r'沿 $(6,0)$ 到 $(10,5)$ 的对角线分割，面积为 $15+34/5=109/5$；原三角形面积为60。',r'概率为 $(109/5)/60=109/300$，故 $p+q=409$。边界等距情形面积为零，不影响概率。'])
b.add(4,'NT06',[],
r'How many positive integers at most2017 have ternary representations using only digits1 and2?',
r'不超过2017的正整数中，三进制表示仅使用数字1、2的有多少个？',
[r'All one- through six-digit ternary strings qualify under the bound, contributing $\sum_{k=1}^{6}2^k=126$, since the largest is $222222_3=728$.',r'Convert the bound: $2017=2202201_3$. A seven-digit nonzero-digit string is allowed precisely when its first two digits are11,12 or21; prefix22 would exceed the bound at the third digit. This gives $3\cdot2^5=96$.',r'Total $126+96=222$.'],
[r'一至六位三进制字符串均在范围内，共 $\sum_{k=1}^{6}2^k=126$ 个，因为其中最大值 $222222_3=728$。',r'上界为 $2017=2202201_3$。七位且无零的字符串，前两位只能为11、12、21；若为22，第三位必大于上界的零，无法符合。共 $3\cdot2^5=96$ 个。',r'总数为 $126+96=222$。'])
b.add(5,'AL01',[('LO03',0)],
r'Four distinct real numbers have six unordered pair sums, listed without order as $189,320,287,234,x,y$. Find the largest possible $x+y$.',
r'四个不同实数的六个无序两两和，未按顺序列为 $189,320,287,234,x,y$。求 $x+y$ 的最大值。',
[r'Let the four-number total be $s$. The six pair sums split into three complementary pairs, each totaling $s$. If $x,y$ formed one pair, the four given values would split into two equal-sum pairs; none of the three pairings does so ($509\ne521$, $476\ne554$, $423\ne607$).',r'Therefore two given values must themselves be a complementary pair. Since all six sums total $3s$, $x+y=3s-1030\le3(320+287)-1030=791$.',r'Attainment is given by the four distinct numbers $103/2,275/2,365/2,471/2$. Their remaining pair sums are373 and418, totaling791.'],
[r'设四数总和为 $s$。六个两两和可分成三对互补数，每对和均为 $s$。若 $x,y$ 自成一对，四个已知数需分成两对等和，但三种配对均失败：$509\ne521,476\ne554,423\ne607$。',r'因此两个已知数必自成互补对。六个和的总和为 $3s$，故 $x+y=3s-1030\le3(320+287)-1030=791$。',r'取四个不同数 $103/2,275/2,365/2,471/2$，其余两两和为373、418，总和791，达到上界。'])
b.add(6,'NT05',[],
r'Find the sum of positive integers $n$ for which $n^2+85n+2017$ is an integer square.',
r'求使 $n^2+85n+2017$ 为整数平方的所有正整数 $n$ 之和。',
[r'Write the square as $m^2$. Completing the square gives $(2m-(2n+85))(2m+(2n+85))=843=3\cdot281$. The first factor is positive because $4m^2>(2n+85)^2$.',r'The increasing positive odd factor pairs are $(1,843)$ and $(3,281)$. If the factors are $u,v$, then $n=(v-u-170)/4$, giving168 and27, respectively; the corresponding $m$ are211 and71.',r'Both satisfy the original equation and positivity. The requested sum is195.'],
[r'将平方写为 $m^2$，配方得 $(2m-(2n+85))(2m+(2n+85))=843=3\cdot281$。因 $4m^2>(2n+85)^2$，第一因子为正。',r'递增正奇因子对只有 $(1,843)$、$(3,281)$。若因子为 $u,v$，则 $n=(v-u-170)/4$，分别得168、27，对应 $m=211,71$。',r'两者均满足原式且为正，所求和为195。'])
b.add(7,'AL04',[('AL01',1)],
r'For how many integers $k\in[-500,500]$ does $\log(kx)=2\log(x+2)$ have exactly one real solution, using common logarithms?',
r'在整数 $k\in[-500,500]$ 中，有多少个使常用对数方程 $\log(kx)=2\log(x+2)$ 恰有一个实数解？',
[r'The domain requires $x>-2$ and $kx>0$. On this domain the equation is $kx=(x+2)^2$, or $x^2+(4-k)x+4=0$.',r'For each $k<0$, the allowed interval is $(-2,0)$; the line $kx$ strictly decreases while $(x+2)^2$ strictly increases, with opposite endpoint order, giving exactly one crossing. All500 negative values work; $k=0$ is undefined.',r'For $k>0$, one needs positive roots. Discriminant $k(k-8)$ is negative below8, zero at8 with double root2, and positive above8 with two positive roots. Only $k=8$ contributes, so the total is501.'],
[r'定义域要求 $x>-2,kx>0$。在此范围，方程等价于 $kx=(x+2)^2$，即 $x^2+(4-k)x+4=0$。',r'对每个 $k<0$，允许区间为 $(-2,0)$。直线 $kx$ 严格递减，$(x+2)^2$ 严格递增，端点处大小关系相反，故恰有一个交点。500个负整数均可；$k=0$ 时无定义。',r'$k>0$ 时需正根。判别式 $k(k-8)$ 在8以下为负、8时为零且重根为2、8以上有两个正根。因此仅 $k=8$ 另贡献一个，共501个。'])
b.add(8,'NT03',[],
r'Count positive integers $n<2017$ for which $\sum_{j=0}^{6}n^j/j!$ is an integer.',
r'求使 $\sum_{j=0}^{6}n^j/j!$ 为整数的正整数 $n<2017$ 的个数。',
[r'After multiplying by720 and removing integral contributions from $1+n$, the condition is divisibility of $F=n^6+6n^5+30n^4+120n^3+360n^2$ by720. Modulo2 and3, only $n^6$ can obstruct divisibility, so $6\mid n$.',r'Write $n=6t$. The last three terms are now multiples of720, while the first two combine to $6^6t^5(t+1)$. Since $720=2^4\cdot3^2\cdot5$, the only remaining condition is $t\equiv0$ or4 modulo5.',r'The range is $1\le t\le336$. Each allowed residue occurs67 times, giving134 integers.'],
[r'乘720并除去 $1+n$ 的整数贡献后，要求 $F=n^6+6n^5+30n^4+120n^3+360n^2$ 可被720整除。模2、3时，仅 $n^6$ 可能妨碍整除，故 $6\mid n$。',r'令 $n=6t$，后三项已是720的倍数，前两项合为 $6^6t^5(t+1)$。因 $720=2^4\cdot3^2\cdot5$，剩余条件只有 $t\equiv0$ 或4模5。',r'范围为 $1\le t\le336$，两个允许余数各出现67次，共134个。'])
b.add(9,'PS02',[('CO01',1)],
r'A deck has one card for each of the49 combinations of seven numbers and seven colors. Choose an eight-card set uniformly, conditional on covering all numbers and colors. The probability that one card can be discarded while retaining complete coverage is reduced $p/q$. Find $p+q$.',
r'七个号码与七种颜色的49种组合各对应一张牌。等可能选择八张牌组成集合，条件是每种号码和颜色均出现。若可丢弃一张仍保持完整覆盖的条件概率为最简分数 $p/q$，求 $p+q$。',
[r'Complete coverage by eight cards means exactly one repeated number and exactly one repeated color. A discard is possible exactly when their intersection card is present, in which case that card is uniquely discardable.',r'A favorable hand comes uniquely from a seven-card number-color matching ($7!$ choices) plus one of the42 unused cards, yielding211680 hands.',r'For an unfavorable hand, choose the repeated number7 ways and its two colors $\binom72$ ways. The repeated color must be among the other5; choose its two numbers from the remaining6 in $\binom62$ ways, then match the four leftover numbers and colors in $4!$ ways. Count $7\binom72\cdot5\binom62\cdot4!=264600$.',r'The conditional probability is $211680/(211680+264600)=4/9$, giving $p+q=13$.'],
[r'八张牌完整覆盖七种号码和颜色，意味着恰有一个号码重复、一个颜色重复。只有二者交叉的那张牌存在时才能丢弃，而且可丢牌唯一。',r'有利手牌可唯一表示为七张号码颜色一一匹配的牌（$7!$种），再加剩余42张之一，故有211680种。',r'不利手牌中，重复号码有7种，其两颜色有 $\binom72$ 种；重复颜色只能从其余5种选，其两号码从剩余6种中选 $\binom62$ 种，余下四号码四颜色有 $4!$ 种匹配。因此共 $7\binom72\cdot5\binom62\cdot4!=264600$ 种。',r'条件概率为 $211680/(211680+264600)=4/9$，所以 $p+q=13$。'])
b.add(10,'GE07',[('GE02',1)],
r'Rectangle $ABCD$ has $AB=84,AD=42$. Let $M$ be the midpoint of $AD$, $N$ the point on $AB$ with $AN=28$, and $O=CM\cap DN$. A segment $BP$, with $P$ on the boundary of quadrilateral $BCON$, splits its area equally. Find $[CDP]$.',
r'矩形 $ABCD$ 中 $AB=84,AD=42$。$M$ 为 $AD$ 中点，$N$ 在 $AB$ 上且 $AN=28$，$O=CM\cap DN$。线段 $BP$ 将四边形 $BCON$ 面积平分，$P$ 在其边界上。求 $[CDP]$。',
[r'Use $A=(0,0),B=(84,0),C=(84,42),D=(0,42)$. Then $CM:y=x/4+21$ and $DN:y=42-3x/2$ intersect at $O=(12,24)$; $N=(28,0)$.',r'Shoelace gives $[BCON]=2184$, with target half1092. Since $[BCO]=1512>1092$, the boundary intersection $P$ lies on $CO$. From base $BC=42$, $[BCP]=1092$ requires horizontal distance52 from $P$ to $BC$.',r'Thus $P_x=32,P_y=32/4+21=29$. Finally $[CDP]=(84/2)(42-29)=546$.'],
[r'取 $A=(0,0),B=(84,0),C=(84,42),D=(0,42)$。则 $CM:y=x/4+21$，$DN:y=42-3x/2$，交点为 $O=(12,24)$，且 $N=(28,0)$。',r'鞋带公式得 $[BCON]=2184$，一半为1092。因 $[BCO]=1512>1092$，故边界交点 $P$ 在 $CO$ 上。以 $BC=42$ 为底，$[BCP]=1092$ 要求 $P$ 到 $BC$ 的水平距离为52。',r'于是 $P_x=32,P_y=29$，最终 $[CDP]=(84/2)(42-29)=546$。'])
b.add(11,'CO06',[('CO04',1)],
r'Each pair of five labeled towns is joined by one road. Count orientations of all ten roads for which every town can reach every other by a directed route.',
r'五个有标签城镇中，每两镇之间恰有一条道路。将十条路都改为单向，求使任意一镇都能沿有向路线到达任意另一镇的定向数。',
[r'For five vertices, failure of strong connectivity forces an all-outgoing source or all-incoming sink. Indeed, a proper set of vertices reachable from a vertex has all cross edges entering it. A reachable set of size1 or2 contains a global sink; if its size is3 or4, the complementary set of size2 or1 contains a global source.',r'An all-outgoing vertex can be chosen5 ways, with the other6 edges free:320 orientations. There is at most one such vertex. Similarly there are320 with an all-incoming vertex.',r'The intersection has5 choices of source,4 of sink and3 free remaining edges, giving160. Out of $2^{10}=1024$ orientations, the valid count is $1024-320-320+160=544$.'],
[r'五顶点情形下，非强连通必有全出边源点或全入边汇点。取某点能到达的真子集，所有跨边均指向该集合。若可达集大小为1或2，其中必有全局汇点；若为3或4，其大小2或1的补集中必有全局源点。',r'选全出边点有5种，其余6条边自由，得320种，且全出边点至多一个。同理全入边情形也有320种。',r'交集可选源点5种、汇点4种、剩余3条边自由，共160种。全部 $2^{10}=1024$ 种中，合法数为 $1024-320-320+160=544$。'])
b.add(12,'AL03',[('AL05',1),('GE06',0)],
r'Circle $C_0$ has radius1 and marked point $A_0$. For $0<r<1$, circle $C_n$ has radius $r^n$ and is internally tangent to $C_{n-1}$ at $A_{n-1}$. Mark $A_n$ by rotating the radius from its center to $A_{n-1}$ counterclockwise by90 degrees. All these disks have one common point $B$. When $r=11/60$, express the distance from the center of $C_0$ to $B$ as reduced $m/n$ and find $m+n$.',
r'圆 $C_0$ 半径为1，标记点为 $A_0$。对 $0<r<1$，圆 $C_n$ 半径为 $r^n$，并在 $A_{n-1}$ 与 $C_{n-1}$ 内切。将从其圆心指向 $A_{n-1}$ 的半径逆时针旋转90度得到 $A_n$。所有闭圆盘共有一点 $B$。当 $r=11/60$，将 $C_0$ 圆心到 $B$ 的距离约为 $m/n$，求 $m+n$。',
[r'Use complex coordinates with initial center0 and $A_0=1$. Let $O_n$ denote the centers. Induction gives $A_n-O_n=r^ni^n$; internal tangency then gives $O_{n+1}-O_n=(1-r)(ir)^n$.',r'The radii shrink to zero in nested disks, so their unique common point is the center limit $B=(1-r)/(1-ir)$. Its distance from0 is $(1-r)/\sqrt{1+r^2}$.',r'At $r=11/60$, this equals $49/\sqrt{3600+121}=49/61$. Thus $m+n=110$. The center-to-limit distance after stage $n$ is $r^n(1-r)/\sqrt{1+r^2}<r^n$, so the point is inside every disk.'],
[r'取复坐标初始圆心为0，$A_0=1$，各圆心记为 $O_n$。归纳得 $A_n-O_n=r^ni^n$，再由内切关系得 $O_{n+1}-O_n=(1-r)(ir)^n$。',r'圆盘嵌套且半径趋零，唯一公共点为圆心极限 $B=(1-r)/(1-ir)$，距0为 $(1-r)/\sqrt{1+r^2}$。',r'代入 $r=11/60$，距离为 $49/\sqrt{3600+121}=49/61$，所求和110。第 $n$ 个圆心到极限点的距离为 $r^n(1-r)/\sqrt{1+r^2}<r^n$，故确实在每个圆盘内部。'])
b.add(13,'CO06',[('CO04',0)],
r'Let $f(n)$ count three-vertex subsets of a regular $n$-gon forming isosceles triangles, including equilateral ones. Find the sum of all integers $n\ge3$ for which $f(n+1)-f(n)=78$.',
r'令 $f(n)$ 为正 $n$ 边形顶点中任选三点组成等腰三角形的个数，等边也计入。求满足 $f(n+1)-f(n)=78$ 的所有整数 $n\ge3$ 之和。',
[r'At each apex there are $\lfloor(n-1)/2\rfloor$ symmetric vertex pairs. Every nonequilateral isosceles triangle has one apex, but an equilateral is counted three times. Thus $f(n)=n\lfloor(n-1)/2\rfloor-(2n/3)\mathbf1_{3\mid n}$.',r'Write $n=6k+j$ for $j=0,1,2,3,4,5$. Substituting into this formula gives successive differences $13k,3k,5k+1,7k+3,9k+6,-k-2$, respectively.',r'Equaling78 yields only $k=6,j=0$; $k=26,j=1$; and $k=8,j=4$. Therefore $n=36,157,52$, with sum245.'],
[r'每个顶点作为顶角，有 $\lfloor(n-1)/2\rfloor$ 对对称底点。非等边等腰三角形只数一次，等边被数三次，故 $f(n)=n\lfloor(n-1)/2\rfloor-(2n/3)\mathbf1_{3\mid n}$。',r'写成 $n=6k+j$，$j=0,1,2,3,4,5$。代入公式，差依次为 $13k,3k,5k+1,7k+3,9k+6,-k-2$。',r'令其为78，仅得 $(k,j)=(6,0),(26,1),(8,4)$，对应 $n=36,157,52$，和为245。'])
b.add(14,'CO06',[('GE07',0),('CO04',2)],
r'In the three-dimensional grid $\{1,\ldots,10\}^3$, count distinct straight lines containing exactly eight grid points.',
r'在三维点阵 $\{1,\ldots,10\}^3$ 中，求恰含八个点阵点的不同直线数。',
[r'Choose a primitive integral direction vector. Eight points span seven primitive steps, so every component has absolute value at most1. Axis-parallel lines contain10 points and do not qualify.',r'If exactly one component is zero, the line lies in one of30 coordinate-parallel $10\times10$ planes. In each plane, two diagonals of each slope $+1,-1$ have exactly8 points (offset magnitude2). This contributes120.',r'If all components are nonzero, there are four directions up to sign, equivalent by cube symmetry. For $(1,1,1)$, normalize a point on the line so its least coordinate is1. Exactly8 points means its greatest coordinate is3. The count of triples in $\{1,2,3\}^3$ using both1 and3 is $27-8-8+1=12$.',r'The space-diagonal contribution is $4\cdot12=48$, for total $120+48=168$.'],
[r'选本原整数方向向量。八点跨越七个本原步长，所以每个分量绝对值至多1。平行坐标轴的直线含10点，不符合。',r'若恰有一个零分量，直线位于30个平行坐标面的 $10\times10$ 平面之一。每平面中，斜率 $+1,-1$ 各有两条偏移量绝对值为2的直线恰含8点，共120条。',r'若三个分量均非零，除整体反向外有四方向，由立方体对称性计数相同。对 $(1,1,1)$，将线上的代表点规范为最小坐标为1，恰含8点要求最大坐标为3。$\{1,2,3\}^3$ 中同时用到1、3的三元组有 $27-8-8+1=12$ 个。',r'空间对角方向贡献 $4\cdot12=48$，总数 $168$。'])
b.add(15,'GE07',[('AL07',1)],
r'Tetrahedron $ABCD$ has opposite edge pairs $AD=BC=28$, $AC=BD=44$, $AB=CD=52$. Minimize $AX+BX+CX+DX$ over all spatial points $X$. If the minimum is $m\sqrt n$ with squarefree positive integer $n$, find $m+n$.',
r'四面体 $ABCD$ 的对棱分别满足 $AD=BC=28,AC=BD=44,AB=CD=52$。在空间任意点 $X$ 中最小化 $AX+BX+CX+DX$。若最小值为 $m\sqrt n$，$n$ 为无平方因子的正整数，求 $m+n$。',
[r'Embed the tetrahedron at $A=(a,b,c),B=(a,-b,-c),C=(-a,b,-c),D=(-a,-b,c)$. The edge equations give $a^2+b^2=196$, $a^2+c^2=484$, $b^2+c^2=676$, so $(a^2,b^2,c^2)=(2,194,482)$. All are positive, and these coordinates realize every given edge.',r'Each vertex vector $v$ has length $R=\sqrt{678}$, and the four vectors sum to0. For any position vector $x$, Cauchy gives $|v-x|\ge(v-x)\cdot(v/R)=R-v\cdot x/R$.',r'Sum this inequality over the four vertices to obtain $f(X)\ge4R$. Equality is attained at $x=0$, so the minimum is $4\sqrt{678}$. As $678=2\cdot3\cdot113$ is squarefree, $m+n=682$.'],
[r'取四面体坐标 $A=(a,b,c),B=(a,-b,-c),C=(-a,b,-c),D=(-a,-b,c)$。棱长给出 $a^2+b^2=196,a^2+c^2=484,b^2+c^2=676$，故 $(a^2,b^2,c^2)=(2,194,482)$，均为正，且这些坐标满足全部给定棱长。',r'各顶点向量 $v$ 长均为 $R=\sqrt{678}$，四向量和为0。对任意位置向量 $x$，柯西不等式给出 $|v-x|\ge(v-x)\cdot(v/R)=R-v\cdot x/R$。',r'将四个顶点的不等式相加得 $f(X)\ge4R$。$x=0$ 时取等号，故最小值为 $4\sqrt{678}$。因 $678=2\cdot3\cdot113$ 无平方因子，所求和为682。'])
b.save()

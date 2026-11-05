from content_helpers import Batch
b=Batch('2017I')
b.add(1,'CO02',[('CO06',0)],
r'On the boundary of a nondegenerate triangle, mark its three vertices and another $3,4,5$ points in the interiors of its three respective sides. How many positive-area triangles have all vertices among these15 points?',
r'在非退化三角形边界上标记三个顶点，并在三条边内部分别再取 $3,4,5$ 个不同点。用这15点作顶点，可组成多少个正面积三角形？',
[r'Choose any three of15 points, giving $\binom{15}{3}=455$ triples. A line not coinciding with a triangle side meets the convex boundary in at most two points, so every degenerate triple lies on one side.',r'Including endpoints, the side counts are $5,6,7$. Their collinear triples are disjoint and total $\binom53+\binom63+\binom73=65$. Thus the answer is $455-65=390$.'],
[r'任取三点共 $\binom{15}{3}=455$ 种。不与三角形边重合的直线至多与凸边界交于两点，所以退化三元组都在同一边上。',r'含端点的三边点数为 $5,6,7$，共线三元组互不重叠，共 $\binom53+\binom63+\binom73=65$ 种。因此答案 $455-65=390$。'])
b.add(2,'NT02',[('NT03',0)],
r'The integers $702,787,855$ all leave the same positive remainder $r$ modulo a positive integer $m$. The integers $412,722,815$ all leave the same positive remainder $s\ne r$ modulo a positive integer $n$. Find $m+n+r+s$.',
r'$702,787,855$ 除以正整数 $m$ 后均余正整数 $r$；$412,722,815$ 除以正整数 $n$ 后均余正整数 $s\ne r$。求 $m+n+r+s$。',
[r'Equal remainders force $m\mid\gcd(787-702,855-787)=\gcd(85,68)=17$. The divisor1 cannot leave a positive remainder, so $m=17,r=5$.',r'Similarly $n\mid\gcd(310,93)=31$, and positivity forces $n=31,s=9$. The sum is $17+31+5+9=62$.'],
[r'同余条件要求 $m\mid\gcd(787-702,855-787)=\gcd(85,68)=17$。除数1不可能产生正余数，所以 $m=17,r=5$。',r'同理 $n\mid\gcd(310,93)=31$，正余数迫使 $n=31,s=9$。相加得 $62$。'])
b.add(3,'NT04',[('AL05',0)],
r'Let $d_n$ be the last decimal digit of $n(n+1)/2$. Compute $\sum_{n=1}^{2017}d_n$ modulo1000.',
r'令 $d_n$ 为 $n(n+1)/2$ 的十进制个位数字，求 $\sum_{n=1}^{2017}d_n$ 模1000的余数。',
[r'Triangular numbers at indices $n+20,n$ differ by $20n+210$, divisible by10. Thus the last digits have period20.',r'One period is $(1,3,6,0,5,1,8,6,5,5,6,8,1,5,0,6,3,1,0,0)$, with sum70. Since $2017=100\cdot20+17$, the remaining first17 terms sum69.',r'Total $7069$ has remainder69, or AIME format069.'],
[r'下标 $n+20,n$ 对应三角数相差 $20n+210$，可被10整除，因此个位数字以20为周期。',r'一周期为 $(1,3,6,0,5,1,8,6,5,5,6,8,1,5,0,6,3,1,0,0)$，和为70。因 $2017=100\cdot20+17$，剩下前17项的和为69。',r'总和7069的余数为69，AIME格式写为069。'])
b.add(4,'GE10',[('GE05',0),('GE03',1)],
r'A tetrahedron has an isosceles base of side lengths $20,20,24$; each edge joining its apex to a base vertex has length25. Its volume is $m\sqrt n$ with squarefree positive integer $n$. Find $m+n$.',
r'四面体的等腰底面三边为 $20,20,24$，顶点到底面三个顶点的棱均长25。体积为 $m\sqrt n$，$n$ 为无平方因子的正整数。求 $m+n$。',
[r'Equal apex distances put its perpendicular projection at the base circumcenter. The base altitude is $\sqrt{20^2-12^2}=16$, so area $K=192$ and circumradius $R=20\cdot20\cdot24/(4K)=25/2$.',r'The pyramid height is $\sqrt{25^2-R^2}=25\sqrt3/2$. Its volume is $K h/3=800\sqrt3$, giving $m+n=803$.'],
[r'顶点到底面三点等距，故垂足为底面外心。底面高为 $\sqrt{20^2-12^2}=16$，面积 $K=192$，外接圆半径 $R=20\cdot20\cdot24/(4K)=25/2$。',r'锥高为 $\sqrt{25^2-R^2}=25\sqrt3/2$。体积 $K h/3=800\sqrt3$，所以 $m+n=803$。'])
b.add(5,'NT06',[],
r'A positive rational has base-eight expansion $ab.cd$ and base-twelve expansion $bb.ba$, with all four digits $a,b,c,d$ nonzero. Find the decimal three-digit numeral $abc$.',
r'一个正有理数的八进制表示为 $ab.cd$，十二进制表示为 $bb.ba$，其中 $a,b,c,d$ 均为非零数字。求十进制三位数 $abc$。',
[r'Fractional parts are below1 in both bases, so integer parts agree: $8a+b=13b$, or $2a=3b$. The base-eight bounds allow only $(a,b)=(3,2),(6,4)$.',r'The fractional equality is $(8c+d)/64=(12b+a)/144$. The two cases respectively give $8c+d=12$ and24. The latter requires a zero units digit, forbidden; the former yields $c=1,d=4$.',r'Thus the requested decimal numeral is321.'],
[r'两个进制的小数部分均小于1，所以整数部分相等：$8a+b=13b$，即 $2a=3b$。八进制数字范围仅允许 $(a,b)=(3,2),(6,4)$。',r'小数部分相等给出 $(8c+d)/64=(12b+a)/144$，两种情形分别要求 $8c+d=12,24$。后一种迫使个位数字为零，被排除；前一种得 $c=1,d=4$。',r'所求十进制数为321。'])
b.add(6,'PS03',[('GE04',0),('AL01',1)],
r'An isosceles triangle with equal base angles $x$ degrees is inscribed in a circle. Two independent uniformly sampled circumference points determine a chord. Its probability of meeting the triangle is $14/25$. Find the largest possible $x$ minus the smallest.',
r'一个等腰三角形内接于圆，两底角均为 $x$ 度。在圆周上独立均匀取两点形成弦，该弦与三角形相交的概率为 $14/25$。求 $x$ 的最大可能值与最小可能值之差。',
[r'The three consecutive arcs between triangle vertices have measures $2x,2x,360-4x$. A chord misses the triangle exactly when both endpoints lie on the same such arc, apart from zero-probability boundary cases.',r'With $u=x/180$, the miss probability is $2u^2+(1-2u)^2=11/25$. This reduces to $75u^2-50u+7=0$, whose roots are $1/5,7/15$.',r'The corresponding angles $36^\circ,84^\circ$ both lie in $(0,90^\circ)$ and form nondegenerate triangles. Their difference is48.'],
[r'三个相邻顶点间的圆弧度数为 $2x,2x,360-4x$。除概率为零的边界情形，弦不碰三角形当且仅当两端点落在同一段弧上。',r'令 $u=x/180$，不相交概率为 $2u^2+(1-2u)^2=11/25$，化为 $75u^2-50u+7=0$，两根 $1/5,7/15$。',r'对应 $36^\circ,84^\circ$，均在 $(0,90^\circ)$ 内，三角形非退化，差为48。'])
b.add(7,'CO02',[],
r'Let $S=\sum_{a,b\ge0,\ a+b\le6}\binom6a\binom6b\binom6{a+b}$. Find $S\bmod1000$.',
r'令 $S=\sum_{a,b\ge0,\ a+b\le6}\binom6a\binom6b\binom6{a+b}$，求 $S$ 模1000的余数。',
[r'Set $c=6-a-b$ and use binomial symmetry. The sum becomes $\sum_{a+b+c=6}\binom6a\binom6b\binom6c$.',r'This counts choosing six objects from three disjoint six-object groups, classified by the number chosen from each. Thus $S=\binom{18}{6}=18564$, with remainder564.'],
[r'令 $c=6-a-b$，用组合数对称性，原和变为 $\sum_{a+b+c=6}\binom6a\binom6b\binom6c$。',r'这表示从三个互不相交的六元素组中共选六个，按各组选中数分类。因此 $S=\binom{18}{6}=18564$，余数564。'])
b.add(8,'PS03',[('GE04',0)],
r'Independently choose $a,b$ uniformly from $(0,75)$ degrees. Let $OP=200$. On the same side of $OP$, choose $Q,R$ with right angles $OQP,ORP$ and angles $POQ=a,POR=b$. If $\Pr(QR\le100)=m/n$ in lowest terms, find $m+n$.',
r'角度 $a,b$ 独立均匀取自 $(0,75)$ 度，$OP=200$。在 $OP$ 同侧取 $Q,R$，使 $OQP,ORP$ 均为直角，且 $POQ=a,POR=b$。若 $\Pr(QR\le100)=m/n$ 为最简分数，求 $m+n$。',
[r'Thales theorem places $Q,R$ on the same semicircle with diameter $OP$ and radius100. The chord length is $QR=200\sin|a-b|$. Since the angle difference is below75 degrees, the event is equivalent to $|a-b|\le30$.',r'In the uniform $75\times75$ parameter square, the excluded region consists of two triangles of leg45. Its total area is $45^2$, so the probability is $1-45^2/75^2=16/25$. Hence $m+n=41$.'],
[r'由泰勒斯定理，$Q,R$ 在以 $OP$ 为直径、半径100的同一半圆上，弦长 $QR=200\sin|a-b|$。角差小于75度，所以事件等价于 $|a-b|\le30$。',r'在均匀的 $75\times75$ 参数正方形中，排除区域为两个直角边45的三角形，总面积 $45^2$。概率为 $1-45^2/75^2=16/25$，故 $m+n=41$。'])
b.add(9,'NT03',[('AL05',0)],
r'Set $a_{10}=10$ and $a_n=100a_{n-1}+n$ for integers $n>10$. Find the smallest $n>10$ such that $99\mid a_n$.',
r'令 $a_{10}=10$，整数 $n>10$ 时 $a_n=100a_{n-1}+n$。求使 $99\mid a_n$ 的最小 $n>10$。',
[r'Modulo99, multiplying by100 does nothing. Hence $a_n\equiv10+11+\cdots+n=(n+10)(n-9)/2$. Since2 is invertible modulo99, the condition is $99\mid(n+10)(n-9)$.',r'The two factors differ by19, coprime to99, so each of the prime powers9 and11 must divide a single factor. The four resulting CRT classes modulo99 are $n\equiv9,45,53,89$.',r'The least representative greater than10 is45; its sum is $55\cdot36/2=990$, divisible by99.'],
[r'模99时，乘100不改变余数，所以 $a_n\equiv10+11+\cdots+n=(n+10)(n-9)/2$。因2在模99下可逆，条件为 $99\mid(n+10)(n-9)$。',r'两因子相差19，与99互质，所以质数幂9、11各须完整整除某一因子。四种CRT同余类为 $n\equiv9,45,53,89\pmod{99}$。',r'大于10的最小值为45，此时和为 $55\cdot36/2=990$，可被99整除。'])
b.add(10,'AL03',[('GE07',1),('GE04',0)],
r'Let $z_1=18+83i,z_2=18+39i,z_3=78+99i$. Among complex $z\ne z_3$ for which $[(z_3-z_1)/(z_2-z_1)][(z-z_2)/(z-z_3)]$ is real, choose the one with largest imaginary part. Find its real part.',
r'令 $z_1=18+83i,z_2=18+39i,z_3=78+99i$。在使 $[(z_3-z_1)/(z_2-z_1)][(z-z_2)/(z-z_3)]$ 为实数的 $z\ne z_3$ 中，选择虚部最大者。求其实部。',
[r'The real cross-ratio condition equates directed inscribed angles modulo180 degrees. Since the three fixed points are noncollinear, the locus is their circumcircle, excluding the undefined point $z_3$.',r'The first two points have perpendicular bisector $y=61$. The second and third have midpoint $(48,69)$ and slope1, so their bisector is $y-69=-(x-48)$. The center is therefore $(56,61)$.',r'The highest point is directly above the center, with real coordinate56. Its height exceeds99, so it is not the excluded point $z_3$.'],
[r'交比为实数等价于有向圆周角模180度相等。三个固定点不共线，故轨迹为其外接圆，去掉使分母为零的 $z_3$。',r'前两点连线的垂直平分线为 $y=61$；后二点中点 $(48,69)$、斜率1，其垂直平分线为 $y-69=-(x-48)$。所以圆心为 $(56,61)$。',r'最高点在圆心正上方，实部为56，且其高度大于99，不是被排除的 $z_3$。'])
b.add(11,'PS06',[('CO01',1)],
r'Arrange digits1 through9 bijectively in a $3\times3$ array. Take the median in each row and then the median of those three medians. If $Q$ arrays give final median5, find $Q\bmod1000$.',
r'将数字1至9各用一次填入 $3\times3$ 数组，先取每行中位数，再取三个中位数的中位数。若最终为5的数组有 $Q$ 个，求 $Q$ 模1000的余数。',
[r'Write the four digits below5 as L and the four above5 as G. The row containing5 must have one L and one G. The remaining two row medians must straddle5.',r'The other row types are either LLL and GGG, or LLG and LGG. Assigning the three row types and ordering the L5G row gives $3!\cdot3!=36$ patterns. The two cases supply another factor1 or9, respectively, for360 letter patterns.',r'Fill the L and G slots independently in $4!$ ways each. Thus $Q=360(4!)^2=207360$, with remainder360.'],
[r'将四个小于5的数字记为L，四个大于5的记为G。含5的行必须同时有一个L、一个G；另两行的中位数须分居5两侧。',r'其余行型只能是LLL与GGG，或LLG与LGG。三行类型的分配及L5G行内部排列共 $3!\cdot3!=36$ 种；两种情形的另两行分别再提供因子1或9，共360种字母模式。',r'L槽、G槽分别有 $4!$ 种数字填法，因此 $Q=360(4!)^2=207360$，余数360。'])
b.add(12,'CO02',[('LO03',1)],
r'Count subsets $S\subseteq\{1,\ldots,10\}$ with no elements $a,b,c\in S$ satisfying $ab=c$; the three elements need not be distinct.',
r'求 $\{1,\ldots,10\}$ 的子集 $S$ 中，不存在 $a,b,c\in S$ 使 $ab=c$ 的个数，其中三元素允许相同。',
[r'The number1 is forbidden by $1\cdot1=1$. If2 and3 are both absent, every subset of $\{4,\ldots,10\}$ works because products exceed10. This contributes128, including the empty set.',r'If3 is the least element, exclude9 and choose freely from $4,5,6,7,8,10$, giving64 sets. If2 is the least, exclude4; the free elements7,8 give a factor4.',r'In the latter case, $\{3,6,9\}$ has five valid choices: empty, each singleton, or $\{6,9\}$. The pair $\{5,10\}$ has three choices, excluding their joint selection. All remaining product constraints have now been covered, giving $4\cdot5\cdot3=60$ sets.',r'Total $128+64+60=252$.'],
[r'由 $1\cdot1=1$，不能含1。若2、3均不选，则 $\{4,\ldots,10\}$ 任意子集都合法，因为乘积大于10，共128个，包含空集。',r'若最小元素为3，排除9，其余 $4,5,6,7,8,10$ 自由选择，共64个。若最小元素为2，排除4，自由元素7、8给出因子4。',r'后一情形中，$\{3,6,9\}$ 有空集、各单点、$\{6,9\}$ 共五种；$\{5,10\}$ 可选三种，不能同时选。全部乘积限制已覆盖，故有 $4\cdot5\cdot3=60$ 个。',r'总数为 $128+64+60=252$。'])
b.add(13,'NT05',[],
r'For integer $m\ge2$, let $Q(m)$ be the smallest positive integer such that every integer $n\ge Q(m)$ admits an integer cube $k^3$ satisfying $n<k^3\le mn$. Find $\sum_{m=2}^{2017}Q(m)$ modulo1000.',
r'对整数 $m\ge2$，令 $Q(m)$ 为最小正整数，使每个整数 $n\ge Q(m)$ 都有整数立方 $k^3$ 满足 $n<k^3\le mn$。求 $\sum_{m=2}^{2017}Q(m)$ 模1000的余数。',
[r'If $k^3\le n<(k+1)^3$, the next candidate cube is $(k+1)^3$. The worst ratio in that block is $(1+1/k)^3$, decreasing with $k$.',r'For $m\ge8$, every block works from $n=1$, so $Q=1$. For $4\le m\le7$, $n=1$ fails, $2\le n\le7$ is covered by8, and blocks $k\ge2$ have ratio at most $27/8<4$, so $Q=2$.',r'For $m=3$, $n=8$ fails; $9\le n\le26$ is covered by27, and later ratios are at most $64/27<3$, so $Q=9$. For $m=2$, $n=31$ fails; $32\le n\le63$ is covered by64, and later ratios are at most $125/64<2$, so $Q=32$.',r'The sum is $32+9+4\cdot2+2010=2059$, with remainder59.'],
[r'若 $k^3\le n<(k+1)^3$，下一候选立方为 $(k+1)^3$。每块中最不利的比为 $(1+1/k)^3$，随 $k$ 递减。',r'$m\ge8$ 时从 $n=1$ 起各块均可行，所以 $Q=1$。$4\le m\le7$ 时，$n=1$ 失败，$2\le n\le7$ 用8覆盖，其后各块比至多 $27/8<4$，故 $Q=2$。',r'$m=3$ 时 $n=8$ 失败，$9\le n\le26$ 用27覆盖，其后比至多 $64/27<3$，故 $Q=9$。$m=2$ 时 $n=31$ 失败，$32\le n\le63$ 用64覆盖，其后比至多 $125/64<2$，故 $Q=32$。',r'总和 $32+9+4\cdot2+2010=2059$，余数59。'])
b.add(14,'AL04',[('NT04',2),('NT03',2)],
r'Numbers $a,x>1$ satisfy $\log_a(\log_a(\log_a2)+\log_a24-128)=128$ and $\log_a(\log_ax)=256$. Find the remainder of $x$ modulo1000.',
r'$a,x>1$ 满足 $\log_a(\log_a(\log_a2)+\log_a24-128)=128$、$\log_a(\log_ax)=256$。求 $x$ 模1000的余数。',
[r'Put $c=\log_2a>0$. Exponentiating the outer first logarithm and multiplying by $c$ gives $\log_2(24/c)=128c+c2^{128c}$. The left side is strictly decreasing and the right strictly increasing, so there is at most one positive solution.',r'The value $c=3/64$ works: the left is $\log_2512=9$, and the right is $6+3=9$. The second equation then gives $x=a^{a^{256}}=(2^{3/64})^{4096}=2^{192}$, a positive integer.',r'Modulo8 the result is0. Modulo125, Euler gives $2^{192}\equiv2^{-8}\equiv6^{-1}\equiv21$. Solving these two congruences gives $x\equiv896\pmod{1000}$.'],
[r'令 $c=\log_2a>0$。将第一式外层对数指数化，再乘 $c$，得 $\log_2(24/c)=128c+c2^{128c}$。左边严格递减、右边严格递增，故正解至多一个。',r'$c=3/64$ 满足：左边 $\log_2512=9$，右边 $6+3=9$。第二式得 $x=a^{a^{256}}=(2^{3/64})^{4096}=2^{192}$，确为正整数。',r'其模8为0；模125时，欧拉定理给出 $2^{192}\equiv2^{-8}\equiv6^{-1}\equiv21$。合并两个同余得 $x\equiv896\pmod{1000}$。'])
b.add(15,'GE07',[('AL07',1),('GE03',0)],
r'A right triangle has legs $5,2\sqrt3$ and hypotenuse $\sqrt{37}$. Among equilateral triangles with one vertex on each side segment, write the smallest area as $m\sqrt p/n$, where $m,n$ are coprime positive integers and $p$ is squarefree. Find $m+n+p$.',
r'直角三角形的两直角边为 $5,2\sqrt3$，斜边为 $\sqrt{37}$。在每条边线段上各取一顶点构成等边三角形，将最小面积写为 $m\sqrt p/n$，其中 $m,n$ 为互质正整数，$p$ 无平方因子。求 $m+n+p$。',
[r'Use outer vertices $(0,0),(5,0),(0,2\sqrt3)$. If the equilateral side joining the legs has endpoints $(s\cos t,0),(0,s\sin t)$, its third vertex in the positive quadrant is $s(\cos t+\sqrt3\sin t,\sin t+\sqrt3\cos t)/2$. The other orientation has a negative coordinate and cannot lie in the triangle.',r'The hypotenuse equation is $2\sqrt3x+5y=10\sqrt3$. Substitution yields $s=20\sqrt3/(7\sqrt3\cos t+11\sin t)$. Cauchy bounds the denominator by $\sqrt{147+121}=2\sqrt{67}$.',r'Equality has $\cos t=7\sqrt3/(2\sqrt{67}),\sin t=11/(2\sqrt{67})$. The leg intercepts are $105/67,55\sqrt3/67$, within the side segments, and the third vertex is $(135/67,80\sqrt3/67)$ on the hypotenuse segment. Thus the bound is attained.',r'The minimum area is $(\sqrt3/4)(300/67)=75\sqrt3/67$, so $m+n+p=145$.'],
[r'取外三角形顶点 $(0,0),(5,0),(0,2\sqrt3)$。若等边三角形跨两直角边的边端点为 $(s\cos t,0),(0,s\sin t)$，则正象限内第三顶点为 $s(\cos t+\sqrt3\sin t,\sin t+\sqrt3\cos t)/2$。另一朝向至少有一个负坐标，不可能在三角形内。',r'斜边方程为 $2\sqrt3x+5y=10\sqrt3$，代入得 $s=20\sqrt3/(7\sqrt3\cos t+11\sin t)$。由柯西不等式，分母至多 $\sqrt{147+121}=2\sqrt{67}$。',r'等号时 $\cos t=7\sqrt3/(2\sqrt{67}),\sin t=11/(2\sqrt{67})$。两直角边截距为 $105/67,55\sqrt3/67$，均在线段内；第三点为 $(135/67,80\sqrt3/67)$，在斜边线段上，所以界可达到。',r'最小面积为 $(\sqrt3/4)(300/67)=75\sqrt3/67$，故所求和为145。'])
b.save()

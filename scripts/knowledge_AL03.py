from knowledge_helpers_source import method as M,save
C='AL03';ms=[]
ms.append(M(C,1,'Separate real and imaginary parts with all sign branches','连同符号分支分离实部与虚部',[
(r'Write $z=x+iy$, expand using $i^2=-1$, and compare real and imaginary parts.',r'写 $z=x+iy$，用 $i^2=-1$ 展开，再比较实部与虚部。'),
(r'Before clearing a complex denominator, exclude its zero. For principal square roots of real quantities, split nonnegative and negative radicands.',r'清除复分母前先排除零；对实数量的主平方根，区分被开方式非负与负。'),
(r'For product systems, introduce the common product and reconstruct both consistent square-root signs.',r'乘积方程组可设置共同乘积，并恢复两个一致的平方根符号。'),
(r'Check modulus, positivity or integrality restrictions on the resulting coordinates.',r'检查所得坐标的模长、正性或整数限制。')],
(r'Find all complex $z$ with $z+2\overline z=6+i$.',r'求满足 $z+2\overline z=6+i$ 的全部复数 $z$。'),[
(r'Write $z=x+iy$, so $\overline z=x-iy$.',r'写 $z=x+iy$，则 $\overline z=x-iy$。'),
(r'The left side is $3x-iy$. Comparing components gives $3x=6,-y=1$.',r'左侧为 $3x-iy$，比较分量得 $3x=6,-y=1$。'),
(r'The unique solution is $z=2-i$, and direct substitution gives $6+i$.',r'唯一解为 $z=2-i$，直接代入得 $6+i$。')],
('A complex number is real exactly when its imaginary part vanishes, including the value zero.','复数为实数当且仅当虚部为零，其中包括数值零。'),
'2007-I-Q03 2009-I-Q02 2012-II-Q08 2016-I-Q07 2018-II-Q05 2019-II-Q08 2023-I-Q15',('AL01','NT05'),[
(r'For a Gaussian integer $a+bi$, the norm is $a^2+b^2$, and its cube has components $a^3-3ab^2$ and $3a^2b-b^3$. Multiplication by a unit $\pm1,\pm i$ and conjugation change signs or exchange component magnitudes. Before a triangle test, verify both candidate components are positive and use $|X-Y|<L<X+Y$ with proved finite bounds on $a,b$.',r'高斯整数 $a+bi$ 的范数为 $a^2+b^2$，立方的分量为 $a^3-3ab^2,3a^2b-b^3$。乘单位 $\pm1,\pm i$ 与共轭可改变符号或交换分量绝对值。检验三角形前，须确认候选分量为正，并使用 $|X-Y|<L<X+Y$，且先证明 $a,b$ 的有限界。')]))
ms.append(M(C,2,'Pair conjugate roots and recover their real polynomial factor','配对共轭根并恢复实系数因子',[
(r'A real-coefficient polynomial contains every nonreal root together with its conjugate and equal multiplicity.',r'实系数多项式的每个非实根都与其共轭以相同重数出现。'),
(r'The pair $u\pm iv$ gives factor $x^2-2ux+(u^2+v^2)$.',r'根对 $u\pm iv$ 给出因子 $x^2-2ux+(u^2+v^2)$。'),
(r'Use Vieta to connect that factor with the remaining roots; for integer coefficients also enforce trace and norm integrality.',r'用韦达将该因子与其余根联系；整系数情形还须施加迹与范数整数性。'),
(r'Separate all-real multisets from the one-nonreal-pair case when counting cubics.',r'统计三次式时，将全实根多重集与一个非实根对的情形分开。')],
(r'A monic real cubic has roots $2+i$ and $-3$. Its $x^2$ coefficient is $-1$. Find the constant term.',r'首一实三次式有根 $2+i,-3$，其 $x^2$ 系数为 $-1$，求常数项。'),[
(r'The third root must be $2-i$. The root sum is $2+i+2-i-3=1$, consistent with coefficient $-1$.',r'第三根必为 $2-i$。根和为 $2+i+2-i-3=1$，与系数 $-1$ 一致。'),
(r'The conjugate pair has product $(2+i)(2-i)=5$.',r'共轭根对乘积为 $(2+i)(2-i)=5$。'),
(r'The three-root product is $-15$, so the constant term is its negative, $15$.',r'三根乘积为 $-15$，所以常数项为其相反数 $15$。')],
('Conjugation fixes the polynomial only when its coefficients are real.','只有系数为实数时，共轭才保持该多项式不变。'),
'2005-I-Q06 2010-II-Q07 2013-I-Q10 2013-II-Q12 2021-II-Q04 2026-II-Q11',('AL02','CO07')))
ms.append(M(C,3,'Use polar powers and unit-circle angle congruences','使用极形式幂与单位圆辐角同余',[
(r'For nonzero $z$, write $z=r e^{i\theta}$; multiplication adds arguments and multiplies moduli.',r'非零 $z$ 写成 $r e^{i\theta}$；相乘时辐角相加、模长相乘。'),
(r'Equality of unit complex numbers is an angle congruence modulo $2\pi$, not an ordinary angle equality.',r'单位复数相等对应模 $2\pi$ 的辐角同余，而非普通角度相等。'),
(r'For reality, set the imaginary part to zero or equate a complex expression to its conjugate.',r'要求实数时，可令虚部为零，或令表达式与其共轭相等。'),
(r'Count a half-open complete argument interval and remove overlapping angle families explicitly.',r'在半开完整辐角区间计数，并明确消除不同辐角族的重叠。')],
(r'How many unit complex numbers satisfy $z^4\in\mathbb R$ but $z^2\notin\mathbb R$?',r'有多少单位复数满足 $z^4\in\mathbb R$ 而 $z^2\notin\mathbb R$？'),[
(r'Write $z=e^{i\theta}$ for $0\le\theta<2\pi$. Reality of $z^4$ requires $4\theta$ a multiple of $\pi$, giving eight angles.',r'写 $z=e^{i\theta}$，其中 $0\le\theta<2\pi$。$z^4$ 为实数要求 $4\theta$ 为 $\pi$ 的倍数，给出八角。'),
(r'Among them $z^2$ is real exactly when $2\theta$ is a multiple of $\pi$, giving four of those angles.',r'其中 $z^2$ 为实数恰当 $2\theta$ 为 $\pi$ 的倍数，共四角。'),
(r'The required difference is $8-4=4$.',r'所求个数为 $8-4=4$。')],
('A root may have modulus one without being a primitive root of its stated order.','根的模为一，并不表示它一定是该次数的本原单位根。'),
'2000-II-Q09 2001-II-Q14 2005-II-Q09 2012-I-Q06 2014-II-Q10 2018-I-Q06 2019-II-Q08 2022-I-Q04',('NT03',)))
ms.append(M(C,4,'Sum rotating displacements with a complex geometric series','以复等比级数累加旋转位移',[
(r'Encode the multiplier for one displacement as $q=r e^{i\theta}$.',r'将一次位移的倍率编码为 $q=r e^{i\theta}$。'),
(r'For finite motion use $\sum_{j=0}^{n-1}q^j=(1-q^n)/(1-q)$; for a limit verify $|q|<1$ first.',r'有限运动用 $\sum_{j=0}^{n-1}q^j=(1-q^n)/(1-q)$；极限问题先验证 $|q|<1$。'),
(r'A rotation about $c$ is $z\mapsto c+e^{i\theta}(z-c)$; composing with translations produces an affine map.',r'绕 $c$ 旋转为 $z\mapsto c+e^{i\theta}(z-c)$；与平移复合得到仿射映射。'),
(r'Compute the final norm only after summing the vectors; for nested disks prove the limit lies in every disk.',r'向量求和后才求最终模长；嵌套圆盘还须证明极限位于每个圆盘内。')],
(r'Find the fixed point of $F(z)=iz+1$ and explain the geometry of all its orbits.',r'求 $F(z)=iz+1$ 的不动点，并说明全部轨道的几何意义。'),[
(r'The fixed point satisfies $c=ic+1$, so $c=1/(1-i)=(1+i)/2$.',r'不动点满足 $c=ic+1$，故 $c=1/(1-i)=(1+i)/2$。'),
(r'Subtraction gives $F(z)-c=i(z-c)$, a counterclockwise quarter-turn about $c$.',r'相减得 $F(z)-c=i(z-c)$，即绕 $c$ 逆时针四分之一周旋转。'),
(r'The fixed point has period one. Every other point has exact period four, because $i^k(z-c)=z-c$ first holds at $k=4$.',r'不动点周期为一；其余每点的准确周期为四，因为 $i^k(z-c)=z-c$ 首次在 $k=4$ 成立。')],
('Adding lengths gives path length; adding complex displacements gives the endpoint.','长度相加得到路程，复位移相加才得到终点。'),
'2008-II-Q09 2013-I-Q14 2017-II-Q12 2020-I-Q08 2026-I-Q05',('AL05','GE07'),[
(r'If nested disks have radii tending to zero and centers converging to $B$, verify $|B-O_n|\le r_n$ for every $n$. Any two common points would have distance at most $2r_n\to0$, proving uniqueness.',r'嵌套圆盘半径趋零、圆心趋于 $B$ 时，须对每个 $n$ 验证 $|B-O_n|\le r_n$。任意两个公共点距离至多为 $2r_n\to0$，故公共点唯一。')]))
ms.append(M(C,5,'Evaluate products over roots of unity','计算单位根上的乘积',[
(r'Use $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$ when the powers exhaust all $n$th roots.',r'当各幂穷尽所有 $n$ 次单位根时，使用 $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$。'),
(r'For nontrivial roots, divide out $x-1$ and evaluate its removable value at one as $n$.',r'对非平凡单位根，先除去 $x-1$，在一处的可去值为 $n$。'),
(r'Factor a general polynomial into its roots, interchange the two products and reduce powers modulo the smaller defining polynomial.',r'一般多项式先按其根分解，交换两重乘积，再以较小的定义多项式约化幂。'),
(r'For chord lengths, take the modulus after the complex product; do not replace a signed algebraic product by a length prematurely.',r'弦长问题应在复乘积之后取模，不能过早把带符号代数乘积换成长度。')],
(r'For a primitive fifth root $\omega$, compute $\prod_{k=1}^4(1-\omega^k)$ and the product of distances from $1$ to those four roots.',r'对本原五次单位根 $\omega$，计算 $\prod_{k=1}^4(1-\omega^k)$，及一到这四根的距离之积。'),[
(r'The polynomial of the nontrivial fifth roots is $1+x+x^2+x^3+x^4$.',r'非平凡五次单位根的多项式为 $1+x+x^2+x^3+x^4$。'),
(r'Evaluating at one gives the algebraic product $5$.',r'在一处代值得代数乘积 $5$。'),
(r'The distance product is the modulus of that product, also $5$.',r'距离乘积为该乘积的模长，也为 $5$。')],
('If the chosen root is not primitive, its powers may repeat and miss roots.','若所选根非本原根，其幂可能重复并遗漏其他根。'),
'2003-II-Q15 2004-I-Q13 2009-II-Q13 2023-II-Q08 2024-II-Q13',('AL02',)))
ms.append(M(C,6,'Translate complex quotients into angles, circles and perpendicularity','将复商转为角、圆与垂直条件',[
(r'For nonzero displacements $u,v$, $u/v$ real means parallel directions; purely imaginary means perpendicular directions.',r'对非零位移 $u,v$，$u/v$ 为实数表示方向平行，为纯虚数表示方向垂直。'),
(r'A real cross-ratio equates directed inscribed angles modulo $\pi$; for three fixed noncollinear points its locus is their circle.',r'实交比表示有向圆周角模 $\pi$ 相等；三个固定点不共线时，轨迹为其外接圆。'),
(r'Equal-distance loci are perpendicular bisectors; a modulus equation $|z-a|=R$ is a circle.',r'等距轨迹是垂直平分线，模方程 $|z-a|=R$ 是圆。'),
(r'Exclude quotient poles and zero displacement legs, then use coordinates or a circle center for the requested extremum.',r'排除商的极点与零位移边，再用坐标或圆心求所需最值。')],
(r'Find the locus of $z$ for which $(z-1)/(z+1)$ is purely imaginary, including zero as an imaginary value.',r'求使 $(z-1)/(z+1)$ 为纯虚数的 $z$ 的轨迹，其中允许纯虚数取零。'),[
(r'The pole $z=-1$ is excluded. Write $z=x+iy$ and multiply numerator and denominator by $x+1-iy$.',r'排除极点 $z=-1$。写 $z=x+iy$，分子分母乘以 $x+1-iy$。'),
(r'The real numerator is $x^2+y^2-1$ and the denominator is positive, so reality of the zero real part requires $x^2+y^2=1$.',r'分子实部为 $x^2+y^2-1$，分母为正，故实部为零要求 $x^2+y^2=1$。'),
(r'The locus is the unit circle with $-1$ deleted; $z=1$ remains because the quotient is zero.',r'轨迹为删去 $-1$ 的单位圆；$z=1$ 保留，因为商为零。')],
('Specify whether zero counts as purely imaginary before using it as a perpendicularity test.','用纯虚数判垂直之前，须明确零是否允许；非退化垂直位移不能为零。'),
'2012-I-Q14 2017-I-Q10 2019-I-Q12 2025-I-Q08',('GE04','GE07')))
ms.append(M(C,7,'Invert a half-plane and carry unions through the map','反演半平面，并把并集随映射传递',[
(r'For $w=1/z=u+iv$, substitute $z=(u-iv)/(u^2+v^2)$ with $w\ne0$.',r'对 $w=1/z=u+iv$，代入 $z=(u-iv)/(u^2+v^2)$，其中 $w\ne0$。'),
(r'Multiply an inequality only by the positive denominator $u^2+v^2$, then complete the square.',r'只以正分母 $u^2+v^2$ 乘不等式，再配方。'),
(r'Preserve strictness and boundary exclusions. The image of a union is the union of the images.',r'保留严格性与边界排除；并集的像是各像之并。'),
(r'For a union of symmetric disks, identify which disk reaches farthest on each ray before computing wedge areas.',r'对对称圆盘并，先确定各射线方向上哪个圆盘伸得最远，再求扇形分区面积。')],
(r'Find the image of the half-plane $\Re z>1$ under $w=1/z$.',r'求半平面 $\Re z>1$ 在 $w=1/z$ 下的像。'),[
(r'The inequality becomes $u/(u^2+v^2)>1$, with a positive denominator.',r'不等式化为 $u/(u^2+v^2)>1$，分母为正。'),
(r'Rearrange to $(u-1/2)^2+v^2<1/4$.',r'整理得 $(u-1/2)^2+v^2<1/4$。'),
(r'The image is the open disk centered at $1/2$ of radius $1/2$. Its boundary includes zero, so zero is already excluded by strictness.',r'像为以 $1/2$ 为圆心、半径 $1/2$ 的开圆盘；零位于其边界，已由严格性排除。')],
('The map 1/z includes conjugation relative to ordinary radial inversion; use the actual algebra.','映射 1/z 相对通常径向反演还含共轭，应使用实际代数表达式。'),
'2008-II-Q13',('GE02','GE04')))
ms.append(M(C,8,'Optimize a complex norm or real part and prove equality','优化复模或实部，并证明等号可达',[
(r'Factor out a fixed modulus or write $z=R(\cos\theta+i\sin\theta)$.',r'提出固定模长，或写 $z=R(\cos\theta+i\sin\theta)$。'),
(r'For distance from a fixed point to a circle, align the radius oppositely for a maximum; for a real part use $A\cos\theta+B\sin\theta\le\sqrt{A^2+B^2}$.',r'固定点到圆的最远距离使半径方向相反；实部最值用 $A\cos\theta+B\sin\theta\le\sqrt{A^2+B^2}$。'),
(r'For independent choices, optimize each summand separately. For an argument range, use tangent rays to the locus.',r'独立选择时分别优化每一项；辐角范围则用轨迹的切射线。'),
(r'Check the equality point respects half-plane, sign and excluded-point restrictions.',r'检查等号点符合半平面、符号与排除点限制。')],
(r'For $|z|=1$, find the maximum of $\Re((3+4i)z)$ and a maximizing $z$.',r'当 $|z|=1$，求 $\Re((3+4i)z)$ 的最大值及一个达到值的 $z$。'),[
(r'With $z=x+iy$, the objective is $3x-4y$ and $x^2+y^2=1$.',r'设 $z=x+iy$，目标为 $3x-4y$，且 $x^2+y^2=1$。'),
(r'Cauchy bounds it by $\sqrt{3^2+(-4)^2}=5$.',r'柯西不等式给出上界 $\sqrt{3^2+(-4)^2}=5$。'),
(r'Take $z=(3-4i)/5$ to attain five, with modulus one as required.',r'取 $z=(3-4i)/5$ 达到五，其模长确为一。')],
('A norm bound needs the direction of equality, not just the numerical upper bound.','模长估界须给出等号方向，而不只是数值上界。'),
'2011-II-Q08 2012-II-Q06 2014-I-Q07 2024-I-Q07',('AL07','GE04')))
ms.append(M(C,9,'Compose fractional maps and control finite polynomial-root orbits','复合分式映射，并控制有限多项式根轨道',[
(r'Compose the exact map symbolically, keeping every pole and any excluded intermediate value.',r'符号复合精确映射，并保留每个极点及被排除中间值。'),
(r'If a small iterate is identity, reduce the index only for orbits proved to avoid the poles.',r'若某个低次迭代为恒等，只能对已证明避开极点的轨道约化下标。'),
(r'For a polynomial root map, a finite invariant root set cannot contain a point whose modulus grows without bound.',r'多项式根映射的有限不变根集不能含模长无限增长的点。'),
(r'Combine root-product modulus and conjugation to restrict the final root set, then substitute back into the original identity.',r'结合根乘积模长与共轭限制最终根集，再代回原恒等式。')],
(r'For $F(z)=1/(1-z)$, show the orbit of $z_0=2$ has period three.',r'对 $F(z)=1/(1-z)$，证明 $z_0=2$ 的轨道周期为三。'),[
(r'The successive values are $2,-1,1/2,2$.',r'逐次值为 $2,-1,1/2,2$。'),
(r'None equals the pole one, so all intermediate maps are defined.',r'各值均不为极点一，因此所有中间映射都有定义。'),
(r'The first three values are distinct and the fourth returns to the first, proving exact period three.',r'前三个值互异，第四个返回首值，故准确周期为三。')],
('An algebraic composition formula may cancel a pole that the original step still cannot cross.','复合公式可能约掉某极点，但原逐步映射仍不能经过该点。'),
'2002-I-Q12 2007-II-Q14',('AL02','AL09')))
save(C,('Choose coordinates for addition, polar form for multiplication, and geometric loci for a modulus or argument condition. The useful bridge is the complex quotient: its modulus is a length ratio and its argument is a directed angle.','加法用直角坐标，乘法用极形式，模长或辐角条件用几何轨迹。关键桥梁是复商：其模长为长度比，其辐角为有向角。'),ms,('AL01','AL02','AL08'))

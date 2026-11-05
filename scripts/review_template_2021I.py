from itertools import product
from math import gcd
from collections import Counter
from review_helpers_template import Review,BY
assert sum((m//gcd(m,n)-n//gcd(m,n))%4==0 for m in range(1,31) for n in range(m+1,31))==63
for positions,expected in [((0,4,8),{'A':2,'B':6}),((0,2,6),{'A':1,'B':4,'C':1,'stop':2}),((0,2,4),{'B':2,'C':2,'stop':4})]:
 out=Counter()
 for d in product((-1,1),repeat=3):
  p=sorted((a+b)%12 for a,b in zip(positions,d))
  key='stop' if len(set(p))<3 else {(4,4,4):'A',(2,4,6):'B',(2,2,8):'C'}[tuple(sorted((p[(i+1)%3]-p[i])%12 for i in range(3)))]
  out[key]+=1
 assert dict(out)==expected
assert next(k for k in range(1,43) if pow(3,k,43)==1)==42
assert next(k for k in range(1,47) if pow(5,k,47)==1)==46
r=Review('2021I')
r.add(1,['Conditioned on location of the unique loss in races2..6. Terminal loss has four stays, internal loss two switches;16+4*8 over243 reduces16/81,97. Initial win fixed, not randomly resampled.'],[('Weight dependent outcome strings by stays and switches','按保持与转换次数赋予相关结果串概率',['PS02'])])
r.add(2,['Checked AF7,FC9 and right angle forF28/5,36/5; its side ofAC is oppositeB. Four second-rectangle halfplanes reduce to one strip inside the first, constant horizontal width35/4 gives105/4 and109. Diagram orientation preserved explicitly.'],[('Intersect rotated rectangles using linear halfplanes','用线性半平面求旋转矩形交集',['GE07','GE02'])])
r.add(3,['Negative integral exponents cannot produce an integer difference after factoring the odd part. Unique2-adic valuation avoids duplicate representations. Counts10,9,8,7,6,4,3,2,1 sum50.'],[('Use the unique odd part to count differences of powers of two','利用唯一奇数部分计算二次幂之差',['NT01'])])
r.add(4,['All2080 ordered positive compositions split into all-equal1, exactly-two-equal93, and distinct1986. The increasing representatives have free6-permutation orbits, giving331.'],[('Count positive compositions and remove repeated-part cases before dividing by symmetry','计算正整数分拆并先排除重复项再按对称性相除',['CO03','CO01'])])
r.add(5,['Centered progression gives d²(a-2)=3a², forcingpositivea-2 dividing12. Tested every divisor and square candidate; sequences0,5,10 and7,14,21 are valid because source terms need only be integers, not positive. Last-term sum31.'],[('Center a three-term progression and force a divisor condition','将三项等差数列中心化并导出整除条件',['NT05','AL05'])])
r.add(6,['Expanded all four cube-distance squares; side-length and linear terms cancel exactly to2PA². Recomputed73728/2=36864, square root192. PointP was not restricted to inside cube.'],[('Cancel coordinate terms in a cube squared-distance identity','在立方体距离平方恒等式中消去坐标项',['GE10','GE07'])])
r.add(7,['Both sines must reach1. After gcd reduction, a Bezout equation gives necessary and sufficient u=vmod4. Independently counted all435 pairs, exactly63. Realx allows any integer phase parameters.'],[('Convert simultaneous sine maxima into a Bezout congruence condition','把同时正弦最大值转化为贝祖同余条件',['AL08','NT02'])])
r.add(8,['Level-root counts checked at negative,zero,100 andabove100:0,3,4,2; genericpositivebelow100 gives6. Distinct target levelsc±21 require both in(0,100), hence57integerc. No endpoint could also total12.'],[('Build a complete horizontal-level root-count table for an even folded parabola','为偶对称折叠抛物线建立完整水平线根数表',['AL06'])])
r.add(9,['Distance determinants give both numerators18u, with denominatorsleg anddiagonal lengths. Subtracting their squared conditions givesa2u/5, thenu45sqrt2/4. Base sum and area yield567 aftersqrt2 scaling.'],[('Convert point-to-line distances into trapezoid coordinate equations','将点到直线距离化为梯形坐标方程',['GE07','GE02'])])
r.add(10,['InvariantI=m-18d and gcd(d+1,I) transition verified. Successive smallest prime cancellations2,7,11,13 occur atindices2,8,18,30; including1 gives59. OnceI1 no future cancellation or d1 is possible.'],[('Find a linear invariant compatible with reduction of rational iterates','寻找与有理数迭代约分相容的线性不变量',['NT02','LO01'])])
r.add(11,['Reflection across a diagonal-angle bisector followed by scale cosθ is one global similarity giving all four perpendicular feet. Ptolemy product59, Brahmagupta area2sqrt210 givecosθ11/59, perimeter242/59 and301.'],[('Recognize crossed diagonal projections as one reflection-dilation similarity','将交叉对角线投影视为同一反射缩放相似',['GE04']),('Combine Ptolemy and cyclic-quadrilateral area to recover a diagonal angle','结合托勒密与圆内接四边形面积恢复对角线夹角',['GE02'])])
r.add(12,['Independently enumerated all eight sign triples in each cyclic gap state and verified all transition counts. Even gaps prevent overtaking before a collision. Solved exact first-step equations tostart expectation16/3 and19.'],[('Lump symmetric collision-walk states by cyclic gap patterns','按循环间隔模式合并对称碰撞游走状态',['CO05']),('Solve first-step expectation equations with absorbing collisions','建立含吸收碰撞的首次步骤期望方程',['PS04'])])
r.add(13,['External tangency gives power difference672r, while radical-axis gradient magnitude2d times distance r/2 givesdr. The common-chord line, not chord segment, is used correctly; distance672 is consistent with two-circle intersection bounds.'],[('Relate a circle-power difference to distance from the radical axis','将圆幂差与到根轴的距离联系起来',['GE06','GE04'])])
r.add(14,['Checked primes173,283 and primitive-root witnesses3mod43,5mod47 by independent orders42,46. These explicitly forceq andq-1; multiplicative divisor-sum proof gives sufficiency for every prime exponent en. Leastlcm factors are distinct and sum125.'],[('Reduce a universal divisor-sum congruence to prime-power factors','把普遍约数和同余归结为素数幂因子',['NT08']),('Prove a universal exponent is least using explicit prime witnesses','用显式素数见证证明普遍指数最小',['NT04'])])
r.add(15,['Circle-combination equation givesR²325/16+3k/2 andk≤280. For1..4 verified no negative quartic root; positive derivative has only one zero, so cannot have4roots. For5..280 four sign-separated roots, including derivative check atboundaryk5, prove attainment. Extreme sum285.'],[('Combine two conic equations to identify the common intersection circle','组合两条圆锥曲线方程识别交点共圆',['GE08']),('Certify four quartic intersections with sign intervals and boundary derivatives','用变号区间与边界导数证明四个四次方程交点',['AL02'])])
r.save()

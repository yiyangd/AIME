from review_2015 import add_review,reviews,save,ROOT,methods,requirements
import json
methods.update({
'2022-I-Q01':[('AL02','Cancel opposite leading terms before interpolation','插值前先消去相反首项',[])],
'2022-I-Q02':[('NT06','Expand a cyclic mixed-base digit rotation','展开混合进位制的循环数位移位',[]),('NT03','Use a small modulus to filter bounded digits','用小模数筛选有界数位',[])],
'2022-I-Q03':[('GE05','Turn adjacent trapezoid bisectors into an isosceles median','将梯形相邻角平分线化为等腰中线',['GE01']),('GE07','Subtract midpoint coordinates at a common height','相同高度下求两中点横坐标差',[])],
'2022-I-Q04':[('AL03','Convert unit complex powers into an angle congruence','将单位复数幂化为辐角同余',[]),('NT03','Count a linear congruence in bounded residue classes','在有限剩余类中计数线性同余',[])],
'2022-I-Q05':[('AL01','Subtract squared water-relative speed equations','相减静水速度平方方程',['GE07']),('GE07','Add the current vector to swimmer velocities','将水流向量与游泳速度合成',[])],
'2022-I-Q06':[('CO04','Classify forbidden arithmetic progressions by variable usage','按变量使用数分类禁等差列',['AL05']),('CO04','Correct the overlap of one-variable forbidden cases','修正单变量禁例交叠',[])],
'2022-I-Q07':[('LO02','Separate numerator-one candidates from an integer quotient bound','由整数分子界分离分子一的候选',[]),('LO02','Exhaust the six larger-denominator digit complements','穷尽六种更大分母的数字补集',[])],
'2022-I-Q08':[('GE06','Solve vertex-circle tangency with both center-location branches','分圆心位置两支求顶点相切圆',[]),('GE07','Intersect two symmetric equal-radius circles on their common axis','在公共对称轴求两等圆交点',[])],
'2022-I-Q09':[('PS01','Place every color once in each position parity class','每种颜色在奇偶位置类各放一次',['CO01'])],
'2022-I-Q10':[('GE09','Compare sphere-section heights by a difference of squares','用平方差比较球截圆高度',[]),('GE09','Project tangent-sphere center distances onto the section plane','将相切球心距投影到截面',[])],
'2022-I-Q11':[('GE04','Recover endpoint tangent lengths from a diagonal secant','由对角割线求端点切线长',[]),('GE05','Relate angle tangency to radius and half-angle tangent','联系角内相切半径与半角正切',['GE03'])],
'2022-I-Q12':[('CO04','Replace intersection-size sums with marked-element incidences','用带标记元素的关联计数替代交集大小和',['CO02']),('CO02','Collapse squared binomial sums by Vandermonde','用范德蒙德合并组合数平方和',[])],
'2022-I-Q13':[('NT07','Characterize reduced repeating-decimal numerators by a coprime divisor bound','用互质约数上界刻画循环小数最简分子',[]),('NT08','Partition numerator classes by shared denominator primes','按共有分母质因数划分分子类别',['CO04'])],
'2022-I-Q14':[('GE05','Prove the midpoint-cleaver direction with unit vectors and equal boundary paths','用单位向量及等长边界路径证明中点周长平分线方向',['GE07']),('GE03','Recover a triangle angle from two cleaver directions','由两周长平分线方向恢复三角形角',['GE05']),('NT05','Reduce an integer-side cosine equation by congruences and a short square table','用同余及短平方表解整数边余弦方程',['NT03'])],
'2022-I-Q15':[('AL08','Use bounded sine-square substitution to linearize radicals','用有界正弦平方代换线性化根式',['AL01']),('AL08','Enumerate complementary pair-angle branches','枚举互补两角和分支',[])],
'2022-II-Q01':[('NT02','Convert population ratios into an integral scale and verify bus counts','将人数比例化为整数尺度并验证巴士人数',['AL01'])],
'2022-II-Q02':[('PS02','Condition on tournament pairings and the final opponent','按赛程配对与决赛对手作条件分析',[])],
'2022-II-Q03':[('GE09','Equate apex and base-vertex distances to an axial sphere center','将顶点与底顶点到轴上球心的距离相等',['GE10'])],
'2022-II-Q04':[('AL04','Subtract equal-exponent logarithm equations to eliminate the input','相减共同指数的对数方程消去自变量',[])],
'2022-II-Q05':[('CO06','Encode circle triangles by two prime label gaps','用两段质数标号差编码圆上三角形',['NT03'])],
'2022-II-Q06':[('AL07','Bound sorted coordinates by total positive and negative mass','用正负总质量约束排序坐标',['AL06']),('AL07','Construct the three-level equality tuple','构造三层常数的等号序列',[])],
'2022-II-Q07':[('GE06','Locate external tangent-line intersection by a radius ratio','用半径比定位外公切线交点',['GE01']),('GE06','Use the tangent angle to recover the bounded triangle','由切线角恢复所围三角形',[])],
'2022-II-Q08':[('AL06','Characterize singleton floor blocks by consecutive jumps','用连续跳变刻画唯一取整区块',[]),('NT03','Combine jump divisibility into residue classes modulo sixty','将跳变整除合并为模六十剩余类',[])],
'2022-II-Q09':[('CO06','Count generic bipartite segment crossings','统计一般位置二部线段交点',['CO02']),('CO06','Apply Euler after splitting edges at crossings','交点分割边后用欧拉公式',[])],
'2022-II-Q10':[('CO02','Rewrite a nested binomial coefficient as a shifted one','将嵌套组合数重写为移位组合数',[]),('AL05','Telescope a binomial row with the hockey-stick identity','以曲棍球杆恒等式求二项式行和',['CO02'])],
'2022-II-Q11':[('GE05','Reflect side endpoints across internal bisectors','关于内角平分线反射边端点',['GE07']),('GE07','Impose the midpoint twice to determine the common height','两次施加中点条件确定共同高度',[])],
'2022-II-Q12':[('GE08','Translate two ellipses into four focal distances','将两椭圆转化为四条焦距',[]),('AL07','Choose a crossed-focus pairing with simultaneous triangle-inequality equality','选择交叉焦点配对使三角不等式同时取等',[])],
'2022-II-Q13':[('CO03','Read a low coefficient from geometric-series exponents','由等比级数指数读取低次系数',[]),('NT03','Normalize each coefficient variable by complementary prime moduli','按互补质数模归一每个计数变量',[]),('CO03','Count the remaining weak composition by stars and bars','用隔板法统计剩余弱拆分',[])],
'2022-II-Q14':[('LO02','Prove the no-gap stamp interval criterion','证明无缺口邮票区间判据',[]),('LO02','Give a uniform sub-97 construction over a full denomination interval','在整个面值区间统一构造少于九十七张的方案',['AL06']),('LO02','Prove sharp stamp minima by mandatory low denominations','用必需低面值邮票证明紧最小张数',[])],
'2022-II-Q15':[('GE04','Split a cyclic hexagon into two cyclic quadrilaterals','将圆内接六边形分为两个内接四边形',[]),('GE03','Derive and compare their common circumradius formulas','推导并比较两个四边形的共同外接圆半径',['GE04']),('GE04','Use Brahmagupta after eliminating the radius product','消去半径乘积后用婆罗摩笈多面积',[])]
})
for slug in('2022I','2022II'):
 for q in json.loads((ROOT/f'data/batches/{slug}.json').read_text(encoding='utf-8')):
  key=q['question_id'][5:];patch={'method_chain':[x[1] for x in methods[key]]};findings=[];verdict='pass'
  if key=='2022-I-Q08':
   verdict='needs_correction';findings=['Internal circle tangency initially has an absolute center-distance branch. Exclude the between-vertex-and-circumcenter branch explicitly before writing d-18.']
   patch['solution_en']=[r'For the vertex-A circle, let its center distance from A be d>0. Its radius is d/2 by the 30-degree half-angle. Internal tangency is |18-d|=18-d/2. If d<=18 this forces d=0, impossible; hence d>18 and d-18=18-d/2, giving d=24 and radius12.']+q['solution_en'][1:]
   patch['solution_zh']=[r'设顶点 A 对应圆的圆心距 A 为 d>0。由三十度半角，半径为 d/2。内切条件是 |18-d|=18-d/2。若 d<=18，会推出 d=0，矛盾。因此 d>18，解 d-18=18-d/2 得 d=24，半径为12。']+q['solution_zh'][1:]
  if key=='2022-I-Q11':
   verdict='needs_correction';findings=['Replace GE06 secondary: the method uses one circle tangent within an angle and an inradius-half-angle relation, so GE05 is the fitting subtype.']
   patch['secondary']=[x for x in q['secondary'] if x['subtype_id']!='GE06']+[{'category_id':'GE','subtype_id':'GE05','reason_en':'The angle-bisector center gives r=6 tan(A/2), linking tangent lengths to the separation of parallel tangent sides.','reason_zh':'角平分线上的圆心给出 r=6 tan(A/2)，将切线长与两平行切边距离联系起来。'}]
  if key=='2022-I-Q14':
   verdict='needs_correction';findings=['Replace the informal cleaver assertion with an exact unit-vector construction and explicitly equal boundary paths; retain all side-length checks.']
   lemma_en=r'To prove the midpoint-cleaver lemma, put $C$ at the origin and use unit vectors $u$ along $CA$ and $v$ along $CB$. Write $a=CB,b=CA,c=AB$ and $M=(bu+av)/2$. If $a\ge b$, let $X=M-b(u+v)/2=((a-b)/2)v$, a point on $CB$. Then $MX$ is parallel to $u+v$, the internal bisector direction at $C$. The boundary route $M-A-C-X$ has length $c/2+b+(a-b)/2=(a+b+c)/2$; the other route $M-B-X$ has the same length $c/2+a-(a-b)/2$. Their common cut segment adds equally to both polygon perimeters. If $b>a$, swap the roles and choose $X=((b-a)/2)u$. Thus the midpoint perimeter bisector is parallel to the opposite internal angle bisector.'
   lemma_zh=r'严格证明中点周长平分线引理：取 C 为原点，u,v 分别为 CA,CB 方向单位向量，写 a=CB,b=CA,c=AB，则 M=(bu+av)/2。若 a>=b，令 X=M-b(u+v)/2=((a-b)/2)v，位于 CB 上。MX 平行内角平分线方向 u+v。边界路径 M-A-C-X 长为 c/2+b+(a-b)/2=(a+b+c)/2，另一条 M-B-X 长为 c/2+a-(a-b)/2，完全相同。公共切割线段对两个多边形周长的贡献相等。若 b>a，交换两边，取 X=((b-a)/2)u 即可。所以中点周长平分线平行对角的内角平分线。'
   patch['solution_en']=[lemma_en,r'Apply the lemma at the midpoints of $AB$ and $AC$: the two lines are parallel to the internal bisectors at $C$ and $B$. Their acute angle is $90^\circ-A/2$, so the given $30^\circ$ forces $A=120^\circ$.']+q['solution_en'][1:]
   patch['solution_zh']=[lemma_zh,r'将引理用于 AB 与 AC 中点，所得两线分别平行 C、B 的内角平分线。两线锐夹角为九十度减 A/2，所以给定三十度推出 A=一百二十度。']+q['solution_zh'][1:]
   patch['secondary']=q['secondary']+[{'category_id':'GE','subtype_id':'GE07','reason_en':'Unit direction vectors construct the cleaver intersection and verify the two equal boundary paths.','reason_zh':'单位方向向量构造周长平分线交点并核对两条等长边界路径。'}]
  add_review(q['question_id'],verdict,findings,patch)

if __name__=='__main__':save();requirements()

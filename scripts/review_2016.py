from review_2022 import add_review,reviews,save,ROOT,methods,requirements
import json
methods.update({
'2016-I-Q01':[('AL05','Relate sums and products of opposite-ratio geometric series','联系相反公比等比级数的和与积',[])],
'2016-I-Q02':[('PS02','Normalize proportional die weights and multiply independent outcomes','归一成比例骰子权重并乘独立结果',['PS01'])],
'2016-I-Q03':[('CO06','Decompose a monotone polyhedron path by its horizontal layers','按水平层分解单调多面体路径',[]),('CO01','Count simple paths on a cycle from a fixed start','从固定起点统计循环上的简单路径',[])],
'2016-I-Q04':[('GE10','Take a perpendicular section to measure a tetrahedron dihedral','用垂直截面测量四面体二面角',['GE03'])],
'2016-I-Q05':[('AL05','Subtract parallel arithmetic-sum equations to fix the day count','相减平行等差求和方程确定天数',['NT02'])],
'2016-I-Q06':[('GE05','Prove arc-midpoint distance equality to the incenter','证明弧中点到内心的等距关系',['GE04']),('GE01','Use two inscribed-angle similar triangles for a secant product','由圆周角构造相似三角形求割线乘积',['GE04'])],
'2016-I-Q07':[('AL03','Separate real-radical and imaginary-radical cancellation branches','分离实根式与虚根式抵消两支',[]),('NT05','Count signed factor pairs with a required sum sign','按和的符号统计带符号因子对',[])],
'2016-I-Q08':[('NT06','Optimize column digit sums under a last-digit constraint','在末位限制下优化各列数位和',[]),('CO01','Permute each fixed digit column independently','独立排列每个固定数字列',[])],
'2016-I-Q09':[('AL07','Impose segment containment before claiming a trigonometric equality case','声称三角最值等号前先施加线段包含条件',['AL08']),('GE07','Find the true boundary maximizer by determinant and dot product','用行列式与点积求真正边界最大点',['GE03'])],
'2016-I-Q10':[('AL05','Parametrize an alternating geometric-arithmetic recurrence by linear factors','用线性因子参数化交替等比等差递推',[]),('NT01','Find the largest square divisor permitted by a late term','由后项限制确定允许平方约数',[])],
'2016-I-Q11':[('AL02','Extract forced roots from a shifted polynomial identity','由平移多项式恒等式抽取必需根',[]),('AL09','Prove a periodic polynomial is constant by finite differences','用有限差分证明周期多项式恒定',[])],
'2016-I-Q12':[('NT03','Exclude all small prime divisors by quadratic residue tables','用二次剩余表排除全部小质因数',[]),('NT01','Compare the first two four-prime products','比较最小两个四质因数乘积',[]),('NT05','Reject a polynomial value with a nonsquare discriminant','用非平方判别式排除多项式取值',[])],
'2016-I-Q13':[('PS04','Solve a reflecting-boundary hitting-time equation','求解反射边界的首次到达时间方程',[]),('AL05','Reduce a constant second difference to an arithmetic first difference','将常二阶差分化为等差一阶差分',[])],
'2016-I-Q14':[('GE07','Use a linear-form distance test for a thin square and circle lattice','以线性式距离判据筛选细小方圆整格',['NT03']),('NT02','Repeat a primitive lattice segment with shared-endpoint correction','重复本原格段并修正公共端点',[])],
'2016-I-Q15':[('GE04','Use directed radical-axis angles to prove a tangent parallelogram','用有向根轴角证明切线平行四边形',[]),('GE01','Prove a crossed similarity and track its full ray order','证明交叉相似并追踪完整射线次序',['GE04']),('GE04','Convert tangent power into a difference of squared secant lengths','将切线幂化为割线长度平方差',[])],
'2016-II-Q01':[('AL05','Use the middle arithmetic term after unequal removals','不等量扣除后利用等差中项',['AL01'])],
'2016-II-Q02':[('PS02','Recover conditional rain rates from a total probability equation','由全概率方程恢复条件降雨率',[])],
'2016-II-Q03':[('AL04','Sum logarithmic variables to a monotone scalar equation','将对数变量求和为单调标量方程',['AL01'])],
'2016-II-Q04':[('CO04','Double-count colored layers in perpendicular directions','从垂直方向双计数彩色切层',['NT02']),('LO02','Construct identical rows attaining a divisibility volume bound','构造相同行以达到整除体积下界',[])],
'2016-II-Q05':[('GE01','Find the constant similarity ratio of iterated right-triangle altitudes','求迭代直角三角形高的固定相似比',['AL05']),('NT05','Recover a primitive Pythagorean triple from a sum identity','由求和恒等式恢复本原勾股三元组',[])],
'2016-II-Q06':[('AL02','Make all coefficient signs nonnegative by evaluating the variable at its negative','以变量变号使所有系数非负',[]),('AL02','Evaluate the coefficient absolute sum at minus one','在负一处求系数绝对值和',[])],
'2016-II-Q07':[('GE07','Use supporting-coordinate widths for nested rotated squares','使用支持坐标宽度处理嵌套旋转正方形',[]),('NT01','Test square-divisibility of the middle square area','检验中层正方形面积的平方整除',[])],
'2016-II-Q08':[('NT01','Distribute prime exponents into three ordered factors','将质因数指数分配到三个有序因子',['CO03']),('CO01','Remove repeated-factor triples before dividing by six','除六前剔除重复因子三元组',[])],
'2016-II-Q09':[('AL05','Combine arithmetic-linear and geometric-exponential terms at separated indices','在间隔下标组合等差线性项与等比指数项',[]),('NT03','Use the universal divisibility of r-power times r-squared-minus-one','利用 r 幂乘 r 平方减一的恒定整除性',[]),('NT05','Exhaust a bounded ratio-and-index list','穷尽有界公比与下标候选',[])],
'2016-II-Q10':[('GE04','Construct an auxiliary cyclic quadrilateral from equal secant products','由相等割线乘积构造辅助共圆四点',[]),('GE01','Transfer chord angles to a length-ratio similarity','将弦角转化为长度比相似',[])],
'2016-II-Q11':[('NT08','Characterize possible divisor counts of kth powers','刻画 k 次幂可能的约数个数',[]),('CO04','Count the union of two divisor-count residue classes','统计两个约数计数剩余类的并',['NT03'])],
'2016-II-Q12':[('CO05','Compare path colorings with cycle colorings by merging equal endpoints','合并同色两端以比较路径与循环涂色',['CO06'])],
'2016-II-Q13':[('PS04','Average a discrete minimum through tail probabilities','用尾概率求离散最小值平均',[]),('CO01','Count permutations with nested allowed-column sets','统计嵌套允许列集合下的排列',[])],
'2016-II-Q14':[('GE09','Use two axial sphere points as a diameter and a right-triangle altitude','以轴上两球面点为直径并使用直角三角形高',['GE10']),('AL08','Recover two positive tangent heights from their sum and product','由和积恢复两个正切高度',[])],
'2016-II-Q15':[('AL07','Rewrite a pair-product constraint as equality in weighted Cauchy','将两两乘积约束改写为加权柯西等号',[]),('AL05','Sum a finite geometric weight list exactly','精确求有限等比权重和',[])]
})
for slug in('2016I','2016II'):
 for q in json.loads((ROOT/f'data/batches/{slug}.json').read_text(encoding='utf-8')):
  key=q['question_id'][5:]
  existing=next((r for r in reviews if r['question_id']==q['question_id']),None)
  if existing:
   existing['patch']['method_chain']=[x[1] for x in methods[key]]
   if key=='2016-I-Q09':
    existing['patch']['secondary']=q['secondary']+[{'category_id':'GE','subtype_id':'GE07','reason_en':'The complete corrected proof uses coordinate containment, determinant area and dot products to establish the attainable boundary maximum.','reason_zh':'完整更正证明使用坐标包含条件、行列式面积与点积，建立可达到的边界最大值。'}]
   continue
  patch={'method_chain':[x[1] for x in methods[key]]};findings=[];verdict='pass'
  if key=='2016-I-Q14':
   verdict='needs_correction';findings=['Preserve the original circles as circumferences rather than replace them by filled disks. The final intersection count is unchanged, because every qualifying long segment crosses or touches the circumference.']
   patch['statement_en']=r'At each lattice point, center a circle of radius $1/10$ and an axis-aligned closed square of side $1/5$. The segment from $(0,0)$ to $(1001,429)$ intersects $m$ squares and $n$ circle circumferences, with tangency included. Find $m+n$.'
   patch['statement_zh']=r'每个整点为圆心作半径 $1/10$ 的圆周，并以该点为中心作边长 $1/5$、边平行坐标轴的闭正方形。从 $(0,0)$ 到 $(1001,429)$ 的线段与 $m$ 个正方形、$n$ 个圆周相交，切触也计入。求 $m+n$。'
   patch['solution_en']=q['solution_en'][:2]+[q['solution_en'][2].replace('A disk is met','A circle can be met')+r' Every center on the segment contributes a true circumference intersection, including the two full-segment endpoints, because the segment extends at least one radius into each corresponding disk.']+q['solution_en'][3:]
   patch['solution_zh']=q['solution_zh'][:2]+[q['solution_zh'][2].replace('圆盘相交','圆周相交')+r' 每个在线段上的圆心都产生实际圆周交点，包括整段两端，因为线段在相应圆盘内至少延伸一个半径。']+q['solution_zh'][3:]
  add_review(q['question_id'],verdict,findings,patch)

if __name__=='__main__':save();requirements()

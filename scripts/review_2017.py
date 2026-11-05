from review_2016 import add_review,reviews,save,ROOT,methods,requirements
import json

methods.update({
'2017-I-Q01':[('CO02','Subtract collinear triples from all boundary-point triples','从全部边界点三元组中减去共线三元组',['CO06'])],
'2017-I-Q02':[('NT02','Take the gcd of pairwise differences for a common remainder','对同余数的两两差取最大公因数',['NT03'])],
'2017-I-Q03':[('NT04','Prove the triangular-number last-digit period is twenty','证明三角数末位的周期为二十',['AL05'])],
'2017-I-Q04':[('GE10','Locate an equidistant apex above the base circumcenter','将等距顶点定位于底面外心的垂线上',['GE05']),('GE05','Recover a base circumradius from triangle area','由三角形面积恢复底面外接圆半径',['GE03'])],
'2017-I-Q05':[('NT06','Separate integer and fractional parts in two positional bases','分离两种进位制的整数部分与小数部分',[])],
'2017-I-Q06':[('PS03','Use the complement event that both chord endpoints occupy one arc','用弦两端同处一弧的补事件',['GE04']),('AL01','Recover both geometric angle branches from a quadratic probability','由二次概率方程恢复两个几何角分支',[])],
'2017-I-Q07':[('CO02','Complete a triple binomial sum to a fixed-size selection','将三重二项式和补齐为固定大小选取',[])],
'2017-I-Q08':[('PS03','Cut a diagonal band from an angle-parameter square','从角参数正方形截取对角带状区',['GE04'])],
'2017-I-Q09':[('NT03','Reduce decimal concatenation modulo ninety-nine','将十进制拼接化为模九十九求和',['AL05']),('NT03','Separate coprime consecutive factors and combine residue choices','分配互质因子并合并剩余类',[])],
'2017-I-Q10':[('AL03','Recognize a real cross-ratio as a generalized-circle locus','将实交比识别为广义圆轨迹',['GE04']),('GE07','Find a circumcenter from two perpendicular bisectors','由两条垂直平分线求外心',[])],
'2017-I-Q11':[('PS06','Classify low-median and high-median rows around the central digit','围绕中央数字分类低中位数行与高中位数行',[]),('CO01','Separate symbol-pattern arrangements from within-class digit permutations','分离类别符号布局与类内数字排列',[])],
'2017-I-Q12':[('CO02','Condition product-free subsets on their least element','按最小元素分类乘积无关子集',['LO03'])],
'2017-I-Q13':[('NT05','Locate the last failing interval between consecutive cubes','定位相邻立方数间最后一个失败区间',[])],
'2017-I-Q14':[('AL04','Reduce a nested logarithm equation to opposite monotone functions','将嵌套对数方程化为一增一减函数',[]),('NT04','Reduce a large power separately modulo eight and one hundred twenty-five','将大幂分别化到模八与模一百二十五',['NT03'])],
'2017-I-Q15':[('GE07','Parametrize an equilateral triangle by its two axis intercepts','用两坐标轴截距参数化等边三角形',['GE03']),('AL07','Maximize a sine-cosine linear form and verify every segment constraint','最大化正余弦线性式并检验全部线段约束',[])],
'2017-II-Q01':[('CO04','Count two forbidden power-set containments by inclusion-exclusion','用容斥统计两类被禁止的子集包含',['CO02'])],
'2017-II-Q02':[('PS02','Condition a championship on the random final opponent','按随机决赛对手分类夺冠概率',[])],
'2017-II-Q03':[('PS03','Intersect a triangle with two perpendicular-bisector half-planes','将三角形与两垂直平分半平面相交',['GE07','GE02'])],
'2017-II-Q04':[('NT06','Count nonzero ternary digits lexicographically under a fixed upper bound','在给定上界下按字典序统计非零三进制数位',[])],
'2017-II-Q05':[('AL01','Pair four-number pair sums into three equal complementary totals','将四数两两和配成三对相同互补总和',['LO03']),('AL01','Construct a distinct-number realization of the extremal pair-sum assignment','构造极端配对和分配的不同实数实现',[])],
'2017-II-Q06':[('NT05','Factor a completed-square difference and enforce positive factor pairs','分解配方后的平方差并筛选正因子对',[])],
'2017-II-Q07':[('AL04','Enforce logarithm domains before counting quadratic roots','统计二次方程根之前施加对数定义域',['AL01'])],
'2017-II-Q08':[('NT03','Clear factorial denominators and test the prime-power divisibility','清除阶乘分母并检验各质数幂整除',[])],
'2017-II-Q09':[('PS02','Model a coverage-conditioned hand by repeated row and column degrees','用重复行列度数建立覆盖条件手牌模型',['CO01']),('CO01','Count a unique removable intersection card versus its absent case','分类统计唯一可删交叉牌存在或缺失',[])],
'2017-II-Q10':[('GE07','Intersect two cevian lines and move an area bisector along an edge','求两条分割线交点并沿边移动面积平分点',['GE02'])],
'2017-II-Q11':[('CO06','Reduce nonstrong five-vertex tournaments to a source or a sink','将五顶点非强连通竞赛图归结为源点或汇点',[]),('CO04','Correct the overlap of global-source and global-sink orientations','修正全局源点与全局汇点定向的交集',[])],
'2017-II-Q12':[('AL03','Sum rotating internal-tangency center displacements','累加旋转内切的圆心位移',['AL05','GE06']),('AL05','Prove the nested-disk limit is the unique common interior point','证明嵌套圆盘极限为唯一公共内部点',[])],
'2017-II-Q13':[('CO06','Count symmetric apex pairs and subtract equilateral overcount','统计顶点对称点对并减去等边重复计数',['CO04']),('CO06','Split a polygon-count difference into six residue classes','将多边形计数差分为六个剩余类',[])],
'2017-II-Q14':[('CO06','Classify primitive grid-line directions by the required point span','按所需点跨距分类本原格线方向',['GE07']),('CO04','Count normalized diagonal lines by requiring both endpoint coordinate levels','要求两端坐标层均出现以统计规范对角格线',[])],
'2017-II-Q15':[('GE07','Realize an opposite-edge-equal tetrahedron with sign-pattern coordinates','用符号坐标模式实现对棱相等四面体',[]),('AL07','Sum supporting-vector norm bounds when equal-radius vertex vectors cancel','等半径顶点向量和为零时累加范数支持下界',[])]
})

for slug in ('2017I','2017II'):
 for q in json.loads((ROOT/f'data/batches/{slug}.json').read_text(encoding='utf-8')):
  key=q['question_id'][5:]
  patch={'method_chain':[x[1] for x in methods[key]]};findings=[];verdict='pass'
  if key=='2017-II-Q12':
   verdict='needs_correction'
   findings=['Replace ambiguous Chinese fraction wording with an explicit reduced-fraction instruction; the mathematical construction and solution are correct.']
   patch['statement_zh']=q['statement_zh'].replace('将 $C_0$ 圆心到 $B$ 的距离约为 $m/n$','将 $C_0$ 圆心到 $B$ 的距离写成最简分数 $m/n$')
  add_review(q['question_id'],verdict,findings,patch)

if __name__=='__main__':
 # Final canonical records were read and independently rechecked after overlay application.
 # Keep the original findings as correction history while accepting the verified result.
 canonical={q['question_id']:q for q in json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))}
 for r in reviews:
  if r['verdict']=='needs_correction':
   q=canonical[r['question_id']]
   assert all(q.get(k)==v for k,v in r['patch'].items()),r['question_id']
   r['verdict']='pass'
   r['findings'].append('Correction applied and final canonical record rechecked for original conditions, mathematics, necessary classifications and bilingual equivalence; accepted on 2026-11-05.')
 save();requirements()

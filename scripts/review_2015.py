from review_root_batches import add_review,reviews,save,ROOT
import json
methods={
'2015-I-01':[('AL05','Pair adjacent product sums','相邻乘积和配对',[])],
'2015-I-02':[('PS01','Count the nationality pattern 2+1','统计国籍二加一模式',['CO02'])],
'2015-I-03':[('NT01','Split a cube difference into prime-constrained factors','分解立方差并用质数限制',['AL02']),('NT01','Check the final prime by trial division','试除验证最终质数',[])],
'2015-I-04':[('GE07','Place equilateral apices and midpoint coordinates','设置等边顶点与中点坐标',[]),('GE02','Take a two-vector determinant area','双向量行列式面积',['GE07'])],
'2015-I-05':[('PS02','Exchange day labels in uniform dealing','均匀发牌中的日期标签交换',[]),('PS02','Track complete pairs after a mismatch','异色抽取后追踪完整同色对',['PS01'])],
'2015-I-06':[('GE04','Relate two minor-arc partitions through an inscribed angle','通过圆周角联系两个小弧分段',[]),('GE01','Check opposite-side ray order before adding angles','相加前核对两射线位于基准线两侧',['GE04'])],
'2015-I-07':[('GE07','Rotate a square side and impose line incidence','旋转正方形边并代入直线条件',[]),('GE02','Rescale nested-square areas from a normalized model','由归一模型缩放嵌套正方形面积',['GE07'])],
'2015-I-08':[('NT06','Use the nine-per-carry digit-sum defect','每次进位使数位和减少九',[]),('NT06','Minimize digits under an exact carry pattern','给定精确进位模式下最小化数位',[])],
'2015-I-09':[('AL05','Find absorbing-zero triggers in a multiplicative recurrence','寻找乘法递推中的零吸收触发',[]),('AL05','Prove permanent growth with adjacent gaps at least two','用相邻差至少二证明永久增长',[]),('CO04','Count overlapping trigger sets by their complement','通过补集统计重叠触发集合',[])],
'2015-I-10':[('AL02','Partition level-set inputs into cubic root triples','将水平值输入分成三次式根组三元组',[]),('AL02','Match root sums and pairwise products','匹配根和与两两乘积和',[])],
'2015-I-11':[('GE05','Relate incenter distance to half-angle cosine','用半角余弦联系内心距离',['GE03']),('NT05','Use side-length integrality after a short geometric bound','几何短范围后的边长整数筛选',['GE05'])],
'2015-I-12':[('PS04','Average subset minima by exchangeable gap compositions','用可交换间隔拆分求子集最小值平均',['CO03'])],
'2015-I-13':[('AL08','Cancel sine products using complementary angles and doubling','用余角与倍角消去正弦乘积',[]),('NT01','Use a prime exponent to fix an integer power representation','用质指数确定整数幂表示',[])],
'2015-I-14':[('AL06','Sum unit trapezoids under a square-root floor graph','对平方根取整图下单位梯形求和',[]),('NT03','Track half-integer area parity across square blocks','按平方区块追踪半整数面积奇偶状态',[])],
'2015-I-15':[('GE10','Project a tilted cylinder section to a central disk strip','将倾斜圆柱截面投影为中央圆带',['GE02']),('GE02','Subtract two circular caps and apply the section tilt factor','减去两弓形并乘截面倾斜倍数',['GE03'])],
'2015-II-01':[('NT02','Convert integral rational percentages to numerator multiples','将整数百分率转为分子公倍数',[])],
'2015-II-02':[('PS02','Normalize subgroup enrollment counts inside the selected class','在选中类别内归一各子群人数',[])],
'2015-II-03':[('NT06','Filter a minimal multiple by digit-sum congruence','用数位和同余筛选最小倍数',['NT03'])],
'2015-II-04':[('GE03','Recognize a logarithm-scaled 3–4–5 triangle','识别对数缩放的三四五三角形',['AL04'])],
'2015-II-05':[('CO06','Count horizontal and vertical cell-neighbor edges','统计方格水平及竖直邻边',[]),('PS01','Compare grid adjacency probability with a strict threshold','比较方格邻接概率与严格阈值',['CO06'])],
'2015-II-06':[('AL02','Extract a fixed root-square sum from Vieta coefficients','由韦达系数抽取固定根平方和',[]),('NT05','Enumerate positive sorted square triples','枚举递增正整数平方三元组',[]),('LO03','Use remaining coefficient ambiguity to choose a root-sum class','由剩余系数歧义选择根和类别',['AL02'])],
'2015-II-07':[('GE03','Find the base altitude from Heron area','由海伦面积求底边高',[]),('GE01','Express inscribed-rectangle height as a linear function of width','将内接矩形高表示为宽的一次式',[])],
'2015-II-08':[('NT05','Turn a rational bound into a short odd-factor product list','将分式界化为短奇因子乘积表',[]),('NT05','Compare all admissible integer targets','比较全部允许整数目标值',[])],
'2015-II-09':[('GE10','Find a diagonal-perpendicular equilateral cube section','求垂直体对角线的等边立方体截面',['GE03']),('GE10','Compute a submerged corner tetrahedron and check barrel depth','计算浸入角部四面体并检验桶深',[])],
'2015-II-10':[('CO05','Insert the maximum at exactly three admissible slots','在恰三个允许位置插入最大元',['CO01']),('CO05','Prove deletion reverses the insertion without creating a forbidden descent','证明删除能逆转插入且不产生禁降',[])],
'2015-II-11':[('GE07','Use circumcenter dot products and a perpendicular line equation','使用外心点积与垂线方程',['GE04'])],
'2015-II-12':[('CO03','Encode binary runs as parts of size one to three','将二元连续段编码为一至三的拆分',[]),('CO05','Use a tribonacci composition recurrence','使用三阶拆分递推',['CO03'])],
'2015-II-13':[('AL08','Telescope a sine sum into a cosine endpoint difference','将正弦和望远镜化为余弦端点差',['AL05']),('AL06','Order one integer from each irrational moving interval','排列每个无理移动区间中的唯一整数',[])],
'2015-II-14':[('AL01','Replace symmetric monomials by sum and product variables','以和与积变量代换对称单项式',['AL02']),('AL01','Eliminate by an equation ratio before recovering the requested invariant','先用方程比消元再恢复目标不变量',[])],
'2015-II-15':[('GE06','Use negative-radius homothety at an external tangency point','在外切点使用负比例位似',[]),('GE07','Impose a signed point-line distance ratio for equal areas','用同侧点线有向距离比表达等面积',['GE02']),('GE06','Recover a circle chord from center-to-line distance','由弦心距恢复圆弦',[])]
}
methods={k[:-2]+'Q'+k[-2:]:v for k,v in methods.items()}
for slug in('2015I','2015II'):
 for q in json.loads((ROOT/f'data/batches/{slug}.json').read_text(encoding='utf-8')):
  key=q['question_id'][5:];spec=methods[key];patch={'method_chain':[x[1] for x in spec]};findings=[];verdict='pass'
  if key in('2015-II-Q05','2015-II-Q08'):
   patch['secondary']=[x for x in q['secondary'] if x['subtype_id']!='AL07']
   findings=['Remove AL07: the solution uses an elementary finite integer threshold/comparison, not a substantive continuous inequality or optimization method.']
   verdict='needs_correction'
  add_review(q['question_id'],verdict,findings,patch)

def requirements():
 result={}
 for key,spec in methods.items():
  for code,en,zh,pre in spec:
   result.setdefault(code,[]).append({'name_en':en,'name_zh':zh,'question_ids':['AIME-'+key],'prerequisites':pre})
 target=ROOT/'data/knowledge_requirements/source_audit.json';target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps([{'subtype_id':k,'methods':v} for k,v in sorted(result.items())],ensure_ascii=False,indent=2),encoding='utf-8')
 print('Saved teaching requirements for',len(result),'subtypes')

if __name__=='__main__':save();requirements()

from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audit/reviews/root_2015_2022.json'
reviews=[]
def add_review(qid,verdict='pass',findings=None,patch=None,refs=None):
    reviews.append({'question_id':qid,'reviewer':'source_audit','review_type':'separate_agent',
      'source_checked':True,'math_checked':True,'classification_checked':True,'language_checked':True,
      'verdict':verdict,'findings':findings or [],'patch':patch or {},'references':refs or []})

add_review('AIME-2016-I-Q09','source_discrepancy_documented',
 ['The original MAA problem PDF uses segments QR and RS. The official equality at beta=gamma places B outside QR, so its key744 is not the literal constrained maximum. Independent constrained optimization gives the exact value below. No MAA acknowledgment of an erratum is asserted.'],
 {'source_answer':744,'answer_status':'source_discrepancy',
 'corrected_answer_en':r'$\displaystyle\frac{248(1600-496\sqrt6)}{2561-992\sqrt6}\approx728.365125470659$',
 'corrected_answer_zh':r'$\displaystyle\frac{248(1600-496\sqrt6)}{2561-992\sqrt6}\approx728.365125470659$',
 'editorial_note_en':r'The historical source key is 744. Its equality configuration does not satisfy B on segment QR. With all original segment conditions retained, the maximum is the exact value shown above, attained when B=R. This is an independently documented source discrepancy; no official acknowledgment of an erratum is claimed.',
 'editorial_note_zh':r'历史来源答案为744，但其等号构型不满足 B 在线段 QR 上。保留原题全部线段条件时，最大值为上列精确值，在 B=R 时达到。这是独立核对发现的来源矛盾，并不声称官方已承认勘误。',
 'solution_en':[
 r'Put $A=(0,0),Q=(w,0),R=(w,h),S=(0,h)$, $B=(w,b),C=(c,h)$ with $0\le b\le h,0\le c\le w$. Let $\beta=\angle BAQ$, $\gamma=\angle CAS$, and $\alpha=\angle BAC$. The triangle lies inside a rectangle corner, so $\alpha$ is acute and $\cos\alpha=2\sqrt6/5$. Also $\beta+\gamma=90^\circ-\alpha$.',
 r'The side lengths give $w=40\cos\beta$, $b=40\sin\beta$, $c=31\sin\gamma$, $h=31\cos\gamma$. Consequently $K=wh=620[\cos(\beta-\gamma)+1/5]\le744$. However equality needs $\beta=\gamma$, where $\tan\beta=\sqrt{2/3}$. Then $b\le h$ would require $40\sqrt{2/3}\le31$, which is false. Thus 744 is an unattainable upper bound for the stated segment problem.',
 r'Impose $b\le h$: using $\cos\gamma=\sin(\alpha+\beta)$ gives $\tan\beta\le31/(200-62\sqrt6)$. The other condition is automatic since $c=31\cos(\alpha+\beta)\le31\cos\alpha\cos\beta<40\cos\beta=w$. The feasible interval is therefore $0\le\beta\le\arctan[31/(200-62\sqrt6)]\approx32.78425^\circ$.',
 r'The unconstrained area increases until $\beta=(90^\circ-\alpha)/2\approx39.23152^\circ$, beyond that feasible interval. Hence the constrained maximum occurs at its right endpoint, where $b=h$ and $B=R$.',
 r'At this endpoint, $d=BC$ is horizontal and cosine law gives $d^2=2561-992\sqrt6$. The determinant and dot product of $AB,AC$ give $hd=40\cdot31\sin\alpha=248$ and $wd=40^2-40\cdot31\cos\alpha=1600-496\sqrt6$.',
 r'Thus $K_{\max}=248(1600-496\sqrt6)/(2561-992\sqrt6)\approx728.365125470659$. It is attained by $h=248/d,w=(1600-496\sqrt6)/d,C=(w-d,h),B=R$; these satisfy all original lengths and containment conditions. The value 744 remains recorded only as the historical source key.'
 ],
 'solution_zh':[
 r'取 $A=(0,0),Q=(w,0),R=(w,h),S=(0,h)$，并令 $B=(w,b),C=(c,h)$，其中 $0\le b\le h,0\le c\le w$。设 $\beta=\angle BAQ,\gamma=\angle CAS,\alpha=\angle BAC$。三角形位于矩形直角内，故 $\alpha$ 为锐角，$\cos\alpha=2\sqrt6/5$，且 $\beta+\gamma=90^\circ-\alpha$。',
 r'由边长得 $w=40\cos\beta,b=40\sin\beta,c=31\sin\gamma,h=31\cos\gamma$。所以面积 $K=620[\cos(\beta-\gamma)+1/5]\le744$。但等号要求 $\beta=\gamma$，此时 $\tan\beta=\sqrt{2/3}$。线段条件 $b\le h$ 却要求 $40\sqrt{2/3}\le31$，实际不成立。因此744只是不可达到的放宽上界。',
 r'保留 $b\le h$，利用 $\cos\gamma=\sin(\alpha+\beta)$ 可得 $\tan\beta\le31/(200-62\sqrt6)$。另一条件自动成立，因为 $c=31\cos(\alpha+\beta)\le31\cos\alpha\cos\beta<40\cos\beta=w$。所以允许 $\beta$ 从零至约 $32.78425^\circ$。',
 r'未加线段限制时，面积一直递增到 $\beta=(90^\circ-\alpha)/2\approx39.23152^\circ$，已超出允许范围。因此真实最大值在允许区间右端取得，此时 $b=h$，即 $B=R$。',
 r'此时令水平边 $d=BC$。余弦定理给出 $d^2=2561-992\sqrt6$；向量行列式和点积分别给出 $hd=248$、$wd=1600-496\sqrt6$。',
 r'故真实最大面积为 $248(1600-496\sqrt6)/(2561-992\sqrt6)\approx728.365125470659$。取 $h=248/d,w=(1600-496\sqrt6)/d,C=(w-d,h),B=R$ 可达到，并满足原题全部边长及包含条件。744仅作为历史来源答案保留。'
 ],'unresolved_issues':[]},
 ['https://www.isinj.com/mt-aime/2016AIME-IProblems.pdf#page=3','https://www.isinj.com/mt-aime/2016AIME-ISolutions.pdf#page=4','audit/reviews/2016I-Q09-feasibility.md','sources/2016I-problem-p2.png','sources/2016I-sol-p4.png'])

add_review('AIME-2016-I-Q15','pass',
 ['Expanded the synthetic proof with directed angles modulo180 degrees, a proof that the radical axes are not parallel, explicit tangent-chord parallels, and the ray ordering Z-M-X-Y.'],
 {'solution_en':[
 r'Let $M$ be the midpoint of the common tangent segment $AB$. Its powers to the two circles are $MA^2=MB^2$, so it lies on their radical axis $XY$. Both circles, and hence $X,Y$, lie in the same half-plane of $AB$. Their near/far order is therefore $M,X,Y$, with $MX\cdot MY=MA^2$.',
 r'All angles in the next two steps are directed modulo $180^\circ$, so replacing a ray by its opposite does not affect the statements. Cyclicity gives $\angle(DAX)=\angle(DYX)$ and $\angle(CBX)=\angle(CYX)$. Since $D,Y,C$ are collinear, these angles agree. If $AD\parallel BC$, this would force $AX\parallel BX$, contradicting $X\notin AB$. Thus $Z=AD\cap BC$ exists, and the radical-axis theorem places it on $XY$.',
 r'The same angle equality now reads $\angle ZAX=\angle ZBX$, proving $A,B,X,Z$ concyclic. From this circle and the tangent-chord theorem on the second original circle, $\angle AZX=\angle ABX=\angle BYX$. Since $ZX\parallel YX$, it follows that $ZA\parallel BY$. Interchanging the two original circles similarly gives $ZB\parallel AY$.',
 r'Thus $AYBZ$ is a parallelogram. Its diagonals $AB,YZ$ bisect each other at $M$, so $Z$ is the reflection of $Y$ through $M$. The full order on their common line is $Z,M,X,Y$. In particular $XZ=MX+MY$ and $XY=MY-MX$.',
 r'For the similarity, $Z,C,B$ are collinear and $Z,D,A$ are collinear. Cyclicity of $B,C,Y,X$ gives $\angle XCZ=\angle XYB=\angle XZD$, using $YB\parallel ZA$. Likewise $\angle XZC=\angle XYA=\angle XDZ$, using $ZC\parallel YA$ and cyclicity of $A,D,Y,X$. Therefore triangles $XZC$ and $XDZ$ are similar, and $XZ/XD=XC/XZ$, hence $XZ^2=XC\cdot XD$.',
 r'Finally $AB^2=4MX\cdot MY=(MX+MY)^2-(MY-MX)^2=XZ^2-XY^2=67\cdot37-47^2=270$.'
 ],
 'solution_zh':[
 r'令 $M$ 为公切线段 $AB$ 中点，其对两圆的幂为 $MA^2=MB^2$，所以在根轴 $XY$ 上。两相交圆位于公切线同侧，故 $X,Y$ 也同侧；结合远近条件，点序为 $M,X,Y$，且 $MX\cdot MY=MA^2$。',
 r'以下角均按模一百八十度的有向角理解，因此可替换反向射线。由共圆得 $\angle DAX=\angle DYX$、$\angle CBX=\angle CYX$。因 $D,Y,C$ 共线，两角相等。若 $AD\parallel BC$，便推出 $AX\parallel BX$，与 $X$ 不在切线 $AB$ 上矛盾。因此 $Z=AD\cap BC$ 存在，根轴定理使 $Z$ 位于 $XY$。',
 r'同一角等式给出 $\angle ZAX=\angle ZBX$，故 $A,B,X,Z$ 共圆。再用该圆及第二原圆切弦角，$\angle AZX=\angle ABX=\angle BYX$。因 $ZX\parallel YX$，得到 $ZA\parallel BY$；交换两原圆同理得 $ZB\parallel AY$。',
 r'所以 $AYBZ$ 为平行四边形，两对角线 $AB,YZ$ 在 $M$ 互相平分。$Z$ 是 $Y$ 关于 $M$ 的反射，完整点序为 $Z,M,X,Y$。故 $XZ=MX+MY$、$XY=MY-MX$。',
 r'由于 $Z,C,B$ 及 $Z,D,A$ 分别共线，利用 $B,C,Y,X$ 共圆和 $YB\parallel ZA$，得到 $\angle XCZ=\angle XYB=\angle XZD$。再用 $ZC\parallel YA$ 及 $A,D,Y,X$ 共圆，得 $\angle XZC=\angle XYA=\angle XDZ$。因此 $XZC\sim XDZ$，比例给出 $XZ^2=XC\cdot XD$。',
 r'最后 $AB^2=4MX\cdot MY=(MX+MY)^2-(MY-MX)^2=XC\cdot XD-XY^2=67\cdot37-47^2=270$。'
 ],
 'secondary':[{'category_id':'GE','subtype_id':'GE01','reason_en':'The parallelogram and two-angle similarity transfer circle incidences into the product XZ²=XC·XD.','reason_zh':'平行四边形与两角相似将圆上关联转化为乘积关系 XZ²=XC·XD。'}],
 'unresolved_issues':[]})

def save():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved',len(reviews),'independent reviews:',OUT)

if __name__=='__main__':save()

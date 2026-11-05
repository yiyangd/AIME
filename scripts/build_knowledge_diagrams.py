"""Original, mathematically constructed SVGs for canonical geometry microexamples.

The separate manifest leaves independently reviewed manuscripts unchanged.
"""
import hashlib,json,math
from pathlib import Path
from xml.sax.saxutils import escape
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/diagrams/knowledge'
DEST.mkdir(parents=True,exist_ok=True)
knowledge=json.loads((ROOT/'data/knowledge.json').read_text(encoding='utf8'))
methods={m['method_id']:m for s in knowledge for m in s['methods']}
BLUE='#163e65';ORANGE='#e77835';MUTED='#6f879b';PALE='#edf4f8';GREEN='#3a8b76'

def example_digest(m):
    return hashlib.sha256(json.dumps({k:m[k] for k in ['example_en','example_zh','solution_en','solution_zh']},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()

class Svg:
    def __init__(self,w=640,h=340):self.w=w;self.h=h;self.items=[]
    def line(self,a,b,color=BLUE,width=2.3,dash=False,arrows=False):
        extra=(' stroke-dasharray="6 5"' if dash else '')+(' marker-start="url(#dim)" marker-end="url(#dim)"' if arrows else '')
        self.items.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{color}" stroke-width="{width}"{extra}/>')
    def poly(self,points,fill='none',stroke=BLUE,width=2.3):
        ps=' '.join(f'{x:.3f},{y:.3f}' for x,y in points)
        self.items.append(f'<polygon points="{ps}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round"/>')
    def circle(self,c,r,color=BLUE,fill='none',width=2.3):
        self.items.append(f'<circle cx="{c[0]:.3f}" cy="{c[1]:.3f}" r="{r:.3f}" fill="{fill}" stroke="{color}" stroke-width="{width}"/>')
    def ellipse(self,c,rx,ry,color=BLUE):
        self.items.append(f'<ellipse cx="{c[0]:.3f}" cy="{c[1]:.3f}" rx="{rx:.3f}" ry="{ry:.3f}" fill="none" stroke="{color}" stroke-width="2.3"/>')
    def point(self,p,color=ORANGE):self.circle(p,3.5,color,color,1)
    def text(self,p,t,size=20,color=BLUE,anchor='middle'):
        self.items.append(f'<text x="{p[0]:.3f}" y="{p[1]:.3f}" fill="{color}" font-size="{size}" text-anchor="{anchor}">{escape(t)}</text>')
    def arc(self,c,r,a,b,color=ORANGE):
        start=(c[0]+r*math.cos(math.radians(a)),c[1]+r*math.sin(math.radians(a)))
        end=(c[0]+r*math.cos(math.radians(b)),c[1]+r*math.sin(math.radians(b)))
        self.items.append(f'<path d="M {start[0]:.3f},{start[1]:.3f} A {r},{r} 0 0 1 {end[0]:.3f},{end[1]:.3f}" fill="none" stroke="{color}" stroke-width="2"/>')
    def save(self,mid,alt_en,alt_zh,check):
        title=mid+' — '+alt_en
        svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="{mid}-title {mid}-desc">
<title id="{mid}-title">{escape(title)}</title><desc id="{mid}-desc">{escape(alt_zh)}</desc>
<defs><marker id="{mid}-dim" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{MUTED}"/></marker></defs>
<rect width="100%" height="100%" fill="white"/>
<g font-family="Arial,Microsoft YaHei,sans-serif">{''.join(self.items)}</g></svg>'''
        svg=svg.replace('url(#dim)',f'url(#{mid}-dim)')
        ET.fromstring(svg)
        path=DEST/f'{mid}.svg';path.write_text(svg,encoding='utf8')
        manifest[mid]=dict(diagram_path=path.relative_to(ROOT).as_posix(),alt_en=alt_en,alt_zh=alt_zh,example_sha256=example_digest(methods[mid]),svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),construction_check=check)

manifest={}

# GE01: the half-scale parallel section has one quarter of the full area.
s=Svg();A=(320,40);B=(120,280);C=(520,280);D=(220,160);E=(420,160)
s.poly([A,B,C]);s.poly([A,D,E],PALE);s.line(D,E,ORANGE,3)
for p,t,off in [(A,'A',(0,-12)),(B,'B',(-15,20)),(C,'C',(15,20)),(D,'D',(-17,0)),(E,'E',(17,0))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t)
s.text((320,125),'¼ area / 面积',18);s.text((320,151),'x',22,ORANGE);s.text((320,310),'BC = 10     DE ∥ BC',20)
assert (200/400)**2==.25
s.save('GE01-M01','A parallel chord cuts a triangle at half its linear scale.','平行截线位于三角形的一半线性比例处。','DE/BC=1/2; [ADE]/[ABC]=1/4.')

# GE02: exact affine one-third points, with no dependency on the triangle shape.
s=Svg();A=(130,270);B=(510,270);C=(270,40)
D=tuple(a+(b-a)/3 for a,b in zip(A,B));E=tuple(a+(b-a)/3 for a,b in zip(B,C));F=tuple(a+(b-a)/3 for a,b in zip(C,A))
s.poly([A,B,C]);s.poly([D,E,F],PALE,ORANGE,2.8)
for p,t,off in [(A,'A',(-15,15)),(B,'B',(15,15)),(C,'C',(0,-13)),(D,'D',(0,24)),(E,'E',(18,0)),(F,'F',(-18,0))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t)
s.text((320,325),'AD/AB = BE/BC = CF/CA = ⅓',21)
area=lambda P:abs(sum(P[i][0]*P[(i+1)%3][1]-P[(i+1)%3][0]*P[i][1] for i in range(3)))/2
assert abs(area([D,E,F])/area([A,B,C])-1/3)<1e-12
s.save('GE02-M01','The inner triangle joins successive one-third division points.','内三角形连接三条边上依次取的三等分点。','Affine coordinates verify the three edge ratios and inner area fraction 1/3.')

# GE03: an accurately scaled 5-12-13 half-triangle.
s=Svg(480,340);A=(240,40);B=(140,280);C=(340,280);D=(240,280)
s.poly([A,B,C]);s.line(A,D,MUTED,1.8,True);s.line((240,269),(251,269),MUTED,1.5);s.line((251,269),(251,280),MUTED,1.5)
s.text((240,26),'A');s.text((125,295),'B');s.text((355,295),'C');s.text((240,305),'D',18);s.text((173,164),'13');s.text((310,164),'13');s.text((258,170),'h',22,ORANGE);s.text((240,332),'BC = 10',21)
assert math.hypot(100,240)==260
s.save('GE03-M01','The apex altitude bisects the base of an isosceles 13-13-10 triangle.','两腰为十三、底边为十的等腰三角形，其顶点高平分底边。','Drawn half-legs are in ratio 5:12:13; the altitude meets the base at its midpoint.')

# GE04: a minor 120-degree arc viewed from the complementary arc.
s=Svg();O=(320,170);r=125;A=(320-r*math.sqrt(3)/2,107.5);B=(320+r*math.sqrt(3)/2,107.5);C=(320,295)
s.circle(O,r);s.poly([A,B,C]);s.line(O,A,MUTED,1.8);s.line(O,B,MUTED,1.8);s.line(A,B,ORANGE,3);s.arc(O,35,-150,-30);s.arc(C,32,-120,-60)
for p,t,off in [(A,'A',(-17,-5)),(B,'B',(17,-5)),(C,'C',(0,26)),(O,'O',(0,22))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t)
s.text((320,129),'120°',18,ORANGE);s.text((383,157),'5',19);s.text((320,251),'θ',21,ORANGE)
assert abs(math.dist(A,B)-5*math.sqrt(3)*25)<1e-10
s.save('GE04-M01','A 120-degree central angle and an inscribed vertex on the opposite arc.','一百二十度圆心角与位于另一段圆弧上的圆周角顶点。','Central angle 120 degrees; inscribed point C is on the major arc, so angle ACB is 60 degrees.')

# GE05: use actual lengths to locate the internal angle bisector.
s=Svg();scale=38;A=(130+2.75*scale,270-math.sqrt(36-2.75**2)*scale);B=(130,270);C=(510,270);D=(282,270)
s.poly([A,B,C]);s.line(A,D,ORANGE,2.8)
for p,t,off in [(A,'A',(0,-13)),(B,'B',(-17,15)),(C,'C',(17,15)),(D,'D',(0,23))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t)
s.text((161,175),'6');s.text((392,175),'9');s.text((320,320),'BC = 10     ∠BAD = ∠DAC',20);s.text((272,164),'ℓ',24,ORANGE)
assert abs(math.dist(A,B)/scale-6)<1e-12 and abs(math.dist(A,C)/scale-9)<1e-12
assert abs(math.dist(A,D)/scale-math.sqrt(30))<1e-12
s.save('GE05-M01','The internal bisector meets the length-ten base in ratio two to three.','内角平分线将长度十的底边按二比三分割。','Coordinates realize AB=6, AC=9, BC=10; BD/DC=2/3 and AD^2=30.')

# GE06: circles at (-1,0), (0,0), (4,0) drawn with one common scale.
s=Svg();O=(320,170);T=(295,170);U=(420,170)
s.circle(O,125);s.circle(T,100,ORANGE,PALE);s.circle(U,25,GREEN)
s.line((175,170),(485,170),MUTED,1.3,True);s.line(O,(320,45),BLUE,1.5);s.line(T,(195,170),ORANGE,1.6)
for p,t,off in [(O,'O',(12,25)),(T,'T',(-13,25)),(U,'U',(0,-12))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t,19)
s.text((338,100),'5',20);s.text((244,156),'r',23,ORANGE);s.text((449,197),'1',19,GREEN);s.text((495,177),'x',19);s.text((320,327),'O = (0,0)     U = (4,0)     T is on −x / T 在负半轴',18)
assert math.dist(O,T)+100==125 and math.dist(T,U)==100+25
s.save('GE06-M01','Two internal tangent circles and their external tangency, drawn to one scale.','两内切圆及其相互外切关系，使用统一比例绘制。','R=5, unit-circle center=(4,0), third center=(-1,0), radius=4; both tangency equalities hold.')

# GE07: the simultaneous midpoint equations produce a vertical segment.
s=Svg(560,340);origin=(250,190);sc=25
pt=lambda x,y:(origin[0]+sc*x,origin[1]-sc*y)
s.line((105,190),(445,190),MUTED,1.5);s.line((250,300),(250,25),MUTED,1.5);s.text((455,196),'x',18);s.text((259,23),'y',18);s.text((238,210),'O',18)
s.line(pt(-2,-4),pt(3,6));s.line(pt(-4,4),pt(4,-4));P=pt(2,4);Q=pt(2,-2);M=pt(2,1)
s.line(P,Q,ORANGE,3);s.line((250,165),M,MUTED,1.3,True)
for p,t,off in [(P,'P',(15,-6)),(Q,'Q',(20,0)),(M,'M = (2,1)',(78,5))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t,20)
s.text((357,55),'y = 2x',20);s.text((397,282),'y = −x',20)
assert (2+2)/2==2 and (4-2)/2==1
s.save('GE07-M01','The segment between two lines has the specified midpoint.','两直线上两点的连线具有给定中点。','P=(2,4), Q=(2,-2), M=(2,1), PQ=6; axes use equal scales.')

# GE08: solve the actual ellipse equation before constructing the drawing.
s=Svg();O=(320,175);sc=50;u=16*math.sqrt(3)/13;v=-22/13
A=(320,75);B=(320-u*sc,175-v*sc);C=(320+u*sc,175-v*sc)
s.line((85,175),(560,175),MUTED,1.3);s.line((320,305),(320,25),MUTED,1.3);s.ellipse(O,200,100);s.poly([A,B,C],PALE,ORANGE,2.6);s.line(A,(320,B[1]),MUTED,1.5,True)
for p,t,off in [(A,'A = (0,2)',(67,-9)),(B,'B',(-16,20)),(C,'C',(16,20))]:s.point(p);s.text((p[0]+off[0],p[1]+off[1]),t,19)
s.text((569,182),'x',18);s.text((329,24),'y',18);s.text((264,169),'s',23,ORANGE);s.text((320,331),'x² + 4y² = 16',22)
assert abs(u*u+4*v*v-16)<1e-12 and abs(math.dist(A,B)-math.dist(B,C))<1e-10
s.save('GE08-M01','An equilateral triangle inscribed in the ellipse with vertical altitude.','内接于椭圆且高位于纵轴上的等边三角形。','Base vertices=(±16sqrt(3)/13,-22/13); both satisfy the ellipse, and all three Euclidean sides agree.')

# GE09: the plane and the two centers lie in this axial cross section.
s=Svg();sc=17;O1=(150,205);O2=(150+8*math.sqrt(2)*sc,205-4*sc);plane=222
s.circle(O1,5*sc);s.circle(O2,7*sc);s.line((35,plane),(560,plane),MUTED,1.5)
rho=math.sqrt(24)*sc
for c,t in [(O1,'O₁'),(O2,'O₂')]:
 p=(c[0],plane);s.line(c,p,MUTED,1.5,True);s.line((c[0]-rho,plane),(c[0]+rho,plane),ORANGE,3);s.point(c);s.point(p);s.text((c[0]+15,c[1]-8),t,20);s.text((c[0],plane+24),'P₁' if t=='O₁' else 'P₂',18);s.line(p,(c[0],309),MUTED,1,True)
T=tuple(a+5*(b-a)/12 for a,b in zip(O1,O2));s.line(O1,T,BLUE,1.5);s.line(T,O2,BLUE,1.5);s.point(T)
s.text((178,174),'5',20);s.text((283,144),'7',20);s.text((101,212),'r',22,ORANGE);s.text((392,211),'r',22,ORANGE);s.text((574,228),'Π',22)
s.line((O1[0],310),(O2[0],310),MUTED,1.4,arrows=True);s.text(((O1[0]+O2[0])/2,334),'8√2',22);s.text((535,50),'Axial section',17);s.text((535,74),'轴截面',17)
assert abs(math.dist(O1,O2)/sc-12)<1e-12 and abs((plane-O1[1])/sc-1)<1e-12 and abs((plane-O2[1])/sc-5)<1e-12
s.save('GE09-M01','An axial cross section of tangent spheres cut by a plane, with equal section radii.','相切球被平面截得等半径截圆时的轴截面。','Sphere radii 5,7; heights 1,5; projected separation 8sqrt(2); common section radius sqrt(24).')

# GE10: canonical reviewed example uses similar closed boxes, not cone reversal.
s=Svg()
def box(x,y,w,h,dx,dy):
 A=(x,y);B=(x+w,y);C=(x+w,y-h);D=(x,y-h);Ap=(x+dx,y+dy);Bp=(x+w+dx,y+dy);Cp=(x+w+dx,y-h+dy);Dp=(x+dx,y-h+dy)
 s.poly([D,C,Cp,Dp],PALE);s.poly([B,C,Cp,Bp],'#fff1e6');s.poly([A,B,C,D],'white')
 for a,b in [(Ap,Bp),(Ap,Dp),(A,Ap)]:s.line(a,b,MUTED,1.5,True)
 for a,b in [(B,Bp),(Bp,Cp),(Cp,Dp),(D,Dp),(C,Cp)]:s.line(a,b)
 return A,B
a,b=box(70,235,120,80,40,-30);c,d=box(340,255,180,120,60,-45)
s.text((130,263),'2k',22,ORANGE);s.text((430,283),'3k',22,ORANGE);s.text((150,105),'S₁',23);s.text((453,70),'S₂',23);s.text((320,332),'S₁ + S₂ = 130     edge ratio / 棱长比 = 2 : 3',20)
assert 180/120==120/80==60/40==(-45)/(-30)==1.5
assert 40+90==130 and 90/40==1.5**2 and 27/8==1.5**3
s.save('GE10-M01','Two similar closed boxes with edge ratio two to three and total surface area 130.','两个相似闭长方体棱长比为二比三，总表面积为一百三十。','All depicted edge vectors have scale 3/2; area ratio=4:9, volume ratio=8:27, total areas 40+90=130.')

(ROOT/'data/knowledge_diagrams.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Saved',len(manifest),'original checked SVG diagrams and separate manifest.')

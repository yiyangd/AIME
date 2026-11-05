"""Exact rational tetrahedral attachment and separating-axis certificate."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def orient(face,opposite):return face if dot(cross(sub(face[1],face[0]),sub(face[2],face[0])),sub(opposite,face[0]))<0 else(face[0],face[2],face[1])
initial=[tuple(map(F,p)) for p in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
faces=[orient(tuple(initial[j] for j in range(4) if j!=i),initial[i]) for i in range(4)];tets=[tuple(initial)];stages=[]
def axisnorm(v):
 if not any(v):return None
 g=reduce(gcd,(abs(int(x)) for x in v));v=tuple(int(x)//g for x in v)
 return tuple(-x for x in v) if next(x for x in v if x)<0 else v
def axes(t):
 out=set()
 for face in combinations(t,3):out.add(axisnorm(cross(sub(face[1],face[0]),sub(face[2],face[0]))))
 return out
def positive_overlap(a,b):
 aa=axes(a);aa.update(axes(b));ea=[sub(a[i],a[j]) for i,j in combinations(range(4),2)];eb=[sub(b[i],b[j]) for i,j in combinations(range(4),2)]
 aa.update(axisnorm(cross(u,v)) for u in ea for v in eb);aa.discard(None)
 for n in aa:
  pa=[dot(n,v) for v in a];pb=[dot(n,v) for v in b]
  if max(pa)<=min(pb) or max(pb)<=min(pa):return False
 return True
def intpoints(points):
 out=[]
 for p in points:
  scaled=[x*8 for x in p];assert all(x.denominator==1 for x in scaled);out.append(tuple(map(int,scaled)))
 return tuple(out)
def tri_positive_overlap(a,b):
 n=cross(sub(a[1],a[0]),sub(a[2],a[0]));nb=cross(sub(b[1],b[0]),sub(b[2],b[0]))
 if any(cross(n,nb)) or dot(n,sub(a[0],b[0])):return False
 drop=next(i for i,x in enumerate(n) if x);a=[tuple(x for i,x in enumerate(p) if i!=drop) for p in a];b=[tuple(x for i,x in enumerate(p) if i!=drop) for p in b]
 for tri in [a,b]:
  for i in range(3):
   e=sub(tri[(i+1)%3],tri[i]);axis=(-e[1],e[0]);pa=[dot(axis,p) for p in a];pb=[dot(axis,p) for p in b]
   if max(pa)<=min(pb) or max(pb)<=min(pa):return False
 return True
for stage in range(3):
 newfaces=[];newtets=[]
 for a,b,c in faces:
  ab=tuple((x+y)/2 for x,y in zip(a,b));bc=tuple((x+y)/2 for x,y in zip(b,c));ca=tuple((x+y)/2 for x,y in zip(c,a))
  n=cross(sub(b,a),sub(c,a));sgn=tuple(1 if x>0 else -1 for x in n);assert all(x for x in n)
  apex=tuple((a[i]+b[i]+c[i])/3+F(2,3*2**stage)*sgn[i] for i in range(3))
  tet=(ab,bc,ca,apex);newtets.append(tet)
  newfaces.extend([(a,ab,ca),(b,bc,ab),(c,ca,bc)])
  for i in range(3):
   base=(ab,bc,ca);face=(base[i],base[(i+1)%3],apex);newfaces.append(orient(face,base[(i+2)%3]))
 oldints=[intpoints(t) for t in tets];newints=[intpoints(t) for t in newtets]
 checked=0
 for a in newints:
  for b in oldints:
   assert not positive_overlap(a,b),(stage,a,b);checked+=1
 for a,b in combinations(newints,2):assert not positive_overlap(a,b),(stage,a,b);checked+=1
 newfaceints=[intpoints(t) for t in newfaces];surfacechecked=0
 for a,b in combinations(newfaceints,2):
  assert not tri_positive_overlap(a,b),(stage,a,b);surfacechecked+=1
 stages.append(dict(stage=stage+1,attached_tetrahedra=len(newtets),total_tetrahedra=len(tets)+len(newtets),boundary_faces=len(newfaces),exact_tetrahedron_pair_checks=checked,exact_surface_triangle_pair_checks=surfacechecked,positive_volume_overlaps=0,positive_area_boundary_overlaps=0))
 tets+=newtets;faces=newfaces
out=dict(method='Exact rational vertex generation; SAT face normals plus all edge cross products for tetrahedra; coplanar2D SAT for exposed triangles. Zero-width projection overlap is boundary contact, not positive volume/area.',stages=stages,relative_volume='69/32',answer=101,passed=True)
p=ROOT/'audit/certificates/2001II-Q12-spatial-certificate.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))

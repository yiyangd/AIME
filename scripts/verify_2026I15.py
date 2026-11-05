"""Exhaustive exact-cover certificate, independent of the source slab lemma."""
from pathlib import Path
import json,time
SIZE=10;FULL=(1<<(SIZE*SIZE))-1
loops=[];bycell=[[] for _ in range(SIZE*SIZE)]
for a in range(2,SIZE+1):
 for b in range(2,SIZE+1):
  for r in range(SIZE-a+1):
   for c in range(SIZE-b+1):
    cells=[i*SIZE+j for i in range(r,r+a) for j in range(c,c+b) if i in (r,r+a-1) or j in (c,c+b-1)]
    mask=sum(1<<v for v in cells);idx=len(loops);loops.append((mask,dict(row=r,column=c,height=a,width=b)))
    for v in cells:bycell[v].append(idx)
solutions=[];visited=0;start=time.time()
def search(used,left,chosen):
 global visited
 visited+=1
 if left==0:
  if used==FULL:solutions.append(chosen)
  return
 missing=FULL^used;n=missing.bit_count()
 if n<4*left or n>36*left:return
 if not missing:return
 # The first uncovered cell gives every unordered cover exactly once.
 v=(missing&-missing).bit_length()-1
 for idx in bycell[v]:
  mask,_=loops[idx]
  if not mask&used:
   count=mask.bit_count()
   if n-count<4*(left-1) or n-count>36*(left-1):continue
   search(used|mask,left-1,chosen+[idx])
search(0,5,[])
result=dict(candidate_loops=len(loops),count=len(solutions),visited_nodes=visited,elapsed_seconds=time.time()-start,partitions=[[loops[i][1] for i in s] for s in solutions])
out=Path(__file__).resolve().parents[1]/'audit/2026I15-exact-cover.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(result,indent=2),encoding='utf8');print({k:v for k,v in result.items() if k!='partitions'})
assert len(solutions)==83

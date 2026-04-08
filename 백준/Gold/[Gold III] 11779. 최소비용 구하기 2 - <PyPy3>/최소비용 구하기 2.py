import sys
from heapq import heappush,heappop
input=sys.stdin.readline


t=int(input())
l=int(input())
mapli=[[] for _ in range(t+1)]
for i in range(l):
  a,b,w=map(int,input().split())
  mapli[a].append((w,b))

s,f=map(int,input().split())


d=[float('INF') for _ in range(t+1)]
d2=[i for i in range(t+1)]

def dijk(s):
  heap=[]
  heappush(heap,(0,s))
  d[s]=0
  while heap:
    w,v=heappop(heap)
    if d[v] < w:
      continue
    for nw,nv in mapli[v]:
      if d[nv] > d[v] + nw:     
        d[nv] = d[v] + nw
        d2[nv]=v
        heappush(heap,(d[nv],nv))
        
        
dijk(s)

print(d[f])

path=[f]
v=f

while v != s:
  v=d2[v]
  path.append(v)
print(len(path))
path.reverse()
for i in path:
  print(i,end=' ')


      



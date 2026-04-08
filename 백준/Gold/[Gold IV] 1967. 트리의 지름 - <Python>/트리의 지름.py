import sys
from heapq import heappush,heappop
input=sys.stdin.readline


t=int(input())
l=t-1
mapli=[[] for _ in range(t+1)]
for i in range(l):
  a,b,w=map(int,input().split())
  mapli[a].append((w,b))
  mapli[b].append((w,a))



def dijk(s):
  d=[float('INF') for _ in range(t+1)]
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
        heappush(heap,(d[nv],nv))
  return d.index(max(d[1:]))

def dijk2(s):
  d=[float('INF') for _ in range(t+1)]
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
        heappush(heap,(d[nv],nv))
  return max(d[1:])
        


deep=dijk(1)
print(dijk2(deep))







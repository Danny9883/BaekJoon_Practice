import sys
from heapq import heappush,heappop
input=sys.stdin.readline

t=10000
l,f=map(int,input().split())

mapli=[[] for _ in range(t+1)]
for i in range(1,t):
  mapli[i-1].append((1,i))
for i in range(l):
  a,b,w=map(int,input().split())
  mapli[a].append((w,b))




d=[float('INF') for _ in range(t+1)]

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
        heappush(heap,(d[nv],nv))
        


dijk(0)
print(d[f])
import sys
input=sys.stdin.readline
from heapq import heappush,heappop



n,t=map(int,input().split())

mapli=[[]for _ in range(n+1)]

for _ in range(n-1):
  a,b,w=map(int,input().split())
  mapli[a].append((w,b))
  mapli[b].append((w,a))

def dijk(s,f):
  heap=[]
  d=[1000000000 for _ in range(n+1)]
  heappush(heap,(0,s))
  d[s]=0
  while heap:
    w,v=heappop(heap)
    if v==f:
      return d[v]
    if d[v] < w:
      continue
    for nw,nv in mapli[v]:
      if d[nv] > d[v] + nw:
        d[nv] = d[v] + nw
        heappush(heap,(d[nv],nv))

for _ in range(t):
  a,b=map(int,input().split())
  print(dijk(a,b))
      
    
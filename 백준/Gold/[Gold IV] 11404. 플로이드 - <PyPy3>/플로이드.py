import sys
from heapq import heappush,heappop
input=sys.stdin.readline

t=int(input())
l=int(input())
mapli=[[] for _ in range(t+1)]
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
        


for i in range(1,t+1):
  dijk(i)
  for j in range(1,t+1):
    if d[j]==float('INF'):
      print(0,end=' ')
    else:
      print(d[j],end=' ')
  print()
  d=[float('INF') for _ in range(t+1)]

      



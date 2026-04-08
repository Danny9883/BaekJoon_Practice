import sys
from heapq import heappush,heappop
input=sys.stdin.readline


t,e=map(int,input().split())

graph=list([] for _ in range(t+1))

for i in range(e):
  a,b,w=map(int,input().split())
  graph[a].append((w,b))
  graph[b].append((w,a))

v1,v2=map(int,input().split())

def dijk(s,e):
  d=[float('INF')]*(t+1)
  heap = []
  heappush(heap,(0,s))
  d[s] = 0
  
  while heap:
    w,v=heappop(heap)
    if d[v] < w:
      continue
    for nw,nv in graph[v]:
      if d[nv] > d[v] + nw:
        d[nv] = d[v] + nw
        heappush(heap,(d[nv],nv))
  
  return d[e]
    

    
ans1=0
ans2=0

ans1+= dijk(1,v1)
ans1+= dijk(v1,v2)
ans1+= dijk(v2,t)

ans2+= dijk(1,v2)
ans2+= dijk(v2,v1)
ans2+= dijk(v1,t)

if ans1 == float('INF') and ans2 == float('INF'):
  print(-1)
else:
  print(min(ans1,ans2))

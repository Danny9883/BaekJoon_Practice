import sys
from heapq import heappush,heappop
input=sys.stdin.readline


t,e=map(int,input().split())
s=int(input())


graph=list([] for _ in range(t+1))

for i in range(e):
  a,b,w=map(int,input().split())
  graph[a].append((w,b))



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


for i in range(1,t+1):
  if d[i] == float('inf'):
    print("INF")
    continue
  print(d[i])
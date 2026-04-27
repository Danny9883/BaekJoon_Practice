import sys
input=sys.stdin.readline
from heapq import heappush,heappop



t, e, k=map(int,input().split())
s, f=map(int,input().split())

graph=list([] for _ in range(t+1))


for i in range(e):
  a,b,w=map(int,input().split())
  graph[a].append((w,b))
  graph[b].append((w,a))

tax = [0]
for _ in range(k):
  tax.append(int(input())+tax[-1])


inf = float('INF')


def dijk(s):
  d=[[inf] * t for _ in range(t+1)]
  heap=[]
  heappush(heap,(0,0,s))
  d[s][0]=0
  while heap:
    w,c,v=heappop(heap)
    flag = False
    for i in range(c):
      if d[v][i] < w:
        flag = True
        break
    if c== t-1 or flag:
      continue
    for nw,nv in graph[v]:
      cost = w + nw
      if d[nv][c+1] > cost:
        d[nv][c+1] = cost
        heappush(heap,(cost,c+1,nv))
  return d

dist = dijk(s)[f]
ans = []
for k in tax:
  min_cost = inf
  for i in range(len(dist)):
    if dist[i]<inf:
      min_cost = min(min_cost, dist[i]+i*k)
  ans.append(min_cost)

for i in ans:
  print(i)





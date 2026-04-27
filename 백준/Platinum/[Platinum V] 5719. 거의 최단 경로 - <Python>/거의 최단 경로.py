import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop


while 1:

  t, e=map(int,input().split())
  if t==0 and e==0:
    break
  s, f=map(int,input().split())

  graph=list([] for _ in range(t+1))
  graph_r=list([] for _ in range(t+1))
  visited = [[False for _ in range(t+1)] for _ in range(t+1)] 

  for i in range(e):
    a,b,w=map(int,input().split())
    graph[a].append((w,b))
    graph_r[b].append((w,a))




  def dijk():
    d=[float('INF') for _ in range(t+1)]
    heap=[]
    heappush(heap,(0,s))
    d[s]=0
    while heap:
      w,v=heappop(heap)
      if d[v] < w:
        continue
      for nw,nv in graph[v]:
        if visited[v][nv]:
          continue
        if d[nv] > d[v] + nw:
          d[nv] = d[v] + nw
          heappush(heap,(d[nv],nv))
    return d

  def bfs(d):
    que = deque()
    que.append(f)
    while que:
      v = que.popleft()
      if v == s:
        continue
      for nw, nv in graph_r[v]:
        if d[nv] + nw == d[v]:
          if not visited[nv][v]:
            visited[nv][v] = True
            que.append(nv)

  min_d = dijk()
  bfs(min_d)
  min_d = dijk()

  if min_d[f] == float('INF'):
    print(-1)
  else:
    print(min_d[f])



import sys
input=sys.stdin.readline
from collections import deque


s,f=map(int,input().split())

t,l=map(int,input().split())

graph=[[]for _ in range(t+1)]

for i in range(l):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


def bfs(s,f):
  que = deque()
  que.append(s)
  d=[-1 for _ in range(t+1)]
  visited = [False for _ in range(t+1)]
  visited[s]=True
  d[s]=0
  while que:
    v = que.popleft()
    if v==f:
      return d[f]
    for i in graph[v]:
      if visited[i]:
        continue
      else:
        que.append(i)
        visited[i]=True
        d[i]=d[v]+1
  return d[f]


print(bfs(s,f))



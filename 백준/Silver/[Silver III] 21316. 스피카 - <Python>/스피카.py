import sys
input=sys.stdin.readline
from collections import deque





t,l=12,12


graph = [[]for _ in range(t+1)]

for _ in range(l):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def find(s):
  visited = [False for _ in range(t+1)]
  d = [0 for _ in range(t+1)]
  que=deque()
  que.append(s)
  visited[s] = True
  d[s]=0
  while que:
    v = que.popleft()
    for i in graph[v]:
      if visited[i]:
        continue
      que.append(i)
      visited[i]=True
      d[i] = d[v]+1
  return d


for i in range(1,t+1):
  if sum(find(i)) == 37:
    print(find(i).index(1))






import sys
input=sys.stdin.readline
from collections import deque



t=int(input())
l=int(input())

graph = [[]for _ in range(t+1)]

for _ in range(l):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def find(s):
  visited = [False for _ in range(t+1)]
  que=deque()
  que.append(s)
  visited[s] = True
  d = [-1 for _ in range(t+1)]
  d[s] = 0
  count = 0
  while que:
    v = que.popleft()
    for i in graph[v]:
      if visited[i]:
        continue
      que.append(i)
      visited[i]=True
      d[i]=d[v]+1
      if 1 <= d[i] <= 2:
        count+=1
  return count

print(find(1))




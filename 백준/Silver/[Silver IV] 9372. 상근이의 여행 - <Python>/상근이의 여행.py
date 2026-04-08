import sys
input=sys.stdin.readline
from collections import deque



for _ in range(int(input())):

  t,l=map(int,input().split())


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
    count = 0
    while que:
      v = que.popleft()
      for i in graph[v]:
        if visited[i]:
          continue
        que.append(i)
        visited[i]=True
        count+=1
    return count

  print(find(1))




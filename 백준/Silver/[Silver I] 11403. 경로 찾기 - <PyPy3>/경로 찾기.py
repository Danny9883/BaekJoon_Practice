import sys
from collections import deque
input=sys.stdin.readline



t=int(input())

graph=[[] for _ in range(t)]

mapli=[]
for i in range(t):
  li=list(map(int,input().split()))
  mapli.append(li)


stack=[]
que=deque()
for i in range(t):
  for j in range(t):
    if mapli[i][j] == 1:
      graph[i].append(j)
      que.append(i)


while que:
  visited=[]
  for i in range(t):
    visit=[False]*t
    visited.append(visit)
  v=que.popleft()
  stack.extend(reversed(graph[v]))
  while stack:
    n=stack.pop()
    mapli[v][n]=1
    for i in graph[n]:
      if visited[n][i]==False:
        stack.append(i)
        visited[n][i]=True




for i in range(t):
  for j in range(t):
    print(mapli[i][j],end=' ')
  print()

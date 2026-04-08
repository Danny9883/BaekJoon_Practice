import sys
from collections import deque
input=sys.stdin.readline

t,l,s=map(int,input().split())

mapli=[[]for _ in range(t+1)]
for i in range(l):
  a,b=map(int,input().split())
  mapli[a].append(b)
  mapli[b].append(a)

for i in range(t+1):
  mapli[i].sort()

visitnum=[0 for _ in range(t+1)]
visited=[False for _ in range(t+1)]

def bfs(s):
  que=deque()
  que.append(s)
  count=1
  visited[s]=True
  while que:
    v = que.popleft()
    if visitnum[v]==0:
      visitnum[v] = count
      count+=1
    for i in mapli[v]:
      if visited[i]==False:
        que.append(i)
        visited[i]=True

bfs(s)
for i in range(1,t+1):
  print(visitnum[i])

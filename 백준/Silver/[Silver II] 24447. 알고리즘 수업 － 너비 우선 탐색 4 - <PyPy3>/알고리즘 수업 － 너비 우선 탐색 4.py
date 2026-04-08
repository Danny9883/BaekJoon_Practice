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

visitnum=[-1 for _ in range(t+1)]
visited=[False for _ in range(t+1)]
visitcount=[0 for _ in range(t+1)]

def bfs(s):
  que=deque()
  que.append(s)
  visitnum[s]=0
  visited[s]=True
  count=1
  while que:
    v = que.popleft()
    if visitcount[v]==0:
      visitcount[v]=count
      count+=1
    for i in mapli[v]:
      if visited[i]==False:
        que.append(i)
        visitnum[i]=visitnum[v]+1
        visited[i]=True

bfs(s)
ans=0
for i in range(1,t+1):
  ans+=(visitnum[i]*visitcount[i])
print(ans)

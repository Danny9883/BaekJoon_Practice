import sys
input=sys.stdin.readline

t,l,s=map(int,input().split())

mapli=[[] for _ in range(t+1)]
for _ in range(l):
  a,b=map(int,input().split())
  mapli[a].append(b)
  mapli[b].append(a)

for i in range(t+1):
  mapli[i].sort()


visited=[-1 for _ in range(t+1)]
visitednum=[0 for _ in range(t+1)]
visited2=[False for _ in range(t+1)]

def dfs(s):
  stack=[]
  stack.append(s)
  visited[s]=0
  num=1
  while stack:
    v=stack.pop()
    visited2[v]=True
    if visitednum[v]==0:
      visitednum[v]=num
      num+=1
    for i in mapli[v]:
      if visited2[i]==False:
        visited[i]=max(visited[v]+1,visited[i])
        stack.append(i)



dfs(s)
ans=0
for i in range(1,t+1):
  ans+=(visited[i]*visitednum[i])
print(ans)





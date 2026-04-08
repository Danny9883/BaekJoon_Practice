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


visited=[0 for _ in range(t+1)]

def dfs(s):
  stack=[]
  stack.append(s)
  visitcount=1
  while stack:
    v=stack.pop()
    if visited[v]==0:
      visited[v]=visitcount
      visitcount+=1
      for i in mapli[v]:
        if visited[i]==0:
          stack.append(i)



dfs(s)
for i in range(1,t+1):
  print(visited[i])





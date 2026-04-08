from collections import deque

a,b,c=map(int,input().split())
li=[]
for i in range(a+1):
  li.append([])
for i in range(b):
  x,y=map(int,input().split())
  li[x].append(y)
  li[y].append(x)
  li[x].sort()
  li[y].sort()



visited = []
def dfs(list,start,visited):
  visited.append(start)
  print(start,end=' ')
  for i in list[start]:
    if i not in visited:
      dfs(list,i,visited)

visited2 = []
def bfs(list,start,visited):
  que = deque()
  que.append(start)
  while que:
    v = que.popleft()
    if v not in visited:
      print(v,end=' ')
      visited.append(v)
      for k in list[v]:
        que.append(k)


dfs(li,c,visited)
print()
bfs(li,c,visited2)
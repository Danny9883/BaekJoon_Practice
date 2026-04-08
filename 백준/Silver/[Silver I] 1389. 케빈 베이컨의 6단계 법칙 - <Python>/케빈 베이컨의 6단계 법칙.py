from collections import deque



a,b=map(int,input().split())

li=[]
for i in range(a+1):
  li.append([])
for i in range(b):
  x,y=map(int,input().split())
  li[x].append(y)
  li[y].append(x)
  li[x].sort()
  li[y].sort()


distance = [0]*(a+1)
def bfs(list,start):
  visited = []
  que = deque()
  que.append(start)
  while que:
    v = que.popleft()
    if v not in visited:
      visited.append(v)
      for k in list[v]:
        que.append(k)
        if k not in visited and distance[k] ==0 :
          distance[k] = distance[v] + 1

ans=[]
for kk in range(1,a+1):
  bfs(li,kk)
  ans.append(sum(distance))
  distance = [0]*(a+1)
print(ans.index(min(ans))+1)

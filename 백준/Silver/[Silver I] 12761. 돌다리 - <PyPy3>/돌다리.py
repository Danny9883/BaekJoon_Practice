import sys
input=sys.stdin.readline
from collections import deque




a,b,n,m=map(int,input().split())

def bfs(s,f,count):
  global a,b
  visited=set()
  que=deque()
  que.append((s,count))
  visited.add(s)
  dx = [1,-1,-a,a,-b,b]
  dx2 = [a,b]
  while que:
    v,count=que.popleft()
    if v==f:
      return count
    for i in range(6):
      nx = dx[i] + v
      if nx<0 or nx>100000 or nx in visited:
        continue
      else:
        que.append((nx,count+1))
        visited.add(nx)
    for i in range(2):
      nx = dx2[i] * v
      if nx<0 or nx>100000 or nx in visited:
        continue
      else:
        que.append((nx,count+1))
        visited.add(nx)

print(bfs(n,m,0))
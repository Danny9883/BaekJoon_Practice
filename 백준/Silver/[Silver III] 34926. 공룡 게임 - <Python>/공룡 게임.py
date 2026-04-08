import sys
input=sys.stdin.readline
from collections import deque





n,k=map(int,input().split())

mapli=list(input().rstrip('\n'))

def jump(s):
  que = deque()
  que.append(s)
  visited = [False for _ in range(n)]
  visited[s]=True
  dx = [1,k]
  while que:
    x = que.popleft()
    if x == n-1:
      print("YES")
      return
    for i in range(2):
      nx = dx[i] + x
      if  nx>=n or visited[nx] or mapli[nx]=="#" :
        continue
      else:
        que.append(nx)
        visited[nx]=True
  print("NO")

jump(0)



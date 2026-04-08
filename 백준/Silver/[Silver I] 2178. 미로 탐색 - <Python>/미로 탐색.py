from collections import deque
import sys

input=sys.stdin.readline


row,col=map(int,input().split())
mapli=[(list(map(int,input().rstrip()))) for _ in range(row) ]

def maze(y,x,c):
  visited = [[False]*col for _ in range(row)]
  que=deque()
  dx = [1,0,-1,0]
  dy = [0,-1,0,1]
  que.append((y,x,c))
  while que:
    y,x,c=que.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny<0 or ny>=row or nx<0 or nx>=col or mapli[ny][nx]==0 or visited[ny][nx] == True:
        continue
      else:
        if ny == row-1 and nx == col-1:
          print(c+1)
          return
        else:
          que.append((ny,nx,c+1))
          visited[ny][nx]=True
  print(-1)

maze(0,0,1)
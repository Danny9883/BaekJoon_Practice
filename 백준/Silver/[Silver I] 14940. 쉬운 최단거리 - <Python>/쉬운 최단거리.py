from collections import deque
import sys
input=sys.stdin.readline

row,col=map(int,input().split())
mapli=[(list(map(int,input().split()))) for _ in range(row) ]

startrow=0
startcol=0
for i in range(row):
  if 2 in mapli[i]:
    startrow=i
    startcol=mapli[i].index(2)

def maze(y,x):
  visited = [[False]*col for _ in range(row)]
  que=deque()
  dx = [1,0,-1,0]
  dy = [0,-1,0,1]
  que.append((y,x))
  visited[y][x]=True
  mapli[y][x] = 0
  while que:
    y,x=que.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny<0 or ny>=row or nx<0 or nx>=col or mapli[ny][nx]==0 or visited[ny][nx] == True:
        continue
      else:
        que.append((ny,nx))
        mapli[ny][nx] = mapli[y][x] + 1
        visited[ny][nx]=True
  for i in range(row):
    for j in range(col):
      if visited[i][j]==False and mapli[i][j]==1:
        mapli[i][j]=-1
      print(mapli[i][j],end=' ')
    print()

maze(startrow,startcol)
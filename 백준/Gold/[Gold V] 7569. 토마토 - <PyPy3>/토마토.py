from collections import deque
import sys
input=sys.stdin.readline

col,row,floor=map(int,input().split())
mapli=[]
for i in range(floor):
  rowm=[(list(map(int,input().split()))) for _ in range(row) ]
  mapli.append(rowm)


tomatovisited=[]
for i in range(floor):
  tomavisitedrow = [[False]*col for _ in range(row)]
  tomatovisited.append(tomavisitedrow)

def tomato(z,y,x):
  visited=[]
  for i in range(floor):
    visitedrow = [[False]*col for _ in range(row)]
    visited.append(visitedrow)

  que=deque()
  dx = [1,0,-1,0,0,0]
  dy = [0,-1,0,1,0,0]
  dz = [0,0,0,0,1,-1]
  que.append((z,y,x))
  visited[z][y][x]=True
  while que:
    z,y,x=que.popleft()
    for i in range(6):
      ny = y + dy[i]
      nx = x + dx[i]
      nz = z + dz[i]
      if ny<0 or ny>=row or nx<0 or nx>=col or nz<0 or nz>=floor or mapli[nz][ny][nx]==-1 :
        continue
      else:
        if mapli[nz][ny][nx] == 1 and visited[nz][ny][nx] ==False:
          que.append((nz,ny,nx))
          visited[nz][ny][nx]=True
          tomatovisited[nz][ny][nx]=True
        elif mapli[nz][ny][nx] <= mapli[z][y][x] + 1 and mapli[nz][ny][nx]!=0:
          continue
        else:
          que.append((nz,ny,nx))
          mapli[nz][ny][nx] = mapli[z][y][x] + 1
          visited[nz][ny][nx]=True
        

for i in range(floor):
  for j in range(row):
    for k in range(col):
      if mapli[i][j][k] == 1 and tomatovisited[i][j][k] ==False:
        tomato(i,j,k)



a=0
day=0
for i in range(floor):
  for j in range(row):
    for k in range(col):
      if mapli[i][j][k] == 0:
        a=1
        break
      day=max(day,mapli[i][j][k])
    
      

if a==1:
  print(-1)
else:
  print(day-1)

from collections import deque
import sys
input=sys.stdin.readline

row,col=map(int,input().split())
mapli=[(list(input())) for _ in range(row) ]

startrow=0
startcol=0
for i in range(row):
  if 'I' in mapli[i]:
    startrow=i
    startcol=mapli[i].index("I")

count=0
def cam(y,x):
  global count
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
      if ny<0 or ny>=row or nx<0 or nx>=col or mapli[ny][nx]=="X" or visited[ny][nx] == True:
        continue
      else:
        que.append((ny,nx))
        visited[ny][nx]=True
        if mapli[ny][nx] == "P":
          count+=1

        

cam(startrow,startcol)
if count==0:
  print("TT")
else:
  print(count)

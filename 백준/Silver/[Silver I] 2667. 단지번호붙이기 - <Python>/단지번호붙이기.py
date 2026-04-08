from collections import deque
import sys
input=sys.stdin.readline

row=int(input())
col=row
mapli=[(list(map(int,input().rstrip()))) for _ in range(row) ]

countli=[]
def dfs(y,x):
  count=0
  stack=[]
  dx = [1,0,-1,0]
  dy = [0,-1,0,1]
  stack.append((y,x))
  mapli[y][x] = 0
  while stack:
    y,x=stack.pop()
    count+=1
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny<0 or ny>=row or nx<0 or nx>=col or mapli[ny][nx]==0 :
        continue
      else:
        stack.append((ny,nx))
        mapli[ny][nx] = 0
  countli.append(count)


for i in range(row):
  for j in range(col):
    if mapli[i][j] == 1:
      dfs(i,j)

countli.sort()
print(len(countli))
for i in countli:
  print(i)


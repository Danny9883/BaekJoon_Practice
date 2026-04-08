import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

while 1:
  col,row=map(int,input().split())
  if col==0 and row==0:
    break

  mapli=[]
  for i in range(row):
    a=list(map(int,input().split()))
    mapli.append(a)
    

  def dfs(x,y):
    dx = [1,0,-1,0,1,1,-1,-1]
    dy = [0,-1,0,1,-1,1,1,-1]
    mapli[y][x] = 0
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<col and 0<=ny<row and mapli[ny][nx]==1:
        dfs(nx,ny)

  count=0
  for r in range(row):
    for c in range(col):
      if mapli[r][c] == 1:
        dfs(c,r)
        count+=1
  print(count)

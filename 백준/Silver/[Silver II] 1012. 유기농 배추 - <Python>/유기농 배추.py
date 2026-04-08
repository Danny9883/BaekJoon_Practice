from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline


ttt=int(input())

for tt in range(ttt):
  col,row,bae=map(int,input().split())

  mapli=[]
  for i in range(row):
    colli=[]
    for j in range(col):
      colli.append(0)
    mapli.append(colli)

  for i in range(bae):
    x,y=map(int,input().split())
    mapli[y][x]=1



  def dfs(x,y):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    mapli[y][x] = 0
    
    for i in range(4):
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
      


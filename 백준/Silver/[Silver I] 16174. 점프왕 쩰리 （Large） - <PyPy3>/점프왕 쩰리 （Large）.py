import sys
input=sys.stdin.readline
from collections import deque



row=int(input())
col=row
mapli=[]
for i in range(row):
  a=list(map(int,input().split()))
  mapli.append(a)

visited=[[False for _ in range(row)] for _ in range(row)]

def game(row,col,map):
  stack=[]
  dx=[0,1]
  dy=[1,0]
  stack.append((row,col))
  while stack:
    y,x=stack.pop()
    move=mapli[y][x]
    if move==0:
      continue
    for i in range(2):
      nx = x+(dx[i])*move
      ny = y+(dy[i])*move
      if nx>map-1 or ny>map-1 or visited[ny][nx]:
        continue
      if mapli[ny][nx]==-1:
        print("HaruHaru")
        return
      else:
        stack.append((ny,nx))
        visited[ny][nx]=True
  print("Hing")

game(0,0,row)

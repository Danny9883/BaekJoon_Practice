import sys
input=sys.stdin.readline

col,row=map(int,input().split())
mapli=[]
for i in range(row):
  a=list(map(int,input().split()))
  mapli.append(a)

def dfs(r,c):
  stack=[]
  dx=[0,1]
  dy=[1,0]
  stack.append((r,c))
  while stack:
    y,x=stack.pop()
    if y==row-1 and x==col-1:
      print("Yes")
      return
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=col or ny<0 or ny>=row or mapli[ny][nx]==0:
        continue
      mapli[y][x]=0
      stack.append((ny,nx))
  print("No")
  return

dfs(0,0)

import sys
input=sys.stdin.readline

row,col=map(int,input().split())

mapli=[]
for _ in range(row):
  a=list(map(int,input().rstrip('\n')))
  mapli.append(a)

ans=[0]
def dfs(r,c):
  stack=[]
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  mapli[r][c]==1
  stack.append((r,c))
  while stack:
    y,x=stack.pop()
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if ny == row:
        ans.append(1)
        return
      if nx<0 or ny<0 or nx>=col or mapli[ny][nx]==1:
        continue
      mapli[ny][nx]=1
      stack.append((ny,nx))
  return



for i in range(col):
  if mapli[0][i] == 0:
    dfs(0,i)


if ans[-1]==0:
  print("NO")
else:
  print("YES")
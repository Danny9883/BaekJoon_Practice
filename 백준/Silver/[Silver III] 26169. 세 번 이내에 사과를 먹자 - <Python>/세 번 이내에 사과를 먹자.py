import sys
input=sys.stdin.readline

row=5
col=5
mapli=[]
for i in range(row):
  a=list(map(int,input().split()))
  mapli.append(a)
r,c=map(int,input().split())

ans=set()
ans.add(0)
def game(y,x,count,apple):
  dx=[0,1,-1,0]
  dy=[1,0,0,-1]
  if mapli[y][x]==1:
    apple+=1
  if apple==2:
    ans.add(1)
    return
  if count==3:
    return
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx>4 or ny>4 or nx<0 or ny<0 or mapli[ny][nx]==-1 :
      continue
    else:
      before=mapli[y][x]
      mapli[y][x]=-1
      game(ny,nx,count+1,apple)
      mapli[y][x]=before


game(r,c,0,0)
print(max(ans))
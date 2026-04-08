import sys
input=sys.stdin.readline


row,col=map(int,input().split())

mapli=[]
for i in range(row):
  li=list(input().rstrip('\n'))
  mapli.append(li)


maxans=0
def dfs(y,x,visit,count):
  global maxans
  count+=1
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if nx<0 or ny<0 or nx>=col or ny>=row or mapli[ny][nx] in visit:
      maxans=max(count,maxans)
      continue
    else:
      a=visit+mapli[ny][nx]
      dfs(ny,nx,a,count)

visited=""
visited += mapli[0][0]
dfs(0,0,visited,0)
print(maxans)









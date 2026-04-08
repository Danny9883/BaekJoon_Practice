import sys
input=sys.stdin.readline
import copy



row=int(input())
col=row

mapli=[]
minh=100
maxh=0
for i in range(row):
  li=list(map(int,input().split()))
  minh=min(min(li),minh)
  maxh=max(max(li),maxh)
  mapli.append(li)



def find(r,c,h):
  stack=[(r,c)]
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  mapli2[r][c]=0
  while stack:
    y,x=stack.pop()
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if ny<0 or nx<0 or ny>=row or nx>=col or mapli2[ny][nx]<=h:
        continue
      else:
        mapli2[ny][nx]=0
        stack.append((ny,nx))



land=set()

for h in range(minh-1,maxh+1):
  mapli2=copy.deepcopy(mapli)
  cc=0
  for r in range(row):
    for c in range(col):
      if mapli2[r][c]>h:
        find(r,c,h)
        cc+=1
  land.add(cc)

print(max(land))

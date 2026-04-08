import sys
input=sys.stdin.readline


row,col,t=map(int,input().split())

mapli=[['.' for _ in range(col)] for _ in range(row)]

for i in range(t):
  r,c=map(int,input().split())
  r,c=r-1,c-1
  mapli[r][c]='#'

trash=set()
def find(r,c):
  count=0
  stack=[(r,c)]
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  mapli[r][c]='.'
  while stack:
    y,x=stack.pop()
    count+=1
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if ny<0 or nx<0 or ny>=row or nx>=col or mapli[ny][nx]=='.':
        continue
      else:
        mapli[ny][nx]='.'
        stack.append((ny,nx))
  trash.add(count)

for r in range(row):
  for c in range(col):
    if mapli[r][c]=='#':
      find(r,c)

print(max(trash))
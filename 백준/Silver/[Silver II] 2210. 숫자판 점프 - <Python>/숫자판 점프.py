import sys
input=sys.stdin.readline

col,row=5,5
mapli=[]
for i in range(row):
  a=list(map(str,input().split()))
  mapli.append(a)

textli=set()

def dfs(y,x,count,text):
  dx=[0,1,0,-1]
  dy=[1,0,-1,0]
  if count==6:
    textli.add(text)
    return
  else:
    text+=mapli[y][x]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or nx>=col or ny<0 or ny>=row :
      continue
    else:
      dfs(ny,nx,count+1,text)
  return

for i in range(5):
  for j in range(5):
    a=''
    dfs(i,j,0,a)
print(len(textli))

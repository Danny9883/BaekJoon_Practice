import sys
input=sys.stdin.readline


row,t=map(int,input().split())

mapli=[[0]*(row+1)]
for i in range(row):
  b=[0]
  a=list(map(int,input().split()))
  b.extend(a)
  # b[1]+=mapli[i][-1]
  for j in range(row):
    b[j+1]+=b[j]
  mapli.append(b)


for _ in range(t):
  ans=0
  y1,x1,y2,x2=map(int,input().split())
  for i in range(y1,y2+1):
    ans+=mapli[i][x2]
    ans-=mapli[i][x1-1]
  print(ans)


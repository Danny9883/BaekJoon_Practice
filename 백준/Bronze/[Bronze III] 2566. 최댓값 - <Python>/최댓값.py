import sys
input=sys.stdin.readline

mapli=[]
maxnum=0
for i in range(9):
  row=list(map(int,input().split()))
  mapli.append(row)
  maxnum = max(maxnum,max(row))


for i in range(9):
  for j in range(9):
    if mapli[i][j] == maxnum:
      a,b=i+1,j+1

print(maxnum)
print(a,b)
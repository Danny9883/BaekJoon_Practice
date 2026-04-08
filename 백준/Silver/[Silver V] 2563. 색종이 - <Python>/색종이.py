import sys
input=sys.stdin.readline

t=int(input())
mapli=[]
for i in range(100):
  row=[0 for _ in range(100)]
  mapli.append(row)


for i in range(t):
  a,b=map(int,input().split())
  for row in range(b,b+10):
    for col in range(a,a+10):
      mapli[row][col] = 1


count=0
for row in range(100):
  for col in range(100):
    if mapli[row][col] ==1:
      count+=1

print(count)
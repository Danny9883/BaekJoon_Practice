import sys
input=sys.stdin.readline

n,m = map(int,input().split())
bag = [0]*(n+1)
for i in range(m):
  a,b,c=map(int,input().split())
  for j in range(a,b+1):
      bag[j]=c


for i in range(1,n+1):
   print(bag[i],end=' ')
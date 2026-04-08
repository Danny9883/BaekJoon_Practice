import sys
input=sys.stdin.readline

n,m = map(int,input().split())
bag = list(i for i in range(n+1))

for i in range(m):
  a,b = map(int,input().split())
  a1=bag[a]
  b1=bag[b]
  bag[a]=b1
  bag[b]=a1



for i in range(1,n+1):
   print(bag[i],end=' ')
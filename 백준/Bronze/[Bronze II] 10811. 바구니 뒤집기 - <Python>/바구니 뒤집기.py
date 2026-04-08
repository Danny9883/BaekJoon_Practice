import sys
input=sys.stdin.readline

n,m = map(int,input().split())
bag = list(i for i in range(n+1))

for i in range(m):
  a,b = map(int,input().split())
  li=[]
  for j in range(a,b+1):
    li.append(bag[j])
  for j in range(a,b+1):
    bag[j]=li.pop()



for i in range(1,n+1):
   print(bag[i],end=' ')
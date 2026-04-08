import sys
input=sys.stdin.readline


na,nb=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=a-b

if len(c)==0:
  print(0)
else:
  c=sorted(c)
  print(len(c))
  for i in c:
    print(i,end=' ')
      
    
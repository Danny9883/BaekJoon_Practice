import sys
input=sys.stdin.readline



t=int(input())

for i in range(t):
  a,b=map(int,input().split())
  count=1
  b2=1
  a2=1
  while count<=a:
    b2*=b
    b-=1
    a2*=count
    count+=1
  ans=b2//a2
  print(ans)
import sys
input=sys.stdin.readline


t=int(input())
xor=0
total=0
for i in range(t):
  a=list(map(int,input().split()))
  if a[0]==1:
    total+=a[1]
    xor ^=a[1]
  elif a[0]==2:
    total-=a[1]
    xor ^=a[1]
  elif a[0]==3:
    print(total)
  elif a[0]==4:
    print(xor)
  


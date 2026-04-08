import sys
input=sys.stdin.readline


t=int(input())
li=[0]
d=[0]*(t+1)
a=list(map(int,input().split()))
li.extend(a)
for i in range(1,t+1):
  for j in range(i):
    if li[i]>li[j]:
      d[i]=max(d[i],d[j]+li[i])
print(max(d))



import sys
input=sys.stdin.readline



t=int(input())

li=[0,1]

for i in range(1,t):
  a=li[i]+li[i-1]
  li.append(a)

ans=li[t]*4 + li[t-1]*2
print(ans)

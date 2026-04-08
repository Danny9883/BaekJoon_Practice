import sys
input=sys.stdin.readline

t=int(input())
li=[[0,0]]
for i in range(t):
  b=[0]
  a=list(map(int,input().split()))
  b.extend(a)
  b.append(0)
  li.append(b)



big=0
for i in range(1,t+1):
  for j in range(1,i+1):
    li[i][j]+=max(li[i-1][j],li[i-1][j-1])
    big=max(big,li[i][j])

print(big)
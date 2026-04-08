t=int(input())
li=list(map(int,input().split()))
li.sort()
s=0
for i in range(t):
  s+=sum(li[0:(t-i)])
print(s)
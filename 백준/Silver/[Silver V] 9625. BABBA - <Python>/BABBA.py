import sys
input=sys.stdin.readline



t=int(input())

ab=[(1,0)]
for i in range(t):
  a,b=ab.pop()
  na,nb=a,b
  a-=na
  b+=na
  a+=nb
  ab.append((a,b))

a,b=ab.pop()
print(a,b)

import sys
input=sys.stdin.readline



m=int(input())
li=[0,1,1,1]
for i in range(4,m+1):
  a=li[i-1]+li[i-3]
  li.append(a)

print(li[m])


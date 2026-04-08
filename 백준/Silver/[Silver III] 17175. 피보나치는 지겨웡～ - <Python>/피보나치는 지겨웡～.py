import sys
input=sys.stdin.readline



m=int(input())
li=[1,1]
for i in range(2,m+1):
  a=li[i-1]+li[i-2]+1
  li.append(a%1000000007)

print(li[m])

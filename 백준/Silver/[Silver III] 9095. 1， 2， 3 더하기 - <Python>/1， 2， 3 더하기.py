import sys
input=sys.stdin.readline


t=int(input())
li=[1,2,4]
for i in range(3,12):
  a=li[i-1]+li[i-2]+li[i-3]
  li.append(a)
for i in range(t):
  n=int(input())
  print(li[n-1])

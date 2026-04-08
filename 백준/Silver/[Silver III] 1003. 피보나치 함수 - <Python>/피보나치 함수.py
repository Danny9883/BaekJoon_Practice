import sys
input=sys.stdin.readline


t=int(input())

li=[0,1,1]
for i in range(3,41):
  a=li[i-1]+li[i-2]
  li.append(a)


for i in range(t):
  k=int(input())
  if k==0:
    print(1,0)
  else:
    print(li[k-1],li[k])
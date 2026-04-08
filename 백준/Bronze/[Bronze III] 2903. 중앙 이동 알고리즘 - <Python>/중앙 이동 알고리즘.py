import sys

input=sys.stdin.readline

t=int(input())

li=[2]
for i in range(15):
  a=(li[i]*2)-1
  li.append(a)

print((li[t])**2)

import sys
input=sys.stdin.readline

li=[i for i in range(1,31)]

for i in range(28):
  a=int(input())
  li.remove(a)

print(li[0])
print(li[1])
      


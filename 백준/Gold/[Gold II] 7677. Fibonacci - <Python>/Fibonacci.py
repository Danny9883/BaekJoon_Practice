import sys
input=sys.stdin.readline

while 1:
  b=int(input())
  if b==-1:
    break
  b%=15000
  li=[0,1]
  for i in range(1,b):
    m = li[i]+li[i-1]
    li.append(m)

  print(li[b]%10000)

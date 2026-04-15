import sys
input=sys.stdin.readline
from collections import deque



t = int(input())

for _ in range(t):
  que = deque()
  n, m = map(int,input().split())
  li = list(map(int,input().split()))
  limax = sorted(li)
  for i in range(len(li)):
    if i == m:
      que.append((li[i],1))
    else:
      que.append((li[i],0))
  i = 1
  while 1:
    a, b = que.popleft()
    if a == limax[-1]:
      if b==1:
        print(i)
        break
      else:
        i += 1
        limax.pop()
    else:
      que.append((a,b))


  



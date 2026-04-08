import sys
input=sys.stdin.readline
from collections import deque




t=int(input())
que=deque()
for _ in range(t):
  li=list(input().rstrip('\n').split())
  if li[0] == "push":
    a=int(li[1])
    que.append(a)
  elif li[0] == "pop":
    if len(que) == 0:
      print(-1)
    else:
      print(que.popleft())
  elif li[0] == "size":
    print(len(que))
  elif li[0] == "empty":
    if len(que) == 0:
      print(1)
    else:
      print(0)
  elif li[0] == "front":
    if len(que) == 0:
      print(-1)
    else:
      print(que[0])
  elif li[0] == "back":
    if len(que) == 0:
      print(-1)
    else:
      print(que[-1])
  
    






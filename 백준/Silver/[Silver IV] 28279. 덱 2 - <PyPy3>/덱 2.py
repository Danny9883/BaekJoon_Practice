import sys
input=sys.stdin.readline
from collections import deque


n=int(input())

deck=deque()

for _ in range(n):
  a=list(map(int,input().split()))

  if a[0] == 1:
    deck.appendleft(a[1])
  elif a[0] == 2:
    deck.append(a[1])
  elif a[0] == 3:
    if len(deck)==0:
      print(-1)
    else:
      print(deck.popleft())
  elif a[0] == 4:
    if len(deck)==0:
      print(-1)
    else:
      print(deck.pop())
  elif a[0] == 5:
    print(len(deck))
  elif a[0] == 6:
    if len(deck)==0:
      print(1)
    else:
      print(0)
  elif a[0] == 7:
    if len(deck)==0:
      print(-1)
    else:
      print(deck[0])
  elif a[0] == 8:
    if len(deck)==0:
      print(-1)
    else:
      print(deck[-1])

    
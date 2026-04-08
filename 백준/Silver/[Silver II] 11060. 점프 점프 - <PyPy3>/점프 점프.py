import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
mapli=[0]
li=list(map(int,input().split()))
mapli.extend(li)


visited=set()
def find(s,count):
  que = deque()
  que.append((s,count))
  while que:
    v,count = que.popleft()
    if v==t:
      return count
    dx = mapli[v]
    for i in range(1,dx+1):
      if v+i not in visited and v+i <= t:
        nx = v + i
        que.append((nx,count+1))
        visited.add(nx)
      else:
        continue
  return -1

print(find(1,0))






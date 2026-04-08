import sys
from collections import deque
input=sys.stdin.readline

s,f=map(int,input().split())

visited=set()
def find(s,f):
  que = deque()
  que.append((s,0))
  while que:
    v,count=que.popleft()
    if v==f:
      return count
    if v*2 not in visited and v*2 <= f:
      que.append((v*2,count+1))
      visited.add(v*2)
    if v+1 not in visited and v+1 <= f:
      que.append((v+1,count+1))
      visited.add(v+1)

print(find(s,f))






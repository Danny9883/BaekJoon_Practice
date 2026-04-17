import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
sys.setrecursionlimit(1000000)


n , m = map(int,input().split())

mem = [[] for _ in range(n+1)]
ind = [0 for _ in range(n+1)]

for _ in range(m):
  a , b = map(int,input().split())
  mem[a].append(b)
  ind[b] += 1

que = deque()


for i in range(1,n+1):
  if ind[i] == 0:
    que.append(i)

sortli = []
while que:
  v = que.popleft()
  sortli.append(v)
  for i in mem[v]:
    ind[i] -= 1
    if ind[i] == 0:
      que.append(i)
  mem[v].clear()


for i in sortli:
  print(i,end=' ')









 

  



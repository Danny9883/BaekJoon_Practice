import sys
input=sys.stdin.readline
from heapq import heappush,heappop





n=int(input())

graph=[[]for _ in range(n+1)]

for _ in range(n-1):
  a,b,w=map(int,input().split())
  graph[a].append((w,b))
  graph[b].append((w,a))

def dijk(s):
  d=[float('INF') for _ in range(n+1)]
  heap = [(0,s)]
  d[s]=0
  while heap:
    w,v=heappop(heap)
    if d[v] < w:
      continue
    for nw,i in graph[v]:
      if d[i] > d[v] + nw:
        d[i] = d[v] + nw
        heappush(heap,(d[i],i))
  ans=0
  for i in d:
    if i != float('INF'):
      ans = max(ans,i)
  return ans

print(dijk(1))



import sys
input=sys.stdin.readline
from collections import deque




t,l=map(int,input().split())

mapli=[[]for _ in range(t+1)]

for _ in range(l):
  a,b=map(int,input().split())
  mapli[a].append(b)
  mapli[b].append(a)

def bfs(s):
  visited=[False for _ in range(t+1)]
  d = [-1 for _ in range(t+1)]
  que = deque()
  que.append(s)
  d[s] = 0
  visited[s]=True
  while que:
    v=que.popleft()
    for i in mapli[v]:
      if visited[i]:
        continue
      else:
        que.append(i)
        d[i] = d[v]+1
        visited[i]=True
  return d[1:]

q=int(input())

for _ in range(q):
  a,b=map(int,input().split())
  mapli[a].append(b)
  mapli[b].append(a)
  ans=bfs(1)
  for i in ans:
    print(i,end=' ')
  print()




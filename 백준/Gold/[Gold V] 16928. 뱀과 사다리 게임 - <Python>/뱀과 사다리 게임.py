import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
sys.setrecursionlimit(1000000)



t,l=map(int,input().split())

mapli=[0] * 101



for _ in range(t+l):
  a,b=map(int,input().split())
  mapli[a] = b




def bfs(s):
  visited=[False for _ in range(101)]
  d = [-1 for _ in range(101)]
  que = deque()
  que.append(s)
  d[s] = 0
  visited[s]=True
  while que:
    v=que.popleft()
    if v==100:
      return d[100]
    for i in range(1,7):
      nx = i + v
      if nx <=100:  
        if mapli[nx] != 0:
          nx = mapli[nx]
        if not visited[nx]:
          que.append(nx)
          d[nx] = d[v] + 1
          visited[nx] = True


        
  

print(bfs(1))








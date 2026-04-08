import sys
from collections import deque
input=sys.stdin.readline


mapli=[]
visited=[]
for i in range(5):
  a=list(map(int,input().split()))
  vi=[False for _ in range(5)]
  mapli.append(a)
  visited.append(vi)

r,c=map(int,input().split())


def bfs(r,c,count):
  que=deque()
  que.append((r,c,count))
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  visited[r][c]=True
  while que:
    y,x,count=que.popleft()
    if mapli[y][x]==1:
      return count
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if nx<0 or ny<0 or nx>=5 or ny>=5 or mapli[ny][nx]==-1 or visited[ny][nx]==True:
        continue
      else:
        que.append((ny,nx,count+1))
        visited[ny][nx]=True
  return -1

print(bfs(r,c,0))
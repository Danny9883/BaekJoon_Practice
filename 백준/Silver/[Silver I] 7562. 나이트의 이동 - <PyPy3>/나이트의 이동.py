import sys
input=sys.stdin.readline
from collections import deque



ttt= int(input())
for _ in range(ttt):

  row=int(input())
  col=row
  sy,sx=map(int,input().split())
  fy,fx=map(int,input().split())

  def bfs(r,c):
    que=deque()
    visited=[[False for _ in range(row)] for _ in range(row)]
    que.append((r,c,0))
    visited[r][c]=True
    dx = [2,2,1,-1,-2,-2,1,-1]
    dy = [1,-1,-2,-2,1,-1,2,2]
    while que:
      y,x,count=que.popleft()
      if y==fy and x==fx:
        return count
      for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or ny<0 or nx>=col or ny>=row or visited[ny][nx]:
          continue
        else:
          que.append((ny,nx,count+1))
          visited[ny][nx]=True

  print(bfs(sy,sx))


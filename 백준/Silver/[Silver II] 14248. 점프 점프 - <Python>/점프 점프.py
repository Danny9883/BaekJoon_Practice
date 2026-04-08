import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


t=int(input())
mapli=[0]
mapli.extend(list(map(int,input().split())))
start=int(input())

visited=[0]*(t+1)

def dfs(index,count):
  move=mapli[index]
  dx=[1,-1]
  visited[index]=1
  for i in range(2):
    nx= index + (dx[i])*move
    if nx<=0 or nx>t or visited[nx]==1:
      continue
    else:
      dfs(nx,count+1)

  
  
dfs(start,1)
print(sum(visited))
  
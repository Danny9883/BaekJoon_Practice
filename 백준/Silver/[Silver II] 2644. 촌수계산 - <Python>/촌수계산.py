import sys
input=sys.stdin.readline

people=int(input())
start,end=map(int,input().split())
t=int(input())
mapli=[]
for i in range(people+1):
  a=[]
  mapli.append(a)


for i in range(t):
  a,b=map(int,input().split())
  mapli[a].append(b)
  mapli[b].append(a)

visited=[]
chon=set()
chon.add(-1)
def dfs(start,end,count):
  v=start
  visited.append(v)
  if v == end:
    chon.add(count)
    return
  for i in mapli[v]:
    if i not in visited:
      dfs(i,end,count+1)
  return

dfs(start,end,0)
print(max(chon))

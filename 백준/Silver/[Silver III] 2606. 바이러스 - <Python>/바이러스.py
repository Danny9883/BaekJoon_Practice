visited = []


a=int(input())
b=int(input())
li=[]
for i in range(a+1):
  li.append([])
for i in range(b):
  x,y=map(int,input().split())
  li[x].append(y)
  li[y].append(x)
  li[x].sort()
  li[y].sort()


def dfs(list,start,visited):
  visited.append(start)
  for i in list[start]:
    if i not in visited:
      dfs(list,i,visited)

dfs(li,1,visited)
print(len(visited)-1)
from collections import deque
import sys
input=sys.stdin.readline



a,b=map(int,input().split())

li=[[]*k for k in range(a+1)]


for i in range(b):
  x,y=map(int,input().split())
  li[x].append(y)
  li[y].append(x)
  li[x].sort()
  li[y].sort()


visit = []
count = 0
def dfs(start,visit):
  global count
  stack = []
  mm=[]
  if start in visit:
    return
  stack.append(start)
  while stack:
    v = stack.pop()
    if v not in visit:
      mm.append(v)
      visit.append(v)
      stack.extend(reversed(li[v]))
  count +=1

      

for i in range(1,a+1):
  dfs(i,visit)
print(count)

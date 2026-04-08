from collections import deque
import sys
input=sys.stdin.readline

n,m,k,x=map(int,input().split())
mapli=[]
for i in range(n+1):
  a=[]
  mapli.append(a)

for i in range(m):
  a,b=map(int,input().split())
  mapli[a].append(b)

def find(start,fin):
  stack=deque()
  distance=[]
  finlist=[]
  for _ in range(n+1):
    distance.append(-1)
  stack.append(start)
  distance[start]=0
  while stack:
    v=stack.popleft()
    for i in mapli[v]:
        if distance[i]>-1:
          continue
        distance[i]=distance[v]+1
        if distance[i]==fin:
          finlist.append(i)
          continue
        stack.append(i)
  finlist.sort()
  if len(finlist)==0:
    print(-1)
  else:
    for j in finlist:
      print(j)

find(x,k)
  
      


import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
li=[]
for i in range(n+1):
  li.append([])

for i in range(n-1):
  a,b=map(int,input().split())
  li[a].append(b)
  li[b].append(a)


def find(s):
  visited=[False]*(n+1)
  parant=[0]*(n+1)
  que=[]
  que.append(s)
  visited[s]=True
  while que:
    v=que.pop()
    for i in li[v]:
      if visited[i]==False:
        parant[i]=v
        que.append(i)
        visited[i]=True
  for i in range(2,n+1):
    print(parant[i])

find(1)






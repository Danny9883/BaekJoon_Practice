import sys
input=sys.stdin.readline
from heapq import heappush,heappop



n , m = map(int,input().split())


mem = [[] for _ in range(n+1)]
ind = [0 for _ in range(n+1)]

for _ in range(m):
  a , b = map(int,input().split())
  mem[a].append(b)
  ind[b] += 1


heap = []


for i in range(1,n+1):
  if ind[i] == 0:
    heappush(heap,i)





sortli = []
li2=[]
while heap:
  v = heappop(heap)
  sortli.append(v)
  maxi=0
  for i in mem[v]:
    ind[i] -= 1
    if ind[i] == 0:
      heappush(heap,i)
  mem[v].clear()



for i in sortli:
  print(i,end=' ')


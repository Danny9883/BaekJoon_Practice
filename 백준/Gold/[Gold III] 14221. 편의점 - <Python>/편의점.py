import sys
input=sys.stdin.readline
from heapq import heappush,heappop





t,l=map(int,input().split())

mapli=[[] for _ in range(t+1)]
for i in range(l):
  a,b,w=map(int,input().split())
  mapli[a].append((w,b))
  mapli[b].append((w,a))

h,c=map(int,input().split())


home = list(map(int,input().split()))
con = list(map(int,input().split()))




def dijk():
  d=[float('INF') for _ in range(t+1)]
  heap=[]
  for i in con:
    heappush(heap,(0,i))
    d[i]=0
  while heap:
    w,v=heappop(heap)
    if d[v] < w:
      continue
    for nw,nv in mapli[v]:
      if d[nv] > d[v] + nw:        
        d[nv] = d[v] + nw
        heappush(heap,(d[nv],nv))
  return d

mindis = 99999999
ansnum = []
dis = dijk()


for j in home:
  if dis[j] < mindis:
    mindis = dis[j]
    ansnum.clear()
    ansnum.append(j)
  elif dis[j] == mindis:
    ansnum.append(j)

print(min(ansnum))






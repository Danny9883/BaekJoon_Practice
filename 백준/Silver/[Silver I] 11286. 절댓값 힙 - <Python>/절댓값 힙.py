import heapq
import sys
input=sys.stdin.readline

heap=[]
t=int(input())
for i in range(t):
  a=int(input())
  if a==0:
    if len(heap)==0:
      print(0)
    else:   
      print(heap[0][1])
      heapq.heappop(heap)
  elif a>0:
    heapq.heappush(heap, [a,a])
  else:
    heapq.heappush(heap, [-a,a])
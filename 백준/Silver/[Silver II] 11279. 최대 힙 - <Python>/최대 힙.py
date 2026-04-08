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
      print(-(heap[0]))
      heapq.heappop(heap)
  else:
    heapq.heappush(heap, -a)

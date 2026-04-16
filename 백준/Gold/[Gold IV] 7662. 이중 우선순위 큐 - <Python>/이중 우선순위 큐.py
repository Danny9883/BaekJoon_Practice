import sys
input=sys.stdin.readline
from heapq import heappush,heappop



t = int(input())

for _ in range(t):
  t2 = int(input())
  heap_m = []
  heap_h = []
  visited = [False] * t2
  for i in range(t2):
    a, n = input().rstrip('\n').split()
    n =  int(n)
    if a == 'I':
      heappush(heap_m,(n,i))
      heappush(heap_h,(-n,i))
      visited[i] = True
    else:
      if n == 1:
        if len(heap_h) != 0:
          visited[heap_h[0][1]] = False
          heappop(heap_h)
          if len(heap_h) == 0 or -(heap_h[0][0]) < heap_m[0][0]:
            heap_m = []
            heap_h = []
        else:
            visited[i] = False
            heap_m = [] 
            heap_h = []
      else:
        if len(heap_m) != 0 :
          visited[heap_m[0][1]] = False
          heappop(heap_m)
          if len(heap_m) == 0 or -(heap_h[0][0]) <  heap_m[0][0]:
            heap_m = []
            heap_h = []
        else:
            visited[i] = False
            heap_m = []
            heap_h = []
      while heap_m and visited[heap_m[0][1]] == False:
        heappop(heap_m)
      while heap_h and visited[heap_h[0][1]] == False:
        heappop(heap_h)
  while heap_m and visited[heap_m[0][1]] == False:
    heappop(heap_m)
  while heap_h and visited[heap_h[0][1]] == False:
    heappop(heap_h)
  if len(heap_m) == 0:
    print('EMPTY')
  else:
    print(-(heap_h[0][0]),heap_m[0][0])




 

  



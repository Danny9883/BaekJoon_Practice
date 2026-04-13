import sys
input=sys.stdin.readline



k, n = map(int,input().split())
li = []
for _ in range(k):
  li.append(int(input()))


def bs(n):
  low = 0
  high = 2200000000
  while low <= high:
    mid = (low + high)//2
    cnt = 0
    for i in li:
      cnt += i//mid
    if cnt < n:
      high = mid - 1
    elif cnt >= n:
      low = mid + 1 
  return high
  
print(bs(n))











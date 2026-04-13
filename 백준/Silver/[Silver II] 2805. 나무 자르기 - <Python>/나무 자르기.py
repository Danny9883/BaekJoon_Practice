import sys
input=sys.stdin.readline


k, n = map(int,input().split())
li = list(map(int,input().split()))



def bs(n):
  low = 0
  high = 2200000000
  while low <= high:
    mid = (low + high)//2
    cnt = 0
    for i in li:
      if i-mid <= 0 :
        continue
      else:
        cnt += i-mid
    if cnt < n :
      high = mid -1
    elif cnt >= n:
      low = mid + 1
    
  return high
    

print(bs(n))











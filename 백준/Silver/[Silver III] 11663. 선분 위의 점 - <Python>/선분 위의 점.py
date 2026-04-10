import sys
input=sys.stdin.readline


def bs(q,n): 
  low = 0
  high = len(s1)-1
  lowt=0
  hight=len(s1)-1
  while low <= high :
    mid = (low + high)//2
    if s1[mid] < n :
      lowt = mid
      low = mid + 1
    elif s1[mid] > n :
      hight = mid
      high = mid -1
    else:
      if q==1:
        while 1:
          if s1[lowt] == n:
            return len(s1) - (lowt)
          else:
            lowt += 1
      elif q==2:
        while 1:
          if s1[hight] == n:
            return hight+1
          else:
            hight -= 1
  if q==1:
    return len(s1) - low
  elif q==2:
    return low
        
  


n , m = map(int,input().split())

s1 = list(map(int,input().split()))
s1.sort()

for _ in range(m):
  a , b = map(int,input().split())
  if a>b:
    print(bs(1,b)+bs(2,a)-len(s1))
  else:
    print(bs(1,a)+bs(2,b)-len(s1))







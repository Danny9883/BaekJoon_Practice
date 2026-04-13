import sys
input=sys.stdin.readline


k = int(input())
li = list(map(int,input().split()))



def bs():
  low = 0
  high = len(li) - 1
  lowt  = 0 
  hight = 0 
  ans = 3000000000
  while low < high:
    t = abs(li[low] + li[high])
    if t < ans:
      ans = t
      lowt = li[low]
      hight = li[high]
      if ans < abs(li[low] + li[high-1]):
        low += 1
      else:
        high -= 1
    elif t > ans:
      if abs(li[low+1] + li[high])> abs(li[low] + li[high-1]):
        high -= 1
      else:
        low += 1
    else:
      ans = t
      lowt = li[low]
      hight = li[high]
      if abs(li[low+1] + li[high])> abs(li[low] + li[high-1]):
        high -= 1
      else:
        low += 1
      
  print(lowt,hight)

bs()











import sys
input=sys.stdin.readline




n, s = map(int,input().split())
li = list(map(int,input().split()))

def sw(s):
  low = 0
  high = 0
  ans = 1000000
  start = 0
  while low <= high :
    if high == len(li):
      break
    start += li[high]
    if start < s :
      high += 1
    else:
      if high - low + 1< ans:
        ans = high - low + 1
      start -= li[low]
      start -= li[high]
      low += 1
  if ans >= 1000000:
    return 0
  return ans

print(sw(s))










import sys
input=sys.stdin.readline



x, y = map(int,input().split())

def bs(x,y):
  low = 0
  high = 1000000000
  z = int(y*100//x)
  ans = -1
  while low <= high:
    mid = (low + high)//2
    if int((y+mid)*100//(x+mid)) == z:
      low = mid + 1
    else:
      high = mid - 1
      ans = mid
  return ans

print(bs(x,y))










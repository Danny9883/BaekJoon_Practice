import sys
input=sys.stdin.readline



def bs(n):
  low = 0
  high = len(d) - 1
  while low <= high:
    mid = (low + high)//2
    if d[mid] < n:
      low = mid + 1
    elif d[mid] > n:
      high = mid - 1
    else:
      return
  d[low] = n
  



t = int(input())
li = [-2000000000]
li.extend( list(map(int,input().split())) )

d = []
d.append(li[1])

for i in range(2,t+1):
  if li[i] > d[-1]:
    d.append(li[i])
  else:
    bs(li[i])

print(len(d))







 

  



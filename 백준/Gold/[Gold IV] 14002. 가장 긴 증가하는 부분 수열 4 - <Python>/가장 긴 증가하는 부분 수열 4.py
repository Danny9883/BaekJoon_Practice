import sys
input=sys.stdin.readline



def bs(n,i):
  low = 0
  high = len(d) - 1
  while low <= high:
    mid = (low + high)//2
    if d[mid] < n:
      low = mid + 1
    elif d[mid] > n:
      high = mid - 1
    else:
      inx[i] = mid+1
      return
  d[low] = n
  inx[i] = low+1
  



t = int(input())
li = [-2000000000]
li.extend( list(map(int,input().split())) )

d = []
d.append(li[1])
inx = [0 for _ in range (t+1)]
inx[1] = 1

hi = 1
for i in range(2,t+1):
  if li[i] > d[-1]:
    d.append(li[i])
    inx[i] = hi+1
    hi+=1
  else:
    bs(li[i],i)

print(len(d))
stack = []
for i in range(t,0,-1):
  if inx[i]==hi:
    stack.append(li[i])
    hi-=1
while stack:
  print(stack.pop(),end=' ')






 

  



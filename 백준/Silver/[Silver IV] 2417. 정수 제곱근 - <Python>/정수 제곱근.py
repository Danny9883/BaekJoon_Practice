n = int(input())

if n==0:
  print(0)
else:
  low = 1
  high = n//2

  while low <= high:
    mid = (low + high)//2
    if mid**2 < n:
      low = mid + 1
    elif mid**2 > n:
      high = mid - 1
    else:
      high = mid - 1
      break
      

  print(high+1)

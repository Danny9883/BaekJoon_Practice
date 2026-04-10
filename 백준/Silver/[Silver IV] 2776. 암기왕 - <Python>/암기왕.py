def bs(n):
  low = 0
  high = len(s1)-1
  while low <= high :
    mid = (low + high)//2
    if s1[mid] < n :
      low = mid + 1
    elif s1[mid] > n :
      high = mid -1
    else:
      return 1
  return 0
  


t = int(input())

for _ in range(t):
  n = int(input())
  s1 = list(map(int,input().split()))
  s1.sort()
  n = int(input())
  s2 = list(map(int,input().split()))

  for i in s2:
    print(bs(i))

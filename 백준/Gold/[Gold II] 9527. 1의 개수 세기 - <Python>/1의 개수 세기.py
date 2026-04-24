import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
sys.setrecursionlimit(1000000)
import math

a, b = map(int,input().split())

dp = [1]
for i in range(1,57):
  x = dp[i-1] * 2 + 2**i
  dp.append(x)
dp.insert(0,0)

def allsum(n):
  if n<=0:
    return 0
  ans = 0
  k = int(math.log2(n))
  ans += dp[k]
  ans += (n - 2**k + 1)
  return ans + allsum(n - 2**k)


print(allsum(b) - allsum(a-1))



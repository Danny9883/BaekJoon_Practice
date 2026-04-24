import sys
input=sys.stdin.readline


c, n = map(int,input().split())

dp = [1000000000 for _ in range(c+101)]
dp[0] = 0


for i in range(n):
  m, p = map(int,input().split())
  
  for j in range(p,c+101):
    dp[j] = min(dp[j], m+dp[j-p])

print(min(dp[c:]))


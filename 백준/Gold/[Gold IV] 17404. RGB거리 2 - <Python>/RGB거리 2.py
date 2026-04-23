import sys
input=sys.stdin.readline


n = int(input())
cost = []

for _ in range(n):
  r, g, b = map(int,input().split())
  cost.append([r,g,b])

ans = float("INF")

for color in range(3):
  dp = [[0] * 3 for _ in range(n)]

  for i in range(3):
    if i == color:
      dp[0][i] = cost[0][i]
    else:
      dp[0][i] = float("INF")

  for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + cost[i][2]

  for i in range(3):
    if i != color:
      ans = min(ans,dp[n-1][i])

  


print(ans)









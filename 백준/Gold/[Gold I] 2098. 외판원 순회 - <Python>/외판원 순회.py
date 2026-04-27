import sys
input=sys.stdin.readline



n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]
visited_all = (1 << n) -1

dp = [[None] * (1<<n) for _ in range(n)]
inf = float('INF')

def tsp(l, visited):
  if visited == visited_all:
    return city[l][0] or inf
  
  if dp[l][visited] is not None:
    return dp[l][visited]
  
  tmp = inf
  for c in range(n):
    if visited & (1<<c) == 0 and city[l][c] != 0 :
      tmp = min(tmp, tsp(c, visited | (1<<c)) +city[l][c] ) 
  dp[l][visited] = tmp
  return tmp


print(tsp(0, 1<<0))







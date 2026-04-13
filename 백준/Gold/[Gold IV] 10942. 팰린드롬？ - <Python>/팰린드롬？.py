import sys
input=sys.stdin.readline




n = int(input())
li = list(map(int,input().split()))
pal = [[0] * n for _ in range(n)]
for i in range(n):
  pal[i][i] = 1

for i in range(n-1):
  if li[i] == li[i+1]:
    pal[i][i+1] = 1

for i in range(3, n+1):
  for j in range(n - i + 1):
    k = j + i - 1
    if li[j] == li[k] and pal[j+1][k-1] == 1:
      pal[j][k] = 1


t = int(input())
for _ in range(t):
  a, b = map(int,input().split())
  a -= 1
  b -= 1
  print(pal[a][b])














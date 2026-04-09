import sys
input=sys.stdin.readline


n, m, q = map(int,input().split())

li = []

for _ in range(n):
  t = list(map(int,input().split()))
  li.append(t)

for _ in range(q):
  t = list(map(int,input().split()))
  if t[0] == 0:
    li[t[1]][t[2]] = t[3]
  else:
    li[t[1]], li[t[2]] = li[t[2]], li[t[1]]

for i in range(n):
  for j in range(m):
    print(li[i][j],end=' ')
  print()










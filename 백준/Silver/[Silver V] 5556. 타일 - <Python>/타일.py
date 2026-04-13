import sys
input=sys.stdin.readline



n = int(input())
t = int(input())
for _ in range(t):
  x , y  = map(int,input().split())
  if n//2 <= x:
    x = n-x+1
  if n//2 <= y:
    y = n-y+1
  if y < x:
    ans = y%3
  else:
    ans = x%3
  if ans == 0 :
    ans += 3
  print(ans)
  







import sys
input=sys.stdin.readline


while 1:

  n, m = map(int,input().split())

  if (n == 0 and m == 0):
    break

  a = set()
  b = set()

  for _ in range(n):
    cd = int(input())
    a.add(cd)

  for _ in range(m):
    cd = int(input())
    b.add(cd)
    
  print( len(a & b) )


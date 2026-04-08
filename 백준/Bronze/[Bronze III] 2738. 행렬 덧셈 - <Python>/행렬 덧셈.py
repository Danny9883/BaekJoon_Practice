from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a1=[]
b1=[]
for i in range(n):
  a=list(map(int,input().split()))
  a1.append(a)
for i in range(n):
  a=list(map(int,input().split()))
  b1.append(a)
for i in range(n):
  for j in range(m):
    print(a1[i][j]+b1[i][j],end=' ')
  print()
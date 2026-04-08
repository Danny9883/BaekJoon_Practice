from itertools import *
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

numli=[i for i in range(1,n+1)]
li=list(combinations(numli,m))
if m ==1:
  for i in numli:
    print(i)
else:
  for i in li:
    a=list(i)
    for j in a:
      print(j,end=' ')
    print()
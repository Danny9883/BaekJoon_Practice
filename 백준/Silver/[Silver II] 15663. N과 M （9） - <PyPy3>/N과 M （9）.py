from itertools import *
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

numli=list(map(int,input().split()))
numli.sort()
li=list(permutations(numli,m))
li=set(li)
li=sorted(li)


if m ==1:
  numli=set(numli)
  for i in numli:
    print(i)
else:
  for i in li:
    a=list(i)
    for j in a:
      print(j,end=' ')
    print()
import sys
from bisect import bisect_left
input=sys.stdin.readline



t=int(input())

li=list(map(int,input().split()))
li2=sorted(set(li))

for i in li:
  print(bisect_left(li2,i),end=' ')
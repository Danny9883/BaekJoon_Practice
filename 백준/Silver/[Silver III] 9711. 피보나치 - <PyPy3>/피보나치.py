import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
for i in range(1,n+1):
  li=[0,1]
  a,b=map(int,input().split())
  if a==1:
    li.append(1%b)
  for j in range(2,a+1):
    pi=li[j-1]+li[j-2]
    li.append(pi%b)
  ans=li[-1]
  print(f"Case #{i}: {ans}") 
  






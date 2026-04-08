import sys
input=sys.stdin.readline

t=int(input())
li=list(map(int,input().split()))
print(min(li)*max(li))
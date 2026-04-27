import sys
input=sys.stdin.readline



n = int(input())
k = 0
li = list(map(int,input().split()))
for i in li:
  k ^= i

if k==0:
  print("cubelover")
else:
  print("koosaga")




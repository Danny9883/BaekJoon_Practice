import sys
input=sys.stdin.readline



n = int(input())
k = 0
li = list(map(int,input().split()))
chk = True
for i in li:
  k ^= i
  if i> 1:
    chk = False

if chk:
  if n%2==0:
    print("koosaga")
  else:
    print("cubelover")
else:
  if k==0:
    print("cubelover")
  else:
    print("koosaga")




import sys
input=sys.stdin.readline



n=int(input())

for _ in range(n):
  li=list(input().rstrip('\n').split())
  while 1:
    a=list(input().rstrip('\n').split())
    if a[0] == "what":
      break
    b=a[-1]
    while b in li:
      li.remove(b)
  for i in li:
    print(i,end=' ')
    

    
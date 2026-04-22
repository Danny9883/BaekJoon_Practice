import sys
input=sys.stdin.readline



tt = int(input())
for _ in range(tt):
  t = int(input())
  li1 = list(map(str,input().rstrip('\n').split()))
  li2 = list(map(str,input().rstrip('\n').split()))
  li1.sort()
  li2.sort()
  ischeat = False
  for i in range(t):
    if li1[i] != li2[i]:
      ischeat = True
      break
  if ischeat:
    print("CHEATER")
  else:
    print("NOT CHEATER")







    















 

  



a,b=map(int,input().split())
bb=(100-b)/100
a*=bb
if a >= 100:
  print(0)
else:
  print(1)
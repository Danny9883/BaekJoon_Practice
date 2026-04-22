import sys
input=sys.stdin.readline



cnt = 1
pi = 3.1415927
while 1:
  l, r ,t = map(float,input().split())
  if r==0:
    break
  dis=l*pi*r/5280/12
  time = t/3600
  print(f"Trip #{cnt}: {dis:.2f} {dis/time:.2f}")
  cnt+=1



    















 

  



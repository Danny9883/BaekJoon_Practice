t=int(input())


for i in range(t):
  fact=1
  a=int(input())
  for i in range(1,a+1):
    fact*=i
  while 1:
    if fact%10==0:
      fact//=10
    else:
      print(fact%10)
      break

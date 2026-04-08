t=int(input())

def fac(n):
  if n==0 or n==1:
    return 1
  else:
    return n * fac(n-1)



for i in range(t):
  a=int(input())
  afac=fac(a)
  print(afac%10)

s=int(input())
for p in range(s):
  t=int(input())
  n=int(input())
  num=list(range(1,n+1))
  num2=[]
  test=0
  for k in range(t):
      for i in range(n):
        num2.append(sum(num[0:(i+1)]))
      num=num2
      num2=[]
  print(num[-1])
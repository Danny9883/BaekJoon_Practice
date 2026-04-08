t=int(input())
for i in range(1,t+1):
  a='*'*i
  b=' '*(2*(t-i))
  print(a+b+a)
for i in range(t-1,0,-1):
  a='*'*i
  b=' '*(2*(t-i))
  print(a+b+a)
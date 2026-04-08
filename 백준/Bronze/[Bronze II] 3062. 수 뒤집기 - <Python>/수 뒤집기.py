t=int(input())
for i in range(t):
  a=input()
  a2=a[::-1]
  a=int(a)
  a2=int(a2)
  b=a+a2
  b=str(b)
  if b == b[::-1]:
    print('YES')
  else:
    print('NO')
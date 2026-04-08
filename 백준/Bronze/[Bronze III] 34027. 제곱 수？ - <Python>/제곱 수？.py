t=int(input())
for i in range(t):
  a=int(input())
  sqa=a**0.5
  sqa=int(sqa)
  if sqa**2 == a:
    print(1)
  else:
    print(0)
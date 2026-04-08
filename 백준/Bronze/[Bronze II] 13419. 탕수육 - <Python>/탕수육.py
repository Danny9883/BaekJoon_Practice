t=int(input())
for i in range(t):
  a=input()
  if len(a)%2==1:
    a*=2
  n1=''
  n2=''
  for j in range(len(a)):
    if j%2==1:
      n2+=a[j]
    else:
      n1+=a[j]
  print(n1)
  print(n2)
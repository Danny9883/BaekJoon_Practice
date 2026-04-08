n=int(input())
if n==1:
  print(1)
else:
  find2=2
  while find2<n:
    find2*=2
  num=find2-n
  print(find2-(num*2))

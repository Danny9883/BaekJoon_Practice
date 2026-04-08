n=int(input())
for kk in range(n):
  t=list(input())
  count=0
  for i in t:
    if i=='(':
      count+=1
    else:
      count-=1
    if count<0:
      break
  if count==0:
    print('YES')
  else:
    print('NO')
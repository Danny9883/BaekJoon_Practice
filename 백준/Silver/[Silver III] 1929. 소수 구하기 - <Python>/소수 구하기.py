m,n=map(int,input().split())
e=[2,3]
for i in range(4,n+1):
  for k in e:
    if i%k==0:
      break
    else:
      if (i**0.5)<k:
        e.append(i)
        break
for i in e:
  if m<= i <=n:
    print(i)
      





n,k=map(int,input().split())
m=[]
for i in range(1,n+1):
  if n%i==0:
    m.append(i)
if len(m)<k:
  print('0')
else:
  print(m[k-1])
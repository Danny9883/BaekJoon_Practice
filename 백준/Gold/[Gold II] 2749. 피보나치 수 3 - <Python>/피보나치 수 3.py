li=[0,1,1]
n=int(input())%1500000
for i in range(3,n+1):
  a=(li[i-1]+li[i-2])%1000000
  li.append(a)

if n==0:
  print(0)
else:
  print(li[-1])
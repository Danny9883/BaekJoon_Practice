li=[0,1,1]
n=int(input())
for i in range(3,n+1):
  a=li[i-1]+li[i-2]
  li.append(a)

if n==0:
  print(0)
else:
  print(li[-1])
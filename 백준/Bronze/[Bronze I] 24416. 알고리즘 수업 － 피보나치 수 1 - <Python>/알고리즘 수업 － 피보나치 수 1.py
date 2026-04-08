li=[0,1]
n=int(input())
for i in range(2,n+1):
  a=li[i-1]+li[i-2]
  li.append(a)
print(li[n],(n-2))
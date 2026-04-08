li=[0,1]
n=int(input())
for i in range(2,n+1):
  a=li[i-1]+li[i-2]
  if a>=1000000007:
    a=a%1000000007
    li.append(a)
  else:
    li.append(a)
print(li[n])
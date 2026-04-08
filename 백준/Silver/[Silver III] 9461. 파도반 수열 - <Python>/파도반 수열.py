t=int(input())
for i in range(t):
  li=[1,1,1]
  a=int(input())
  for j in range(3,a):
    k=li[j-2]+li[j-3]
    li.append(k)
  print(li[-1])

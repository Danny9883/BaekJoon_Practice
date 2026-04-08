t=int(input())
li=[]
for i in range(t):
  a=int(input())
  if a==0:
    li.pop()
  else:
    li.append(a)
print(sum(li))
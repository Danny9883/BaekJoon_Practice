m=int(input())
n=int(input())
li=[]
for i in range(m,n+1):
  for j in range(2,i+1):
    if i==j:
      li.append(i)
    elif i%j==0:
      break
sum=0
for i in li:
  sum+=i
if len(li)==0:
  print(-1)
else:
  print(sum)
  print(li[0])
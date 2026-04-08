t=int(input())
x=t//5
li=[]
for i in range(0,x+1):
  if (t-(i*5))%3==0:
    ans=i+((t-(i*5))//3)
    li.append(ans)
li.sort()
if len(li)==0:
  print(-1)
else:
  print(li[0])
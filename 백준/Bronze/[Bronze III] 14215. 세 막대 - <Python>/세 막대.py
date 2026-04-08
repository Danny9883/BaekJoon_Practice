a,b,c=map(int,input().split())
li=[]
li.append(a)
li.append(b)
li.append(c)
li.sort()
if li[-1]>=li[0]+li[1]:
  sum=(li[0]+li[1])*2-1
else:
  sum=a+b+c
print(sum)

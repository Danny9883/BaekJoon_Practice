n,l=map(int,input().split())
l=str(l)
count=0
num=1
while count<n:
  num=str(num)
  if l in num:
    num=int(num)
    num+=1
  else:
    count+=1
    num=int(num)
    num+=1
print(num-1)
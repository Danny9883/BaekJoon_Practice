count=0
t=int(input())
i=666
while count<t:
  i=str(i)
  if '666' in i:
    i=int(i)
    count+=1
    i+=1
  else:
    i=int(i)
    i+=1
print(i-1)
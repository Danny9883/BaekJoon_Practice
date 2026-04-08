t=int(input())
fac=1
for i in range(1,t+1):
  fac=fac*i
fac=str(fac)
fac=list(fac)
count=0
for i in fac[::-1]:
  if i=='0':
    count+=1
  else:
    break
print(count)
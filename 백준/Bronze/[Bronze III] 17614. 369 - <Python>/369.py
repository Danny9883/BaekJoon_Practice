t=int(input())

count=0
for i in range(1,t+1):
  i=str(i)
  count += i.count('3') + i.count('6') + i.count('9') 

print(count)
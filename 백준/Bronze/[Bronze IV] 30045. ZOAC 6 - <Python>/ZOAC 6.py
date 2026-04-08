t=int(input())
count=0
for i in range(t):
  a=input()
  if 'OI' in a :
    count+=1
  elif "01" in a:
    count+=1
print(count)
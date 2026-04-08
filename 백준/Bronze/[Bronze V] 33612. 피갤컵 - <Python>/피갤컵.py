y=24289
n=int(input())
y+=n*7
if y%12==0:
  print((y//12)-1,12)
else:
  print(y//12,y%12)

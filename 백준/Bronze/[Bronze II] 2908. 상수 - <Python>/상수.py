a,b=input().split()
a=list(a)
b=list(b)
a2=100*int(a[-1])+10*int(a[-2])+int(a[-3])
b2=100*int(b[-1])+10*int(b[-2])+int(b[-3])
if a2>b2:
  print(a2)
else:
  print(b2)

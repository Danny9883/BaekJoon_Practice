x,y=map(int,input().split())
x1,y1=map(int,input().split())
b=y*y1
a=x*y1+y*x1
bb=b
aa=a
if a<b:
  while b%a!=0:
    c=b%a
    b=a
    a=c
  print(aa//a,bb//a)
elif a>b:
  while a%b!=0:
      c=a%b
      a=b
      b=c
  print(aa//b,bb//b)
else:
   print(1,1)
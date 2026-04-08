a=int(input())
x=int(input())
x*=21
b=int(input())
y=int(input())
y*=21
t=int(input())

if t >=30 :
  t2=t-30
  ans1=a+x*t2
else:
  ans1=a

if t >=45 :
  t2=t-45
  ans2=b+y*t2
else:
  ans2=b

print(ans1,ans2)

a,b = input().split()
a2=a
b2=b
a=a.replace('5','6')
b=b.replace('5','6')
a=int(a)
b=int(b)

a2=a2.replace('6','5')
b2=b2.replace('6','5')
a2=int(a2)
b2=int(b2)

max=a+b
min=a2+b2
print(min,max)
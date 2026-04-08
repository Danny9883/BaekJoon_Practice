l=list(input())
ls=l.index('*')
l[ls]=0
a1=int(l[0])
a2=int(l[1])*3
a3=int(l[2])
a4=int(l[3])*3
a5=int(l[4])
a6=int(l[5])*3
a7=int(l[6])
a8=int(l[7])*3
a9=int(l[8])
a10=int(l[9])*3
a11=int(l[10])
a12=int(l[11])*3
a13=int(l[12])
sum=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13
if ls%2==0:
    test=sum%10
    t=10-test
    if t==10:
        t=0
    else:
        t=t
else:
    test=sum*3
    t=test%10
    
print(t)
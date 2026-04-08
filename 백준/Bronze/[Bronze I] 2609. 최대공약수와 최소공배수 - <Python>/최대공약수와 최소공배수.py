a,b=map(int,input().split())
c=a*b
if a==b:
    mnm=a
    mxm=a
elif a>b:
    while True:
        if a%b==0:
            mnm=b
            break
        else:
            n=a%b
            a=b
            b=n
else:
    while True:
        if b%a==0:
            mnm=a
            break
        else:
            n=b%a
            b=a
            a=n

mxm=int(c/mnm)
print(mnm)
print(mxm)
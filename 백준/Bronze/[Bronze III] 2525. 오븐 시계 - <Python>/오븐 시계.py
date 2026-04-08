h,m=map(int,input().split())
t=int(input())
m+=t
if m>=60:
    mt=m%60
    mh=m//60
    h+=mh
    m=mt
    if h>=24:
        h-=24
    print(h,m)
else:
    print(h,m)
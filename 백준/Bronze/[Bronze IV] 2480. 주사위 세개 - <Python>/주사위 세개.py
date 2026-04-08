a,b,c=map(int,input().split())
if a==b==c:
    m=10000+a*1000
    print(m)
elif a==b or b==c:
    m=1000+b*100
    print(m)
elif a==c:
    m=1000+a*100
    print(m)
else:
    if a > b and b > c:
        m=a*100
        print(m)
    elif b > a and a > c:
        m=b*100
        print(m)
    elif c > a and a > b:
        m=c*100
        print(m)
    elif a > b and b < c:
        if a > c :
            m=a*100
            print(m)
        else:
            m=c*100
            print(m)
    elif b > a and a < c:
        if b > c:
            m=b*100
            print(m)
        else:
            m=c*100
            print(m)


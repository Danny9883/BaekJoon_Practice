a,b,c=map(int,input().split())
if a==b==c:
    print(a)
elif a==b or a==c:
    print(a)
elif b==c:
    print(b)
elif a > b and a > c:
    if b>c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a>c:
        print(a)
    else:
        print(c)
elif c > a and c > b:
    if a>b:
        print(a)
    else:
        print(b)
    
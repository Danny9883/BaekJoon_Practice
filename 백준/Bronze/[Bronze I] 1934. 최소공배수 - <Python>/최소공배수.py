t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    aa=a
    bb=b
    if a<b:
        while b%a!=0:
            c=b%a
            b=a
            a=c
        print(int(aa*bb/a))
    elif a>b:
        while a%b!=0:
            c=a%b
            a=b
            b=c
        print(int(aa*bb/b))
    else:
        print(a)
        

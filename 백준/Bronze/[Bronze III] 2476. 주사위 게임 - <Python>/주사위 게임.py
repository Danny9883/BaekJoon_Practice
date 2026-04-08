t=int(input())
list=[]
for i in range(t):
    a,b,c=map(int,input().split())
    if a==b==c:
        m=a*1000+10000
    elif a==b or a==c:
        m=a*100+1000
    elif b==c:
        m=b*100+1000   
    elif a>b and a>c:
        m=a*100
    elif b>a and b>c:
        m=b*100
    elif c>a and c>b:
        m=c*100
    list.append(m)
m2=0
for k in list:
    if m2<k:
        m2=k
print(m2)

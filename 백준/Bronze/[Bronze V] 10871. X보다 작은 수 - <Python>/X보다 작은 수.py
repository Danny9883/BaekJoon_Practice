a,b=map(int,input().split())
l=list(map(int,input().split()))
l2=[]
for i in l:
    if i<b:
        l2.append(i)
for j in l2:
    print(j,end=' ')

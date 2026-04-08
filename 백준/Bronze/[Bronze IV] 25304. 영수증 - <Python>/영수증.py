m=int(input())
n=int(input())
m2=0
for i in range(n):
    cost,ex=map(int,input().split())
    m2+=(cost*ex)
if m==m2: 
    print("Yes")
else:
    print('No')

t=int(input())
s=list(map(int,input().split()))
count=0
for i in s:
    n=2
    if i>=2:
        while n<=i:
            if n==i:
                count+=1
                break
            elif i%n==0:
                break
            elif i%n!=0:
                n+=1
    else:
        pass
print(count)
n=int(input())
size=list(map(int,input().split()))
t,p=map(int,input().split())
t2=0
for i in size:
  if i!=0:
    if t>=i:
      t2+=1
    else:
      if i%t==0:
        t2+=(i//t)
      else:
        t2+=(i//t)+1
print(t2)
print(n//p,n%p)

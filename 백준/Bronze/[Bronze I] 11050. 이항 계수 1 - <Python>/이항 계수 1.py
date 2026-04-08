n,k=map(int,input().split())
t=n-k
nf=1
kf=1
tf=1
for i in range(1,n+1):
  nf*=i
for i in range(1,k+1):
  kf*=i
for i in range(1,t+1):
  tf*=i
p=kf*tf
print(int(nf/p))
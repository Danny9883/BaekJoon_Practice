n=int(input())

for _ in range(n):
  ans=0
  a=list(map(int,input().split()))
  ans+=sum(a)
  print(ans)
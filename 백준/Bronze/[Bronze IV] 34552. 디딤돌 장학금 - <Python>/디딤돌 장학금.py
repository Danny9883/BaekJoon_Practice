li=list(map(int,input().split()))
n=int(input())
money=0
for i in range(n):
  a,b,c=map(float,input().split())
  a=int(a)
  c=int(c)
  if c>=17 and b>=2.00:
    money+=li[a]
print(money)
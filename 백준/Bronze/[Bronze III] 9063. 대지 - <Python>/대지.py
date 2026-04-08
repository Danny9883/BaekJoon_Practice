t=int(input())
lix=[]
liy=[]
for i in range(t):
  x,y=map(int,input().split())
  lix.append(x)
  liy.append(y)
lix.sort()
liy.sort()
a=lix[-1]-lix[0]
b=liy[-1]-liy[0]
print(a*b)
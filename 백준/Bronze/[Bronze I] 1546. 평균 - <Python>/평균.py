t=int(input())
s=list(map(int,input().split()))
max=0
for i in s:
  if max<i:
    max=i
s2=[]
for i in s:
  a=i/max*100
  s2.append(a)
sum=0
for i in s2:
  sum+=i
an=sum/len(s2)
print(an)
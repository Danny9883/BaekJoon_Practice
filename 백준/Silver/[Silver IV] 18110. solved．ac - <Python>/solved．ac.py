import sys
input=sys.stdin.readline

t=int(input())
li=[]
for i in range(t):
  a=int(input())
  li.append(a)
li.sort()
cut=int((t*0.15)+0.5)
if t==0:
  print(0)
else:
  if cut==0:
    b=t-(2*cut)
    li_sum=sum(li)
    li_sum=int((li_sum/b)+0.5)
    print(li_sum)
  else:
    b=t-(2*cut)
    li_sum=sum(li[cut:(-cut)])
    li_sum=int((li_sum/b)+0.5)
    print(li_sum)
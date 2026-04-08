import sys
input = sys.stdin.readline

t=int(input())
for i in range(t):
  dic={}
  t2=int(input())
  for j in range(t2):
    a,b=input().split()
    if b in dic:
      dic[b]+=1
    else:
      dic[b]=1
  ans=1
  for k in dic:
    ans*=((dic[k])+1)
  print(ans-1)








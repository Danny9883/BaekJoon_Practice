import sys
input=sys.stdin.readline



m=int(input())

five=0
two=0
maxf=m//5
ans=-1
while maxf>=0:
  if (m-(maxf*5))%2==0:
    five=maxf
    two = (m-(maxf*5))//2
    ans=five+two
    break
  else:
    maxf-=1

print(ans)

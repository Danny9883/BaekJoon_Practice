import sys
input=sys.stdin.readline
n=int(input())
a=list(input().split())
card={}
for i in a:
  if i in card:
    card[i]+=1
  else:
    card[i]=1
n2=int(input())
a2=list(input().split())
re=[]
for i in a2:
  if i in card:
    re.append(str(card[i]))
  else:
    re.append('0')
print(' '.join(re))
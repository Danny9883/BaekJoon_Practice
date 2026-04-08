import sys
input=sys.stdin.readline


t=input().rstrip('\n')
bomb=input().rstrip('\n')
blen=len(bomb)
k=bomb[-1]
stack=[]

for i in t:
  stack.append(i)
  if len(stack)>=blen and ''.join(stack[-blen:]) == bomb:
    del stack[-blen:]



if len(stack)==0:
  print("FRULA")
else:
  print(''.join(stack))



      



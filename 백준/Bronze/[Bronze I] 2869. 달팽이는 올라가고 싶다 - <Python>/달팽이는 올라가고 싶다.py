a,b,v=map(int,input().split())
move=a-b
if (v-b)%move==0:
  print((v-b)//move)
else:
  print(((v-b)//move)+1)
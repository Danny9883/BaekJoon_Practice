t=int(input())
li=[]
for i in range(t):
  x,y=map(int,input().split())
  li.append([y,x])
li.sort()
for i in range(len(li)):
  print(li[i][1],li[i][0])
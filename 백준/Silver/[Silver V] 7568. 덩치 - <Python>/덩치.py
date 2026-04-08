t=int(input())
li=[]
linum=[]
for i in range(t):
  h,w = map(int,input().split())
  li.append([h,w])

for i in range(len(li)):
  num=1
  for j in range(len(li)):
    if li[i][0] < li[j][0] and  li[i][1] < li[j][1]:
      num+=1
  linum.append(num)

for i in linum:
  print(i,end=' ')
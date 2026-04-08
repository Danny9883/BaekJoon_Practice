import sys
input=sys.stdin.readline

n,m=map(int,input().split())
li=[0]
li2=list(map(int,input().split()))
for i in range(n):
  li.append(li[i]+li2[i])

for i in range(m):
  s,f=map(int,input().split())
  print(li[f]-li[s-1])


  
      


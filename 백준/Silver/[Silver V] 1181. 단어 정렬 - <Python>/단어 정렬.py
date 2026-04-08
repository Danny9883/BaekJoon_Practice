li={}
t=int(input())
for i in range(t):
  a=input()
  li[a]=len(a)
li2=sorted(li.items())
li2=dict(li2)
li2=dict(sorted(li2.items(),key=lambda x:x[1]))
for i in li2:
  print(i)
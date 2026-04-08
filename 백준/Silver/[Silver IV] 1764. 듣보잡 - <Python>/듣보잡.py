a,b=map(int,input().split())
li=set()
li2=set()
for i in range(a):
  h=input()
  li.add(h)
for i in range(b):
  h=input()
  li2.add(h)
li3=li&li2
li3=sorted(li3)
print(len(li3))
for i in li3:
  print(i)
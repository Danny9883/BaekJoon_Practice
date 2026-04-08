import sys
input=sys.stdin.readline

t=int(input())
li=set()
for i in range(t):
  a=list(input().split())
  if len(a) == 2:
    a[1]=int(a[1])
  if a[0] == 'add':
    li.add(a[1])
  elif a[0] == 'remove':
    try:
      li.remove(a[1])
    except:
      pass
  elif a[0] == 'check':
    if a[1] in li:
      print(1)
    else:
      print(0)
  elif a[0] == 'toggle':
    if a[1] in li:
      li.remove(a[1])
    else:
      li.add(a[1])
  elif a[0] == 'all':
    li=set(range(1,21))
  elif a[0] == 'empty':
    li=set()
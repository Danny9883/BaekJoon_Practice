while True:
  a,b,c=map(int,input().split())
  if a==b==c==0:
    break
  elif a==b==c:
    print('Equilateral')
  else:
    li=[]
    li.append(a)
    li.append(b)
    li.append(c)
    li.sort()
    if li[-1]>=li[0]+li[1]:
      print('Invalid')
    elif a==b or a==c or b==c:
      print('Isosceles')
    else:
      print('Scalene')
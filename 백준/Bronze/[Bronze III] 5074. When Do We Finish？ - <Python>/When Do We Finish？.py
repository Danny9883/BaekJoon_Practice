while 1:
  a,b=input().split()
  a=a.split(':')
  b=b.split(':')
  h1=int(a[0])
  h2=int(b[0])
  m1=int(a[1])
  m2=int(b[1])
  h=h1+h2
  m=m1+m2
  if h==0 and m==0:
    break
  n=0
  if m>=60:
    m-=60
    h+=1
  if h>=24:
    n=h//24
    h=h%24
  if h<10:
    h=str(h)
    h="0"+h
  if m<10:
    m=str(m)
    m="0"+m
  if n>=1:
    print(f'{h}:{m} +{n}')
  else:
    print(f'{h}:{m}')
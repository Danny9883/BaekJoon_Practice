while True:
  n=int(input())
  li=[]
  li2=[]
  if n==-1:
    break
  else:
    for i in range(1,n):
      if n%i==0:
        li.append(i)
        li2.append(i)
        li2.append('+')
        sum=0
    li2.pop()
    li3=''
    for p in li2:
      li3+=str(p)+' '
    for j in li:
      sum+=j
    if n==sum:
      print(f'{n} = {li3}')
    else:
      print(f'{n} is NOT perfect.')

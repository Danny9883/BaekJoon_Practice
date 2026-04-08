n=int(input())
start=1
while start<=n:
  test=str(start)
  textli=[]
  for i in range(len(test)):
    textli.append(test[i])
  test=int(test)
  for i in textli:
    i=int(i)
    test+=i
  if test==n:
    break
  else:
    start+=1
if test==n:
  print(start)
else:
  print(0)
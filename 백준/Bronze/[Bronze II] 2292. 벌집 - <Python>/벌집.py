n=int(input())
i=1
room=1
while 1:
  if n<=room:
    print(i)
    break
  room+=i*6
  i+=1
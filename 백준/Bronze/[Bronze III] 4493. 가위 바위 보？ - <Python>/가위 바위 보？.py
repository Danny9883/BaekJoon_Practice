t=int(input())
for i in range(t):

  n=int(input())
  p1c=0
  p2c=0
  for j in range(n):
    p1,p2 = input().split()
    if p1 == 'R' and p2 =='P':
      p2c+=1
    elif p1 == 'R' and p2 =='S':
      p1c+=1
    elif p1 == 'P' and p2 =='R':
      p1c+=1
    elif p1 == 'P' and p2 =='S':
      p2c+=1
    elif p1 == 'S' and p2 =='P':
      p1c+=1
    elif p1 == 'S' and p2 =='R':
      p2c+=1
  if p1c > p2c :
    print('Player 1')
  elif p1c < p2c :
    print('Player 2')
  else:
    print("TIE")

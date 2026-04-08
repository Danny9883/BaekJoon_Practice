case=1
while 1:
  num=0
  fact=1
  t=int(input())
  if t == 0 :
    break
  
  
  while 1:
    num+=t//5
    num+=t//25
    num+=t//125
    num+=t//625
    num+=t//3125
    num+=t//15625
    num+=t//78125
    num+=t//390625
    num+=t//1953125

    print(f'Case #{case}: {num}')
    case+=1
    break

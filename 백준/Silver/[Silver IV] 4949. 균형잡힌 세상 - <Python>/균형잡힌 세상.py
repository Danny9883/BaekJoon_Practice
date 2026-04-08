while 1:
  t=list(input())
  testli=[]
  if t[0]=='.':
    break
  for i in t:
    if i=='(':
      testli.append(i)
    elif i=='[':
      testli.append(i)
    elif i==')':
      if len(testli) == 0:
        testli.append(i)
        break
      elif testli[-1] =='(':
        testli.pop()
      else:
          testli.append(i)
          break
    elif i==']':
        if len(testli) == 0:
          testli.append(i)
          break
        elif testli[-1] =='[':
          testli.pop()
        else:
          testli.append(i)
          break
    
  if len(testli) == 0:
    print('yes')
  else:
    print('no')

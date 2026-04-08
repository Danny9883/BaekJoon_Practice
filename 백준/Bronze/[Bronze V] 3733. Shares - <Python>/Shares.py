while True:
  try:
    t,p=map(int,input().split())
    t+=1
    print(p//t)
  except EOFError:
    break

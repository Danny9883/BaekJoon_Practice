import sys
input=sys.stdin.readline

while 1:
  try:
    t=int(input())
    count='1'
    while 1:
      count=int(count)
      if count%t!=0:
        count=str(count)
        count+='1'
      else:
        count=str(count)
        print(len(count))
        break
  except:
    break
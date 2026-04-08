import sys
input=sys.stdin.readline

mapli=[]
maxcol=0
for i in range(5):
  row=list(input().rstrip('\n'))
  mapli.append(row)
  maxcol = max(maxcol,len(row))


for col in range(maxcol):
  for row in range(5):
    try:
      print(mapli[row][col],end='')
    except:
      pass


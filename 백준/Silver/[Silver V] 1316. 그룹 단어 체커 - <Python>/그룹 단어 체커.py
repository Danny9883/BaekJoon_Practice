import sys
input=sys.stdin.readline

t=int(input())
count=0
for k in range(t):
  text=list(input().rstrip('\n'))
  visit=set()
  for i in range(len(text)):
    if text[i] not in visit:
      visit.add(text[i])
    elif text[i] in visit:
      if text[i]!=text[i-1]:
        break
    if i==len(text)-1:
      count+=1
  
print(count)

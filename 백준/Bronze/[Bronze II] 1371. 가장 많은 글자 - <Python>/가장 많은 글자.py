import sys
text=[]
enli={}
for i in range(97,123):
  enli[chr(i)]=0
for t in sys.stdin.read():
  for a in t:
    if a=='':
      break
    elif a==' ' or a=='\n':
      pass
    else:
      text.append(a)

for i in text:
  enli[i]+=1
mxm=max(enli.values())
for i in enli:
  if enli[i]==mxm:
    print(i,end='')

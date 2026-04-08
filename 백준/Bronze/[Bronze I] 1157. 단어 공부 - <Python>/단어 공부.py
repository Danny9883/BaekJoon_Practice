import sys
input=sys.stdin.readline

dic={}
for i in range(65,91):
  dic[chr(i)]=0

text = list((input().rstrip('\n')).upper())
for i in text:
  dic[i] += 1

maxinum = max(dic.values())

dicchk = [k for k,v in dic.items() if v==maxinum]
if len(dicchk)==1:
  print(dicchk[0])
else:
  print('?')
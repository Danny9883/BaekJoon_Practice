import sys
input=sys.stdin.readline

dic={}
aa=10
for i in range(65,91):
  dic[aa] = chr(i)
  aa+=1
for i in range(0,10):
  dic[i]=str(i)


num,t=(input().rstrip('\n')).split()
num=int(num)
t=int(t)

ans=''
while 1:
  if num//t == 0 and num%t==0:
    break
  a = num%t
  ans+= dic[a]
  num=num//t

print(ans[::-1])

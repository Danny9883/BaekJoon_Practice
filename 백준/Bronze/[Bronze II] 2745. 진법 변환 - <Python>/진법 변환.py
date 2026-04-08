import sys
input=sys.stdin.readline

dic={}
a=10
for i in range(65,91):
  dic[chr(i)] = a
  a+=1
for i in range(0,10):
  dic[str(i)]=i


num,t=(input().rstrip('\n')).split()
t=int(t)

ans=0
for i in range(len(num)):
  a = num[-1-i]
  count=t**i
  ans+=dic[a]*count

print(ans)

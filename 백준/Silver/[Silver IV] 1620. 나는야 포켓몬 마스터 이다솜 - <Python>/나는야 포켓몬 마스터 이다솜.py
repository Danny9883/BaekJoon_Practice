import sys
input = sys.stdin.readline

n,t=map(int,input().split())
dic={}
dic2={}
for i in range(1,n+1):
  name=input().rstrip()
  dic[i] = name
  dic2[name] = i

for i in range(t):
  test=input().rstrip()
  try:
    test=int(test)
  except ValueError:
    print(dic2[test])
  else:
    test=int(test)
    print(dic[test])
    

  
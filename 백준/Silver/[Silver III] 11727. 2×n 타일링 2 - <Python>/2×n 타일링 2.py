import sys
input = sys.stdin.readline

li=[1,3]
n=int(input())
if n < 3:
  print((2**n)-1)
else:
  for i in range(3,n+1):
    num=(2**i)-li[-1]
    li.append(num)
  
  print(li[-1]%10007)





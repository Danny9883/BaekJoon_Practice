import sys
input = sys.stdin.readline

li=[1,2]
n=int(input())
if n < 3:
  print(n)
else:
  for i in range(2,n):
    num=li[i-1]+li[i-2]
    li.append(num)
  
  print(li[-1]%10007)
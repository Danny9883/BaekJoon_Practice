import sys
input=sys.stdin.readline



n = int(input())

a , b = map(int,input().split())
x = [a]
y = [b]
for _ in range(n-1):
  a1 , b1 = map(int,input().split())
  x.append(a1)
  y.append(b1)

x.append(a)
y.append(b)

sum1 = 0
sum2 = 0

for i in range(n):
  sum1 += x[i]*y[i+1]
  sum2 += x[i+1]*y[i]

sum0 = abs(sum1-sum2)/2

print(f"{sum0:.1f}")







 

  



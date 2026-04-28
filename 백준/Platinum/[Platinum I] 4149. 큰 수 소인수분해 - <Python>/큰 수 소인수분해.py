import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
import random


ans=[]

def is_prime(n):
  if n < 2 :
    return False
  if n==2 or n==3 :
    return True
  if n % 2 == 0 :
    return False
  
  d = n - 1
  s = 0
  while d % 2 == 0:
    d //= 2
    s += 1

  for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
    if n <= a:
      break
    if not miller(n,a,d,s):
      return False
  return True

def miller(n,a,d,s):
  x = pow(a,d,n)
  if x==1 or x==n-1:
    return True
  for _ in range(s-1):
    x = pow(x,2,n)
    if x==n-1:
      return True
  return False


def gcd(a,b):
  while b:
    a, b = b, a%b
  return a

def pollard(n):
  if n%2==0:
    return 2
  if is_prime(n):
    return n
  
  x = random.randrange(2,n)
  c = random.randrange(1,n)
  y=x
  d=1

  while d==1:
    x = (pow(x,2,n)+c ) % n
    y = (pow(y,2,n)+c ) % n
    y = (pow(y,2,n)+c ) % n
    d = gcd(abs(x-y), n)
    if d==n:
      return pollard(n)
  return d

def find(n):
  if n==1:
    return 1
  if is_prime(n):
    ans.append(n)
    return
  
  d = pollard(n)
  find(d)
  find(n//d)



n = int(input())

find(n)
ans.sort()

for i in ans:
  print(i)




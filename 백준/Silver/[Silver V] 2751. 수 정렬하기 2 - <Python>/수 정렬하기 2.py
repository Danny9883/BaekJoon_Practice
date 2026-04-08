import sys

input=sys.stdin.readline
t=int(input())
l=[]
for i in range(t):
  a=int(input())
  l.append(a)
l.sort()
sys.stdout.write(''.join(str(i)+ '\n' for i in l))
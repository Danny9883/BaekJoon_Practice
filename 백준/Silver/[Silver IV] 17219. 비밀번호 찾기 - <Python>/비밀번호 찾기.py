import sys
input=sys.stdin.readline

n,k=map(int,(input().rstrip("\n")).split())
dic={}
for i in range(n):
  a,b=input().split()
  dic[a]=b
for i in range(k):
  a=input().rstrip("\n")
  print(dic[a])
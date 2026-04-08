n=int(input())
li=list(map(int,input().split()))
n2=int(input())
li2=list(map(int,input().split()))
li.sort()

def ff(i,li):
  start=0
  last=len(li)-1
  while start<=last:
    mid=(start+last)//2
    if i==li[mid]:
      return print(1)
    elif i<li[mid]:
      last=mid-1
    elif i>li[mid]:
      start=mid+1
  return print(0)

for i in li2:
  ff(i,li)
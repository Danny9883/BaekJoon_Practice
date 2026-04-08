x,y,w,h=map(int,input().split())
a=w-x
b=h-y
li=[a,b,x,y]
li.sort()
print(li[0])
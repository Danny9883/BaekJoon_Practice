import sys
input=sys.stdin.readline
stack=[]
t=int(input())
for i in range(t):
    a=list(input().split())
    if a[0]=='push':
        stack.append(int(a[1]))
    elif a[0]=='pop':
        if len(stack)==0:      
            print(-1)
        else:
            print(stack[0])
            stack.pop(0)      
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='back':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif a[0]=='front':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[0])
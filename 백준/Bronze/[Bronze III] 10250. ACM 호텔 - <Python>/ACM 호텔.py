t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    if h*w==n:
        room=h*100+w
        print(room)
    else:
        if n%h==0:
            f=h
            num=n//h
            room=f*100+num
            print(room)
        else:
            f=n%h
            num=n//h+1
            room=f*100+num
            print(room)


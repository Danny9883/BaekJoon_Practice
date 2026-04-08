t=int(input())
for i in range(t):
    d,s=input().split()
    d=int(d)
    text=('')
    for i in list (s):
        text+=i*d
    print(text)
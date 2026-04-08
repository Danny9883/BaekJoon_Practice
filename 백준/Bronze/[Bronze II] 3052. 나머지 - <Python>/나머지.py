l=[]
for i in range(10):
    a=int(input())
    a=a%42
    if a in l:
        pass
    else:
        l.append(a)
print(len(l))
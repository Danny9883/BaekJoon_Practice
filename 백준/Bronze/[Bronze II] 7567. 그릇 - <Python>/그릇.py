line=list(input())
s=int(len(line))      
h=10
n=1
for i in line:
    if line[n]==i:
        h+=5
        n+=1
        if n==s:
            break
            
    else:
        h+=10
        n+=1
        if n==s:
            break
print(h)

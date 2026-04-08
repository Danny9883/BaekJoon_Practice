t=int(input())
s=input()
s=list(s)
sum=0
bonus=0
n=1
for i in s:
    if i =='O':
        sum+=n
        sum+=bonus
        bonus+=1
        n+=1
    else:
        bonus=0
        n+=1
print(sum)
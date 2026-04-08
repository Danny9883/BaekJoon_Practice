t=int(input())
for i in range(t):
    sum=0
    s=list(input())
    bonus=0
    for j in s:
        if j == 'O':
            bonus+=1
            sum+=bonus
        if j == "X":
            bonus=0
    print(sum)
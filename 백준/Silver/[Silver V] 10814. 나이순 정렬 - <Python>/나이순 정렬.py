t=int(input())
li=[]
for i in range(t):
    age,name=input().split()
    age=int(age)
    li.append([age,name])
li2=sorted(li, key=(lambda x:int(x[0])))
for i in li2:
    print(int(i[0]),i[1])
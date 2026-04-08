mxm=0
count=1
for i in range(1,10):
    num=int(input())
    if num>mxm:
        mxm=num
        count=i
print(mxm)
print(count)
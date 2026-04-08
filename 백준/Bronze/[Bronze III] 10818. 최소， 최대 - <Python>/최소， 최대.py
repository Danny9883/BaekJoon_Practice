t=int(input())
num=list((input()).split())
mxm=-100000000
mnm=100000000
for i in num:
    i=int(i)
    if i>mxm:
        mxm=i
    if mnm>i:
        mnm=i

        
        
print(mnm,mxm)

      
    
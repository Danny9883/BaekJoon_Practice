n,k=map(int,input().split())
k2=k-1
li=list(range(1,n+1))
yo=[]
while len(li)>0:
    yo.append(li[k2])
    li.remove(li[k2])
    k2+=k-1
    if len(li)==0:
      break
    elif k2>=len(li):
      k2=k2%len(li)

te=''
for i in range(0,(len(yo)-1)):
  te+=str(yo[i])+', '
te+=str(yo[-1])
print(f'<{te}>')

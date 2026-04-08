mem=[]
for i in range(1,6):
  li=list(map(int,input().split()))
  sumli=sum(li)
  mem.append([sumli,i])
mem.sort()
print(mem[-1][1],mem[-1][0])

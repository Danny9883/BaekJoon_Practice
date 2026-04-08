n,k=map(int,input().split())
c_list=[]
count=0
for i in range(n):
  coin=int(input())
  c_list.append(coin)
c_list.sort(reverse=True)
for i in c_list:
  count+=k//i
  k=k%i
print(count)
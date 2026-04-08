li=[]
for i in range(10):
  a=int(input())
  li.append(a)

li_sum=sum(li)
print(li_sum//10)
dic={}
for i in li:
  if i in dic:
    dic[i] +=1
  else:
    dic[i] = 1
aa=max(dic.values())
for key, val in dic.items():
  if val == aa:
    print(key)
dic={'ABC':3,
     'DEF':4,
     'GHI':5,
     'JKL':6,
     'MNO':7,
     'PQRS':8,
     'TUV':9,
     'WXYZ':10}
s=list(input())
sum=0
for i in s:
  for j in dic.keys():
    if i in j:
      sum+=dic[j]
print(sum)
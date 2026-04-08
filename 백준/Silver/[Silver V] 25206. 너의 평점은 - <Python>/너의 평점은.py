dic={'A+':4.5,
     'A0':4.0,
     'B+':3.5,
     'B0':3.0,
     'C+':2.5,
     'C0':2.0,
     'D+':1.5,
     'D0':1.0,
     'F':0.0}
sum=0
score=0
for i in range(20):
  name,sc,g=input().split()
  sc=float(sc)
  if g=='P':
    pass
  else:
    for j in dic.keys():
      if g==j:
        gc=dic[j]
        to=gc*sc
        score+=to
        sum+=sc
print(score/sum)
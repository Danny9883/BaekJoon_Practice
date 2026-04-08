t=int(input())
alp= list(range(65,91))

for i in range(1,t+1):

  ansli=[0] * 26

  text=input().upper()
  for j in text:
    if ord(j) in alp:
      ansli[ord(j)-65] +=1

  ans=min(ansli)

  if ans==0:
    print(f"Case {i}: Not a pangram")
  elif ans==1:
    print(f"Case {i}: Pangram!")
  elif ans==2:
    print(f"Case {i}: Double pangram!!")
  elif ans>=3:
    print(f"Case {i}: Triple pangram!!!")
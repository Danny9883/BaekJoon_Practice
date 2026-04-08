hash={}
for i in range(97,123):
  hash[chr(i)]=i-96
t=int(input())
text=input()
ans=0
for i in range(len(text)):
  ans+=hash[text[i]]*(31**i)
print(ans%1234567891)
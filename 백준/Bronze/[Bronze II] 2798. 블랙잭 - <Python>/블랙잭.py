t,blackjack=map(int,input().split())
card=list(map(int,input().split()))
card.sort(reverse='1')
s=[]
for i in range(len(card)):
  for j in range(i+1,len(card)):
    for k in range(j+1,len(card)):
      ans=card[i]+card[j]+card[k]
      if ans <= blackjack:
        s.append(ans)
        break       
print(max(s))


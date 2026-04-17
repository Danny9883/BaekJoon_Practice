import sys
input=sys.stdin.readline



n=int(input())

isprime=[True for _ in range(n+1)]
isprime[1] = False


for i in range(2,int(n**0.5)+1):
  if isprime[i] == False:
    continue
  for j in range(i*2,n+1,i):
    isprime[j] = False

prime = []

for i in range(2,n+1):
  if isprime[i]:
    prime.append(i)


cnt = 0 
left = 0
right = 1
while left < right:
  if right==len(prime)+1:
    break
  if sum(prime[left:right]) > n:
    left += 1
  elif sum(prime[left:right]) < n:
    right += 1
  elif sum(prime[left:right])==n:
    cnt += 1
    left += 1
    right += 1
    


print(cnt)








 

  



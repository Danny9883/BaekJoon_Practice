import sys
input=sys.stdin.readline


n = int(input())
li = list(map(int,input().split()))
li = set(li)
m = max(li)
score = [0 for _ in range(m+1)]
for i in li:
  for j in range(i*2,m+1,i):
    if j in li:
      score[i] += 1
      score[j] -= 1

for i in li:
  print(score[i],end=' ')



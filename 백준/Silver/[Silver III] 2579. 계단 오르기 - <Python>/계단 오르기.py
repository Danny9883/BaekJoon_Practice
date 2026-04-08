from collections import deque
import sys
input=sys.stdin.readline

t=int(input())
li=[0]
for i in range(t):
  a=int(input())
  li.append(a)


def find(t):
  hi=[]
  for _ in range(t+1):
    a=[-1,-1]
    hi.append(a)
  maxscore=0
  que=deque()
  que.append((0,0,-1))
  while que:
    v,score,count=que.popleft()
    if v > t :
      continue
    score += li[v]
    ans = score
    if hi[v][count] < ans:
      hi[v][count]=ans
    else:
      continue
    if v == t:
      if score > maxscore:
        maxscore=score
      continue
    if count <= 0:
      if v+1 > t:
        continue
      elif v+1 ==t:
        que.append((v+1,ans,count+1))
      else:
        que.append((v+1,ans,count+1))
        que.append((v+2,ans,0))
    if count == 1:
      if v+2>t:
        continue
      else:
        que.append((v+2,ans,0))
  return maxscore


print(find(t))

  
      


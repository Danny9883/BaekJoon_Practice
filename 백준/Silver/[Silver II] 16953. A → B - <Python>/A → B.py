from collections import deque
import sys
input=sys.stdin.readline

a,b=map(int,input().split())

def find(a,b,count):
  que=deque()
  visit=set()
  que.append((a,b,count))
  while que:
    a,b,count=que.popleft()
    if a==b:
      return count
    elif a>b:
      continue
    else:
      if a*2 not in visit:
        que.append((a*2,b,count+1))
        visit.add(a*2)
      if (a*10)+1 not in visit:
        que.append(((a*10)+1,b,count+1))
        visit.add((a*10)+1)
  return -1

print(find(a,b,1))
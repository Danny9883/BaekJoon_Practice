import sys
input=sys.stdin.readline
from collections import deque


f=int(input())


def find(start,fin):
  dic={}
  visit=set()
  que = deque()
  que.append((start,[]))
  dic[start]=0
  while que:
    v,li = que.popleft()
    li.append(v)
    if v not in visit:
      visit.add(v)
      if v == fin:
        print(dic[v])
        for _ in range(len(li)):
          print(li.pop(),end=' ')
        break
      else:
        if v*3 not in visit and v*3 <= 1000000:
          try:
            if dic[v*3] > 0:
              pass
          except:
            que.append(((v*3),li[:]))
            dic[v*3] = dic[v] + 1
        if v*2 not in visit and v*2 <= 1000000:
          try:
            if dic[v*2] > 0:
              pass
          except:
            que.append(((v*2),li[:]))
            dic[v*2] = dic[v] + 1
        if v+1 not in visit:
          try:
            if dic[v+1] > 0:
              pass
          except:
            que.append(((v+1),li[:]))
            dic[v+1] = dic[v] + 1

find(1,f)







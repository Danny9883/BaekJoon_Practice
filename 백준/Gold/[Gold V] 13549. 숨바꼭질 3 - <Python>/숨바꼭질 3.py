import sys
from collections import deque
input=sys.stdin.readline


s,f=map(int,input().split())


def find(start,fin):
  dic={}
  visit=set()
  que = deque()
  que.append(start)
  dic[start]=0
  while que:
    v = que.popleft()
    if v not in visit:
      visit.add(v)
      if v == fin:
        print(dic[v])
        break
      else:
        if v*2 not in visit and v*2 <= 100000:
          try:
            if dic[v*2] > 0:
              pass
          except:
            que.append(v*2)
            dic[v*2] = dic[v]
        if v-1 not in visit:
          try:
            if dic[v-1] > 0:
              pass
          except:
            que.append(v-1)
            dic[v-1] = dic[v] + 1
        if v+1 not in visit:
          try:
            if dic[v+1] > 0:
              pass
          except:
            que.append(v+1)
            dic[v+1] = dic[v] + 1

find(s,f)
  
      



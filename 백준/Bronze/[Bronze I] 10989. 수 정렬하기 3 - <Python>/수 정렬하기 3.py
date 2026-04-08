from collections import Counter
import sys
input = sys.stdin.readline
nums={}
for i in range(1,10001):
  nums[i]=0

t=int(input())
for i in range(t):
  a=int(input())
  nums[a]+=1

num_c=Counter(nums)
fil={num: count for num, count in num_c.items() if count >0 }

for i in fil:
  try:
    for k in range(fil[i]):
      print(i)
  except KeyError:
    pass
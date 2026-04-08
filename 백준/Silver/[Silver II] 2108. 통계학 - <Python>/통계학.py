import collections
import sys
input=sys.stdin.readline

t=int(input())
li=[]
for i in range(t):
  a=int(input())
  li.append(a)
li.sort()
avg=(sum(li)/len(li))
if avg<0:
  avg=int(avg-0.5)
else:
  avg=int(avg+0.5)
mid=li[len(li)//2]
maxi=collections.Counter(li)
maxi2=[k for k,v in maxi.items() if max(maxi.values()) == v]
if len(maxi2)<=1:
  maximum=maxi2[0]
else:
  maximum=maxi2[1]
ranges=li[-1]-li[0]
print(avg)
print(mid)
print(maximum)
print(ranges)



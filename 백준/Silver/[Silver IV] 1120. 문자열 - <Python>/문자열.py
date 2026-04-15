import sys
input=sys.stdin.readline


a, b = input().rstrip('\n').split()
l = len(b)-len(a)



c = []
for i in range(l+1):
  cnt = 0
  for j in range(i,i+len(a)):
    t1 = b[j]
    t2 = a[j-i]
    if t1 != t2:
      cnt += 1
  c.append(cnt)



print(min(c))

  



import sys
input=sys.stdin.readline



v = int(input())
parent = [0] * (v)

for i in range(v):
  parent[i] = i

xli, yli, zli = [], [], []
for i in range(v):
  x,y,z = map(int,input().split())
  xli.append((x,i))
  yli.append((y,i))
  zli.append((z,i))

xli.sort()
yli.sort()
zli.sort()

e = []
for c in xli, yli, zli:
  for i in range(1, v):
    w1, a = c[i-1]
    w2, b = c[i]
    e.append((abs(w1-w2),a, b))
e.sort()

def find_parent(li, x):
  if parent[x] != x:
    parent[x] = find_parent(li,parent[x])
  return parent[x]

def union(li,a,b):
  a = find_parent(li,a)
  b = find_parent(li,b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a

def kruskal():
  ans = 0
  for cost, a, b in e:
    if find_parent(parent,a) != find_parent(parent,b):
      union(parent,a ,b)
      ans += cost
  return ans

print(kruskal())














 

  



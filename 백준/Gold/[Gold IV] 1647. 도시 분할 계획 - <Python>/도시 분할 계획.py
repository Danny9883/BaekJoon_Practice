import sys
input=sys.stdin.readline



# kruskal 알고리즘
v , e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
  parent[i] = i

li = []
ans = 0 

for _ in range(e):
  a, b, c = map(int,input().split())
  li.append((c,a,b))
  li.append((c,b,a))

li.sort()


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

maxi=0
for i in li:
  c, a, b = i
  if find_parent(li,a) != find_parent(li,b):
    union(li,a,b)
    ans += c
    if maxi<c:
      maxi=c

print(ans-maxi)

    


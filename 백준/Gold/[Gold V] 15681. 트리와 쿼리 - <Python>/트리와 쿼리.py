import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


n, r, q = map(int,input().split())
graph  = [[]for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
tree   = [[]for _ in range(n+1)]
v_count= [0 for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def makeTree(root, p):
  for c in graph[root]:
    if c != p:
      parent[c] = root
      tree[root].append(c)
      makeTree(c, root)

def count_v(root):
  v_count[root] = 1
  for c in tree[root]:
    if v_count[c] == 0:
      count_v(c)
    v_count[root] += v_count[c]

makeTree(r, -1)
count_v(r)

for _ in range(q):
  a = int(input())
  print(v_count[a])



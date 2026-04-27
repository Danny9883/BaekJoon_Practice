import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


n = int(input())

g = [[0]*8 for _ in range(8)]
g[0][1] , g[0][2] = 1,1
g[1][0] , g[1][2], g[1][3] = 1,1,1
g[2][0] , g[2][1], g[2][3], g[2][4] = 1,1,1,1
g[3][1] , g[3][2], g[3][4], g[3][5] = 1,1,1,1
g[4][2] , g[4][3], g[4][5], g[4][7] = 1,1,1,1
g[5][3] , g[5][4], g[5][6] = 1,1,1
g[6][5] , g[6][7] = 1,1
g[7][4] , g[7][6] = 1,1

def mul(a,b):
  ans = [[0]*8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      for k in range(8):
        ans[i][j] += a[i][k]*b[k][j]
      ans[i][j] %= 1000000007
  return ans

def cal(a,n):
  if n==1:
    return a
  cal2 = cal(a,n//2)
  if n%2==0:
    return mul(cal2,cal2)
  else:
    return mul(mul(cal2,cal2),a)
  
ans = cal(g,n)
print(ans[0][0])











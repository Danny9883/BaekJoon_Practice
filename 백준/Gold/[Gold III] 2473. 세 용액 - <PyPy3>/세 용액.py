import sys
input=sys.stdin.readline



n = int(input())
li = list(map(int,input().split()))
li.sort()

ans = [float('INF'), float('INF'), float('INF')]
for i in range(n):
  k = i+1
  j = n-1
  while k < j :
    if abs(li[i]+li[j]+li[k]) < abs(sum(ans)):
      ans = [li[i], li[k], li[j]]
    
    if li[i]+li[j]+li[k] > 0:
      j -= 1
    elif li[i]+li[j]+li[k] < 0:
      k += 1
    else:
      break

print(ans[0],ans[1],ans[2])









t=int(input())
for i in range(1,t):
  print(' '*(t-i-1),'*'*(2*i-1),'')
print('*'*(2*t-1),'')
for i in range(1,t):
  print(' '*((t-(t-i)-1)),'*'*(((t-i)*2)-1),'')
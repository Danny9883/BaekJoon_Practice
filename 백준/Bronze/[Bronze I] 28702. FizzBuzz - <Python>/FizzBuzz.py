a=input()
b=input()
c=input()
if a!='Fizz' and a!='Buzz' and a!='FizzBuzz':
  a=int(a)
  ans=a+3
  if ans%15==0:
    print('FizzBuzz')
  elif ans%3==0:
    print('Fizz')
  elif ans%5==0:
    print('Buzz')
  else:
    print(ans)
elif b!='Fizz' and b!='Buzz' and b!='FizzBuzz':
  b=int(b)
  ans=b+2
  if ans%15==0:
    print('FizzBuzz')
  elif ans%3==0:
    print('Fizz')
  elif ans%5==0:
    print('Buzz')
  else:
    print(ans)
elif c!='Fizz' and c!='Buzz' and c!='FizzBuzz':
  c=int(c)
  ans=c+1
  if ans%15==0:
    print('FizzBuzz')
  elif ans%3==0:
    print('Fizz')
  elif ans%5==0:
    print('Buzz')
  else:
    print(ans)

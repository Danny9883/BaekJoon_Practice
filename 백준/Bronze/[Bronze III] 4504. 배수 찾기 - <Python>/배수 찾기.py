a=int(input())
while True:
    b=int(input())
    if b==0:
        break
    if b%a==0:
        print('%d is a multiple of %d.' %(b,a))
    else:
        print('%d is NOT a multiple of %d.' %(b,a))

       
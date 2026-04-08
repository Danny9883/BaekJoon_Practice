s=input()
n=0.0
if "A" in s:
    n+=4
elif "B" in s:
    n+=3
elif "C" in s:
    n+=2
elif "D" in s:
    n+=1
if "+" in s:
    n+=0.3
elif "-" in s:
    n-=0.3
print(n)
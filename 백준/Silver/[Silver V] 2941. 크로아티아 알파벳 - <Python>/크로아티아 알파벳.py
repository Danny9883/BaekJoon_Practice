import sys
input=sys.stdin.readline

text=input().rstrip('\n')
text=text.replace('c=','A')
text=text.replace('c-','A')
text=text.replace('dz=','A')
text=text.replace('d-','A')
text=text.replace('lj','A')
text=text.replace('nj','A')
text=text.replace('s=','A')
text=text.replace('z=','A')

print(len(text))
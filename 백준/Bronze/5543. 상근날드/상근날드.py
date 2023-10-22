import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

x = min(a,b,c)
y = min(d,e)

print(x+y-50)
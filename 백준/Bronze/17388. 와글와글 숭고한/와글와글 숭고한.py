import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

total = a + b + c
minNum = min(a, b, c)

if total >= 100:
    print('OK')
elif minNum == a:
    print("Soongsil")
elif minNum == b:
    print("Korea")
else:
    print("Hanyang")

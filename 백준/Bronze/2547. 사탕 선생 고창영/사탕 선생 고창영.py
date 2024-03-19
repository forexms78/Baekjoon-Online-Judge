import sys

input = sys.stdin.readline
n = int(input())
null = input()
for i in range(n):
    n2 = int(input())
    final = 0
    for j in range(n2):
        k = int(input())
        final += k
    null = input()

    if final % n2 == 0:
        print('YES')
    else:
        print('NO')

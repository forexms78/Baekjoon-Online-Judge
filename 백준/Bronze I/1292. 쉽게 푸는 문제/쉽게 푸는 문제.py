import sys

input = sys.stdin.readline

x = []
for i in range(1, 1001):
    for j in range(i):
        x.append(i)

n, m = map(int, input().split())

cnt = 0
for k in range(n-1, m):
    cnt += x[k]

print(cnt)
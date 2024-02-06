import sys

input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    K = int(input())
    K -= 1
    count += K

count += 1
print(count)
import sys

input = sys.stdin.readline

ball = 1

cnt = int(input())

for i in range(cnt):
    N, M = map(int, input().split())

    if N == ball:
        ball = M
    elif M == ball:
        ball = N

print(ball)
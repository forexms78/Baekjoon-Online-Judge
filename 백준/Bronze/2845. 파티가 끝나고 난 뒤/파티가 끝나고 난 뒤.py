import sys

input = sys.stdin.readline

A, B = map(int, input().split())

K = list(map(int, input().split()))

C = A * B

for i in K:
    print(i - C, end=" ")

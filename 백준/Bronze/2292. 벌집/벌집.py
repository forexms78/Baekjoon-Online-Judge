import sys

input = sys.stdin.readline

N = int(input())
honeycomb = 1
cnt = 1
while N > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1


print(cnt)
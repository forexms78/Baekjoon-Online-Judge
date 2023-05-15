import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

my_array = []

for i in range(N):
    X, Y = map(int, input().split())
    my_array.append([X, Y])

my_array.sort()
for i in my_array:
    print(' '.join(str(j) for j in i))

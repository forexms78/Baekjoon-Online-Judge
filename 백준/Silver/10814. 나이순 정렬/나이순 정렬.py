import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

my_array = []

for i in range(N):
    X, Y = input().split()
    X = int(X)
    my_array.append([X, Y])

my_array.sort(key=lambda x: x[0])

for i in my_array:
    print(' '.join(str(j) for j in i))

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

my_array = []

for i in range(N):
    X, Y = map(int, input().split())
    my_array.append([X, Y])

list2 = sorted(my_array, key=lambda x: (x[1], x[0]))


for i in list2:
    print(' '.join(str(j) for j in i))

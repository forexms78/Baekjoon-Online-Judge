import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
N_deque = deque(i for i in range(1, N+1))
count = M
print("<", end="")

while len(N_deque) > 1:
    while count > len(N_deque):
        count -= len(N_deque)
    print(N_deque[count-1], end="")
    if len(N_deque) != 1:
        print(",", end=" ")
    del N_deque[count-1]
    count += M-1


print(N_deque[0], end="")
print(">", end="")

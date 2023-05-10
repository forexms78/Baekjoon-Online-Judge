import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
N_deque = deque(i for i in range(1, N+1))

count = 1

while len(N_deque) > 1:
    if count == 1:
        N_deque.popleft()
        count = 2

    elif count == 2:
        N_deque.rotate(-1)
        count = 1

print(N_deque[0])

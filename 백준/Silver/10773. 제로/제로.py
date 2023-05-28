import sys
from collections import deque

input = sys.stdin.readline


my_deque = deque()
cnt = int(input())

for i in range(cnt):
    number = int(input())
    if number == 0 and len(my_deque) > 0:
        my_deque.pop()
    else:
        my_deque.append(number)

print(sum(my_deque))

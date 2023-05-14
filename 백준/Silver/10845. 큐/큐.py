import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
my_deque = deque()

while N:
    N -= 1

    text = input().rstrip('\n')

    if text.count(" ") > 0:
        text, number = text.split(" ")

    if text == 'push':
        my_deque.append(number)

    if text == 'pop':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque.popleft())

    if text == 'size':
        print(len(my_deque))

    if text == 'empty':
        if len(my_deque) == 0:
            print(1)
        else:
            print(0)

    if text == 'front':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque[0])

    if text == 'back':
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque[-1])

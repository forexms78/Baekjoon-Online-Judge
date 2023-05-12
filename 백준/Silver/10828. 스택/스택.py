import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deque_stack = deque()

while N:
    N -= 1

    text = input().rstrip('\n')

    if text.count(" ") > 0:
        text, number = text.split(" ")

    if text == 'push':
        deque_stack.append(number)

    if text == 'size':
        print(len(deque_stack))

    if text == 'top':
        if len(deque_stack) == 0:
            print(-1)
        else:
            print(deque_stack[-1])

    if text == 'empty':
        if len(deque_stack) == 0:
            print(1)
        else:
            print(0)

    if text == 'pop':
        if len(deque_stack) == 0:
            print(-1)
        else:
            print(deque_stack.pop())

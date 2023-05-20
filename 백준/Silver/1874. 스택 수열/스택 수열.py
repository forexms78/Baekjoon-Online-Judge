import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
my_stack = deque()
number = 1
my_array = []
no = 0

for i in range(n):
    k = int(input())

    while k >= number:
        my_stack.append(number)
        number += 1
        my_array.append('+')

    if my_stack.pop() == k:
        my_array.append('-')
    else:
        no += 1

if no >= 1:
    print('NO')
else:
    for i in my_array:
        print(i)

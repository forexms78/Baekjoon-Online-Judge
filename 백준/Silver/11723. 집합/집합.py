from array import array
import sys

N = int(input())

arr = array('i', [0] * 20)

for i in range(N):
    input_str = sys.stdin.readline().split()

    if len(input_str) == 1:
        command = input_str[0]
        number = 0
    else:
        command, number = input_str
        number = int(number)
    if command == 'add':
        arr[number - 1] = 1
    elif command == 'remove':
        arr[number - 1] = 0
    elif command == 'check':
        print(arr[number - 1])
    elif command == 'toggle':
        arr[number - 1] = 1 - arr[number - 1]
    elif command == 'all':
        arr = array('i', [1] * 20)
    elif command == 'empty':
        arr = array('i', [0] * 20)
import sys

input = sys.stdin.readline

first = input().strip('\n')
arr = list(first)

second = input().strip('\n')
arr2 = list(second)
arr3 = []

test1len = -(-len(arr) // len(arr2))

arr2 = arr2 * test1len

arr2 = arr2[:len(arr)]

for i in range(len(arr)):
    test1 = ord(arr[i]) - 96
    test2 = ord(arr2[i]) - 96

    test3 = test1 - test2

    if test1 == -64:
        arr3.append(' ')
    elif test3 <= 0:
        test3 += 26
        arr3.append(chr(test3 + 96))
    else:
        arr3.append(chr(test3 + 96))

for i in arr3:
    print(i, end='')

import sys

count = int(sys.stdin.readline())

my_array = [0] * 10001

for _ in range(count):

    K = int(sys.stdin.readline())

    my_array[K] += 1

for i in range(10001):
    if my_array[i] != 0:
        for j in range(my_array[i]):
            print(i)

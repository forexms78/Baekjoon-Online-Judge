import sys

count = int(sys.stdin.readline())

my_array = []

while count:
    count -= 1

    K = int(sys.stdin.readline())

    my_array.append(K)

my_array.sort()

for i in my_array:
    print(i)

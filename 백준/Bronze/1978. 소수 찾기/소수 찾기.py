import math

count = int(input())

num_array = list(map(int,input().split()))

for i in num_array:
    if i == 1:
        count -= 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count -= 1
            break

print(count)
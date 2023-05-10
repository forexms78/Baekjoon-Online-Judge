import sys
input = sys.stdin.readline

N = int(input())
N_array = [i for i in range(1, N+1)]

count = 1

while len(N_array) > 1:
    if count == 1:
        print(N_array[0], end=" ")
        del N_array[0]
        count = 2

    elif count == 2:
        N_array.append(N_array[0])
        del N_array[0]
        count = 1


print(N_array[0])

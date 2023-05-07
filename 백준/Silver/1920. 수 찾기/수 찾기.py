import sys
input = sys.stdin.readline

N = int(input())

N_array = list(map(int,input().split()))

M = int(input())

M_array = list(map(int,input().split()))

N_array.sort()

my_array = [ 0 for i in range(M)]

for i in range(M):
    left = 0
    right = len(N_array) -1
    while left <= right:
        middle = (left+right)//2

        if M_array[i] < N_array[middle]:
            right = middle - 1

        elif N_array[middle] < M_array[i]:
            left = middle + 1

        else:
            my_array[i] = 1
            break

for i in my_array:
    print(i)
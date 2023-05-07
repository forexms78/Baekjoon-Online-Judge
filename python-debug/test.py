import sys
input = sys.stdin.readline

N = int(input())

N_array = list(map(int,input().split()))

M = int(input())

M_array = list(map(int,input().split()))

N_array.sort()

my_array = [ 0 for i in range(M)]

for i in range(M):
    for j in range(N):
        if M_array[i] == N_array[j]:
            my_array[i] = 1
            break


for i in my_array:
    print(i)
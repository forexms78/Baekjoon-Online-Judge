import sys

input = sys.stdin.readline

N, M = map(int, input().split())

N_list = input()
N_list = N_list.split()
N_list = [int(x) for x in N_list]

# Calculate the prefix sum
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + N_list[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])

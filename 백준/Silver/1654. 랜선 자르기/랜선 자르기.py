import sys

input = sys.stdin.readline

N, K = map(int, input().split())
len_array = []
for i in range(N):
    len_line = int(input())
    len_array.append(len_line)

start = 1
end = max(len_array)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in len_array:
        count += i // mid
    if count >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)

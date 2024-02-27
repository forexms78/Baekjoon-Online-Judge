import sys

input = sys.stdin.readline

N = int(input())
congressman = []
for i in range(N):
    congressman.append(int(input()))
cnt = 0
while True:
    max_number = max(congressman)
    max_indices = [index for index, value in enumerate(congressman) if value == max_number]
    if max_indices[0] == 0 and len(max_indices) == 1:
        break
    elif len(max_indices) == 1 and max_indices[0] != 0:
        congressman[max_indices[0]] -= 1
        congressman[0] += 1
        cnt += 1
    else:
        congressman[max_indices[1]] -= 1
        congressman[0] += 1
        cnt += 1

print(cnt)



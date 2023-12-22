N, K = map(int, input().split())
cnt = 0
arr = []

for i in range(N):
    X = int(input())
    arr.append(X)

# Sort the array in descending order
arr.sort(reverse=True)

for i in range(N):
    if K >= arr[i]:
        cnt += K // arr[i]
        K %= arr[i]

print(cnt)
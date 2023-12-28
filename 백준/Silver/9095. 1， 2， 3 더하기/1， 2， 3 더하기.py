N = int(input())

arr = [1, 2, 4]

for _ in range(N):
    K = int(input())

    if K <= 3:
        print(arr[K - 1])
    else:
        if len(arr) < K:
            for i in range(len(arr), K):
                arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
        print(arr[K - 1])

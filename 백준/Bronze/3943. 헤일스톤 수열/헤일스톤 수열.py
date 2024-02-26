import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    K = int(input())
    J = K
    while J != 1:
        if J % 2 == 0:
            J /= 2
            J = int(J)
        else:
            J *= 3
            J += 1

        K = max(J, K)
    print(K)

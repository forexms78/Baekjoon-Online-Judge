from itertools import combinations
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().rstrip().split()

    if N > 32:
        print(0)
    else:
        res = 13
        case = combinations(mbti, 3)

        for a, b, c in case:
            dist = 0
            for i, j in zip(a, b):
                if i != j:
                    dist += 1
            for i, j in zip(b, c):
                if i != j:
                    dist += 1
            for i, j in zip(a, c):
                if i != j:
                    dist += 1

            res = min(res, dist)
        print(res)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A_set = set()
B_set = set()

# A 리스트 입력 받기
for _ in range(N):
    A_set.add(input())

# B 리스트 입력 받기
for _ in range(M):
    B_set.add(input())

# A와 B의 교집합 구하기
result_set = A_set.intersection(B_set)

print(len(result_set))
for i in sorted(result_set):
    print(i, end='')
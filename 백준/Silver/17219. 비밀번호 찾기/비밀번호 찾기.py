import sys

N , M = map(int, sys.stdin.readline().split())

arr = {}

for i in range(N):
    site, password = sys.stdin.readline().split()
    arr[site] = password

for i in range(M):
    print(arr[sys.stdin.readline().strip()])
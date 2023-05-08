import sys
input = sys.stdin.readline

N = list(input())
M = list(input())

print("no" if len(N) < len(M) else "go")
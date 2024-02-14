import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

lower_bound = (N // 100) * 100


if lower_bound % F == 0:
    result = 0
else:
    result = F - (lower_bound % F)

print(f"{result:02}")
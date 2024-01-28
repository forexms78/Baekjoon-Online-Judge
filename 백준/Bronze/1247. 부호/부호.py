import sys

input = sys.stdin.readline

for _ in range(3):
    sumNum = 0
    N = int(input())
    for _ in range(N):
        K = int(input())
        sumNum += K

    if sumNum == 0:
        print(0)
    elif sumNum < 0:
        print("-")
    else:
        print("+")

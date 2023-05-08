import sys
input = sys.stdin.readline

while 1:
    N, M = map(int,input().split())

    if N > M:
        print("Yes")
    elif M == 0 and N == 0:
        break 
    else:
        print("No")

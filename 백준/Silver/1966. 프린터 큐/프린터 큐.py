import sys
from collections import deque

input = sys.stdin.readline


def solve(n):

    for __ in range(n):
        N, M = map(int, input().split())
        M += 1
        test_queue = list(map(int, input().split()))
        rank_queue = deque()
        cnt = 1
        for number in test_queue:
            rank_queue.append([number, cnt])
            cnt += 1

        my_array = []

        while len(rank_queue) > 0:
            print_pass = 0
            for y in range(len(rank_queue)):
                if rank_queue[0][0] < rank_queue[y][0]:
                    print_pass += 1
                    break
            if print_pass > 0:
                rank_queue.append(rank_queue.popleft())
            else:
                my_array.append(rank_queue.popleft())

        for x in range(N):
            if my_array[x][1] == M:
                print(x+1)
                break

    answer = 0
    return answer


n = int(input())

solve(n)

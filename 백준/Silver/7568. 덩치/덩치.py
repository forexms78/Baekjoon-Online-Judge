import sys
input = sys.stdin.readline


def solve(n, people):
    ranks = []

    for i in range(n):
        rank = 1

        for j in range(n):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
        ranks.append(rank)

    return ranks


n = int(input())

people = []

for _ in range(n):
    height, weight = map(int, input().split())
    people.append((height, weight))

result = solve(n, people)

print(*result)

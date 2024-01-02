from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)


def bfs(start):
    q = deque([start])
    visited1[start] = True
    while q:
        start = q.popleft()
        print(start, end=' ')
        for i in range(1, N + 1):
            if not visited1[i] and graph[start][i]:
                q.append(i)
                visited1[i] = True


def dfs(start):
    visited2[start] = True
    print(start, end=' ')
    for i in range(1, N + 1):
        if not visited2[i] and graph[start][i]:
            dfs(i)


dfs(V)
print()
bfs(V)

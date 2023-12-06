N = int(input())

player_A = 100
player_B = 100

for _ in range(N):
    A, B = map(int, input().split())

    if A > B:
        player_B -= A
    elif B > A:
        player_A -= B


print(player_A)
print(player_B)
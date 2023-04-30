N, M = map(int, input().split())
board = [input() for i in range(N)]
ans = N*M

for i in range(N-7):
    for j in range(M-7):
        cnt1 , cnt2 = 0,0
        for k in range(8):
            for l in range(8):
                if (k+l)%2 == 0:
                    if board[i+k][j+l] != "W":
                        cnt1 += 1
                    elif board[i+k][j+l] != "B":
                        cnt2 += 1
                else:
                    if board[i+k][j+l] != "B":
                        cnt1 += 1
                    elif board[i+k][j+l] != "W":
                        cnt2 += 1
        ans = min(ans, cnt1, cnt2)

print(ans)
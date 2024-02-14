N = int(input())

P = N
cnt = 0
while True:
    cnt += 1
    if P < 10:
        A = 0
        B = P
    else:
        A = P // 10
        B = P % 10

    C = A+B
    if C >= 10:
        C = C % 10
    P = (B * 10) + C

    if P == N:
        break
print(cnt)
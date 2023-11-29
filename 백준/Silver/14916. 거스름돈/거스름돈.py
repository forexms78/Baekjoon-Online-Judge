N = int(input())
cnt = 0

while True:
    if N >= 5 and N % 2 != 0:
        N -= 5
        cnt += 1
    elif N >= 10 and N % 2 == 0:
        N -= 10
        cnt += 2
    elif N >= 2:
        N -= 2
        cnt += 1
    else:
        break


if N >= 1:
    print(-1)
else:
    print(cnt)
N = int(input())

A, B = map(int,input().split())

cnt = 0


while N >= 1:

    if A >= 2 or B >= 1:

        N -= 1
        if A >= 2:
            A -= 2
            cnt += 1
        elif B >= 1:
            B -= 1
            cnt += 1
    else:
        break

print(cnt)

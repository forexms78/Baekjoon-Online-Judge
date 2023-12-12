N = int(input())

A, B, C = map(int,input().split())

cnt = 0

if N >= A:
    cnt += A
else:
    cnt += N


if N >= B:
    cnt += B
else:
    cnt += N


if N >= C:
    cnt += C
else:
    cnt += N


print(cnt)

import sys

input = sys.stdin.readline

운동횟수, 현재맥박, 최대맥박, 운동심박, 휴식심박 = map(int, input().split())

cnt = 0
초기맥박 = 현재맥박
if (현재맥박 + 운동심박) > 최대맥박 and (현재맥박 - 휴식심박) < 초기맥박:
    cnt = -1

else:
    while 운동횟수 != 0:
        cnt += 1

        if (현재맥박 + 운동심박) <= 최대맥박:
            운동횟수 -= 1
            현재맥박 += 운동심박
        else:
            현재맥박 -= 휴식심박
            if 현재맥박 < 초기맥박:
                현재맥박 = 초기맥박
print(cnt)
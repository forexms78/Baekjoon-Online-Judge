import sys
input = sys.stdin.readline

# 입력
race = []
for _ in range(8):
    tmp = list(input().split())
    race.append(tmp)

# 정렬
race.sort()

# 점수 계산
score_red = 0
score_blue = 0
score = [10, 8, 6, 5, 4, 3, 2, 1]

for i in range(8):
    if race[i][1] == 'R':
        score_red += score[i]
    else:
        score_blue += score[i]

# 출력
print('Red' if score_red > score_blue else 'Blue')
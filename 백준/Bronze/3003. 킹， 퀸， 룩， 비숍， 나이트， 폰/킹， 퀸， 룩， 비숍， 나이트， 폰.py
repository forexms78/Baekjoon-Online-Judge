main_chess = [1,1,2,2,2,8]

your_chess = list(map(int,input().split()))

answer_chess = []

for i in range(6):
    print(main_chess[i] - your_chess[i], end=" ")
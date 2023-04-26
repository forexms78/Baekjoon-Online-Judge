basket, ball = map(int,input().split())

basketArray = [0] * basket

while ball:
    ball -= 1
    i, j, k = map(int, input().split())
    for num in range(i,j+1):
        basketArray[num-1] = k
    

print(*basketArray)
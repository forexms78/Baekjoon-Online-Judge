count = int(input())

while count:
    count -= 1
    k=int(input())
    n=int(input())

    matrix = [[1 for j in range(n)] for i in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if j == 0:
                continue
            else:
                try:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                except IndexError:
                    continue
    print(matrix[-1][-1])
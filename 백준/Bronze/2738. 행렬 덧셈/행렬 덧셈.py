N, M = map(int,input().split())
A, B = [], []
N1 , N2 = N, N

while N1:
    N1 -= 1
    row = list(map(int,input().split()))
    A.append(row)
while N2:
    N2 -= 1
    row = list(map(int,input().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()
    




N = int(input())
M = list(map(int, input().split()))
K = []
count = 0

for i in range(0, N):
    if i == 0:
        K.append(M[i])
    else:
        if M[i] != 0:
            O = i - 1
            K.append(K[O]+1)
        else:
            K.append(0)

sum = 0
for i in K:
    sum += i

print(sum)

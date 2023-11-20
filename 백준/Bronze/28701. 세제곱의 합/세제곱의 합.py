N = int(input())
K = 0
Y = 0
for i in range(N):
    K += i+1

for i in range(N):
    Y += ((i+1)**3)

print(K)
print(K ** 2)
print(Y)
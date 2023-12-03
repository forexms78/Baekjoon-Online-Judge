K = 0

for _ in range(5):
    N = int(input())

    if N < 40:
        N = 40
    
    K += N

print(int(K / 5))
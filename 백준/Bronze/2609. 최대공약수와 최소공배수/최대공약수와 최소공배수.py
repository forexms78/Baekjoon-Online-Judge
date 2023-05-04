N, M = map(int,input().split())

N_array = []
M_array = []
least_common_multiple = 1
greatest_common_divisor = 0

my_array = []

if N <= 1 and M <= 1:
    if N == 0 and M == 1:
        greatest_common_divisor = 1
        least_common_multiple = 0
    elif N == 1 and M == 0:
        greatest_common_divisor = 1
        least_common_multiple = 0
    elif N == 1 and M == 1:
        greatest_common_divisor = 1
        least_common_multiple = 1
    else:
        greatest_common_divisor = 0
        least_common_multiple = 0
elif N == M:
    greatest_common_divisor = N
    least_common_multiple = M
else:
    for i in range(1,N+1):
        if N % i == 0:
            N_array.append(i)

    for i in range(1,M+1):
        if M % i == 0:
            M_array.append(i)

    for i in N_array:
        for j in M_array:
            if i == j:
                greatest_common_divisor = i

    best_number = max(N,M)

    for i in range(2,best_number):
        while N % i == 0 and M % i == 0:
            N = N // i
            M = M // i
            my_array.append(i)

    for i in my_array:
        least_common_multiple *= i

    least_common_multiple = least_common_multiple * N * M



        
print(greatest_common_divisor)
print(least_common_multiple)

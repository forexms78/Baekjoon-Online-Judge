N = int(input())
N_list = list(map(int,input().split()))


if N <= 1:
    print(N_list[0]**2)
else:
    A = min(N_list)
    B = max(N_list)   
    print(A*B)
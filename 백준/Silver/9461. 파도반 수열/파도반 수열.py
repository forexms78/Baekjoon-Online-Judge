N = int(input())

pado = [1,1,1]

for _ in range(N):
    K = int(input())

    if K <= len(pado):
        print(pado[K-1])
    else:
        for i in range(len(pado),K):
            pado.append(pado[i-2] + pado[i-3])
        print(pado[-1])
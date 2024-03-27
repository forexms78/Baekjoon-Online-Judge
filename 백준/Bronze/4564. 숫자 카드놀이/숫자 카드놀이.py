while True:
    A = list(map(int, str(input())))

    results = []

    if len(A) == 1 and A[0] == 0:
        break

    while True:
        result = ''.join(str(number) for number in A)
        results.append(result)  # 결과를 리스트에 추가

        if len(A) == 1:
            break

        total = 1
        for i in range(len(A)):
            total *= A[i]

        A = list(map(int, str(total)))

    print(' '.join(results))

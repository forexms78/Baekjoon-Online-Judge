while True:
    a = list(map(int, str(input())))
    if a[0] == 0 and len(a) == 1:
        break
    b = 1
    for i in range(len(a)):
        if a[i] == 0:
            b += 5
        elif a[i] == 1:
            b += 3
        else:
            b += 4
    print(b)

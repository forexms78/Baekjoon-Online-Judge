while 1:
    X,Y,Z = map(int,input().split())

    if X == 0 and Y == 0 and Z == 0:
        break
    X = X * X
    Y = Y * Y
    Z = Z * Z

    if X + Y == Z:
        print("right")
    elif X + Z == Y:
        print("right")
    elif Y + Z == X:
        print("right")
    else:
        print("wrong")
a = int(input())
b = int(input())
c = int(input())

total = a + b + c

if total != 180:
    print('Error')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or a == c:
    print('Isosceles')
elif a != b != c:
    print('Scalene')

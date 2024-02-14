
um = 0
A = input()
B = input()
C = input()

if A == 'black':
    um += 0
elif A == 'brown':
    um += 10
elif A == 'red':
    um += 20
elif A == 'orange':
    um += 30
elif A == 'yellow':
    um += 40
elif A == 'green':
    um += 50
elif A == 'blue':
    um += 60
elif A == 'violet':
    um += 70
elif A == 'grey':
    um += 80
else:
    um += 90

if B == 'black':
    um += 0
elif B == 'brown':
    um += 1
elif B == 'red':
    um += 2
elif B == 'orange':
    um += 3
elif B == 'yellow':
    um += 4
elif B == 'green':
    um += 5
elif B == 'blue':
    um += 6
elif B == 'violet':
    um += 7
elif B == 'grey':
    um += 8
else:
    um += 9

if C == 'black':
    um *= 1
elif C == 'brown':
    um *= 10
elif C == 'red':
    um *= 100
elif C == 'orange':
    um *= 1000
elif C == 'yellow':
    um *= 10000
elif C == 'green':
    um *= 100000
elif C == 'blue':
    um *= 1000000
elif C == 'violet':
    um *= 10000000
elif C == 'grey':
    um *= 100000000
else:
    um *= 1000000000

print(um)


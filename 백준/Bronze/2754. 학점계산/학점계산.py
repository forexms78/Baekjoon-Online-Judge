학점 = list(input())
점수 = 0.0

for i in 학점:
    if i == "A":
        점수 += 4
    elif i == "B":
        점수 += 3
    elif i == "C":
        점수 += 2
    elif i == "D":
        점수 += 1

    if i == "+":
        점수 += 0.3
    elif i == "-":
        점수 -= 0.3
    
print(점수)
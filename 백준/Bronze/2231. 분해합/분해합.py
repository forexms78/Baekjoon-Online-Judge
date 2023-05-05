number = int(input())
low_number = number


for i in range(number):
    check = number - i
    check_array = list(str(check))
    b_number = check
    for j in check_array:
        b_number += int(j)
    if b_number == number:
        low_number = min(low_number, check)

if(low_number == number):
    print(0)
else:
    print(low_number)
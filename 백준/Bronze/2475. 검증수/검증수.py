my_list = list(map(int,input().split()))
total = 0

for i in my_list:
    total += i ** 2

print(total % 10)
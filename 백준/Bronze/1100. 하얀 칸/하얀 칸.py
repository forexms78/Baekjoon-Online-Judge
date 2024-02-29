arr = {}
cnt = 1
for i in range(8):
    list_number = list(input())
    for j in list_number:
        arr[cnt] = j
        cnt += 1
total = 0
key_number = 1
arr_count = 0
for key, value in arr.items():
    arr_count += 1
    if key % 2 == key_number and value == 'F':
        total += 1
    if arr_count == 8:
        arr_count = 0
        if key_number == 1:
            key_number = 0
        else:
            key_number = 1


print(total)
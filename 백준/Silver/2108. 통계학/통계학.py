import sys
from collections import deque, Counter

input = sys.stdin.readline

n = int(input())
EDC_array = []

for _ in range(n):
    EDC_array.append(int(input()))

EDC_array.sort()


avg_result = round(sum(i for i in EDC_array) / len(EDC_array))
middle_result = EDC_array[len(EDC_array) // 2]

counter = Counter(EDC_array)
duplicates = [value for value, count in counter.items()]
max_duplicates = max(duplicates, key=lambda value: counter[value])

counter_items = list(counter.items())
sorted_items = sorted(counter_items, key=lambda item: item[1], reverse=True)
my_key, my_value = sorted_items[0]

if len(sorted_items) >= 2:
    my_key2, my_value2 = sorted_items[1]
    if my_value2 == my_value:
        second_most_number = my_key2
    else:
        second_most_number = my_key
else:
    second_most_number = my_key

range_result = abs(EDC_array[0] - EDC_array[-1])


print(avg_result)
print(middle_result)
print(second_most_number)
print(range_result)

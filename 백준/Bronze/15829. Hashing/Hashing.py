import sys

input = sys.stdin.readline

n = int(input())
total_number = 0
ascii_array = list(input().strip())

for i in range(n):
    ascii_number = ord(ascii_array[i])-96
    total_number += ascii_number*(31**i)


print(total_number)
import sys
input = sys.stdin.readline

N = int(input())
N_array = list(map(int, input().split()))

M = int(input())
M_array = list(map(int, input().split()))
 
count_dict = {}
for num in N_array:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

my_array = []
for num in M_array:
    if num in count_dict:
        my_array.append(count_dict[num])
    else:
        my_array.append(0)

print(" ".join(str(i) for i in my_array))

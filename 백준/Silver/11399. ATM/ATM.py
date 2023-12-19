N = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

total = 0
add = 0
for i in arr:
    add += i
    total += add

print(total)
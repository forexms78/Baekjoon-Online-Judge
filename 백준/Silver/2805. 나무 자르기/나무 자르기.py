import sys

input = sys.stdin.readline

tree_cnt, meter = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

low = 0
high = max(trees)  # Set the highest possible value initially

while low < high:
    mid = (low + high) // 2

    wood = 0
    for tree in trees:
        if tree > mid:
            wood += tree - mid

    if wood < meter:
        high = mid
    else:
        low = mid + 1

cutter = low - 1
print(cutter)
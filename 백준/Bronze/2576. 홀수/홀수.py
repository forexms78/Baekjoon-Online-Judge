import sys

input = sys.stdin.readline
li = []
sum1 = 0

for i in range(7):
    nub = int(input())
    if nub % 2 == 1:
        li.append(nub)
        sum1 += nub
li.sort()
if len(li) == 0:
    print(-1)
else:
    print(sum1)
    print(li[0])

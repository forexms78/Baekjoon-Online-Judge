import sys

input = sys.stdin.readline

G, B, I = map(int, input().split())
cnt = 0

for k in range(I):
    if G >= (2*B):
        G -= 1
    else:
        B -= 1

while True:
    G -= 2
    B -= 1
    if G < 0 or B < 0:
        break
    else:
        cnt += 1

print(cnt)
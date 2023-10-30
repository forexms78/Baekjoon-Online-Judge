import sys
input = sys.stdin.readline
import math

D, H, W = map(int,input().split())

k = math.sqrt(D**2 /(H**2 + W**2) )

print(int(k*H),int(k*W))
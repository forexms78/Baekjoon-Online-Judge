import sys
from collections import deque

import math

input = sys.stdin.readline

N, K = map(int, input().split())


result = math.factorial(N) // (math.factorial(K)*math.factorial(N-K))

print(result)

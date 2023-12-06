def gcd(a,b):
    if a > b:
        a , b = b , a
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)
    
def solve(a,b,c):
    if c > a and c > b:
        return False
    return c % gcd(a,b) ==0

T = int(input())
for _ in range(T):
    a,b,c, = map(int,input().split())
    if solve(a,b,c):
        print("YES")
    else:
        print("NO")
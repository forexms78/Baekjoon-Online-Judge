def solve():
    # 최대 N은 40이므로 N이 40까지에 대한 dp 테이블을 만든다.
    dp_zeros = [0] * 41
    dp_ones = [0] * 41

    # base cases
    dp_zeros[0] = 1  # fibonacci(0) -> 0이 한 번 출력
    dp_ones[0] = 0   # fibonacci(0) -> 1은 출력되지 않음
    dp_zeros[1] = 0   # fibonacci(1) -> 0은 출력되지 않음
    dp_ones[1] = 1    # fibonacci(1) -> 1이 한 번 출력

    # 2부터 40까지 dp 배열을 채운다.
    for i in range(2, 41):
        dp_zeros[i] = dp_zeros[i-1] + dp_zeros[i-2]
        dp_ones[i] = dp_ones[i-1] + dp_ones[i-2]

    # 테스트 케이스 입력
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp_zeros[N], dp_ones[N])

# 함수 실행
solve()

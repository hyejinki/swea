def fac(N):
    if N == 0:
        return 1        # 0 이면 리턴 1
    return N * fac(N - 1)

T= int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = N // 10
    ans = 1                             # 모두 20X1 로 이뤄지는 경우는 1
    for i in range(1, n // 2 + 1):             # 20X20 종이의 수
        small = n - 2 * i                      # 20X1 의 수
        ans += fac(small + i)/(fac(small)*fac(i)) * 2**i
        # (small + i) : 직사각형 개수   / 20X20로 만들 수 있는 경우의 수 ** i장
    print(f'#{test_case}', int(ans))





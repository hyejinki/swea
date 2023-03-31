def f(i, k, e, c):
    global minC

    if minC <= c:
        return

    if arr[i] >= k - i - 1:
        if minC > c:
            minC = c

    else:
        f(i + 1, k, arr[i] - 1, c + 1)
        if e > 0:
            f(i + 1, k, e-1, c)


T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    N = temp[0]
    arr = temp[1:] + [0]
    minC = 10000
    f(0, N, arr[0], 0)
    print(f'#{test_case}',minC + 1)
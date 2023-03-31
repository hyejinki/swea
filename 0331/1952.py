def f(i, s):
    global minV
    if s > minV:
        return
    if i > 11:
        if minV > s:
            minV = s
        return

    else:
        f(i + 1, s + arr[i] * d)
        f(i + 1, s + m)
        if i + 3 < 13:
            f(i + 3, s + t)
        f(12, s + y)

T = int(input())
for test_case in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    arr = list(map(int, input().split()))
    minV = 36000
    f(0, 0)
    print(f'#{test_case}', minV)
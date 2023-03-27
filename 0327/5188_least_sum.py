def f(i, j, N, s):
    global minV
    if i >= N or j >= N:
        return
    elif i == N - 1 and j == N - 1:
        s += arr[i][j]
        if minV > s :
            minV = s

    else:
        f(i, j + 1, N, s + arr[i][j])
        f(i + 1, j, N, s + arr[i][j])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000
    s = 0
    f(0, 0, N, s)
    print(f'#{test_case}', minV)
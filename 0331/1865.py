def f(i, N, s):
    global maxV
    if i == N:
        if maxV < s:
            maxV = s
    else:
        for j in range(N):
            if col[j] == 0:
                col[j] = 1
                f(i + 1, N, s * arr[i][j])
                col[j] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    maxV = 0
    f(0, N, 0)
    print(maxV * (0.0001))
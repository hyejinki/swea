def f(i, k):
    global minV
    if i == k:
        s = 0
        P = [1] + p + [1]           # 루트 그대로
        for i in range(N):
            s += arr[P[i]-1][P[i + 1]-1]
        if s < minV:
            minV = s

    else:
        for j in range(k):  # 사용하지 않은 숫자를
            if used[j] == 0:  # used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1  # j번 자리 숫자 사용으로 표시
                f(i + 1, k)
                used[j] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * (N - 1)
    P = []
    used = [0] * N
    minV = 10000

    A = [0] * (N - 1)
    for i in range(2, N+1):
        A[i - 2] = i

    f(0, N - 1)
    print(f'#{test_case}', minV)

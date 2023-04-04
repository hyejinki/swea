def f(N):
    INF = 100000000
    Q = []
    D = [[INF] * N for _ in range(N)]
    Q.append((0, 0))
    D[0][0] = 0
    while Q:
        i, j = Q.pop(0)
        for di, dj in [[0, 1], [1, 0],[0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and D[ni][nj] > (D[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j])):
                D[ni][nj] = D[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j])
                Q.append((ni, nj))
    return D[N-1][N -1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f(N))
def dij(n):
    INF = 100000000
    D = [[INF] * N for _ in range(N)]
    D[0][0] = 0
    U = [[0] * N for _ in range(N)]
    U[0][0] = 1
    for _ in range(N * N - 1):
        wi = wj = 0
        minV = INF
        for i in range(N):
            for j in range(N):
                if U[i][j] == 0 and minV > D[i][j]:
                    minV = D[i][j]
                    wi, wj = i, j
        U[wi][wj] = 1

        for di, dj in [[0, 1], [1, 0],[0, -1], [-1, 0]]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < N and 0 <= nj < N and U[ni][nj] == 0:
                cost = 1 + max(0, arr[ni][nj] - arr[wi][wj])
                D[ni][nj] = min(D[ni][nj], D[wi][wj] + cost)

    return D[N-1][N-1]




T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(dij(N))
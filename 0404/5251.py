def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    for i in range(V + 1):
        D[i] = adjM[s][i]

    N = V + 1
    for _ in range(N - 1):
        minV = INF
        w = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1

        for v in range(V + 1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])


INF = 1000
T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0] * (N + 1)
    dijkstra(0, N)
    print(f'#{test_case}', D[N])
def prim(V):
    INF = 1000
    key = [INF] * (V + 1)
    key[0] = 0
    MST = [0]
    for _ in range(V):      # 나머지 V개의 정점에 대해
        # MST에 포함되지 않은 정점 중 key가 최소인 u찾기
        u = 0
        minV = INF
        for i in range(V + 1):
            if i not in MST and minV > key[i]:
                u = i
                minV = key[i]
        MST.append(u)
        # u에 인접인 v에 대해 비용 갱신을 시도
        for v in range(V+1):
            if v not in MST and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)
T = int(input())
for test_case in range(1, T + 1):

    V, E = map(int, input().split())
    adjM = [[0] *(V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w  # 방향이 없으므로

    print(f'#{test_case}', prim(V))
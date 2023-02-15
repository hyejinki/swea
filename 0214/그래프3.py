def f(v, G):                # N : 마지막 정점 / 그래프 탐색, DFS
    if v == G:
        return 1
    else:
        visited[v] = 1
        for w in adjL[v]:
            if visited[w] == 0:             # 인접하고 방문안한 w
                if f(w, G):                 # 목적지를 찾고 리턴하는 경우
                    return 1
        return 0


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]  # 인접 리스트
    visited = [0]* (V+1)
    for _ in range(E):
        v, w = map(int, input().split())    # v출발, w 도착 (유향그래프)

        adjL[v].append(w)

        # adjM[w][v] = 1                      # 무향그래프였다면
    S, G = map(int, input().split())        # S출발, G 도착
    print(f'#{test_case} {f1(S, G, V)}')
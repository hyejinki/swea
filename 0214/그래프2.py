def f1(S, G, N):                # N : 마지막 정점 / 그래프 탐색, DFS
    visited = [0] * (N + 1)     # 방문 표시
    stack = []                  # 스택
    v = S
    while True:
        # v 방문
        if v == G:                  # 방문해서 목적지이면
            return 1                # (1) 성공!
        visited[v] = 1
        for w in adjL[v]:           # 인접하고 방문하지 않은 w가 있으면
            if visited[w] == 0:
                stack.append(v)     # 현재 정점 push
                v = w
                break
        else:                      # 더이상 갈 곳이 없는 경우
            if stack:              # pop
                v = stack.pop()
            else:                   # 스택이 비어있으면
                break
    # return visited[G]             # (2) 탐색 중에 G를 거쳐갔다면 visited[G] == 1
    return 0                        #(1) v == G 를 검사한 경우


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]  # 인접행렬
    for _ in range(E):
        v, w = map(int, input().split())    # v출발, w 도착 (유향그래프)

        adjL[v].append(w)

        # adjM[w][v] = 1                      # 무향그래프였다면
    S, G = map(int, input().split())        # S출발, G 도착
    print(f'#{test_case} {f1(S, G, V)}')
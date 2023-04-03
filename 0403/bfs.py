def bfs(s, k):
    q = []  # 큐 생성
    visited = [0] * (k + 1)     #visited 생성
    q.append(s)                 # 시작점 enq
    visited[s] = 1              # 시작점 방문체크
    while q:                    # 큐가 비어있지 않으면 반복
        v = q.pop(0)            # v <- 디큐
        print(v)                # v 방문 처리       if v == goal : break라던가
        for w in range(1, k + 1):    # v 에 인접하고, 방문 안 한 w가 있으면
            if adjM[v][w] == 1 and visited[w] ==0:
                q.append(w)         # 인큐,
                visited[w] = 1 + visited[v]     #방문표시


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1  # 방향이 없는 경우
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V)
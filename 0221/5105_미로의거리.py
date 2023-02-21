def bfs(i, j, arr):
    d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # 위부터 시계방향
    queue = [(i, j)]
    visited = [[0] * N for _ in range(N)]       # arr와 같은 사이즈
    visited[i][j] = 1
    while len(queue) > 0:
        (p, q) = queue.pop(0)                   # 현재 인덱스
        for k in range(4):
            ni, nj = p + d_ij[k][0], q + d_ij[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                if (arr[ni][nj] == '0' and visited[ni][nj] == 0) or arr[ni][nj] == '3':     # 방문하지 않은 곳 중 0이면
                    if arr[ni][nj] == '3':          # '3' 나오면
                        return visited[p][q] - 1    # 직전에 거쳐온 블럭 수 - 1
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[p][q] + 1

    return 0        # 끝까지 돌았으면

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                r, c = i, j
                break

    print(f'#{test_case}', bfs(r, c, arr))

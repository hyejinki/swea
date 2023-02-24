d_ij = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 상 하 좌 우
T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    p = [[1], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]] # 1: 상 , 2: 하, 3: 좌, 4: 우
    opp = {0: 1, 1: 0, 2: 3, 3: 2}      # 서로 연결되는 애들
    visited = [[0]*M for _ in range(N)]
    q = [(R, C)]
    visited[R][C] = 1

    while len(q):
        x = q.pop(0)
        ci, cj = x[0], x[1]
        if visited[ci][cj] == L:
            break
        for dr in p[arr[ci][cj]]:
            ni, nj = ci + d_ij[dr][0], cj + d_ij[dr][1]
            # 크기안에, 방문하지 않았으면, 값이 0이 아니면
            if 0 <= ni <N and 0 <= nj < M and opp[dr] in p[arr[ni][nj]] and visited[ni][nj] == 0 and\
                    arr[ni][nj] != 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    counts = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                counts += 1

    print(f'#{test_case}', counts)
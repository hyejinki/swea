d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 위부터 시계방향

def cost(r, c, M):
    q = [(r, c)]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    counts = 0
    K = 1
    if arr[r][c] == 1:
        profit = counts * M - 1
        maxV = 1
    else:
        profit = 0
        maxV = 0
    while K < N:
        s = q.pop(0)
        ci, cj = s[0], s[1]  # 현재 인덱스
        K += 1
        for d in range(4):
            ni, nj = ci + d_ij[d][0], cj + d_ij[d][1]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                if arr[ni][nj] == 1:        # 집이 있으면
                    counts += 1

        profit = counts * M - (K * K + (K - 1) * (K - 1))  # 이윤
        if profit > 0 and maxV > counts:
            maxV = counts

    return maxV

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            result.append(cost(i, j, M))

    print(max(result))
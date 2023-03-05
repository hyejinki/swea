d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]], [[-1, 1], [1, 1], [1, -1], [-1, -1]]
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(N):
            for t in range(2):
                ans = arr[i][j]
                for di, dj in d_ij[t]:
                    for m in range(1, M):
                        ni , nj = i + di * m, j + dj * m
                        if 0 <= ni < N and 0 <= nj < N:
                            ans += arr[ni][nj]
                maxV = max(ans, maxV)
    print(f'#{test_case}', maxV)
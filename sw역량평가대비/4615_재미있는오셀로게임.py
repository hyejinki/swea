d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 2) for _ in range(N + 2)]
    arr[N//2][N//2], arr[N//2+1][N//2+1], arr[N//2][N//2+1], arr[N//2+1][N//2] = 2, 2, 1, 1
    for _ in range(M):
        x, y, wb = map(int, input().split())
        r, c = y, x
        arr[r][c] = wb
        for k in range(8):
            li = []
            ni, nj = r + d_ij[k][0], c + d_ij[k][1]
            while arr[ni][nj] != c and arr[ni][nj] != 0:
                li.append((ni, nj))
                ni, nj = ni + d_ij[k][0], nj + d_ij[k][1]
            if arr[ni][nj] == c:
                for x, y in li:
                    arr[x][y] = wb
    cnt1 = 0
    cnt2 = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1

    print(f'#{test_case}', cnt1, cnt2)
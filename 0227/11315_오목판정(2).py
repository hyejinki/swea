d_ij = [[0, 1], [1, 1], [1, 0], [1, -1]]   # 오른쪽부터 시계방향으로 왼까지
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = ''
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    count = 1
                    r, c = i, j
                    while True:
                        ni, nj = r + d_ij[k][0], c + d_ij[k][1]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                count += 1
                            else:
                                count = 0
                            r, c = ni, nj
                        else:
                            break
                        if count == 5:
                            ans = 'YES'
                            break
                    if len(ans) != 0:       # Yes면
                        break
            if len(ans) != 0:  # Yes면
                break
        if len(ans) != 0:  # Yes면
            break

    if len(ans) == 0:
        ans = 'NO'

    print(f'#{test_case}', ans)
d_ij = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for t in range(1, total+1):
                for k in range(4):
                    ni, nj = i + d_ij[k][0]*t, j + d_ij[k][1]*t
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
            ans.append(total)

    print(f'#{test_case}', max(ans))
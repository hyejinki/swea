def dfs(arr, N, x, y):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    stack = []
    visited = []
    v = (x, y)
    visited.append(v)
    while True:
        if arr[x][y] == 3:
            return 1
        else:
            for w in range(4):
                ni, nj = i + di[w], j + dj[w]
                if ni < N - 1 and nj < N:
                    if arr





T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
                break

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]          # 오 아래 왼 위
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    k = i = j = 0
    while True:
        for n in range(1, N**N+1):
            arr[i][j] = n
            i = i + di[k]
            j = j + dj[k]
            if i == N or j == N or arr[i][j] != 0:
                k += 1
                i = i + di[k]
                j = j + dj[k]



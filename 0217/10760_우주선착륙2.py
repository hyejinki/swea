dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]    # 위부터 시계방향
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] + list(map(int, input().split()))+ [0] for _ in range(N)]
    arr = [[0] * (M + 2)] + arr + [[0] * (M + 2)]   # 사방에 0
    result = 0
    for i in range(1, N+1):         # 0으로 둘러쌓았기 때문에
        for j in range(1, M+1):
            count = 0
            for k in range(8):
                ni, nj = i + dir[k][0], j + dir[k][1]
                if arr[ni][nj] != 0 and arr[i][j] > arr[ni][nj]:    # 0 제외
                    count += 1
                if count == 4:      # 4개 이상이면 후보지
                    result += 1
                    break
    print(f'#{test_case}', result)
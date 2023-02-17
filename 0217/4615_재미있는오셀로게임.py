dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    bw = ['w', 'b']
    for i in range(2):      # 초기 작업 에휴
        for j in range(2):
            if i == j:
                arr[N // 2 - 1 + i][N // 2 - 1 + j] = bw[0]
            else:
                arr[N // 2 - 1 + i][N // 2 - 1 + j] = bw[1]
    for _ in range(M):
        i, j, color = map(int, input().split())

        if color == 1:
            for k in range(8):      # w 찾을 거임
                ni, nj = i + dir[k][0], j + dir[k][1]
                stack = []
                while arr[ni][nj] == 2:   # 계속 진행하다가(스택에 쌓아 놓고) 제한 조건 걸리면 바꿔
                    stack.append((ni,nj))
                    ni += dir[k][0]
                    nj += dir[k][1]



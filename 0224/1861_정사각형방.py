d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 위부터 시계방향
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    li = [0] * (N ** 2 + 1)
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + d_ij[k][0], j + d_ij[k][1]
                # 4방향 중 자신보다 1 큰 거 찾아
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    li[arr[i][j]] = 1
    # 연속된 1의 최대 개수, 처음 시작하는 인덱스
    maxV = 0
    maxIdx = 0
    counts = 1
    for i in range(len(li)):
        if li[i] == 1:
            counts += 1
            if counts > maxV:
                maxV = counts
                maxIdx = i
        else:
            counts = 1
    print(f'#{test_case}', maxIdx + 1 - maxV + 1, maxV)
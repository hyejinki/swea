T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    maxV = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            else:
                count = 0
            if maxV < count:
                maxV = count

    for i in range(M):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            else:
                count = 0
            if maxV < count:
                maxV = count

    print(f'#{test_case}', maxV)
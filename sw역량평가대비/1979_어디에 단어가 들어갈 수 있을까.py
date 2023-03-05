T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr += [[0] * (N + 1)]
    ans = 0
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[j][i] == 1:
                cnt2 += 1
            else:
                cnt2 = 0
            if cnt1 == K and arr[i][j+1] == 0:
                ans += 1
            if cnt2 == K and arr[j+1][i] == 0:
                ans += 1

    print(f'#{test_case}', ans)
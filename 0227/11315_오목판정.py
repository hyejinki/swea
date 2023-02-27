T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    cnt1 = cnt2 = cnt3 = cnt4 = 0   # 가로 / 세로 / 대각선1/ 대각선2
    ans = ''
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    # 가로
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[j][i] == 'o':    # 세로
                cnt2 += 1
            else:
                cnt2 = 0
            if arr[j][j] == 'o':    # 오른쪽 아래 대각선
                cnt3 += 1
            else:
                cnt3 = 0
            if arr[j][N-j-1] == 'o':    # 왼쪽 아래 대각선
                cnt4 += 1
            else:
                cnt4 = 0
            if cnt1 == 5 or cnt2 == 5 or cnt3 == 5 or cnt4 == 5:
                ans = 'YES'
                break

        if len(ans) != 0:
            break

        cnt1 = cnt2 = cnt3 = cnt4 = 0

    if len(ans) == 0:       # ans가 비어있으면
        ans = 'NO'

    print(f'#{test_case}', ans)
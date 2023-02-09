def transpose(arr, N):
    arr_T = ['' for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_T[i] += arr[j][i]
    return (arr_T)

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [str(input())for _ in range(N)]
    arr_T = transpose(arr, N)
    # for i in range(N):
    #     for j in range(int(M/2)):
    ans = ''
    for i in range(N):
        for j in range(N-M+1):
            # arr[i][j+0] - arr[i][j+M-1] 회문인지 확인
            # k : 0 -> M//2-1
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
                else:
                    for l in range(M):
                        ans += arr[i][j+l]
        print(ans)

        for j in range(N-M+1):
            l = j
            r = j + M - 1
            if arr_T[i][l] == arr_T[i][r]:
                l += 1
                r -= 1
            if l == (j + j + M)//2:
                check2 = 1
        if check2:
            print(f'#{testcase}', arr_T[i])
            break




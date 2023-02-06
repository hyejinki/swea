def diff(a, b):
    if a - b >= 0:
        ans = a - b
    else:
        ans = b - a
    return ans


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            a = []
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    ans += diff(arr[ni][nj], arr[i][j])
    print(f'#{test_case}', ans)

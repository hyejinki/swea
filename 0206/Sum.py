def maxV(N):
    maxv = 0
    if maxv < N:
        maxv = N
    return maxv


for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    daegak1 = daegak2 = 0
    # 가로 합, 세로 합, 대각선 합
    for i in range(100):
        garo = 0
        sero = 0
        daegak1 += arr[i][i]
        daegak2 += arr[99-i][i]
        maxdae1 = maxV(daegak1)
        maxdae2 = maxV(daegak2)

        for j in range(100):
            garo +=  arr[i][j]
            sero += arr[j][i]
            maxgaro = maxV(garo)
            maxsero = maxV(sero)
    for i in [maxdae1, maxdae2, maxgaro, maxsero]:
        ans = maxV[i]
    print(ans)
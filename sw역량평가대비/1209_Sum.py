for test_case in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = 0
    c3 = 0
    c4 = 0
    for i in range(100):
        c1 = 0
        c2 = 0
        for j in range(100):
            c1 += arr[i][j]     # 가로
            c2 += arr[j][i]     # 세로
        maxV = max(c1, c2, maxV)
        c3 += arr[i][i]
        c4 += arr[99-i][i]
        maxV = max(c3, c4, maxV)
    print(f'#{T}', maxV)


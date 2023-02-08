
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    # 양 옆에 0으로 채워줌
    new_arr = [[0]*102 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_arr[i][j+1] = arr[i][j]
    di = 99
    dj = arr[99].index(2)

    while di >= 0:          # 0행까지
        if di == 0:
            break
        if dj >= 1 and arr[di][dj - 1]:  # 왼쪽에 있으면
            while dj > 0:
                if arr[di-1][dj-1]:
                    di -= 1
                    dj -= 1
                    break
                else:
                    dj -= 1
        elif dj <= 98 and arr[di][dj + 1]:       # 오른쪽에 있으면
            while dj < 99:
                if arr[di-1][dj-1]:
                    di -= 1
                    dj -= 1
                    break
                else:
                    dj += 1
        else:
            arr[di][dj] == 0
            di -= 1                 # 양쪽에 사다리 없으면 위로
    print(f'#{test_case}', dj)
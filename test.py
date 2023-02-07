
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    i = 99
    j = arr[99].index(2)

    while i >= 0:          # 0행까지
        if i == 0:
            break
        if j >= 1 and arr[i][j - 1]:  # 왼쪽에 있으면
            while j > 0:
                if arr[i-1][j-1]:
                    i -= 1
                    j -= 1          # 왼쪽으로
                    break
                else:
                    j -= 1
        elif j <= 98 and arr[i][j+1]:       # 오른쪽에 있으면
            while j < 99:
                if arr[i-1][j+1]:
                    i -= 1
                    j += 1          # 오른쪽으로
                    break
                else:
                    j += 1
        else:
            arr[i][j] == 0
            i -= 1                 # 양쪽에 사다리 없으면 위로
    print(f'#{test_case}', j)
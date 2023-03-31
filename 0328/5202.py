
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[1])
    i =  0
    j = cnt = 1
    while i + j < N:
        if arr[i][1] <= arr[i + j][0]:
            i += j
            j = 1
            cnt += 1
        else:
            j += 1

    print(f'#{test_case}', cnt)
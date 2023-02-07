T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if arr[j] < arr[minidx]:                # j번째가 더 작으면
                minidx = j                          # 젤 작은 거
        arr[i], arr[minidx] = arr[minidx], arr[i]   # 바꾼다
    print(f'#{test_case}', *arr)
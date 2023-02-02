T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    idx = 0
    while(idx < N):
        count = 0
        for i in range(N):
            if arr[i] == 1:
                count += 1
                maxV = count
            else:
                count = 0
                
        if count > maxV:
            maxV = count
        idx += 1
    print(f'#{test_case}', maxV)
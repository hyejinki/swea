T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    idx = 0
    while(idx < N):
        count = 1
        maxV = 1
        for i in range(1, len(C)):
            if C[i] == C[i-1] + 1:
                count += 1
                maxV = count
            else:
                count = 1

        if maxV < count:
            maxV = count
        idx += 1
    print(f'#{test_case}', maxV)

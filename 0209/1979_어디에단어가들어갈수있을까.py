T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    ans = 0
    i = j = 0
    count = 0
    while True:
        if arr[i][j] != 1:
            count = 0

        else:
            count += 1
        
        j += 1

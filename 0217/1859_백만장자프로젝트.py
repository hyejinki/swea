T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))
    sum_n = maxV = 0
    i = N - 1
    while i > -1:
        if s[i] > maxV:
            maxV = s[i]             # 최댓값
        sum_n += maxV - s[i]
        i -= 1
    print(f'#{test_case}', sum_n)
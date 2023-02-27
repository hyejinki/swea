T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))    # 사람들
    res = []                    # 준비된 붕어빵
    i = 1
    ans = ''
    while len(res) < N:
        for _ in range(K):      # 개수만큼
            res.append(i*M)
        i += 1
    for i in range(N-1, -1, -1):            # 사람들(li) 정렬해 -> 버블정렬
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    for i in range(N):
        if li[i] < res[i]:              # 준비된 것보다 사람들이 더 빨리 오면 안돼
            ans = 'Impossible'
            break
    if len(ans) == 0:                   # 다 패스했으면 가.능
        ans = 'Possible'
    print(f'#{test_case}', ans)
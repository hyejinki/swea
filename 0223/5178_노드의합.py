def post_order(i, N):
    if i <= N:
        if arr[i] == 0:
            r1 = post_order(i*2, N)     # 왼쪽자식의 값 확인
            r2 = post_order(i*2+1, N)   # 오른쪽 자식 값 확인
            arr[i] = r1 + r2    # post_order(i*2) + post_order(i*2+1)
        return arr[i]
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        arr[node] = num
    post_order(1, N)
    print(f'#{test_case}', arr[L])
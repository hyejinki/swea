def f(i, k, s):
    global cnt
    if i == N:
        if s == k:
            cnt += 1
        return

    else:
        f(i + 1, k, s + arr[i])
        f(i + 1, k, s)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    f(0, K, 0)
    print(f'#{test_case}', cnt)
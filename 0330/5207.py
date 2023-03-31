def binarysearch(A, l, r, key):
    global flag
    if l > r:
        return -1
    else:
        m = (l + r) // 2
        if key == A[m]:
            return m
        elif key < A[m]:
            if flag == 1:
                return -1
            flag = 1
            return binarysearch(A, l, m - 1, key)
        else:
            if flag == 0:
                return -1
            flag = 0
            return binarysearch(A, m + 1, r, key)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for x in B:
        flag = -1
        if x in A:
            q = binarysearch(A, 0, N - 1, x)
            if q != -1:
                ans += 1


    print(f'#{test_case}', ans)
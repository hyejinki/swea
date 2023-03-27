def f(i, n, k):
    if i == k:
        print(*p)
    else:
        for j in range(N):      # k가 아님에 주의
            if used[j] == 0:
                used[j] = 1
                p[i] = A[j]
                f(i + 1, n, k)
                used[j] = 0

A = [1,2,3,4,5]
N = 5
k = 3

p = [0] * k
used = [0] * N
f(0, N, k)
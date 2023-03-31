N = int(input())
A = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i):
        if A[i - 1] > A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
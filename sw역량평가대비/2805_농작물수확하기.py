T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    ans = 0
    for i in range(N):
        # j는 N//2일때 N만큼 (최대), N//2와 i의 차이만큼
        for j in range(abs(N//2 - i), N-abs(N//2 - i)):
            ans += arr[i][j]
    print(f'#{test_case}', ans)

    
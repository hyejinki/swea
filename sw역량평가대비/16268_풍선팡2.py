d_ij = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]] 
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    sum_list = []
    for i in range(N):
        for j in range(M):
            total_sum = 0
            for k in range(5):
                ni, nj = i + d_ij[k][0], j + d_ij[k][1]
                if 0 <= ni < N and 0 <= nj < M:
                    total_sum += arr[ni][nj]
            sum_list.append(total_sum)
    print(f'#{test_case}', max(sum_list))